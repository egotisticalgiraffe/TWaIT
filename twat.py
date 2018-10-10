#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Metadata
__author__ = "SherlockSec";
__version__ = "1.0";
__license__ = "GPL-3.0";

#Imports
import sys;
import os;
import subprocess;

#Declarations
possible_packages = [
    "httrack",
    "apache2",
    "beef-xss",
];
colour_headers = [
    "\033[1;32;40m", #Bright Green   
    "\033[1;31;40m", #Bright Red    
];



if len(sys.argv) == 1:
    print("Error: no arguments given");
    #Display arguuments here
   
def DependencyCheck(possible_packages):
    for x in possible_packages:
        devnull = open(os.devnull, "w")
        check = subprocess.Popen(["dpkg", "-s", x], stdout=devnull, stderr=subprocess.STDOUT);
        devnull.close();
        if check != 0:
            print("%sPackage - %s - is not installed." % (colour_headers[1], x));
        else:
            print("%sPackage - %s - is installed." % (colour_headers[0], x));
