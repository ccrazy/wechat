# -*-coding:utf-8-*-
import requests
import json
URL = "https://wx2.qq.com"
COOKIE = "RK=ho1nxteaWD; pgv_pvi=3866932224; pac_uid=1_1163443987; _ga=GA1.2.1293549484.1500358725; tvfe_boss_uuid=5c43233ce2e78bd4; mobileUV=1_15dd006e9e8_b521; webwxuvid=a83b2dfa286fd8070858ae9f719ad2fbfbe8bcb40284762bdbf8bbbd8a97ac07b1793ed9efd7ed3864023c895a7834ec; ptcz=36e172c634bab45d04a22a456378844f9bc1f7f07c4c40dc27c75974329ddcfe; pt2gguin=o1163443987; pgv_pvid=2318594800; o_cookie=1163443987; MM_WX_NOTIFY_STATE=1; MM_WX_SOUND_STATE=1; mm_lang=zh_CN; webwx_auth_ticket=CIsBEOXFv+ABGoABQVFTjLEVLO5HqQZ30YiL/UTAQlxIHlvsApMEYJFjWe/jdl/9t++iDfNc5H+ItvSiNLZh1HFPbvZIjBLGNQzuqgizw8F6+xCfMtIxWAZMyhUZagJaTtRkaW/EHfwj6JFxYIM9T3QK6sm1rKkN0byC6xwmuOSVID3kUlIQYwIpR+E=; login_frequency=1; last_wxuin=2896078163; wxloadtime=1506236159_expired; wxpluginkey=1506226682; wxuin=2896078163; wxsid=b9TmkkBZvSB3pPZG; webwx_data_ticket=gSd78WF/h0Plysgtv5Qj6oIQ"
AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
head = {"Cookie": COOKIE, "User-Agent": AGENT}
param = {"r": "1506236180828",
         "seq": 0,
         "skey": "@crypt_7ad54c36_fd2334f828a105ce1bab0d41699dd31b"
         }


def build_uri(enter):
    return "/".join([URL, enter])

# /cgi-bin/mmwebwx-bin/webwxgeticon?seq=628702143&username=@18ec7189028392844aa4d37d7cace3d2&skey=@crypt_7ad54c36_73d7fbd424ae831b0c750bdf75309ad0
def getimg():
    reponse = requests.get(
        build_uri("cgi-bin/mmwebwx-bin/webwxgetcontact"), headers=head, params=param)
    reponse.encoding = "gzip"
    friends = reponse.json()
    memberlist = friends["MemberList"]
    print(type(friends))
    print(type(memberlist))
    print(len(memberlist))
    for fr in memberlist:
        img = requests.get("https://wx2.qq.com"+fr["HeadImgUrl"],headers=head,stream=True)
        username = fr["UserName"]
        with open(username+".jpeg","wb") as fi:
            for chunk in img.iter_content(128):
                fi.write(chunk)
        # return


if __name__ == "__main__":
    getimg()
