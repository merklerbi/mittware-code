#!/usr/bin/env python

import os
from os.path import exists
# maybe you have to install something
import hashlib
from dotenv import load_dotenv

env_file=".env"

def init_env():
    load_dotenv()
    return os.getenv('DBPW')

def compare_passwords(DBPW):
    execption = str("7073420f60d8c5f923a92e656516a5b4")

    if hashlib.md5(DBPW.encode()).hexdigest() == execption:
        print(f'You got it!\nThe DBPW is {DBPW}')
    else:
        print(f'You failed!\nThe DBPW isn\'t {DBPW}')
    exit()

if __name__ == "__main__":
    file_exists = os.path.exists(env_file)
    if file_exists:
        DBPW = init_env()
    else:
        print(f'No {env_file} provided!\n')
        DBPW = str(input("Please give Database Password: "))

    compare_passwords(DBPW)
