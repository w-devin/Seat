#ͼ�����λ�Զ�ԤԼǩ��ϵͳ�Ĳ���

���ߣ� w-devin & BinYou

![](http://weimg.idevin.cn/15495488187585.png-rt)

#### ǰ��

Ϊ�˿��з��������һ��ͨ��д��һ��ͼ��ݵ��Զ�ԤԼǩ��ϵͳ, �������ñȽ��鷳, һֱ���������Լ����ְ��������, ��д���̳�Ҳһֱû��ʱ��, ֱ��������п�����һ�²���

#### ׼��

1. Ubuntu 16.04�ķ�����(����Ҳ��)
2. ssh����

#### ����

1. sshԶ�̵�������
2. �� Github `clone` ����, �� `cd` �� `./Seats` Ŀ¼��

 ```bash
 git clone https://github.com/w-devin/Seat.git
 cd Seat
 ```
3. ��װ�����ú�python����

 ```bash
 sudo apt-get install python3
 sudo apt-get install python3-pip
 sudo pip3 install -r requirements.txt
 ```
4. ��װ�����ú� MySQL

 ```bash
 sudo apt-get install mysql-server
 cd Database

 mysql -h localhost -u root -p
 ```
��������ݿ�

 ```sql
 mysql> create database Seats;
 mysql> use Seats;

 mysql> source admin.sql;
 mysql> source rooms.sql;
 mysql> source seats.sql;
 mysql> source tasks.sql;


 mysql> insert into admin values(0, 'wang', '123456');
 #��������Ա�˻�, ���е�һ������0��ָ��������Ա, ��������Աֻ����һ��, �ܿ����������������й���Ա�����ļ�¼, ��ͨ����Ա��ֻ�ܿ����ʹ����Լ������ļ�¼

 exit
 ```
�����ϲ�Ŀ¼

 ```bash
 cd ../
 ```

5. �������ó���
- `runserver.py` �������÷������еĶ˿ں�
- `config.py` ��������ÿ�������ִ��ʱ��
- `./Seats/db.py` line11 ��Ҫ�������ݿ�������������루��������������̳�ӦΪlocalhost��
- `./Seats/templates/index.html` ����������վ��ҳ����ʾ����

6. ����������
 ```bash
 sudo python3 runserver.py &
 ```
����, ��ϵͳ����ͨ�����ʷ�����ip/������ʹ��


#### һ���л�

1. �ֹ�
 - �Ҹ�����λ��ԤԼ��ǩ��, BinYou����ǰ��ҳ��
2. ϵͳ���ڵ�һЩ����
 - �����¼ʱ������˺��������ᵼ�·���������, ������һҳ�������뼴�� 
 - �½���¼ʱ, �����ʱ��ĵ�λΪСʱ, �޸ļ�¼ʱ��λ��Ϊ����
 - `msg.log` Ϊǰ�����¼����־�����м�¼�����������Ϣ
 - ��Ϊ��ϵͳ�ǿ����ڼ�, ��(Wang)��BinYouͨ���Ϲ���������, ���ܻ����һЩ��ֵ�bug