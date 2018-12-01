from selenium.webdriver.support.wait import WebDriverWait

from base import baseAction
from element.element import ELEMENT_HOME


class HomePage(baseAction.Action):
    def click_login(self):
        """点击登录按钮"""
        self.click(*ELEMENT_HOME['login_button'])

    def get_login_status(self):
        """
        获取登录状态
        :return: True为已登录状态, Flase为未登录状态
        """
        try:
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*ELEMENT_HOME['logout_button']))
            return True
        except:
            return False

