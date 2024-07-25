import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import json
from selenium.webdriver.common.by import By
import os
import re

headers = {
    #配置你的headers,至少包含'User-Agent'、 'Accept'和'Accept-Language'，你可以在网上找到有关教程
}
cookies_of_download = '#配置你下载使用的浏览器cookies路径，不需要高清视频可以将此项置空'
path_of_download = '#配置你视频的下载路径，脚本会自动在这个路径下以你输入的uid为名称创建新的文件夹，如果你想以其他规则命名新文件夹，请自行修改'
with open('NameList.txt', 'r') as file:
    for line in file:
        uid = line.strip()  
        print(f'Processing user with ID: {uid}')
        option=webdriver.ChromeOptions() #使用chrome浏览器，若想使用其他浏览器请自行修改
        option.add_argument('--headless')
        option.add_argument("--log-level=3")
        option.add_argument("--disable_notifications")
        url = f'https://space.bilibili.com/{uid}/video?tid=0&pn=1&keyword=&order=pubdate'
        response = requests.get(url,headers=headers)

        browser = webdriver.Chrome(options=option)
        browser.get(f'{url}')
        sleep(5)
        browser.delete_all_cookies()
        with open('jsoncookie.json','r') as f:
            ListCookies = json.loads(f.read())
        for cookie in ListCookies:
            browser.add_cookie({
                'domain': '.bilibili.com',
                'name': cookie['name'],
                'value': cookie['value'],
                'path': '/',
                'expires': None,
                'httponly': False,
            })

        browser.get(f'{url}')
        
        sleep(5)

        print(response.status_code)

        if response.status_code == 200:
            page_source = browser.page_source
            with open(f'{uid}.html', 'w', encoding='utf-8') as f:
                f.write(page_source)

            with open(f"{uid}.html", "r",encoding='utf-8') as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            tags = soup.find_all(class_='be-pager-total')
            tag=tags[0]
            last_page_element = tag.text[2:-2]
            print(last_page_element)
            if last_page_element:
                last_page = int(last_page_element)
            else:
                print("无法找到最后一页的页码")
                continue
            for page in range(1, last_page+1):
                url = f'https://space.bilibili.com/{uid}/video?tid=0&pn={page}&keyword=&order=pubdate'
                response = requests.get(url,headers=headers)
                if response.status_code == 200:
                    browser.get(f'{url}')
                    sleep(5)
                    page_source=browser.page_source
                    with open(f'{uid}{page}.html', 'w', encoding='utf-8') as f:
                        f.write(page_source)
                    with open(f"{uid}{page}.html", "r",encoding='utf-8') as file:
                        html_content = file.read()
                    elements = re.findall(r'data-aid="([^"]*)"', html_content)
                    data_aid_list = [element for element in elements]
                    with open(f'data_aid_list_{uid}_page{page}.txt', 'w') as tmpfile:
                        for data_aid in data_aid_list:
                            tmpfile.write(data_aid + '\n')
                else:
                    print(f"Error code {response.status_code}")
            with open(f'links_{uid}.bat', 'w') as script_file:
                for page in range(1, last_page+1):
                    with open(f'data_aid_list_{uid}_page{page}.txt', 'r') as bvcode_file:
                        for bvcode in bvcode_file:
                            bvcode = bvcode.strip()
                            if cookies_of_download!='':
                                script_file.write(f'you-get {cookies_of_download} -o {path_of_download}\\{uid} https://www.bilibili.com/video/{bvcode}\n')
                            else:
                                script_file.write(f'you-get -o {path_of_download}\\{uid} https://www.bilibili.com/video/{bvcode}\n')
                        folder_path = f"{path_of_download}\\{uid}"
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
            for page in range(1,last_page+1):
                txttmpPath = f"data_aid_list_{uid}_page{page}.txt"
                htmltmpPath = f"{uid}{page}.html"
                os.remove(txttmpPath)
                os.remove(htmltmpPath)
            os.remove(f"{uid}.html")        
            with open('BatList.txt', 'a') as batlist:
                batlist.write(f'links_{uid}.bat\n')
        else:
            print(f"Error code {response.status_code}")

print('.bat生成完成')