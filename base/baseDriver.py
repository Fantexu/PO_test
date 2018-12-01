from selenium import webdriver


def get_driver(is_hearless=False):
    """
    初始化浏览器驱动
    :param is_hearless: 是否隐藏
    :param args: (bool, time) 是否开启隐式等待, 等待时间
    :return:    驱动对象
    """
    option = webdriver.ChromeOptions()
    if is_hearless:
        option.add_argument('headless')
    driver = webdriver.Chrome(options=option)
    return driver

