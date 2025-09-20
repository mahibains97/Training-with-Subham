import os
import datetime

def run_command(command):
    return os.system(command)

def show_time():
    return datetime.datetime.today()

run_command("df -h")

today = show_time()
print(today)