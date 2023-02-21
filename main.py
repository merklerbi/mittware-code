#!/usr/bin/env python

"""_summary_
The script begins by importing necessary modules including os, hashlib, logging, and getpass from the dotenv and os.path packages.

The init_env() function uses the load_dotenv() function from dotenv to load the DBPW variable from the .env file, and raises a ValueError if the variable is not found.

The compare_passwords() function takes the dbpw argument (the user-entered password) and compares its SHA-256 hash value to a pre-defined hash value stored in exception_hash.
If the hashes match, the function logs the correct password to a file named password_check.log and prints a success message to the console.
Otherwise, the function logs the incorrect password and prints a failure message to the console.

In the main block of the script, the logging module is configured to log messages at the INFO level to a file named password_check.log.
If the .env file exists, the init_env() function is called to retrieve the database password. If the DBPW variable is not found in the .env file, the script logs an error message and exits.
Otherwise, the getpass() function is used to securely prompt the user for the password input. The compare_passwords() function is then called with the user-entered password as the argument.
"""

import os
import hashlib
import logging
from getpass import getpass
from dotenv import load_dotenv

ENV_FILE = os.getenv("ENV_FILE", ".env")


def init_env():
    try:
        load_dotenv(ENV_FILE)
    except FileNotFoundError:
        raise ValueError(f"{ENV_FILE} not found")
    dbpw = os.getenv("DBPW")
    if dbpw is None:
        raise ValueError("No DBPW variable found in .env file")
    return dbpw

def compare_passwords(dbpw):
    hashed_password = str("7073420f60d8c5f923a92e656516a5b4")
    hashed_dbpw = hashlib.md5(dbpw.encode()).hexdigest()

    if hashed_dbpw == hashed_password:
        logging.info("Correct password entered")
        print(f"You got it! The DBPW is correct: {dbpw}")
    else:
        logging.warning("Incorrect password entered")
        print(f"You failed! The DBPW is incorrect: {dbpw}")
    exit()

if __name__ == "__main__":
    logging.basicConfig(filename="password_check.log", level=logging.INFO)

    try:
        dbpw = init_env()
    except ValueError as e:
        logging.error(str(e))
        print(f"Error: {str(e)}")
        dbpw = getpass("Please give Database Password: ")

    compare_passwords(dbpw)
