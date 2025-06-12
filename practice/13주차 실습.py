'''
import tkinter as tk

root_win=tk.Tk()
root_win.title('나의 첫 윈도우')
root_win.geometry('500x200-0+50') #윈도우 크기 및 위치 설정
root_win.resizable(width=False, height=False)]

root_win.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk

def display_options(widget):
    config=widget.configure()
    for key, value in config.items():
        print(f'{key:15s}\t{value}')

widget=ttk.Label(None)
display_options(widget)
'''
'''
import tkinter as tk
from tkinter import ttk

#사용자 정의 함수부
def buildGUI():
    text_label1=ttk.Label(win, text='안녕하세요')

    text_label2=ttk.Label(win)
    text_label2.configure(text='반가워요',
                          foreground='white',
                          background='red',
                          font=('맑은 고딕', 20)
    )

    text_label1.pack()
    text_label2.pack()

#주 프로그램부
win=tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk

#사용자 정의 함수부
def buildGUI():
    s=ttk.Style()
    s.configure('WR.TLabel',
                foreground='white',
                background='red',
                font=('맑은 고딕', 20)
    )

    text_label1=ttk.Label(win, text='안녕하세요', style='WR.TLabel')
    
    text_label2=ttk.Label(win)
    text_label2.configure(text='반가워요', style='WR.TLabel')

    text_label1.pack()
    text_label2.pack()
    

#주 프로그램부
win=tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk

#사용자 정의 함수부
def buildGUI():
    global text_label
    text_label=ttk.Label(win, text='안녕하세요')

    global name
    name=tk.StringVar()
    input_entry=ttk.Entry(win, textvariable=name)
    
    input_btn=ttk.Button(win, text='입력',
                         command=input_btn_handler)

    quit_btn=ttk.Button(win, text='종료',
                        command=win.destroy)

    text_label.pack()
    input_entry.pack()
    input_btn.pack()
    quit_btn.pack()

def input_btn_handler():
    text_label.configure(text='반가워요, '+name.get())
    name.set('')
        

#주 프로그램부
win=tk.Tk()
win.title('라벨 위젯 예1')
buildGUI()
win.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

#사용자 정의 함수부
def buildGUI():
    global text_area
    text_area=scrolledtext.ScrolledText(win,
                      width=30, height=5, wrap=tk.WORD)

    input_btn=ttk.Button(win, text='출력',
                         command=input_btn_handler)

    text_area.pack()
    input_btn.pack()
    
def input_btn_handler():
    print(text_area.get(0.0, tk.END))
    text_area.delete(0.0, tk.END)
        

#주 프로그램부
win=tk.Tk()
buildGUI()
win.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#사용자 정의 함수부
def buildGUI():
    global check
    check=tk.IntVar()
    check_btn=ttk.Checkbutton(win, text='옵션을 선택하세요',
                              variable=check,
                              command=open_dialog_box)

    check_btn.pack()
    
def open_dialog_box():
    if check.get()==1:
        messagebox.showinfo('확인', '옵션 선택')
    else:
        messagebox.showinfo('확인', '옵션 해제')

#주 프로그램부
win=tk.Tk()
buildGUI()
win.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk

GENDERS=['남성', '여성', '기타']
COLORS=['red', 'yellow', 'purple']

#사용자 정의 함수부
def buildGUI():
    text_label=ttk.Label(win, text='당신의 성별은?')
    text_label.pack()
    
    global gender
    gender=tk.IntVar()
    for i in range(3):
        radio_btn=ttk.Radiobutton(win,
                                  text=GENDERS[i],
                                  value=i,
                                  variable=gender,
                                  command=radio_btn_hadler
        )
        radio_btn.pack()

    gender.set(-1)

def radio_btn_hadler():
    choice=gender.get()
    win.configure(background=COLORS[choice])
    
#주 프로그램부
win=tk.Tk()
win.title('버튼 위젯 예')
buildGUI()
win.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk

#사용자 정의 함수부
def buildGUI():
    btn1=ttk.Button(win, text='버튼1')
    btn2=ttk.Button(win, text='버튼2')
    btn3=ttk.Button(win, text='버튼3')
    btn4=ttk.Button(win, text='버튼4')
    btn5=ttk.Button(win, text='버튼5')

    btn1.pack(side=tk.BOTTOM)
    btn2.pack(ipadx=10, ipady=10)
    btn3.pack(padx=10, pady=10)
    btn4.pack(fill=tk.X)
    btn5.pack(fill=tk.X, padx=10, ipadx=10, ipady=10)

#주 프로그램부
win=tk.Tk()
win.title('pack() 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()
'''
'''
import tkinter as tk
from tkinter import ttk

#사용자 정의 함수부
def buildGUI():
    btn1=ttk.Button(win, text='버튼1')
    btn2=ttk.Button(win, text='매우 긴~~~ 너비와 높이를 갖는\n버\n튼\ㅜ2')
    btn3=ttk.Button(win, text='버튼3')
    btn4=ttk.Button(win, text='버튼4')
    btn5=ttk.Button(win, text='버튼5')

    btn1.grid(row=0, column=0, sticky='se')
    btn2.grid(row=0, column=1, columnspan=2)
    btn3.grid(row=1, column=1, sticky='w')
    btn4.grid(row=1, column=2)
    btn5.grid(row=2, column=0)
    
#주 프로그램부
win=tk.Tk()
win.title('grid 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()
'''
import tkinter as tk
from tkinter import ttk

#사용자 정의 함수부
def buildGUI():
    btn1=ttk.Button(win, text='버튼1')
    btn2=ttk.Button(win, text='매우 긴~~~ 너비와 높이를 갖는\n버\n튼\ㅜ2')
    btn_group=ttk.Frame(win)
    btn3=ttk.Button(btn_group, text='버튼3')
    btn4=ttk.Button(btn_group, text='버튼4')
    btn5=ttk.Button(win, text='버튼5')

    btn1.grid(row=0, column=0, sticky='se')
    btn2.grid(row=0, column=1, columnspan=2)
    btn3.pack(side=tk.LEFT)
    btn4.pack(side=tk.LEFT)
    btn_group.grid(row=1, column=1, sticky='w')
    btn5.grid(row=2, column=0)
    
#주 프로그램부
win=tk.Tk()
win.title('Frame 배치의 예')
win.geometry('300x200')
buildGUI()
win.mainloop()
