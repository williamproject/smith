
from django.test import TestCase

from myApp.mylog import logger



class TestDB(TestCase):

    # def __init__(self):
    #     super().__init__("testConn")
    #     print('--单元测试ｓｔａｒｔ')

    def testConn(self):
        logger.info('开始运行测试')
        a = None
        self.assertIsNone(a, 'a是None')

    def __del__(self):
        print('--单元测试over----')