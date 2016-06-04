#/bin/python
#coding=utf-8
#by cw
#2016-06-03

import os

User_conf_file='D:\chenwei\data\user_config.conf'
User_conf_tmp='D:\chenwei\data\user_config_tmp.conf'
Count_limt=0



def Welcome_Main():
    print '''
    Welcome to Python World!!!!!!!

    by cw

    '''

def Read_Config_File(file,username):
    '''
    :param file: 配置文件
    :param username: 输入的用户名
    :return: 读取用户配置文件，返回用户名，锁定状态
    '''
    fn=open(file)
    User_conf=''
    Status=''
    Count=''
    Passwd=''
    for line in fn:
        if line.split(',')[0].strip() == username: #根据用户名去查找,需要注意去掉空格
          User_conf=line.split(',')[0]   #返回用户名
          Passwd=line.split(',')[1]  #返回密码
          Status=line.split(',')[2]  #返回状态
          Count=line.split(',')[3]  #返回次数
    fn.close()
    return (User_conf,Passwd,Status,Count)  # 返回状态

def Input_Check(username,passwd):
    Flag=True
    if len(username) == 0:
        print 'The username is NULL,please input againt!!!'
        Flag=False
    if len(passwd) == 0:
        print 'The passwd is NUll,please input againt!!!!'
        Flag=False
    if len(passwd) < 6:
        print "The passwd length is not enough!"
        Flag=False
    return Flag

def Login_Lock_Check(status):
     if status == 'Y':
         return False    #the user don't locked
     else:
         return True    #the user locked

def Lock_Usered(file,file_tmp,username):
    fn = open(file)
    fn_tmp = open(file_tmp, 'a')
    new_line = []
    for line in fn.readlines():    #读取配置文件的每一行
        if line.split(',')[0].strip() == username:
            new_line.append("%s ," % username)
            new_line.append("%s ," % line.split(',')[1].strip())
            new_line.append('N,')
            new_line.append('%s \n' % line.split(',')[3].strip())
            fn_tmp.writelines(new_line)
            continue
        fn_tmp.writelines(line)
    fn.close()
    fn_tmp.close()
    os.remove(file)
    os.rename(file_tmp, file)


while True:
    Config_list=''
    Name = raw_input('Please input your name: ')
    Passwd = raw_input('Please input your password: ')

    if Input_Check(Name,Passwd) == False :     #检查用户名和密码的规范性
        continue
    else:
        Config_list=Read_Config_File(User_conf_file,Name)    #返回配置文件里面的内容
    if Login_Lock_Check(Config_list[2]): #返回用户状态
        print "The user is locked"
        exit()
    else:
        if Name == Config_list[0] and Passwd == Config_list[1]:
           Welcome_Main()
           exit()
        else:
            Count_limt = Count_limt + 1
            if Count_limt == 1:
                print 'The Username or password is not right,you maybe try two!!!'
            if Count_limt == 2:
                print 'The Username or password is not right,you maybe try one!!!'
            if Count_limt >= 3:
                Lock_Usered(User_conf_file,User_conf_tmp,Name)
                print "user locked!!!"
                exit()







