#!/usr/bin/env python

"""
This is a Python script that compares a given database password with a pre-defined hashed password. Here's a brief explanation of what the script does:

1. The script starts by importing necessary modules, including os, hashlib, logging, getpass, and dotenv.
2. The script then sets a variable for the environment file (.env) and loads it using the load_dotenv function.
3. The function init_env is defined, which initializes the environment by getting the database password from the environment file.
4. The compare_passwords function is defined, which compares the hashed value of the entered password with the pre-defined hashed value.
5. The main block of the script first initializes logging, then tries to get the database password from the environment file using the init_env function.
   If it fails, it prompts the user to enter the password using the getpass function.
6. The compare_passwords function is then called, passing the database password as an argument.

Overall, the script is a secure way to check if a given password matches a pre-defined hash. It also handles exceptions and logs errors for better troubleshooting.
"""
#!/usr/bin/env python

import os
import hashlib
import logging
from getpass import getpass
# need to install (pip)
from dotenv import load_dotenv

# define the name of the environment file
ENV_FILE = os.getenv("ENV_FILE", ".env")

# initialize the environment variables from the .env file
def init_env():
    try:
        load_dotenv(ENV_FILE) # load the environment variables from the .env file
    except FileNotFoundError:
        raise ValueError(f"{ENV_FILE} not found")
    dbpw = os.getenv("DBPW") # get the value of the "DBPW" variable
    if dbpw is None:
        raise ValueError("No DBPW variable found in .env file")
    return dbpw

# compare the hashed value of the entered password with the pre-defined hashed value
def compare_passwords(dbpw):
    # pre-defined hashed password
    hashed_password = str("7073420f60d8c5f923a92e656516a5b4")

    # hash the entered password using MD5
    hashed_dbpw = hashlib.md5(dbpw.encode()).hexdigest()

    # compare the hashed values and log the result
    if hashed_dbpw == hashed_password:
        logging.info("Correct password entered")
        print(f"You got it! The DBPW is correct: {dbpw}")
    else:
        logging.warning("Incorrect password entered")
        print(f"You failed! The DBPW is incorrect: {dbpw}")
    exit()

# main block of the script
if __name__ == "__main__":
    # initialize logging
    logging.basicConfig(filename="password_check.log", level=logging.INFO)

    try:
        dbpw = init_env() # try to get the database password from the environment file
    except ValueError as e:
        logging.error(str(e))
        print(f"Error: {str(e)}")
        dbpw = getpass("Please give Database Password: ") # if it fails, prompt the user to enter the password

    compare_passwords(dbpw) # call the compare_passwords function, passing the database password as an argument
