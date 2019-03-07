#图书馆座位自动预约签到系统的部署

作者： w-devin & BinYou

![](http://weimg.idevin.cn/15495488187585.png-rt)

#### 前言

为了考研方便跟舍友一个通宵写了一个图书馆的自动预约签到系统, 由于配置比较麻烦, 一直以来都是自己动手帮别人配置, 想写个教程也一直没有时间, 直到最近才有空梳理一下步骤

#### 准备

1. Ubuntu 16.04的服务器(其他也可)
2. ssh工具

#### 步骤

1. ssh远程到服务器
2. 从 Github `clone` 代码, 并 `cd` 到 `./Seats` 目录下

 ```bash
 git clone https://github.com/w-devin/Seat.git
 cd Seat
 ```
3. 安装并配置好python环境

 ```bash
 sudo apt-get install python3
 sudo apt-get install python3-pip
 sudo pip3 install -r requirements.txt
 ```
4. 安装并配置好 MySQL

 ```bash
 sudo apt-get install mysql-server
 cd Database

 mysql -h localhost -u root -p
 ```
随后建立数据库

 ```sql
 mysql> create database Seats;
 mysql> use Seats;

 mysql> source admin.sql;
 mysql> source rooms.sql;
 mysql> source seats.sql;
 mysql> source tasks.sql;


 mysql> insert into admin values(0, 'wang', '123456');
 #创建管理员账户, 其中第一个数字0是指超级管理员, 超级管理员只能有一个, 能看到并管理其他所有管理员创建的记录, 普通管理员则只能看到和创建自己创建的记录

 exit
 ```
返回上层目录

 ```bash
 cd ../
 ```

5. 按需配置程序
- `runserver.py` 可以设置服务运行的端口号
- `config.py` 可以设置每个任务的执行时间
- `./Seats/db.py` line11 需要配置数据库的主机名和密码（主机名如果按本教程应为localhost）
- `./Seats/templates/index.html` 可以设置网站主页的显示内容

6. 启动服务器
 ```bash
 sudo python3 runserver.py &
 ```
至此, 本系统可以通过访问服务器ip/域名来使用


#### 一点闲话

1. 分工
 - 我负责座位的预约和签到, BinYou负责前端页面
2. 系统存在的一些问题
 - 如果登录时输入的账号密码错误会导致服务器错误, 返回上一页重新输入即可 
 - 新建记录时, 输入的时间的单位为小时, 修改记录时单位则为分钟
 - `msg.log` 为前几项记录的日志和所有记录的密码错误信息
 - 因为本系统是考研期间, 我(Wang)和BinYou通宵赶工制作而来, 可能会存在一些奇怪的bug