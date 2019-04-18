import tkinter as tk
from tkinter import *
import dict_proc

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        pad=0
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
        self.pack()
        self.create_widgets()

    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom
        
    def create_widgets(self):
        self.text_fld = tk.Entry(self)
        self.text_fld.pack(side="top")

        self.go_btn = tk.Button(self)
        self.go_btn["text"] = "GO!"
        self.go_btn["command"] = self.defines
        self.go_btn.pack(side="top")

        self.text_area = tk.Text(self, height=30, width=120)
        self.scroll = tk.Scrollbar(self)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.back = tk.Button(self)
        self.back["text"] = "Back"
        self.back["command"] = self.go_back
        
    def defines(self):
        self.text_fld.pack_forget()
        self.go_btn.pack_forget()
        self.back.pack(side="bottom")

        self.text_area.pack(side="left")
        self.scroll.pack(side="right")
        self.scroll.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scroll.set)

        defn = dict_proc.define(self.text_fld.get())
        string_of_defn = ""
        if defn is None: 
            string_of_defn = "Result not found!\nTip: Use Nouns!"
        else:
            string_of_defn += "Definations: \n"
            counter = 1
            for definations in defn:
                string_of_defn += str(counter) + ": " + definations[0] + "\n"
                counter += 1

        self.text_area.insert(INSERT, string_of_defn)
    
        #print(type(self.text_fld.get()))

    def go_back(self):
        self.back.pack_forget()
        self.scroll.pack_forget()
        self.text_area.delete(1.0, END)
        self.text_area.pack_forget()
        self.text_fld.pack(side="top")
        self.go_btn.pack(side="top")


root = tk.Tk()
app = Application(master=root)

app.mainloop()