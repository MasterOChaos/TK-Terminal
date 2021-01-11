import tkinter as tk
import tkinter.ttk as ttk
import os
class mn:
 def __init__(self,master=None):
  self.rt=tk.Frame(master)
  self.ent=tk.Entry(self.rt)
  self.ent.config(background='#000000',borderwidth='0',cursor='arrow',exportselection='true')
  self.ent.config(foreground='#ffffff',insertborderwidth='0',selectbackground='#ffffff',selectborderwidth='0')
  self.ent.config(selectforeground='#000000',takefocus=True,width='50')
  self.ent.pack(side='top')
  self.ent.config(highlightthickness='0')
  self.log=tk.Text(self.rt)
  self.log.config(background='#000000',foreground='#ffffff',height='10',selectbackground='#ffffff')
  self.log.config(selectforeground='#000000',width='50')
  self.log.pack(side='top')
  self.log.config(highlightthickness='0')
  self.rt.config(height='200',width='200')
  self.rt.pack(side='top')
  def kp(event):
   cmd=self.ent.get() + " > log.txt"
   os.system(cmd)
   self.ent.delete(0,'end')
   self.log.delete(1.0,"end")
   file = open("log.txt")
   readfile = file.read()
   self.log.insert(1.0, readfile)
   print(readfile)
   file.close
   os.remove("log.txt")
  self.ent.bind_all('<Return>',kp)
  self.mainwindow=self.rt
 def run(self):
  self.mainwindow.mainloop()
if __name__=='__main__':
 import tkinter as tk
 root=tk.Tk()
 root.title("TK TERMINAL")
 root.iconphoto(False, tk.PhotoImage(file='icon.png'))
 app=mn(root)
 app.run()


