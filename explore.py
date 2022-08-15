import requests
import base64
import pandas as pd

def request(data):
    return requests.get(params=data)

if __name__=="__main__":
    df = pd.read_csv('tem.csv')
    pt_list=list(df['pt_en'])
    pt_pred_list=list(df['pt_pred_en'])
    # print(len(df))
    # n = len(df)
    # result_list = []
    # pt_list = []
    # pt_pred_list = []
    # drop_list=[]
    # result_set = set()
    # for index in range(n):
    #     tem_tup1 = (df['pt_en'][index], df['pt_pred_en'][index])
    #     tem_tup2 = (df['pt_pred_en'][index], df['pt_en'][index])
    #     if ((tem_tup1 not in result_set) and (tem_tup2 not in result_set)):
    #         result_set.add(tem_tup1)
    #     else:
    #         drop_list.append(index)
    # print(drop_list)
    # df=df.drop(drop_list,axis=0)
    # df.to_csv('tem8.1.csv',index=0)
    # print(len(df))
    result_list=[]
    for tem in range(len(df)):
        result_list.append(0)
    df['refine_label']=result_list
    url='https://fofa.info/api/v1/search/all'
    for index, tem in enumerate(pt_list):
        print(index,end=' ')
        data = {}
        data['email'] = 'zhaohaiquan@whu.edu.cn'
        data['key'] = 'd06b004e26399ddfdb9e613c7e6d0e99'
        query_str = 'app="' + tem + '" && app="' + pt_pred_list[index] + '"'
        # query_str='app="ClipShare" && app="Ruvar-OA"'
        qbase64=base64.b64encode(query_str.encode())
        data['qbase64']=qbase64
        res=requests.get(url=url,params=data).json()
        tem_data=dict(res)
        if('errmsg' in res):
            print('errmsg:',tem_data['errmsg'])
        else:
            if(tem_data['size']>0):
                df['refine_label'][index]=1
            print('size:',tem_data['size'])
    df.to_csv('result.csv',index=0)

if __name__=='__main1__':
    # df = pd.read_csv('tem8.1.csv')
    # pt_list = list(df['pt_en'])
    # pt_pred_list = list(df['pt_pred_en'])
    url = 'https://fofa.info/api/v1/search/all'
    result_list = []
    for index in range(1):
        print(index, end=' ')
        data = {}
        data['email'] = 'zhaohaiquan@whu.edu.cn'
        data['key'] = 'd06b004e26399ddfdb9e613c7e6d0e99'
        # query_str = 'app="' + pt_list[index] + '" && app="' + pt_pred_list[index] + '"'
        # query_str='app="Spark-Jobs" && app="Spark"'
        query_str = 'app="Non-book-resource-management-platform" && app="Hui-Wen-Libsys-Book-Management-System"'
        qbase64 = base64.b64encode(query_str.encode())
        data['qbase64'] = qbase64
        res = requests.get(url=url, params=data)
        print(res,end='')
        print(res.json())
        # tem_data = dict(res)
        # if ('errmsg' in res):
        #     print('errmsg:', tem_data['errmsg'])
        #     result_list.append(-1)
        # else:
        #     result_list.append(tem_data['size'])
        #     print('size:', tem_data['size'])
    # df['label'] = result_list
    # df.to_csv('result1.csv', index=0)



if __name__=='__main1__':
    df1=pd.read_excel('tem.xlsx')
    df2=pd.read_csv('result1.csv',encoding='ISO-8859-1')
    result_list=[]
    for i in range(len(df1)):
        for j in range(len(df2)):
            if((df1['pt'][i]==df2['pt'][j] and df1['pt_pred'][i]==df2['pt_pred'][j]) or (df1['pt'][i]==df2['pt_pred'][j] and df1['pt_pred'][i]==df2['pt'][j])):
                print(i,j)
                if(df2['label_8.2'][j]>0):
                    result_list.append(1)
                    j=len(df2)
                else:
                    result_list.append(0)
                    j = len(df2)
    df1['isReponse']=result_list
    df1.to_csv('result_8.9.csv', index=0)

if __name__=='__main1__':
    df=pd.read_csv('result9.9.csv', encoding='ISO-8859-1')
    i=0
    for tem in df['label']:
        if(tem>0):
            i+=1
    print(i)