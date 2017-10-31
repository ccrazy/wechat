#-*-coding:utf-8-*-
#!/usr/bin/env python3
from db import database
def onetable(tablename,fields="*",where=""):
    if len(where)<=0:
        sql = "select "+fields+" from "+tablename
    else:
        sql = "select "+fields+" from "+tablename+" where "+where
    cursor = database.cursor()
    try:
        cursor.execute(sql)
        return cursor
    except:
        print("查询错误")
        return

def mkpie():
    #性别分析
    pass

def province():
    #区域分析
    pass

def signature():
    #签名分析
    pass

def subscription():
    #公众号分析
    pass

# def main():
#     pass

if __name__ == '__main__':
    cur = onetable("friends",where="id<5")
    print(cur.fetchone())