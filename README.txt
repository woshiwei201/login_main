####by cw#####
login_main_v1.1.py
#2016-06-04

一 程序介绍
  1.1 文件分布
  login_user.jpg   流程图信息
  README.txt
  login_main_v1.1.py  主程序
  user_config.conf   配置文件


程序运行说明：
1.运行程序login_main.py
2.输入用户名和密码，Input_check()检查用户输入是否正确，用户名和密码不能为空，密码至少6位数，如果不符合规范，返回到登录界面即可输入
3.如果合格，那么就执行Login_check(),检查用户是否被锁定，如果锁定，则退出，如果没有锁定，继续下一步
4.继续检查用户Login_passwd_check()，登录用户名是否正确，如果正确，就给出欢迎界面
5.如果用户名和密码不对，执行Login_Limit_Check()那么就返回到登录界面，计数器加1，如果计数器大于了3次，那么锁定用户并退出
后续可扩展的内容：
注册用户到mysql
锁定用户可以存储到memcached/redis
web展现次功能
根据后面综合练习继续改进


cat user_config.conf 
#username,password,status,lock_count
chenwei ,chenwei ,N,0 
chenwei2,chenwei,Y,0
chenwei3,chenwei,Y,0

#######end README.txt###############


