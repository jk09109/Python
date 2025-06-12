#14주차 - 연습문제 13.1~3
'''
import tkinter as tk
from tkinter import ttk

#클래스 정의부
class ConvTempWin():
    def __init__(self):
        self.win=tk.Tk()    #기본 윈도우 객체 생성
        self.win.title('온도변환기-1단계')
        self.__buildGUI()   #화면 구성
        self.win.geometry('270x190') #오류나면 큰 따옴표로 바꿀 것

    def __buildGUI(self):
        fahr_Label=ttk.Label(self.win, text='화씨')

        self.__fahr=tk.IntVar()
        fahr_entry=ttk.Entry(self.win, justify=tk.RIGHT, width=11,
                             textvariable=self.__fahr)

        cel_Label=ttk.Label(self.win, text='섭씨')

        self.__cels=tk.DoubleVar()
        cel_entry=ttk.Entry(self.win, justify=tk.RIGHT, width=11,
                            textvariable=self.__cels)

        f2c_btn=ttk.Button(self.win, text='화씨->섭씨',
                           command=self.__f2c_handler)
        c2f_btn=ttk.Button(self.win, text='섭씨->화씨',
                           command=self.__c2f_handler)
        reset_btn=ttk.Button(self.win, text='초기화',
                             command=self.__reset_handler)
        quit_btn=ttk.Button(self.win, text='종료',
                             command=self.win.destroy)

        fahr_Label.pack()
        fahr_entry.pack()
        cel_Label.pack()
        cel_entry.pack()

        f2c_btn.pack()
        c2f_btn.pack()
        reset_btn.pack()
        quit_btn.pack()

    def __f2c_handler(self):
        fahr=self.__fahr.get()
        cels=(fahr-32)*5/9
        self.__cels.set(f'{cels:.2f}')
        
    def __c2f_handler(self):
        cels=self.__cels.get()
        fahr=cels*9/5+32
        self.__fahr.set(f'{fahr:.0f}')
        
    def __reset_handler(self):
        self.__fahr.set('')
        self.__cels.set('')
        
    def start(self):
        self.win.mainloop()

#주 프로그램부
tConverter=ConvTempWin()
tConverter.start()
'''
'''
import tkinter as tk
from tkinter import ttk

#클래스 정의부
class ConvTempWin():
    def __init__(self):
        self.win=tk.Tk()    #기본 윈도우 객체 생성
        self.win.title('온도변환기-2단계')
        self.__buildGUI()   #화면 구성

    def __buildGUI(self):
        fahr_Label=ttk.Label(self.win, text='화씨')

        self.__fahr=tk.IntVar()
        fahr_entry=ttk.Entry(self.win, justify=tk.RIGHT, width=11,
                             textvariable=self.__fahr)

        cel_Label=ttk.Label(self.win, text='섭씨')

        self.__cels=tk.DoubleVar()
        cel_entry=ttk.Entry(self.win, justify=tk.RIGHT, width=11,
                            textvariable=self.__cels)

        f2c_btn=ttk.Button(self.win, text='화씨->섭씨',
                           command=self.__f2c_handler)
        c2f_btn=ttk.Button(self.win, text='섭씨->화씨',
                           command=self.__c2f_handler)
        reset_btn=ttk.Button(self.win, text='초기화',
                             command=self.__reset_handler)
        quit_btn=ttk.Button(self.win, text='종료',
                             command=self.win.destroy)

        fahr_Label.grid(row=0, column=0) #pack 함수를 grid 함수로 변경
        fahr_entry.grid(row=0, column=1) #grid 함수로 좌표값 설정해 위치지정
        cel_Label.grid(row=0, column=2)
        cel_entry.grid(row=0, column=3)

        f2c_btn.grid(row=1, column=0)
        c2f_btn.grid(row=1, column=1)
        reset_btn.grid(row=1, column=2)
        quit_btn.grid(row=1, column=3)

    def __f2c_handler(self):
        fahr=self.__fahr.get()
        cels=(fahr-32)*5/9
        self.__cels.set(f'{cels:.2f}')
        
    def __c2f_handler(self):
        cels=self.__cels.get()
        fahr=cels*9/5+32
        self.__fahr.set(f'{fahr:.0f}')
        
    def __reset_handler(self):
        self.__fahr.set('')
        self.__cels.set('')
        
    def start(self):
        self.win.mainloop()

#주 프로그램부
tConverter=ConvTempWin()
tConverter.start()
'''
'''
import tkinter as tk
from tkinter import ttk

#클래스 정의부
class ConvTempWin():
    def __init__(self):
        self.win=tk.Tk()    #기본 윈도우 객체 생성
        self.win.title('온도변환기-3단계')
        self.__buildGUI()   #화면 구성

    def __buildGUI(self):
        self.__create_input_frame().pack() #pack 메소드 사
        self.__create_button_frame().pack()

    def __create_input_frame(self):
        frame=ttk.Frame(self.win)
        
        fahr_Label=ttk.Label(frame, text='화씨')

        self.__fahr=tk.IntVar()
        fahr_entry=ttk.Entry(frame, justify=tk.RIGHT, width=11,
                             textvariable=self.__fahr)

        cel_Label=ttk.Label(frame, text='섭씨')

        self.__cels=tk.DoubleVar()
        cel_entry=ttk.Entry(frame, justify=tk.RIGHT, width=11,
                            textvariable=self.__cels)

        fahr_Label.pack(side=tk.LEFT)
        fahr_entry.pack(side=tk.LEFT)
        cel_Label.pack(side=tk.LEFT)
        cel_entry.pack(side=tk.LEFT)

        return frame

    def __create_button_frame(self):
        frame=ttk.Frame(self.win)

        f2c_btn=ttk.Button(frame, text='화씨->섭씨',
                           command=self.__f2c_handler)
        c2f_btn=ttk.Button(frame, text='섭씨->화씨',
                           command=self.__c2f_handler)
        reset_btn=ttk.Button(frame, text='초기화',
                             command=self.__reset_handler)
        quit_btn=ttk.Button(frame, text='종료',
                             command=self.win.destroy)

        f2c_btn.pack(side=tk.LEFT)
        c2f_btn.pack(side=tk.LEFT)
        reset_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)

        return frame

    def __f2c_handler(self):
        fahr=self.__fahr.get()
        cels=(fahr-32)*5/9
        self.__cels.set(f'{cels:.2f}')
        
    def __c2f_handler(self):
        cels=self.__cels.get()
        fahr=cels*9/5+32
        self.__fahr.set(f'{fahr:.0f}')
        
    def __reset_handler(self):
        self.__fahr.set('')
        self.__cels.set('')
        
    def start(self):
        self.win.mainloop()

#주 프로그램부
tConverter=ConvTempWin()
tConverter.start()
'''
#연습문제 13.4
'''
import tkinter as tk
from tkinter import ttk

#클래스 정의부
class MemberReg():
    hobby_list=['영화시청', '음악감상', '사진찍기', '운동']

    def __init__(self):
        self.win=tk.Tk()    #기본 윈도우 객체 생성
        self.win.title('회원가입')
        self.__buildGUI()   #화면구성

    def __buildGUI(self):
        self.__create_name_input_frame().grid(row=0, column=0, sticky='w')  #sticky='w' 왼쪽 정렬
        self.__create_grade_input_frame().grid(row=1, column=0, sticky='w')
        self.__create_hobby_input_frame().grid(row=2, column=0, sticky='w')
        self.__create_button_frame().grid(row=3, column=0, sticky='e')      #sticky='e' 오른쪽 정

    def __create_name_input_frame(self):
        frame=ttk.Frame(self.win)

        self.text_label=ttk.Label(frame, text='이름:')

        self.name=tk.StringVar()
        input_entry=ttk.Entry(frame, textvariable=self.name)

        self.text_label.grid(row=0, column=0)
        input_entry.grid(row=0, column=1)

        return frame

    def __create_grade_input_frame(self):
        frame=ttk.Frame(self.win)

        self.text_label=ttk.Label(frame, text='학년:')
        self.text_label.grid(row=0, column=0)

        sub_frame=ttk.Frame(frame)
        self.grade=tk.IntVar()
        for i in range(1, 5):
            grade_btn=ttk.Radiobutton(sub_frame,
                                      text=f'{i}학년',
                                      value=i,
                                      variable=self.grade,
                                      )
            grade_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0, column=1)

        return frame

    def __create_hobby_input_frame(self):
        frame=ttk.Frame(self.win)

        self.text_label=ttk.Label(frame, text='취미:')
        self.text_label.grid(row=0, column=0)

        sub_frame=ttk.Frame(frame)
        self.hobby=[]
        for i in range(4):
            self.hobby.append(tk.IntVar())
            hobby_btn=ttk.Checkbutton(sub_frame,
                                      text=self.hobby_list[i],
                                      variable=self.hobby[i],
                                      )
            hobby_btn.pack(side=tk.LEFT)
        sub_frame.grid(row=0, column=1)

        return frame

    def __create_button_frame(self):
        frame=ttk.Frame(self.win)

        input_btn=ttk.Button(frame, text='입력',
                             command=self.__input_btn_clicked)
        quit_btn=ttk.Button(frame, text='종료',
                            command=self.win.destroy)

        input_btn.pack(side=tk.LEFT)
        quit_btn.pack(side=tk.LEFT)

        return frame

    def __input_btn_clicked(self):
        print(self.name.get())
        print(self.grade.get())

        for i in range(4):
            if self.hobby[i].get()==True:
                print(self.hobby_list[i])
    
#주 프로그램부
member=MemberReg()
member.win.mainloop()
'''
#연습문제 13.5
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

