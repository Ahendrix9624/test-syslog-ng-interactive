#!/usr/bin/python3
'''
USAGE - This Python code is a program designed for testing the syslog-ng logging system. 
        It imports the necessary modules for logging in Python, sets up a logger, and 
        prompts the user for a log level and message to log.
        
        The program allows the user to choose a log level from a list of options, 
        which is used to determine the severity level of the log message. The program 
        then prompts the user for a message to log, and logs the message at the chosen 
        log level using the Python logging module.

        The program uses the SysLogHandler from the logging.handlers module, which 
        sends the log message to the syslog-ng system on the local machine. The program 
        continues to prompt the user for log levels and messages until the user chooses 
        to exit the program.

AUTHOR - https://github.com/Ahendrix9624
'''
import sys
import syslog
import logging
import logging.handlers

# Set up logger
logger = logging.getLogger("10×13")
logger.setLevel(logging.DEBUG)
handler = logging.handlers.SysLogHandler(address='/dev/log', facility=16)
handler.setLevel(logging.DEBUG)
log_format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(log_format)
logger.addHandler(handler)

while True:
    # Prompt user for log level and message
    print("Which log level do you want to use?")
    print("1. DEBUG")
    print("2. INFO")
    print("3. WARNING")
    print("4. ERROR")
    print("5. CRITICAL")
    print("6. ALL")
    print("7. Exit Program")
    log_level_choice = int(input())
    log_level = None

    if log_level_choice == 1:
        log_level = "DEBUG"
    elif log_level_choice == 2:
        log_level = "INFO"
    elif log_level_choice == 3:
        log_level = "WARNING"
    elif log_level_choice == 4:
        log_level = "ERROR"
    elif log_level_choice == 5:
        log_level = "CRITICAL"
    elif log_level_choice == 6:
        log_level = "ALL"
    elif log_level_choice == 7:
        print("Goodbye!")
        break
    else:
        print("Invalid choice for log level.")
        continue

    print("What message do you want to log?")
    log_message = input()

    # Log the message at the chosen level(s)
    if log_level == "DEBUG" or log_level == "ALL":
        logger.debug(log_message)
    if log_level == "INFO" or log_level == "ALL":
        logger.info(log_message)
    if log_level == "WARNING" or log_level == "ALL":
        logger.warning(log_message)
    if log_level == "ERROR" or log_level == "ALL":
        logger.error(log_message)
    if log_level == "CRITICAL" or log_level == "ALL":
        logger.critical(log_message)