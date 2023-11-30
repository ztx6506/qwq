import pickle
import configparser
# 初始化
def w_data(num,id,type):
    with open('./db/data.pkl', 'rb') as file:
        existing_data = pickle.load(file)
    existing_data[num] = {'id': id, 'type': type}

    with open('./db/data.pkl', 'wb') as file:
        pickle.dump(existing_data, file)

def int():
    with open('./db/data.pkl', 'rb') as file:
        existing_data = pickle.load(file)
    existing_data={}
    with open('./db/data.pkl', 'wb') as file:
        pickle.dump(existing_data, file)
    print('初始化完成')
def config(name,tag,tid):
    config = configparser.ConfigParser()

# 添加一些配置项
    config[name] = {
        'tag': tag,
        'tid': tid,
    }

# 写入配置到文件
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
def 修改(): 
    with open('./db/data.pkl', 'rb') as file:
        loaded_data1 = pickle.load(file)
    print(loaded_data1)
    loaded_data1[7]['type']='TomsJurjaks'

    with open('./db/data.pkl', 'wb') as file:
        pickle.dump(loaded_data1, file)
def query(munum):
    with open('./db/data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
    data=loaded_data[munum]['type']
    return data
def query_all():
    with open('./db/data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
    return loaded_data
# while True:
#     with open('./db/data.pkl', 'rb') as file:
#         loaded_data = pickle.load(file)
#     id=input('id:')
#     type=input('name')
#     num=len(loaded_data)
#     tag=input('tag:')
#     tid=input('tid:')
#     w_data(num,id,type)
#     with open('./db/data.pkl', 'rb') as file:
#         loaded_data1 = pickle.load(file)
#     print(loaded_data1)
#     config(type,tag,tid)
