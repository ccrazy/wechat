# -*-coding:utf-8-*-
import requests
import json
from db import database
#数据库名
table = "liudeyin"
#微信好友数据接口顶级域名
URL = "https://wx2.qq.com"
#登录cookie
COOKIE = "RK=ho1nxteaWD; pgv_pvi=3866932224; pac_uid=1_1163443987; _ga=GA1.2.1293549484.1500358725; tvfe_boss_uuid=5c43233ce2e78bd4; mobileUV=1_15dd006e9e8_b521; webwxuvid=a83b2dfa286fd8070858ae9f719ad2fbfbe8bcb40284762bdbf8bbbd8a97ac07b1793ed9efd7ed3864023c895a7834ec; ptcz=36e172c634bab45d04a22a456378844f9bc1f7f07c4c40dc27c75974329ddcfe; pgv_pvid=2318594800; o_cookie=1163443987; luin=o1163443987; lskey=00010000200e3e0912e64c4abaaf423949266248987cab8be3c8c1b1f7f650978fe8693aad9b892f45b6daa6; pt2gguin=o1163443987; webwx_auth_ticket=CIsBEJSH4I8EGoAB2QZKg8/0ENWeQqMPEai0dhBgshR/4qOjGtdRn2oClFzOuEZABffUbjrIi4fahYYaxn4JGx15T0nBxnVRv5dXbnBCXc6cTpSNYa582tkGL5hHyJ0aKQepTG4za+L3Ez2+UMY+NbW4dPWyvxx+INqhphy6C6m5iwrh84nm2SdGlIY=; login_frequency=1; last_wxuin=988464464; wxloadtime=1506351975_expired; wxpluginkey=1506335942; wxuin=988464464; wxsid=n/uJ9i0LH/tsKatH; webwx_data_ticket=gSdaZtaD25mw0wML8xlcL/Ir; mm_lang=zh_CN; MM_WX_NOTIFY_STATE=1; MM_WX_SOUND_STATE=1"
#浏览器头
AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
#http请求头
head = {"Cookie": COOKIE, "User-Agent": AGENT,
        "Referer": "https://wx.qq.com/?&lang=zh_CN"}
#请求数据
param = {"r": "1506351992112",
         "seq": 0,
         "skey": "@crypt_ec368e3d_51929cad3f19509e08b0538a7b17c27a",
        #  "lang": "zh_CN"
         }
#接口生成
def build_uri(enter):
    return "/".join([URL, enter])
#获取好友信息
def getlist():
    #请求好友信息接口
    reponse = requests.get(
        build_uri("cgi-bin/mmwebwx-bin/webwxgetcontact"), headers=head, params=param)
    #设置请求编码
    reponse.encoding = "gzip"
    friends = reponse.json()
    #获取好友列表
    memberlist = friends["MemberList"]
    #组合数据表创建sql
    sql = "CREATE TABLE " + table + "(id INT AUTO_INCREMENT,PRIMARY KEY(id),"
    demo = memberlist[0]
    d = sorted(demo.items(), key=lambda d: d[0])
    for it in d:
        if isinstance(it[1], int):
            sql = sql + it[0] + " " + "int,"
        elif isinstance(it[1], str):
            sql = sql + it[0] + " " + "varchar(1000),"
        else:
            t = str(it[1])
            sql = sql + it[0] + " " + "varchar(1000),"
    sql = sql[:-1] + ")"
    #执行数据表创建sql
    cursor = database.cursor()
    try:
        cursor.execute(sql)
        database.commit()
    except:
        print("数据库创建失败")
        return
    #写入微信好友信息
    for i in range(len(memberlist)):
        user = memberlist[i]
        u = sorted(user.items(), key=lambda d: d[0])
        value = []
        value.append(i + 1)

        for j in u:
            v = j[1]
            if isinstance(v, list):
                v = "".join(v)
            value.append(v)
        
        try:
            cursor.execute('insert into ' + table +
                           ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', value)
            database.commit()
            print(1)
        except:
            print('失败')
    database.close()


if __name__ == "__main__":
    getlist()
