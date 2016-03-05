import requests
from bs4 import BeautifulSoup
"""
url:    http://rd2.zhaopin.com/portal/myrd/regnew.asp?za=2
accout:     hxjs5875 hxjs123456
search: http://rdsearch.zhaopin.com/
http://rdsearch.zhaopin.com/Home/ResultForCustom?SF_1_1_1=python&SF_1_1_2=200300&orderBy=DATE_MODIFIED,1&SF_1_1_27=0&exclude=1
"""


sess = requests.session()

# 得到验证码
def get_checkcode():
    global sess

    r = sess.get('https://passport.zhaopin.com/checkcode/imgrd')
    print('****************************************')
    print(id(sess))
    print('****************************************')
    return r.content

# 模拟登录
def simulation_login(checkcode):
    global sess
    payload = {
        'LoginName': 'hxjs5875',
        'Password': 'hxjs123456',
        'CheckCode': checkcode
    }
    res = sess.post('https://passport.zhaopin.com/org/login', data=payload)
    print('****************************************')
    print(id(sess))
    print('****************************************')

    res = sess.get('http://rd2.zhaopin.com/s/loginmgr/loginproc_new.asp')

    search_value = {
        'SF_1_1_1': 'python',
        'SF_1_1_2': '200300',
        'orderBy': 'DATE_MODIFIED,1',
        'SF_1_1_27': '0',
        'exclude': '1'
    }
    result = sess.get('http://rdsearch.zhaopin.com/Home/ResultForCustom', \
                   params=search_value)
    print('****************************************')
    print(id(sess))
    print(result.text)
    print('****************************************')

    return '222222222222'



# 模拟搜索 POST
def simulation_search(s):
    #r = s.get('http://rdsearch.zhaopin.com/')
    #soup = BeautifulSoup(r.text, 'lxml')
    search_value = {
        'SF_1_1_1': 'python',
        'SF_1_1_2': '200300',
        'orderBy': 'DATE_MODIFIED,1',
        'SF_1_1_27': '0',
        'exclude': '1'
    }
    result = s.post('http://rdsearch.zhaopin.com/Home/ResultForCustom', \
                   params=search_value)
    print(result.text)



if __name__ == '__main__':
    get_checkcode()
