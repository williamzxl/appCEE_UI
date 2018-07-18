import json
import jmespath


class JMESPathExtractor(object):
    def extract(self, query=None, body=None):
        try:
            return jmespath.search(query, json.load(body))
        except Exception as e:
            raise ValueError("Invalid query: {0} {1}".format(query, e))


if __name__ == "__main__":
    from utils.client import HTTPClient
    res = HTTPClient(url='http://www.baidu.com').send()
    j = JMESPathExtractor()
    j_1 = j.extract(query='data.forecast[1].date', body=res.text)
    j_2 = j.extract(query='data.ganmao', body=res.text)