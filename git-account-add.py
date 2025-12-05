#!/usr/bin/python3.12

import json
import os

prefix_config = "/home/aldebaran/Project/.tools/config-account.json"

def is_config_empty(config_file):
    try:
        ConfigFile = open(config_file,"r")
        get_status = len(ConfigFile.read())
        if get_status > 0:
            ConfigFile.close()
            return False
        else:
            ConfigFile.close()
            return True
    except FileNotFoundError:
        print("The config file " + config_file + " is not found")

def read_config_file(config_file):
    ConfigFile = None
    ConfigFileJSON = None
    if not is_config_empty(config_file):
        ConfigFile = open(config_file,"r")
        ConfigFileContent = ConfigFile.read()
        ConfigFileJSON = json.loads(ConfigFileContent)
        ConfigFile.close()
        return ConfigFileJSON
    else:
        return False
    
def add_value_config_file(config_file,new_config_value,write_once = False):
    try:
        ConfigData = read_config_file(config_file)
        ConfigFile = open(config_file,"w")
        if ConfigData:
            ConfigData.update(new_config_value)
            NewJSONData = json.dumps(ConfigData,indent=4)
            ConfigFile.write(NewJSONData)
            if write_once:
                ConfigFile.close()
        else:
            NewConfig = dict()
            NewConfig.update(new_config_value)
            NewJSONData = json.dumps(NewConfig,indent=4)
            ConfigFile.write(NewJSONData)
            ConfigFile.close()
    except FileNotFoundError:
        print("File config not found!")
        return False

if __name__ == "__main__":
    username = str(input("new git user name: "))
    email = str(input("new git user email: "))

    add_value_config_file(prefix_config,{username : {"user" : username, "email" : email}},write_once=True)
    print("adding new user with name " + username)