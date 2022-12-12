#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Author
__author__ = "Rainer C. B. Herold"
__copyright__ = "Copyright 2022, Rainer C. B. Herold"
__credits__ = "Rainer C. B. Herold"
__license__ = "MIT license"
__version__ = "0.1"
__maintainer__ = "Rainer C. B. Herold"
__status__ = "Production"

# Libraries
try:
    from argparse import ArgumentParser, FileType, RawTextHelpFormatter, SUPPRESS
    from numpy import array
    from multiprocessing import active_children, Process, Queue
    from os import name as osname, makedirs, system
    from os.path import dirname, exists, join, realpath
    from random import randint
    from requests import get, post, Session
    from requests.exceptions import *
    from requests_pkcs12 import Pkcs12Adapter
    from sys import argv, stdout
    from time import perf_counter, sleep, strftime
except ModuleNotFoundError as e: input(f"The module was not found\n\n{e}\n\nPlease confirm with the button 'Return'"), exit()
