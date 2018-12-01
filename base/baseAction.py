import os
import sys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


def py_path(p, file):
    return os.path.join(os.path.dirname(file), p)


class Action:
    """公用方法类"""

    # driver = webdriver.Chrome()
    def __init__(self, driver):
        """初始化浏览器对象,链接,标题"""
        self.driver = driver

    def open(self, url):
        """打开链接,并判断链接是否正确"""
        self.driver.get(url)
        time.sleep(3)
        # assert title in self.driver.title, u'页面打开失败:{}'.format(url)

    def find_element(self, *loc):
        """
        封装查找元素方法,进行异常处理
        :param loc: (By关键字,value)
        :return:    查找到的元素
        """
        try:
            result = WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*loc))
            return result
        except:
            print('查找元素失败' + str(loc))
            self.driver.get_screenshot_as_file(py_path('../result/elementError/', __file__) + '{}_{}_查找元素失败'.format(*loc)
                                               + time.strftime('%Y%m%d_%H%M%S') + '.png')

    def send_keys(self, value, *loc, is_clear=True):
        element = self.find_element(*loc)
        if not is_clear:
            element.clear()
        element.send_keys(value)

    def click(self, *loc):
        self.find_element(*loc).click()

    def get_screen(self, filename):
        # filename =  + '_' + time.strftime('%Y_%m_%d_%H_%M_%S')
        os.mkdir(os.path.join(py_path('../result/assert_screen/', __file__), filename))
        self.driver.save_screenshot(os.path.join(py_path('../result/assert_screen/{}/'.format(filename), __file__),
                                                 '{}_{}.png'.format(sys._getframe(2).f_code.co_name,
                                                                    time.strftime('%Y_%m_%d_%H_%M_%S'))))


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    t_driver = webdriver.Chrome(options=option)
    t_driver.implicitly_wait(10)
    t_url = 'http://localhost/index.php/Home/user/login.html'
    a = Action(t_driver)
    a.open(t_url)
    ele = (By.ID, 'userna45me')
    a.find_element(*ele)
    time.sleep(3)
    t_driver.quit()
