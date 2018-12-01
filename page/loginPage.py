from base import baseAction
from element.element import ELEMENT_LOGIN


class LoginPage(baseAction.Action):

    def ins_user(self, username):
        """填写用户名"""
        self.send_keys(username, *ELEMENT_LOGIN['username_input'])

    def ins_pwd(self, password):
        """填写密码"""
        self.send_keys(password, *ELEMENT_LOGIN['pwd_input'])

    def ins_code(self, code):
        """填写验证码"""
        self.send_keys(code, *ELEMENT_LOGIN['code_input'])

    def click_login(self):
        """点击登录按钮"""
        self.click(*ELEMENT_LOGIN['login_button'])

    def login(self, username, password, code):
        """
        登录操作
        :param username:账户
        :param password: 密码
        :param code: 验证码
        :return:
        """
        self.ins_user(username)
        self.ins_pwd(password)
        self.ins_code(code)
        self.click_login()

