#!/usr/bin/python3.12

import os
import json

prefix_config = "/home/aldebaran/Project/.tools/config-account.json"

def execute_shell_query(shell_query):
    if isinstance(shell_query,dict):
        command_query = shell_query["command"]
        command_argument = shell_query["argument"]
        str_shell_query = command_query + " " + command_argument
        os.system(str_shell_query)
    elif isinstance(shell_query,str):
        os.system(shell_query)
    else:
        print("script cannot be executed on shell, not command!")

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
    
def switch_account(account_name,config_file):
    JSONData = read_config_file(config_file)
    ListUserTemp = read_config_file(config_file)
    if isinstance(ListUserTemp,dict):
        ListUser = list(ListUserTemp.keys())
        if account_name in ListUser:
            account_user = ListUserTemp[account_name]["user"]
            account_email = ListUserTemp[account_name]["email"]
            execute_shell_query({"command" : "git","argument" : "config user.name %s" % (account_user)})
            execute_shell_query({"command" : "git","argument" : "config user.email %s" % (account_email)})
            return True
        else:
            return False
    else:
        return False
    
if __name__ == "__main__":
    username = str(input("switch to user: "))
    if switch_account(username,prefix_config):
        print("success to switch into %s" % (username))
    else:
        print("user %s not found in user list" % (username))
    