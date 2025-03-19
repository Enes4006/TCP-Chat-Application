import socket

host="127.0.0.1"
port=5500

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind((host,port))

s.listen()

conn,addr=s.accept()

if conn:
    print(f"Bir kullanıcı bağlandı {addr}")
    
    while 1:
    
        ldata=conn.recv(1024)
        
        if ldata.decode("utf-8")=="exit":
            conn.close()
            
        else:
            print(ldata.decode("utf-8"))
            
        
        data=input("message: ")
        
        if data.encode("utf-8")=="exit":
            conn.close()
        else:
            conn.sendall(data.encode("utf-8"))
            
               
# bu uygulamalarda ilk önce server sonra istemciden veya tam tersi 
# mesaj istendiği için ilk önce dinleme sonra alma yapılır veya tam tersi 