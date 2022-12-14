#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold
# Version 0.1, 09.12.2022

# Libraries
from Resources.VF import *

# Main
if __name__ == '__main__':
    parser = ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter, description=Colors.ORANGE+Program_Description+Colors.RESET)
    required = parser.add_argument_group(Colors.ORANGE+'required arguments'+Colors.RESET)
    auth_arguments = parser.add_argument_group(Colors.ORANGE+'authentication arguments'+Colors.RESET)
    generator_arguments = parser.add_argument_group(Colors.ORANGE+'generator arguments'+Colors.RESET)
    performance_arguments = parser.add_argument_group(Colors.ORANGE+'performance arguments'+Colors.RESET)
    optional = parser.add_argument_group(Colors.ORANGE+'optional arguments'+Colors.RESET)

    required.add_argument('-u', '--url', type=str, help=Colors.GREEN+'This parameter specify one target.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    required.add_argument('-iL', '--import-list', type=str, help=Colors.GREEN+'This parameter specifies your targets.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    required.add_argument('-tID', '--target-id', type=str, required=True, help=Colors.GREEN+'This parameter specifies the html tag which you want to attack.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)

    auth_arguments.add_argument('-up', '--user-password', type=str, help=Colors.GREEN+'This parameter is required to specify a single user with password like in the example\nbelow'+Colors.RESET+'\n\nExample:\n  - admin:admin\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    auth_arguments.add_argument('-pk', '--pkcs12-path', type=bool, nargs='?', const=True, help=Colors.GREEN+'This parameter is used to switch your requests to pkcs12 certificate requests'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    auth_arguments.add_argument('-pkPw', '--pkcs12-password', type=str, help=Colors.GREEN+'This parameter specifies the password for the pkcs12 certificate'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    auth_arguments.add_argument('-iuL', '--import-user-list', type=str, help=Colors.GREEN+'This parameter specifies your user list.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)

    performance_arguments.add_argument('-mx', '--max-connections', type=int, default=15, help=Colors.GREEN+'This parameter specifies your max connections to do not DDOS the target.'+Colors.RESET+'\n\nDefault: 15\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    performance_arguments.add_argument('-s', '--sleep', type=float, default=0.25, help=Colors.GREEN+'This parameter specifies the time between the requests.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)

    generator_arguments.add_argument('-gL','--generate-list', type=bool, nargs='?', const=True, help=Colors.GREEN+'This parameter generates a random list of payment numbers.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    generator_arguments.add_argument('-mid', '--max-ids', type=int, default=5000, help=Colors.GREEN+'This parameter specifies the max count to generate ids'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    optional.add_argument('-o','--output-path', type=str, default=join(File_Path, "cracked_ids.txt"), help=Colors.GREEN+'This parameter specifies the output path.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    optional.add_argument('-lP','--list-path', type=str, default=join(File_Path, "payment_ids.txt"), help=Colors.GREEN+'This parameter specifies the path of your custom payment ids.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    optional.add_argument('-h','--help', action='help', default=SUPPRESS, help=Colors.GREEN+'Show this help message and exit.'+Colors.RESET+'\n\n'+Colors.BLUE+'-------------------------------------------------------------------------------------'+Colors.RESET)
    args = parser.parse_args()

    Initials()
    if (args.generate_list != None): Generate_List(args.list_path, args.max_ids)

    if (args.import_list != None and args.url != None):
        print ("It's not possible to use a target list in combination with a single target!"), exit()
    elif (args.import_list != None and args.url == None): Array_Targets = Read_File(args.import_list)
    elif (args.import_list == None and args.url != None): Array_Targets.append(args.url)

    if (args.pkcs12_password == None): pkcs_pw = ""
    else: pkcs_pw = args.pkcs12_password

    if (exists(Template_Path)): Array_Template = Read_File(Template_Path)

    Counter_Connections = 0
    for URL in array(Array_Targets):
        for IDs in array(Read_File(args.list_path)):
            if (IDs not in Array_Template):
               if (args.pkcs12_path != None): p = Process(target=Brute_Target, args=[URL, IDs, args.sleep, args.list_path, args.output_path, args.pkcs12_path, pkcs_pw, Template_Path], daemon=True)
               else: p = Process(target=Brute_Target, args=[URL, IDs, args.sleep, args.list_path, args.output_path, args.target_id, pkcs_pw, pkcs_pw, Template_Path], daemon=True)
               p.start()
               Counter_Connections += 1
               if (Counter_Connections == args.max_connections):
                   Timer = perf_counter()
                   while (len(Array_Threads) > 0):
                       for Thread_ID in array(Array_Threads):
                           if (Thread_ID not in str(active_children())):
                              try: Array_Threads.remove(Thread_ID)
                              except ValueError: pass
                              Counter_Connections -= 1
                       Status = perf_counter()
                       if (int(Status - Timer) < 90):
                           sleep(2.25)
                       else:
                           Kill_Command, Counter_Connections = True, 0
                           Array_Threads.clear(), sleep (1.5)
                           Kill_Command = False
               else:
                   if (p.name not in Array_Threads): Array_Threads.append(p.name), sleep(args.sleep)
    print (Colors.ORANGE+"\nAll Targets have been checked!"+Colors.RESET)
