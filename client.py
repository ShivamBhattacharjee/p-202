import socket
from threading import Thread
from tkinter import *

# nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

class gui:
    def __init__(self):
        self.window=Tk()
        self.window.withdraw()
        self.login=Toplevel()
        self.login.title("login screen")
        self.login.config(width=400,height=400)
        self.login.resizable(width=False,height=False)
        self.message=Label(self.login,text="Please login to continue",justify=CENTER,font=("monospace",15))
        self.message.place(relheight=0.15,relx=0.2,rely=0.07)

        self.label=Label(self.login,text="name:",font=("monospace",15))
        self.label.place(relheight=0.2,relx=0.1,rely=0.2)

        self.entry=Entry(self.login,font=("monospace",15))
        self.entry.place(relheight=0.12,relwidth=0.4,relx=0.35,rely=0.2)
        self.entry.focus()

        self.goButton=Button(self.login,text="continue",font=("monospace",15),command=lambda:self.nextpg(self.entry.get()))
        self.goButton.place(relx=0.4,rely=0.55)
        
        self.window.mainloop()

    def nextpg(self,name):
        self.login.destroy()
        self.name=name
        recieve=Thread(target=self.recv)
        recieve.start()

    def recv(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    print(message)
            except:
                print("An error occured!")
                client.close()
                break

g=gui()



# def receive():
#     

# def write():
#     while True:
#         message = '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('utf-8'))

# receive_thread = Thread(target=receive)
# receive_thread.start()
# write_thread = Thread(target=write)
# write_thread.start()
