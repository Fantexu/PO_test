import os
import sys
PROJECT_PATH = os.path.join(os.getcwd(), '..')
sys.path.append(PROJECT_PATH)

from base.baseRun import *

case_path = '../case'
report_path = '../result/report'
# # # run_case(add_case(case_path))
run_case_HTMLText(add_case(case_path), report_path)



# from case.test_login import TestLogin
#
# su = unittest.TestSuite()
# su.addTest(TestLogin('test_login_01'))
# unittest.TextTestRunner().run(su)
