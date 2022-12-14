[![Linux](https://svgshare.com/i/Zhy.svg)](https://svgshare.com/i/Zhy.svg)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
![visitors](https://visitor-badge.glitch.me/badge?page_id=jarl-bjoern/skadi&left_color=grey&right_color=blue)
<a href="https://github.com/jarl-bjoern">
      <img title="Follower" src="https://img.shields.io/github/followers/Jarl-Bjoern.svg?style=social&label=Follow&maxAge=2592000"><a href="https://github.com/Jarl-Bjoern?tab=followers"></a>

# General Description
UNDER CONSTRUCTION

# Table of Contents
- [How to download and install the tool](#download_install)
  - [Download and start the tool](#start_install)
  - [Using the help section to see which parameters do we have](#help_install)
      
<a name="download_install"></a>
# How to download and install the tool
<a name="start_install"></a>
## Download and start the tool
```bash
sudo git clone https://github.com/Jarl-Bjoern/skadi
cd skadi
sudo python3 Skadi.py
```

<a name="help_install"></a>
## Using the help section to see which parameter do we have
```bash
-------------------------------------------------------------------------------------
|  Created by Rainer Christian Bjoern Herold                                        |
|  Copyright 2022. All rights reserved.                                             |
|                                                                                   |
|  Please do not use the program for illegal activities.                            |
|                                                                                   |
|  If you got any problems don't hesitate to contact me so I can try to fix them.   |
-------------------------------------------------------------------------------------

required arguments:
  -u URL, --url URL     This parameter specify one target.
                        
                        -------------------------------------------------------------------------
  -iL IMPORT_LIST, --import-list IMPORT_LIST
                        This parameter specifies your targets.
                        
                        -------------------------------------------------------------------------
  -tID TARGET_ID, --target-id TARGET_ID
                        This parameter specifies the html tag which you want to attack.
                        
                        -------------------------------------------------------------------------

authentication arguments:
  -up USER_PASSWORD, --user-password USER_PASSWORD
                        This parameter is required to specify a single user with password 
                        like in the example below
                        
                        Example:
                          - admin:admin
                        
                        -------------------------------------------------------------------------
  -pk [PKCS12_PATH], --pkcs12-path [PKCS12_PATH]
                        This parameter is used to switch your requests to pkcs12 certificate 
                        requests
                        
                        -------------------------------------------------------------------------
  -pkPw PKCS12_PASSWORD, --pkcs12-password PKCS12_PASSWORD
                        This parameter specifies the password for the pkcs12 certificate
                        
                        -------------------------------------------------------------------------
  -iuL IMPORT_USER_LIST, --import-user-list IMPORT_USER_LIST
                        This parameter specifies your user list.
                        
                        -------------------------------------------------------------------------

generator arguments:
  -gL [GENERATE_LIST], --generate-list [GENERATE_LIST]
                        This parameter generates a random list of payment numbers.
                        
                        -------------------------------------------------------------------------
  -mid MAX_IDS, --max-ids MAX_IDS
                        This parameter specifies the max count to generate ids
                        
                        -------------------------------------------------------------------------

performance arguments:
  -mx MAX_CONNECTIONS, --max-connections MAX_CONNECTIONS
                        This parameter specifies your max connections to do not DDOS the target.
                        
                        Default: 15
                        
                        -------------------------------------------------------------------------
  -s SLEEP, --sleep SLEEP
                        This parameter specifies the time between the requests.
                        
                        -------------------------------------------------------------------------

optional arguments:
  -o OUTPUT_PATH, --output-path OUTPUT_PATH
                        This parameter specifies the output path.
                        
                        -------------------------------------------------------------------------
  -lP LIST_PATH, --list-path LIST_PATH
                        This parameter specifies the path of your custom payment ids.
                        
                        -------------------------------------------------------------------------
  -h, --help            Show this help message and exit.
                        
                        -------------------------------------------------------------------------
```

# Remark
It should be said that the script is still under development.
