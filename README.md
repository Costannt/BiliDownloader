# Read me

#### 这是一个B站视频下载工具。

## 功能

#### 爬取多个up主的所有视频

这是闲话*有天网上冲浪的时候，惊觉我的B站收藏夹里的视频很多都失效了，于是想批量保存某些up主的所有视频，防止他们某天突然消失。*

*找了很多工具，要么不好用，要么门槛略高（我是新手，只有一点点C语言基础）。*

*于是在ChatGpt和Google的帮助下，这个工具诞生了*



**这个工具使用Selenium批量抓取视频链接，结合you-get生成批处理文件将视频保存在指定路径**

由于我是小白，各种命名不规范随处可见（其实我根本不知道python怎么命名才规范）。面向对象也是我没接触过的东西。完全不懂。

不过像我一样只会开箱即用的小白应该够用了。

#### 

## 给小白的使用教程

​		-1、你需要安装python，并正确配置。

​			你可以[点击这里](https://www.python.org/)来下载python。请选择较新的版本。

​			你需要安装```requests   beautifulsoup   selenium```才能正常使用这个工具。

​			你可以通过下面三条命令来轻松地安装他们：
​			```pip install requests```

​			```pip install beautifulsoup4```

​			```pip install selenium```

​			**或者你可以参考网络上的相关教程**

​	零、你需要一个Google Chrome浏览器，你可以[点击这里](https://www.google.cn/intl/zh-CN/chrome/)来下载它

​	一、打开```cookies_get.py```，如果一切正常，那么Chrome会打开一个未登录的B站主页。这时，你需要登录你的B站账号。登录成功			后，你可以回到你运行```cookies_get.py```的窗口，键入回车。如果一切正常，等待终端中出现“获取cookies成功”的字样后，此时，			`jsoncookie.json`应位于```cookies_get.py```所在的同级目录。

​	二、打开```biliDownloader.py```,按照注释配置你的headers、下载用的cookies路径以及保存路径

​		1.headers的配置（仍然以Chrome为例）：打开你的Chrome——打开B站——按下F12打开开发者工具——点击”网络“（Network）			——翻到最上面，在左侧”名称“（Name）一栏寻找```www.bilibili.com```（如果没有就按F5刷新一下）——点击```www.bilibili.com```，在右侧点击“标头”（Headers），向下翻找。找到“请求标头”（Request Headers）。你可以在这里找到配置你的			headers需要的一切。

​		2.下载用的cookies路径：这是 you-get 需要调用的参数。根据官方说明，目前只支持两种 `cookie` 格式 即`Mozilla cookies.sqlite` 			和`Netscape cookies.txt`。前者是火狐浏览器的cookies文件，你可以在火狐浏览器上登录你的B站账号并选择“记住密码”，然后			在你的“文件资源管理器”（或者“我的电脑”....）中输入```%appdata%/Mozilla/firefox/profiles```，然后你能够看到一些文件和文件			夹，其中一个文件夹叫做```[8位数字字母].default-release```，打开它，你可以找到```cookies.sqlite```，它正是需要的文件。选中后右			键它，点击“复制文件位置即可”。这里要注意：神奇的Windows路径如果直接输入进去会运行不了（主要是代码缺陷），你需要			将原来的单斜杠```\```变为双斜杠```\\```，注意斜杠的方向。关于第二种格式，尚未尝试过，猜测可以通过将第一步中所得的cookies转			换为.txt来使用，请自行尝试。

​			你可以[点击这里](https://www.firefox.com.cn/)来下载火狐浏览器

​		3.保存路径：你希望视频保存的位置，没什么特别的，只要和上面一样注意斜杠的问题就可以了。需要注意的是：虽然you-get提供			了默认的保存路径，但是由于代码缺陷，如果你将保存路径置空，会出现问题。

​	三、在```NameList.txt```中，每行一个地填入你想要下载的up主的UID，你可以在你浏览器上方的地址栏找到他们的UID。记得保存。

​	四、运行```biliDownloader.py```。等待完成。运行过程中出现```[uid][数字].html```和```data_aid_list_[uid]_page[数字].txt```是正常的，运行			完成后会自行删除。

​	五、如果一切正常，运行完成后，应当生成一系列的```links_[uid].bat```文件，你可以点击```Start.bat```来开始并行的下载每一个up主的		  作品（单个up主的作品是逐个下载的）



# 免责声明

请勿将`biliDownloader`应用到任何可能会违反法律规定和道德约束的工作中，请友善使用`biliDownloader`，遵守蜘蛛协议，不要将`biliDownloader`用于任何非法用途。如您选择使用`biliDownloader`即代表您遵守此协议，作者不承担任何由于您违反此协议带来任何的法律风险和损失，一切后果由您承担
