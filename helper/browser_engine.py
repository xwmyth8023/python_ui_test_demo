# -*- coding:utf-8 -*-
import configparser
import os.path
from selenium import webdriver
from helper.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    chrome_driver_path = os.path.join(os.path.abspath('.'), 'tools/chromedriver')
    firefox_driver_path = os.path.join(os.path.abspath('.'), 'tools/geckodriver')
    ie_driver_path = os.path.join(os.path.abspath('.'), 'tools/iedriver')
    # print(chrome_driver_path,firefox_driver_path)

    def __init__(self, driver):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = os.path.join(os.path.abspath('.'),'config/config.ini')
        # print(file_path)
        config.read(file_path)

        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)


        if browser == "Firefox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            print(self.chrome_driver_path)
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()