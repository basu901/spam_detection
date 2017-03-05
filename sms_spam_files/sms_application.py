# -*- coding: UTF-8 -*-
from Tkinter import *
import test

class Test(Frame):
    text=""
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.parent=parent
        self.initUI()
        

    def initUI(self):
        self.parent.title("SPAM FILTER")
        self.pack(fill="both",expand=True)
        frame1=Frame(self)
        frame1.pack(fill=X)
        label_entry=Label(frame1,text="ENTER SINGLE SMS",width=20)
        label_entry.pack(expand=True,pady=10)
        frame2=Frame(self)
        frame2.pack(fill="x")
        self.input_txt=Text(frame2,height=10)
        self.input_txt.pack(fill="x",pady=5,padx=5,expand=True)
        frame3=Frame(self)
        frame3.pack(fill="x",expand=True)
        redbutton=Button(frame3,text="CHECK",width=10,command=self.work_on_input)
        redbutton.pack(side="top",anchor="center")
        frame4=Frame(self)
        frame4.pack(fill="both",expand=True)
        label_verdict=Label(frame4,text="Verdict :")
        self.label_process=Label(frame4,text="Waiting for input")
        label_verdict.pack(side=LEFT,padx=5)
        self.label_process.pack(side=LEFT)
        frame5=Frame(self)
        frame5.pack(fill="x",expand=True)
        exit_button=Button(frame5,text="EXIT",command=self.quit,width=10)
        exit_button.pack(side="right",padx=5,pady=5)


    def work_on_input(self):
        self.text=(self.input_txt.get("1.0",'end-1c'),)
        s=self.text[0].lstrip()
        pos=len(s)
        if s.find('\n')>-1:
            pos=s.find('\n')

        txt=s[:pos]
        res=test.main(txt)
        if pos!=len(s):
            if res==1:
                self.label_process.config(text="Non Spam(Only first sms was checked)")
            else:
                self.label_process.config(text="Spam(Only first sms was checked)")
        else:
            if res==1:
                self.label_process.config(text="Non Spam")
            else:
                self.label_process.config(text="Spam")
    

        
def main():
    root=Tk()
    root.geometry("300x300+300+300")
    app=Test(root)  
    root.mainloop()
    
def me(self):
    return True

if __name__=='__main__':
    main()