#클래스 정의부
class WordMaster:
    def __init__(self):
        self.win=tk.Tk()
        self.win.title('단어장')
        self.win.geometry('400x100')

        self.buildGUI()

        self.words=self.loadData()

    def buildGUI(self):
        #위젯 생성
        l_word=ttk.Label(self.win, text='단어:')
        self.word=tk.StringVar()
        e_word=ttk.Entry(self.win, textvariable=self.word, width=15)

        l_meaning=ttk.Label(self.win, text='뜻:')
        self.mean=tk.StringVar()
        e_meaning=ttk.Entry(self.win, textvariable=self.mean, width=35)

        b_search=ttk.Button(self.win, text='검색', width=5, command=self.search)
        b_add=ttk.Button(self.win, text='추가', width=5, command=self.add)
        b_reset=ttk.Button(self.win, text='초기화', command=self.reset)
        b_exit=ttk.Button(self.win, text='종료', command=self.end)

        #위젯 배치  
        l_word.grid(row=0, column=0, sticky='e', padx=10)
        e_word.grid(row=0, column=1, sticky='w')
        b_search.grid(row=0, column=2, ipadx=10, ipady=5, sticky='w')
        b_add.grid(row=0, column=3, ipadx=10, ipady=5, sticky='w')

        l_meaning.grid(row=2, column=0, sticky='e', padx=10)
        e_meaning.grid(row=2, column=1, columnspan=3, sticky='w')

        b_reset.grid(row=3, column=0, ipadx=10, ipady=5, padx=10, sticky='w')
        b_exit.grid(row=3, column=1, ipadx=10, ipady=5, sticky='w')

    #파일로부터 읽어들이기
    def loadData(self):
        words={}
        if not os.path.exists('words.txt'):
            return words
        fp=open('words.txt', 'r', encoding='utf-8')

        for line in fp:
            word=line.split(':')

            for i in range(0, len(word)):
                word[i]=word[i].strip()

            key=word[0]
            value=word[1]
            words[key]=value

        fp.close()

        return words

    #딕셔너리에 추가하기
    def add(self):
        w=self.word.get()
        m=self.mean.get()

        self.words[w]=m

        messagebox.showinfo('추가 확인', '단어'+w+'를 추가했습니다.')

        self.word.set('')
        self.mean.set('')

    #딕셔너리에서 단어 검색하기
    def search(self):
        w=self.word.get()

        if w not in self.words:
            messagebox.showinfo('검색 오류', w+'란 단어는 없습니다!')
            self.reset()
            return

        m=self.words[w]

        self.mean.set(m)

    #위젯 초기화
    def reset(self):
        self.word.set('')
        self.mean.set('')

    #프로그램 종료 처리
    def end(self):
        fp=open('words.txt', 'w', encoding='utf-8')

        for w in self.words.keys():
            m=self.words[w]
            fp.write(w+':'+m+'\n')  #fp.writelines(w+':'+m+'\n')

        fp.close()

        self.win.destroy()

#주 프로그램
wm=WordMaster()
wm.win.mainloop()
