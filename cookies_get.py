import json
from selenium import webdriver
 
driver = webdriver.Edge()
driver.get('https://www.bilibili.com/')
 
'''
打开网页后登录
登录完成后在命令行内按回车
等提示进程已结束，退出代码，看到同级目录下多出一个名为 jsoncookie.json的文件，说明正常工作
'''
 
driver.implicitly_wait(10)
 
input()
dictcookie = driver.get_cookies()
print('dictcookie:',dictcookie)
jsoncookie = json.dumps(dictcookie)
print('jsoncookie:',jsoncookie)

with open('jsoncookie.json','w') as f:
    f.write(jsoncookie)
print('获取cookies成功')
driver.close()