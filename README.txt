####by cw#####
login_main_v1.1.py
#2016-06-04

һ �������
  1.1 �ļ��ֲ�
  login_user.jpg   ����ͼ��Ϣ
  README.txt
  login_main_v1.1.py  ������
  user_config.conf   �����ļ�


��������˵����
1.���г���login_main.py
2.�����û��������룬Input_check()����û������Ƿ���ȷ���û��������벻��Ϊ�գ���������6λ������������Ϲ淶�����ص���¼���漴������
3.����ϸ���ô��ִ��Login_check(),����û��Ƿ�������������������˳������û��������������һ��
4.��������û�Login_passwd_check()����¼�û����Ƿ���ȷ�������ȷ���͸�����ӭ����
5.����û��������벻�ԣ�ִ��Login_Limit_Check()��ô�ͷ��ص���¼���棬��������1�����������������3�Σ���ô�����û����˳�
��������չ�����ݣ�
ע���û���mysql
�����û����Դ洢��memcached/redis
webչ�ִι���
���ݺ����ۺ���ϰ�����Ľ�


cat user_config.conf 
#username,password,status,lock_count
chenwei ,chenwei ,N,0 
chenwei2,chenwei,Y,0
chenwei3,chenwei,Y,0

#######end README.txt###############


