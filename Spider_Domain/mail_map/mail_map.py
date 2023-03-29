import re
import sys
import requests
import urllib3
urllib3.disable_warnings()
import pandas as xcsv


def mail_map(mail):
    try:
        url="https://www.skymem.info/srch?q="
        fast="&ss=srch"
        all=url+mail+fast
        all=all.replace("\n","")
        rep=requests.get(all,verify=False,timeout=2)
        if "did not match any documents" in rep.text:
            prmail=mail.replace("\n","")
            print(prmail+": 不存在泄露的邮箱")
        else:
            #第一层正则
            re1 = re.compile(r'@(.*?)</a>')
            re2 = re1.findall(rep.text)
            #长度
            # lenth=len(re2)
            # 匹配数量
            re1_num = re.compile(r"<title>(.*?)</title>")
            re2_num = re1_num.findall(rep.text)
            num=re2_num[0]
            re3_num =re.compile(r'\d+')
            re4_num =re3_num.findall(num)
            numall=re4_num[0]
            printnum=mail+":邮箱数量:"+numall+ " 最大免费数量为：25条，如果超过25条，请自行去0.zone查询"
            printnum=printnum.replace("\n","")
            print(printnum)
            #匹配加密id
            re1_id = re.compile(r"Doc.DomainEmails.IdEntity='(.*?)'")
            re2_id = re1_id.findall(rep.text)
            mailid=re2_id[0]
            numall=int(numall)
            if numall < 10:
                xcsv_mail = []
                for email in re2:
                    # 第二层正则
                    pa = r'>\S+'
                    re2_mail = re.findall(pa, email)
                    result = re2_mail[0]
                    result = result.replace(">", "")
                    xcsv_mail.append(result)
                    req_xcsv_dict = {mail+" "+str(numall): xcsv_mail}
                    req_data = xcsv.DataFrame(req_xcsv_dict)
                    remail = mail.replace("\n", "")
                    path=remail+'.csv'
                    req_data.to_csv(path)   # 将请求的写入到csv文件
            else:
                xcsv_mail = []
                url2 = "https://www.skymem.info/domain/"
                fast2 = "?p="
                for i in range(3):
                    ai=i+1
                    ai=str(ai)
                    allid = url2 + mailid+ fast2+ai
                    allid = allid.replace("\n", "")
                    repid=requests.get(allid,verify=False,timeout=2)
                    # 第一层正则
                    re1 = re.compile(r'@(.*?)</a>')
                    re2 = re1.findall(repid.text)
                    #第二层
                    for email in re2:
                        # 第二层正则
                        pa = r'>\S+'
                        re2_mail = re.findall(pa, email)
                        result = re2_mail[0]
                        result = result.replace(">", "")
                        xcsv_mail.append(result)
                        req_xcsv_dict = {mail: xcsv_mail}
                        req_data = xcsv.DataFrame(req_xcsv_dict)
                        remail=mail.replace("\n","")
                        path =remail + '.csv'
                        req_data.to_csv(path)  # 将请求的写入到csv文件
    except Exception as e:
        print(e)



def for_domain(txt):
    f =open(txt)
    f=f.readlines()
    for mail in f:
        mail_map(mail)

def do_domain(do):
    mail_map(do)


def help():
    p='''
    python3 mail_map.py -f <url.txt>
    python3 mail_map.py -d <domain>
    '''
    print(p)


if __name__=="__main__":

    try:
        cmd1 = sys.argv[1]
        cmd2 = sys.argv[2]
        if "f" in cmd1:
            for_domain(cmd2)
        elif "d" in cmd1:
            do_domain(cmd2)
        else:
            help()
    except:
        help()
        print("")

    # print(xcsv_mail)
    # print(xcsv_num)