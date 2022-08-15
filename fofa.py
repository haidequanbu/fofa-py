import requests
import base64

class Fofa():
    def __init__(self,email,key):
        self.email=email
        self.key=key
        self.search_url='https://fofa.info/api/v1/search/all'

    def get_data(self,query_str='',page=1,size=100,field='',full=False):
        params={}
        params['email']=self.email
        params['key']=self.key
        qbase64=base64.b64encode(query_str.encode())
        params['qbase64']=qbase64
        if(page!=1):
            params['page']=page
        if(size!=100):
            params['size']=size
        if(field!=''):
            params['field']=field
        if(full!=False):
            params['full']=full
        res=requests.get(self.search_url,params=params).json()
        return res
