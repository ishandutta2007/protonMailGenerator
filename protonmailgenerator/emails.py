from selenium import webdriver
import time
import random
import os
import signal
import logging
import pickle
import re
from settings import Settings
from socialcommons.browser import set_selenium_local_session
from socialcommons.file_manager import get_logfolder
from socialcommons.file_manager import get_workspace

def get_logger():
    logger = logging.getLogger('ishandutta2007@gmail.com')
    logger.setLevel(logging.DEBUG)
    logfolder = get_logfolder('ishandutta2007@gmail.com', False, Settings)
    file_handler = logging.FileHandler("{}general.log".format(logfolder))
    file_handler.setLevel(logging.DEBUG)
    extra = {
    }
    logger_formatter = logging.Formatter(
        "%(levelname)s [%(asctime)s] [protonMailGenerator:]  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    file_handler.setFormatter(logger_formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(logger_formatter)
    logger.addHandler(console_handler)

    logger = logging.LoggerAdapter(logger, extra)
    return logger

url = 'https://protonmail.com/'
# driver = webdriver.Chrome('/Users/johnfisher/Downloads/chromedriver')
logger = get_logger()
driver, err_msg = set_selenium_local_session(
    None,
    None,
    None,
    False,
    False,
    None,
    True,
    25,
    logger,
    Settings,
)

print(err_msg)

if len(err_msg) > 0:
    raise SocialPyError(err_msg)

driver.get(url)

driver.find_element_by_xpath('//*[@title="SIGN UP"]').click()

time.sleep(2)

driver.find_element_by_class_name('panel-heading').click()

time.sleep(4)

driver.find_element_by_id('freePlan').click()

time.sleep(2)

driver.find_element_by_id('username').send_keys('usernameForUser')

time.sleep(1.5)

driver.find_element_by_id('password').send_keys('passwordForUser')

time.sleep(2)

driver.find_element_by_id('passwordc').send_keys('passwordForUser')

time.sleep(2)

driver.find_element_by_class_name('signUpProcess-btn-create').click()

time.sleep(1)

driver.find_element_by_id('confirmModalBtn').click()
































