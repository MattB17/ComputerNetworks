import socket
import ssl

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

mailserver = "smtp.gmail.com"
mailserverPort = 587

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((mailserver, mailserverPort))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

clientSocket.send('HELO Matt\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

clientSocket.send('STARTTLS\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

clientSocketSSL = ssl.wrap_socket(clientSocket)

clientSocketSSL.send('HELO Matt\r\n'.encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

clientSocketSSL.send('MAIL FROM: <matt.buckley1755@gmail.com>\r\n'.encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')


clientSocketSSL.send("RCPT TO: <mbuckley@cs.toronto.edu>\r\n".encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')


clientSocketSSL.send("DATA\r\n".encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '354':
    print('354 reply not received from server.')

clientSocketSSL.send(msg.encode())
clientSocketSSL.send(endmsg.encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '250':
    print('250 reply not received from server.')

clientSocketSSL.send("QUIT\r\n".encode())
recv = clientSocketSSL.recv(1024).decode()
print(recv)
if recv[:3] != '221':
    print('221 reply not received from server.')
