from fofa import Fofa

if __name__=="__main__":
    fofa=Fofa(email='XXXX',key='XXXXX')
    res=fofa.get_data(query_str='XXXX')
    print(res)