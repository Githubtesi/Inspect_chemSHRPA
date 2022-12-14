#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.4
#  in conjunction with Tcl version 8.6
#    Aug 12, 2022 07:08:12 PM JST  platform: Windows NT

import tkinter as tk
from gui import chem_support


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = 'gray40'  # X11 color: #666666
        _ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
        _ana2color = 'beige'  # X11 color: #f5f5dc
        _tabfg1 = 'black'
        _tabfg2 = 'black'
        _tabbg1 = 'grey75'
        _tabbg2 = 'grey89'
        _bgmode = 'light'

        top.geometry("431x272+826+288")
        top.minsize(120, 1)
        top.maxsize(3004, 2399)
        top.resizable(1, 1)
        top.title("chemSHRPA検索")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.07, rely=0.147, height=27, relwidth=0.705)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")
        self.Entry1.delete(0, tk.END)
        self.Entry1.configure(state='readonly')

        self.Entry2 = tk.Entry(self.top)
        self.Entry2.place(relx=0.07, rely=0.368, height=27, relwidth=0.705)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")
        self.Entry2.delete(0, tk.END)
        self.Entry2.configure(state='readonly')

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.812, rely=0.147, height=24, width=47)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=chem_support.BT_select_serch_folder)
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''参照''')

        self.Button2 = tk.Button(self.top)
        self.Button2.place(relx=0.812, rely=0.368, height=24, width=47)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(command=chem_support.BT_select_output_file)
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''参照''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.07, rely=0.074, height=13, width=104)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''検索対象のフォルダ''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.07, rely=0.294, height=13, width=84)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''出力先ファイル''')

        self.Button3 = tk.Button(self.top)
        self.Button3.place(relx=0.673, rely=0.846, height=24, width=57)
        self.Button3.configure(activebackground="beige")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(command=chem_support.BT_output)
        self.Button3.configure(compound='left')
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''出力''')

        self.Button4 = tk.Button(self.top)
        self.Button4.place(relx=0.835, rely=0.846, height=24, width=57)
        self.Button4.configure(activebackground="beige")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(command=chem_support.BT_cancel)
        self.Button4.configure(compound='left')
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''キャンセル''')


def start_up():
    chem_support.main()


if __name__ == '__main__':
    chem_support.main()
