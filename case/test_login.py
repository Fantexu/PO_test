import time
import unittest

# import os, sys
# sys.path.append(os.getcwd())


from page.page import BasePage
from data.data import *
from base.baseDriver import get_driver
from base import baseAction
# from run import runCase


class TestLogin(unittest.TestCase):

    def assert_result(self, is_result=True):
        """断言登录状态的处理"""
        result = self.page.home_page.get_login_status()
        try:
            if is_result:
                self.assertTrue(result)
            else:
                self.assertFalse(result)
        except:
            print()
            # 对断言结果进行截图
            filename = self.__class__.__name__ + '_' + time.strftime('%Y_%m_%d_%H_%M_%S')
            baseAction.Action(self.driver).get_screen(filename)
            raise

    def setUp(self):

        self.driver = get_driver(is_hearless=True)
        self.page = BasePage(self.driver)
        self.page.home_page.open(DATA_HOME['url'])
        self.page.home_page.click_login()

    def tearDown(self):
        self.driver.quit()

    def test_login_01(self):
        self.page.login_page.login(DATA_LOGIN['手机号'], DATA_LOGIN['密码'], DATA_LOGIN['验证码'])
        self.assert_result()

    # def test_login_02(self):
    #     self.page.login_page.login(DATA_LOGIN['不存在的手机号'], DATA_LOGIN['密码'], DATA_LOGIN['验证码'])
    #     self.assert_result()
    #
    # def test_login_03(self):
    #     self.page.login_page.login(DATA_LOGIN['格式过长的手机号'], DATA_LOGIN['密码'], DATA_LOGIN['验证码'])
    #     self.assert_result(False)
    #
    # def test_login_04(self):
    #     self.page.login_page.login(DATA_LOGIN['非1开头的手机号'], DATA_LOGIN['密码'], DATA_LOGIN['验证码'])
    #     self.assert_result(False)
    #
    # def test_login_05(self):
    #     self.page.login_page.login(DATA_LOGIN['第二数不为2的手机号'], DATA_LOGIN['密码'], DATA_LOGIN['验证码'])
    #     self.assert_result(False)
    #
    # def test_login_06(self):
    #     self.page.login_page.login(DATA_LOGIN['非自然数的手机号'], DATA_LOGIN['密码'], DATA_LOGIN['验证码'])
    #     self.assert_result(False)
    #
    # def test_login_07(self):
    #     self.page.login_page.login(DATA_LOGIN['手机号'], DATA_LOGIN['错误的密码'], DATA_LOGIN['验证码'])
    #     self.assert_result(False)
    #
    # def test_login_08(self):
    #     self.page.login_page.login(DATA_LOGIN['手机号'], DATA_LOGIN['密码'], DATA_LOGIN['错误的验证码'])
    #     self.assert_result(False)
    #
    # def test_login_09(self):
    #     self.page.login_page.login('', DATA_LOGIN['密码'], DATA_LOGIN['验证码'])
    #     self.assert_result(False)
    #
    # def test_login_10(self):
    #     self.page.login_page.login(' ', DATA_LOGIN['密码'], DATA_LOGIN['验证码'])
    #     self.assert_result(False)


# if __name__ == '__main__':
#     # unittest.main()
#     su = unittest.TestSuite()
#     # tests = [TestLogin('test_login_01'), TestLogin('test_login_02')]
#     su.addTest(TestLogin('test_login_02'))
#     # su.addTests(tests)
#     # unittest.TextTestRunner().run(su)
#     runCase.run_case_HTMLText(su, '../result/report')

