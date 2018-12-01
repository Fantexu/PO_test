import os
import sys
PROJECT_PATH = os.path.join(os.getcwd(), '..')
sys.path.append(PROJECT_PATH)

from base.baseRun import *

case_path = '../case'
report_path = '../result/report'


send_main(report_path, '593019378@qq.com', 'touyzfnevxiabfhj', ['2285031211@qq.com', '15521067546@163.com'],
          'smtp.qq.com')