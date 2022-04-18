from tkinter import *
root=Tk()
def send():
    send=" "+e.get()
    txt.insert(END,"\n"+send)
    if(e.get()=="hi"):
        # end== is constant and literal conktnate
        txt.insert(END,"\n"+"\t"*9+"Hello")
    elif(e.get()=="what are you doing"):
        txt.insert(END,"\n"+"\t"*7+"i am talking with you..")    
    elif(e.get()=="i mean what are you doing in study"):
        txt.insert(END,"\n"+"\t"*7+"i am doing python..")
    elif(e.get()=="where are you live in "):
        txt.insert(END,"\n"+"\t"*7+"i live in pune..")    
    else:
        txt.insert(END,"\n"+"\t"*7+"Sorry i didnt get it")
        # delete==delete user input hi
    e.delete(0,END)   
txt=Text(root)
txt.grid(row=0,column=0,columnspan=1)
# entery=it works as a form of s user input
e=Entry(root,width=200,bg="pink",fg="dark blue")
# fg==fore head    bg==background
# command ==we use butoon funcatility
# butoon ==is keywirds
send=Button(root,text="Send",command=send).grid(row=1,column=1)
# grid==row and column
# get =to get the out put to wight the text wanr txt data
e.grid(row=1,column=0) 
root["bg"]="light blue"
# title 
root.title("CHART BOX")
root.mainloop()