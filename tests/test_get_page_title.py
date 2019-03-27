# coding = utf-8
import unittest
import sys
# sys.path.insert(0, '..')
sys.path.append('..')
# import helper.browser_engine.BrowserEngine
from helper.browser_engine import BrowserEngine
# from pageobjects.baidu_homepage import HomePage
# import pageobjects.baidu_homepage.HomePage
from pages.baidu_homepage import HomePage


class GetPageTitle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_get_title(self):
        homepage = HomePage(self.driver)
        print (homepage.get_page_title())

if __name__ == '__main__':
    unittest.main()