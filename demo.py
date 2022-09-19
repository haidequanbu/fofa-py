from fofa import Fofa

if __name__=="__main1__":
    # 对应邮箱和api_key（需要有查询的权限才能够请求接口）
    fofa=Fofa(email='XXXX',key='XXXX')

    # fofa.get_data(self,query_str='',page=1,size=100,field='',full=False)
    # fofa.get_data参数：
    # query_str:输入到fofa引擎中的查询语句,必须要有（必须参数）
    # page:是否翻页，默认第一页（非必需参数）
    # size:每页查询数量，最大10000条/页
    # field:默认host,ip,port,可参考官网给的附录
    # full:默认一年内数据，设置为True是查询所有记录
    res=fofa.get_data(query_str='app="APPNODE"')
    if ('errmsg' in res):
        print(res)
    else:
        data = dict(res)
        print(data)
        for tem in data['results']:
            print(tem)

if __name__=="__main1__":
    # 对应邮箱和api_key（需要有查询的权限才能够请求接口）
    fofa = Fofa(email='xxxx', key='xxxx')

    # get_host(self,host='',detail=False)
    # fofa.get_host参数：
    # host:ip地址
    # detail：是否显示端口详情
    res = fofa.get_host(host='xxxxxx')
    if ('errmsg' in res):
        print(res)
    else:
        data=dict(res)
        print(data)

if __name__=="__main3__":
    # 对应邮箱和api_key（需要有查询的权限才能够请求接口）
    fofa = Fofa(email='xxxx', key='xxxx')

    # get_stats(self,query_str='',field='')
    # fofa.get_stats参数：
    # query_str：查询语句
    # field:默认host,ip,port,可参考官网给的附录
    res = fofa.get_stats(query_str='app="APPNODE"')
    if ('errmsg' in res):
        print(res)
    else:
        data=dict(res)
        print(data)