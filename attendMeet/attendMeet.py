from time import sleep
from sys import exit
from getpass import getpass
from abc import ABC, abstractmethod

import selenium.common.exceptions
from selenium.webdriver.firefox.webdriver import WebDriver

import os
EXECUTABLE_PATH = os.environ["HOME"] + "/geckodriver"



class AttendMeet(ABC):
    def __init__(self, **kwargs):
        """
        Parameters:\n
            kwargs['code'] (string): Meeting code\n
        """
        self.__login_data = {}
        self.__login_url = None
        self.__driver = None
        self.__meet_url = None

        try: self.login_url = kwargs["code"]
        except KeyError: print("ERROR ****** ********\nSome parameters may be missing! Check 'help(AttendMeet)' for more details ******")


    @abstractmethod
    def doLogin(self): raise NotImplementedError

    @abstractmethod
    def enter_class(self): raise NotImplementedError


    @property
    def login_data(self): return self.__login_data

    @login_data.setter
    def login_data(self, data):
        try:
            self.__login_data = {"user": data["user"], "passwd": data["passwd"]} 
        except KeyError:
            user = str(input("User: "))
            passwd = getpass("Password: ")
            self.__login_data = {"user": user, "passwd": passwd}

    @property
    def login_url(self): return self.__login_url

    @login_url.setter
    def login_url(self, platform):
        plat_login = {
            "google": "https://accounts.google.com/Login?hl=pt-BR",
            "meet": "https://accounts.google.com/Login?hl=pt-BR",
            "zoom": "https://zoom.us/google_oauth_signin"
        }
        try: self.__login_url = plat_login[platform]
        except KeyError: print("ERROR ****** ******** Platform not available! ******")

    @property
    def meet_url(self):
        return self.__meet_url

    @meet_url.setter
    def meet_url(self, code):
        raise NotImplementedError

    @property
    def driver(self): return self.__driver

    @driver.setter
    def driver(self, browser):
        if browser == "firefox": self.__driver = WebDriver(executable_path=EXECUTABLE_PATH)
        else: self.__driver = None

    
