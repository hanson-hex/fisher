import  requests
from urllib import request, parse
from urllib import parse
import json

class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text


class HTTP1:
    @staticmethod
    def get_with_url(url, json_return=True):
        url = request.quote(url, safe='/:?&')
        try:
            with request.urlopen(url) as r:
                result_str = r.read()
                result_str = result_str.decode('utf-8')
                print('result_str', result_str)
                if json_return:
                    return json.loads(result_str)
                return result_str
        except OSError as e:
            print(e)
            if json_return:
                return {}
            else:
                return None


# http = HTTP1()
# print(http.get_with_url('http://www.baidu.com', json_return=False))
# values = {'username': '3234', 'password': 'dds'}
# data = parse.urlencode(values).encode('utf-8')
# url = request.quote('http://zzk.cnblogs.com/s?w=python爬虫&t=b', safe='/:?&')
# resp = request.urlopen(url)
# print(resp.read().decode('utf-8'))