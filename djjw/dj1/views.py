#coding:utf-8
import cookielib
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
import urllib
import urllib2

import re
import string
import types
import requests
import sys
import base64
# from django.views.decorators.csrf import requires_csrf_token

# Create your views here.
reload(sys)
sys.setdefaultencoding("utf-8")

# @requires_csrf_token
def index(request):
    # cookies1=request.COOKIES
    global opener
    cookie = cookielib.CookieJar()  # 储存获取到的cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    CaptchaUrl = "http://jwgl.nwsuaf.edu.cn/academic/getCaptcha.do"  # 验证码图片URL
    picture = opener.open(CaptchaUrl).read()



    # session = requests.session()
    # image = session.get(CAPTCHA_URL)
    # request.session['JSESSIONID'] = session.cookies['JSESSIONID']
    # print (type(image.content))
    captcha = base64.b64encode(picture)

    print cookie
    return render(request, 'index.html',{'captcha': captcha,'cookie':cookie})

def jwlogin(request):
    query=request.POST.get('username','')
    query2=request.POST.get('password','')
    query3=request.POST.get('captcha','')
    print (query)
    print (query2)
    print (query3)

    res=NWAFU(query,query2,query3).getpage()
    # print (res)
    return render(request,'test1.html',locals())

# class NPU:
#     def __init__(self, name, passwd):
#         # 登录URL
#         self.loginUrl = 'http://bbs.nwafulive.cn/'
#         # 成绩URL
#         self.gradeUrl = 'http://free.hwss.pw/user/'
#         self.cookies = cookielib.MozillaCookieJar('cookie.txt')
#         self.postdata = urllib.urlencode({
#             'email': name,
#             'passwd': passwd,
#             'remember_me': 'week',
#             # 'session_locale': 'zh_CN',
#         })
#         # 成绩对象数组
#         # 构建opener
#         self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
#
#     # 获取本学期成绩页面
#     def getPage(self):
#         try:
#             request = urllib2.Request(url=self.loginUrl, data=self.postdata)
#             # 建立连接，模拟登陆
#             result = self.opener.open(request)
#             self.cookies.save(ignore_discard=True, ignore_expires=True)
#             # 打印登录内容
#             # print 'asdf'
#             # print result.read()
#             # 获得成绩界面的html
#             result = self.opener.open(self.gradeUrl)
#             return result.read().decode('utf-8')
#         except urllib2.URLError, e:
#             print '连接失败'
#             if hasattr(e, "reason"):
#                 print "error", e.reason
#                 return None


# def gg(uemail,upasswd):
#         # cookie = cookielib.CookieJar()  # 储存获取到的cookie
#         # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#
#         loging_data = urllib.urlencode([
#             ('email', uemail),
#             ('passwd', upasswd),
#             ('remember_me', 'week')])  # POST用到的数据
#
#         # 请求头
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
#             'Host': 'free.hwss.pw',
#             # 'Origin':'http://free.hwss.pw',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#             # 'Accept-Encoding':'gzip, deflate',
#             'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
#             'Referer': 'http://free.hwss.pw/user/login.php',
#             # Cookie:	user_pwd=b34c9391df229cd8a2a3a1c9d8c77cb8e489349c312f6; uid=429; user_email=804194244%40qq.com; __cfduid=d8ef321cdcb20f2206c28f8e37dc4e4d91486381093; PHPSESSID=m5s0fkchm31bvs76sqo3nt4tb2',
#             'Connection': 'keep-alive',
#             # 'X-Requested-With':'XMLHttpRequest',
#             # 'Content-Length':'57',
#             # 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#             'Upgrade-Insecure-Requests': '1',
#             # 'Cache-Control':'max-age=0'
#         }
#         # 构造request
#         req = urllib2.Request(url='http://free.hwss.pw/user/_login.php',
#                               data=loging_data.encode(encoding='utf-8'),
#                               headers=headers)
#         try:
#             # req1 = session.post('http://ss.hwss.pw/user/login.php', data=loging_data, headers=headers)
#             result = opener.open(req)  # 访问请求的链接
#
#             print 'tttttttttttt'
#             # print(result.read().decode('utf-8'))
#         except urllib2.HTTPError:
#             print("connect failed")
#         try:
#             # session.get('http://ss.hwss.pw/checkin.php', headers=headers)
#             # result=opener.open('http://free.hwss.pw/user/index.php')#进入教务系统个人成绩信息界面
#             print '2222'
#             req = urllib2.Request(url='http://free.hwss.pw/user/',
#                                   data=loging_data.encode(encoding='utf-8'),
#                                   headers=headers)
#             result2 = opener.open(req)
#
#             return result2.read().decode('utf-8')
#             # print (result2.read().decode('utf-8'))
#
#             # print(result.read().decode('utf-8'))
#             # page=result.read()
#             # print (page)
#             # f=file("score.html","w") #写入一个html文件
#             # f.write(page)
#             # f.close()
#
#
#         except Exception, e:
#             print str(e)
#             return "ssss"
class NWAFU:
    def __init__(self, uname, upwd,capt):
    # def login1(uname,upwd,capt):

        # self.cookie = cookielib.CookieJar()  # 储存获取到的cookie
        # print self.cookie
        print 1111111
        # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        self.loging_data = urllib.urlencode([
            ('j_username', uname),
            ('j_password', upwd),
            ('j_captcha', capt)])  # POST用到的数据

        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' +
                          '(KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36'
        }

    def getpage(self):
        # 构造request
        req = urllib2.Request(url='http://jwgl.nwsuaf.edu.cn/academic/j_acegi_security_check',
                              data=self.loging_data.encode(encoding='utf-8'),
                              headers=self.headers)

        try:
            # req1 = session.post('http://jwgl.nwsuaf.edu.cn/academic/j_acegi_security_check', data=self.loging_data, headers=self.headers)
            result = opener.open(req)  # 访问请求的链接

        except urllib2.HTTPError:
            print("connect failed")
        try:
            result = opener.open(
                'http://jwgl.nwsuaf.edu.cn/academic/student/currcourse/currcourse.jsdo?groupId=&moduleId=2000')  # 进入教务系统个人成绩信息界面
            page = result.read().decode('gbk')

            return page

        except urllib2.HTTPError:
            print("error")


def get_captcha(request):
        CAPTCHA_URL = "http://jwgl.nwsuaf.edu.cn/academic/getCaptcha.do"
        session = requests.session()
        image = session.get(CAPTCHA_URL)
        request.session['JSESSIONID'] = session.cookies['JSESSIONID']
        print type(image.content)
        return image.content
def register(request,self):
        if request.method == "GET":
            captcha =self.get_captcha(request)
            return render(request, 'index.html', {'captcha': captcha})