from tinydb import TinyDB, Query
class DB:
    def __init__(self,path='db/db.json'):
        self.db = TinyDB(path)
    def add(self,data):
        self.db.insert(data)
        print('插入成功')
    def query(self,query):
        result=self.db.search(query)
        return result
    def close(self):
        self.db.close()
        print('数据库已关闭')