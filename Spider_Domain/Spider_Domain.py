import sys
import socket
import pandas as xcsv
import requests
import re

spider_domain='''
                     $$                                                           
  $$$         $$     $$                 $$$$$                            $$       
 $$  $               $$                 $$  $$                                    
 $$    $$$$$  $$  $$$$$  $$$$  $$ $$    $$   $$  $$$$  $$$$$ $$$   $$$$  $$ $$$$$ 
  $$$  $$  $$ $$ $$  $$ $$  $$ $$$$$    $$   $$ $$  $$ $$  $$  $$     $$ $$ $$  $$
    $$ $$  $$ $$ $$  $$ $$$$$$ $$       $$   $$ $$  $$ $$  $$  $$  $$$$$ $$ $$  $$
 $  $$ $$  $$ $$ $$  $$ $$     $$       $$  $$  $$  $$ $$  $$  $$ $$  $$ $$ $$  $$
  $$$  $$$$$  $$  $$$$$  $$$$$ $$       $$$$$    $$$$  $$  $$  $$  $$$$$ $$ $$  $$ 
       $$                                                                          v1.0.1                       
       $$                                                                         
'''

print('')
print(spider_domain)
print('')

xcsv_domain=[]
xcsv_ip = []
xcsv_title = []
xcsv_code =[]

def req(req_domain):
    d =req_domain
    h = ['http://','https://']
    for http in h:
        url = http+d
        try:
            data =requests.get(url,timeout=2)
            data.encoding = data.apparent_encoding
            data_text =data.text
            code = data.status_code

            re1 = re.compile(r"<title>(.*?)</title>",re.S)
            re2 = re1.findall(data_text)
            # print(f'状态码：{code}')
            if code == 200:
                # print(re2[0])
                xcsv_title.append(re2[0])
                xcsv_code.append(code)
                break
            elif code == 403 or code ==404 or code == 400 or code == 302 or code == 301 or code == 500 or code == 503:
                # print(data)
                xcsv_title.append(data)
                xcsv_code.append(code)
                break
            else:
                xcsv_title.append('No Data')
                xcsv_code.append('')
                break
        except:
            # time.sleep(0.1)
            # pass
            xcsv_title.append('No Data')
            xcsv_code.append('')
            break

def sub_domain(doamin,dic):

        doamin = doamin.replace('www.','')
        doamin = doamin.replace('http://', '')
        doamin = doamin.replace('https://', '')
        doamin = doamin.replace('/', '')

        f = open(dic)  #根据自己的字典修改
        for doamin_one in f :
            doamin_list_one = doamin_one +'.'+ doamin
            doamin_list_one = doamin_list_one.replace('\n','')
            # print(doamin_list_one)
            try:
                ip = socket.gethostbyname(doamin_list_one)
                print(f'[+]子域名{doamin_list_one}存在')

                xcsv_domain.append(doamin_list_one)  # 将domain写入到xcsv_domain列表
                xcsv_ip.append(ip)

                req(doamin_list_one)  # 调用该函数进行请求获取标题以及状态码

                ##以下是存在web服务的子域名进行写入到csv文件
                req_xcsv_dict = {'标题': xcsv_title, '子域名': xcsv_domain, 'IP地址': xcsv_ip, '状态码': xcsv_code}
                req_data = xcsv.DataFrame(req_xcsv_dict)
                req_data.to_csv(doamin + '.csv')  # 将请求的写入到csv文件

            except:
                continue
        # print(f'[-]子域名{doamin_list_one}不存在')

def help():
    print('查看帮助：')
    print('python Spider_Domain.py -h or --help')
    print('python Spider_Domain.py -t  www.yourdomain.com dic_top3000.txt')
    print('python Spider_Domain.py --target  域名 指定字典')

if __name__ == '__main__':
    try:
        cmd1 =sys.argv[1]
        if cmd1 == '--target' or cmd1 == '-t':
            cmd2 =sys.argv[2]
            cmd3 =sys.argv[3]
            sub_domain(cmd2,cmd3)
        else:
            help()
    except:
        help()

