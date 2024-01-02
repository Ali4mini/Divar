from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import pickle
import time
import traceback
class Sheypoor:
    """scraping data from Sheypoor."""

    def __init__(self, arg):
        super(Sheypoor, self).__init__()
        self.arg = arg
