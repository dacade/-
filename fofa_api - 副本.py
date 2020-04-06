# -*- coding: utf-8 -*-
import argparse
import time
import requests
import json
import base64
import pandas as pd
#消除提示
requests.packages.urllib3.disable_warnings()


def fofa_work(fofa_search,size):
    start=time.time()
    fofa_sql=fofa_search
    base64_str = base64.b64encode(fofa_sql.encode())
    fofa_size =size
    url = f'https://fofa.so/api/v1/search/all?email={fofa_name}&key={fofa_key}&size={fofa_size}&page=1&fields=ip,host,port,domain,title,country,province,city,country_name,server,protocol,banner,lastupdatetime&qbase64={str(base64_str)[2:-1]}'
    rs = requests.get(url, verify=False, headers=headers)
    rs_text = rs.text
    res = json.loads(rs_text)
    error = res['error']
    if error:
        errmsg = res['errmsg']
        if '401 Unauthorized' in errmsg:
            print('用户名或API 无效！或者是该账户未充值升级vip会员')
            exit(1)
        else:
            print('GG')
            exit(1)
    else:
        ips=[]
        hosts=[]
        ports=[]
        domains=[]
        titles=[]
        countrys=[]
        provinces=[]
        cities=[]
        country_names=[]
        servers=[]
        protocols=[]
        # banners=[]
        lastupdatetimes=[]
        for i in res['results']:
            ip=i[0]
            host=i[1]
            port=i[2]
            domain=i[3]
            title=i[4]
            country=i[5]
            province=i[6]
            city=i[7]
            country_name=i[8]
            server=i[9]
            protocol=i[10]
            banner=i[11]
            lastupdatetime=i[12]

            ips.append(ip)
            hosts.append(host)
            ports.append(port)
            domains.append(domain)
            titles.append(title)
            countrys.append(country)
            provinces.append(province)
            cities.append(city)
            country_names.append(country_name)
            servers.append(server)
            protocols.append(protocol)
            # banners.append(banner)
            lastupdatetimes.append(lastupdatetime)
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        datess=pd.DataFrame({'ip':ips,'host':hosts,'port':ports,'domain':domains,'title':titles,'country':countrys,'province':provinces,'city':cities,'country_name':country_names,'server':servers,'protocol':protocols,'lastupdatetime':lastupdatetimes})
                if ':' in fofa_search:
            fofa_search = fofa_search.replace(':', '：')
        if '?' in fofa_search:
            fofa_search = fofa_search.replace('?', '？')
        if '<' in fofa_search:
            fofa_search = fofa_search.replace('<', '《')
        if '>' in fofa_search:
            fofa_search = fofa_search.replace('>', '》')
        if '\\' in fofa_search:
            fofa_search = fofa_search.replace('\\', '。')
        if '/' in fofa_search:
            fofa_search = fofa_search.replace('/', '。')
        if '|' in fofa_search:
            fofa_search = fofa_search.replace('|', '。')
        if '*' in fofa_search:
            fofa_search = fofa_search.replace('*', '。')
        if '"' in fofa_search:
            fofa_search = fofa_search.replace('"', '\'')
        datess.to_csv(f'{now}'+'('+f'{fofa_search}'+').csv',encoding='utf_8_sig')
        stop=time.time()
        timess=stop-start
        print("Download successed,Spent time: "+str(timess))


if __name__ == '__main__':
    # 用户email
    fofa_name = ''
    # FOFA 用户key
    fofa_key = ''
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    parser = argparse.ArgumentParser(description='FOFA API下载')
    parser.add_argument('-s','--fofa_search',help='FOFA 查询语句')
    parser.add_argument('-n', '--size', help='每页数量，fofa默认为 10000，使用该脚本时必须添加-n参数指定数目', type=int, default=10)
    args = parser.parse_args()
    size=args.size
    fofa_search = args.fofa_search
    if fofa_search:
        fofa_work(fofa_search,size)
    else:
        parser.print_help()
