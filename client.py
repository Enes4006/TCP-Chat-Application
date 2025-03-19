import socket

host="127.0.0.1"
port=5500

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp protokolü

s.connect((host,port))

while 1:
    data=input("message: ")
    
    if data.encode("utf-8")=="exit":
        print("Bir kullanıcı ayrıldı")
        
    else:
        s.sendall(data.encode("utf-8"))
        
    ldata=s.recv(1024)
    
    if ldata.decode("utf-8")=="exit":
        print(f"Bir kullanıcı ayrıldı {s}")
        
    else:
        print(ldata.decode("utf-8"))
        
        
        
# bu uygulamalarda ilk önce server sonra istemciden veya tam tersi 
# mesaj istendiği için ilk önce dinleme sonra alma yapılır veya tam tersi 