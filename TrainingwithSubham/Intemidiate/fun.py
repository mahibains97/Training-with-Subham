import os

command = "df -h"  ## disk space
command = "free -h"  ## Memory detail
command = "ls -ltr" ## show the file list

def check_cpu(command):
    print(os.system(command))

check_cpu("df -h")

def check_ram(command):
    print(os.system(command))

check_ram("free -h")

def check_list(command):
    print(os.system(command))

check_list("ls -ltr")

def check_date(command):
    print(os.system(command))

check_date("date")

