from socket import *
# subject = "I love computer networks!"
# msg = "I love computer networks! \r\n.\r\n"
# toAddress = "1804817170@qq.com"

def sendData(subject,msg,toAddress):
    #编辑邮件内容
    msg=msg+' \r\n.\r\n'
    contentType = "text/plain"
    #与邮件服务器建立TCP连接
    mailServer = "smtp.qq.com"
    fromAddress = "1804817170@qq.com"

    username = "MTgwNDgxNzE3MEBxcS5jb20="
    password = 'c3l4aG1mdGlmcXBxZWdpZw==' #syxhmftifqpqegig

    s = socket(AF_INET, SOCK_STREAM) #创建客户连接套接字
    s.connect((mailServer, 587)) #进行连接
    recv = s.recv(1024).decode() #接收报文
    print("创建客户连接套接字: ",recv)

    heloCommand = 'HELO winis\r\n'
    s.send(heloCommand.encode()) #开始与服务器的交互
    recv1 = s.recv(1024).decode()
    print('开始与服务器的交互: ',recv1)

    s.sendall('AUTH LOGIN\r\n'.encode()) #发送"AUTH LOGIN"命令验证身份
    recv = s.recv(1024).decode()
    print('发送"AUTH LOGIN"命令验证身份: ',recv)

    s.sendall((username + '\r\n').encode()) #发送经过base64编码的用户名
    recv = s.recv(1024).decode()
    print('发送经过base64编码的用户名: ',recv)

    s.sendall((password + '\r\n').encode()) #发送经过base64编码的密码
    recv = s.recv(1024).decode()
    print('发送经过base64编码的密码: ',recv)

    s.sendall(('MAIL FROM: <' + fromAddress + '>\r\n').encode()) #发送"MAIL FROM"命令，并包含发件人邮箱地址
    recv = s.recv(1024).decode()
    print('发送"MAIL FROM"命令: ',recv)

    s.sendall(('RCPT TO: <' + toAddress + '>\r\n').encode()) #发送"RCPT TO"命令，并包含收件人邮箱地址
    recv = s.recv(1024).decode()
    print('发送"RCPT TO"命令: ',recv)

    s.send('DATA\r\n'.encode()) #发送"DATA"命令，表示即将发送邮件内容
    recv = s.recv(1024).decode()
    print('发送"DATA"命令: ',recv)

    #编辑整合邮件内容message
    message = 'from:' + fromAddress + '\r\n' + 'to:' + toAddress + '\r\n' + 'subject:' + subject + '\r\n' + 'Content-Type:' + contentType + '\t\n' + '\r\n' + msg
    s.sendall(message.encode()) #发送邮件内容
    recv = s.recv(1024).decode()
    print('发送邮件内容: ',recv)

    s.sendall('QUIT\r\n'.encode()) #发送"QUIT"命令，断开与邮件服务器的连接
    s.close()