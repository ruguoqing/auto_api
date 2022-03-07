# coding:utf-8

'''
http接口，get，post 请求
'''

import requests


class HttpRequest:

    def __init__(self, method, url, header, data):
        self.method = method
        self.url = url
        self.header = header
        self.data = data

    def http_request(self):
        if self.method == 'get':
            res = requests.get(self.url, headers=self.header, params=self.data, verify=False)
        else:
            res = requests.post(self.url, headers=self.header, json=self.data, verify=False)

        return res


if __name__ == '__main__':
    Token = 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiI0NjUiLCJzdWIiOiI0NjUiLCJpYXQiOjE2NDUwMDAwMTcsImF1ZCI6ImJhY2tlbmQiLCJleHAiOjE2NTM2NDAwMTd9.qNb2ukpbzCbcCA5_mLXYlOjdZ21BDXHKMBjUUbpdYw3-B8NxGUjShjLrVwY6vc797JWj7IRkXWMtXqodIbBpwg'
    note_url = 'https://crm-test.meishubao.com/k8s/api/crm/api/v1/note/create'  # 请求url地址
    header = {'Content-Type': 'application/json', 'Authorization': Token}  # 请求头
    body = {
        "uid": 4173876,
        "mid": "1778687",
        "contactType": "1",  # 跟踪渠道
        "flowPlan": "3",  # 跟进进度
        "note": "这是个测试数据222",
        "userId": 4173876}
    note = HttpRequest('post', note_url, header, body).http_request()
    print(note.json()['status'])
