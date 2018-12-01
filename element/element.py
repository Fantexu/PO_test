import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from base.baseYaml import get_yaml
from base.baseAction import py_path


def get_element(path):
    text = get_yaml(path)
    for x in text:
        text[x] = eval(text[x])
    return text


ELEMENT_LOGIN = get_element(py_path('LoginElement.yaml', __file__))
ELEMENT_HOME = get_element(py_path('HomeElement.yaml', __file__))


# if __name__ == '__main__':
#