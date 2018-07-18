import unittest
from utils.config import Config,REPORT_PATH
from utils.client import HTTPClient
from utils.log import logger

from BeautifulReport import BeautifulReport


class TestBaiDuHttp(unittest.TestCase):
    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url=self.URL, method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        self.assertIn('百度一下，你就知道', res.text)


if __name__ == "__main__":
    # report = REPORT_PATH + '\\report1122.html'
    # with open(report, 'w') as f:
    #     runner = HTMLTestRunner(f, verbosity=2, title="Test", description="Test baidu http")
    #     runner.run(TestBaiDuHttp('test_baidu_http'))
    pass