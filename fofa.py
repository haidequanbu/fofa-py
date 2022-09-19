import requests
import base64

class Fofa():
    def __init__(self,email,key):
        self.email=email
        self.key=key
        self.search_url='https://fofa.info/api/v1/search/all'
        self.user_info_url='https://fofa.info/api/v1/info/my'
        self.host_url='https://fofa.info/api/v1/host/'
        self.stats_url='https://fofa.info/api/v1/search/stats'
        self.get_user_info()

    def get_user_info(self):
        params = {}
        params['email'] = self.email
        params['key'] = self.key
        try:
            res=requests.get(self.user_info_url,params=params).json()
            data=dict(res)
            print('Welcome to fofa,' + data['username']+'!')
        except:
            raise RuntimeError('http请求失败')

    def get_host(self,host='',detail=False):
        host_url=self.host_url+host
        print(host_url)
        params = {}
        params['email'] = self.email
        params['key'] = self.key
        params['detail']=detail
        try:
            res=requests.get(host_url,params=params).json()
        except:
            raise RuntimeError('http请求失败')
        return res

    def get_stats(self,query_str='',field=''):
        params = {}
        params['email'] = self.email
        params['key'] = self.key
        qbase64 = base64.b64encode(query_str.encode())
        params['qbase64'] = qbase64
        params['fields'] = field
        try:
            res=requests.get(self.stats_url,params=params).json()
        except:
            raise RuntimeError('http请求失败')
        return res

    def get_data(self,query_str='',page=1,size=100,field='',full=False):
        params={}
        params['email']=self.email
        params['key']=self.key
        qbase64=base64.b64encode(query_str.encode())
        params['qbase64']=qbase64
        params['page']=page
        params['size']=size
        params['field']=field
        params['full']=full
        try:
            res=requests.get(self.search_url,params=params).json()
        except:
            raise RuntimeError('http请求失败')
        return res
