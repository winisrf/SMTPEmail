from socket import *
import re
import base64

def getEmail(j):
    #与邮件服务器建立TCP连接
    mailServer = "smtp.qq.com"
    fromAddress = "1804817170@qq.com"
    toAddress = "1804817170@qq.com"
    username = "1804817170@qq.com"
    password = 'syxhmftifqpqegig'

    s = socket(AF_INET, SOCK_STREAM) #创建连接套接字
    s.connect((mailServer, 110)) #进行连接
    recv = s.recv(1024).decode() #接收报文
    print("创建连接套接字: ",recv)

    s.sendall(('user '+ username + '\r\n').encode()) #发送用户名
    recv = s.recv(1024).decode()
    print('发送用户名: ',recv)

    s.sendall(('pass '+ password + '\r\n').encode()) #发送授权码
    recv = s.recv(1024).decode()
    print('发送授权码: ',recv)

    s.sendall(('list'+'\r\n').encode()) #请求邮件列表
    recv = s.recv(1024).decode()
    print('请求邮件列表: ',recv)

    lists=recv.split('\r\n')

    #for j in range(1,len(lists)-2):
    s.sendall(('retr '+str(j)+'\r\n').encode()) #请求邮件内容
    recvs = b''
    while True:
        tmp = s.recv(1024)
        if not tmp:
            break
        recvs += tmp
        if recvs.endswith(b'\n.\r\n'):
            break

    print('请求第'+str(j)+'封邮件内容: \n',recvs,'\n请求完成\n\n')
    content=decodeEmail(recvs)
    f=open("emailData.txt",'w')
    f.write(str(content))
    f.close()

    s.sendall('QUIT\r\n'.encode()) #发送"QUIT"命令，断开与邮件服务器的连接
    s.close()
    return lists,content

def decodeEmail(recv):
    data = recv.split(b'\r\n')
    print('\n切片处理\n',data)
    content=[]

    p=0
    for i in data:
        # print(i)
        gets = re.findall('(?<=\" <).*?(?=>\')', str(i))
        if gets and p == 0:
            gets1 = re.findall('(?<=From: \"=\?gb18030\?B\?).*?(?=\?=)', str(i))
            bs = base64.b64decode(gets1[0])
            bs = bs.decode('GB2312')
            print('From:', bs,gets[0])
            content.append('发件人：'+ bs+' '+ gets[0])
            p += 1
        elif gets:
            gets2 = re.findall('(?<=To: \"=\?gb18030\?B\?).*?(?=\?=)', str(i))
            bs = base64.b64decode(gets2[0])
            bs = bs.decode('GB2312')
            print('To:', bs,gets[0])
            content.append('收件人：' + bs+' '+ gets[0])
            break

    for i in data:

        gets = re.findall('(?<=Date: ).*?(?=\')', str(i))
        if gets:
            print('Date: ', gets[0])
            content.append('时 间：'+ gets[0])
            break

    for i in data:
        gets = re.findall('(?<=Subject: =\?gb18030\?B\?).*?(?=\?=)', str(i))
        if gets:
            bs = base64.b64decode(gets[0])
            bs = bs.decode('GB2312')
            print('Subject：', bs)
            content.append('主题：'+bs)
            #content+='From:'+gets[0]+'\n'
            break

    p = 0
    for i in range(0, len(data)):
        if data[i] == b'Content-Transfer-Encoding: base64':
            gets = data[i + 2]
            # print(gets)
            bs = base64.b64decode(gets)
            bs = bs.decode('GB2312')
            content.append(bs)
            print(bs)
            break

    print(content)
    return content


#recv=getEmail(1)