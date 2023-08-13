from abc import ABC
from ast import Str, keyword
from tkinter import *
from tkinter.messagebox import QUESTION
from difflib import SequenceMatcher  


window = Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')

page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')

def similar(a,b):
     return SequenceMatcher(None,a,b).ratio()


def show_frame(frame):
    frame.tkraise()

show_frame(page1)

def simi1():
   StudentsAnswer=getvals1()
   TeachersAnswer=getvals3()
   sim =float(similar(TeachersAnswer,StudentsAnswer))
  
   return sim

def getvals():
    question=pag1_entry.get()   
    return question

def getvals1():
    sanswer=pag2_entry.get()
    return sanswer

def getvals3():
    tanswer=pag1_entry2.get()
    return tanswer

def getvals4():
    Keyword=pag1_entry3.get()
    return Keyword

def mark():
    a=simi1()
    Keyw=getvals4() 
    Stans=getvals1()
    if Keyw in Stans:

     if a>=0.90:
           marks=5
     elif a>=0.80:
          marks=4
     elif a>=0.70:
          marks=3
     elif a>=0.60:
          marks=2
     elif a>=0.50:
          marks=1
     else:
          marks=0
    else:
      if a>=0.90:
          marks=4
      elif a>=0.80:
          marks=3
      elif a>=0.70:
         marks=2
      elif a>=0.60:
          marks=1
      else: 
         marks=0
    return marks
 
# ============= Page 1 =========
pag1_label = Label(page1, text='Enter Question', font=('Arial', 15, 'bold'))
pag1_label.place(x=450, y=240)

pag1_entry = Entry(page1)
pag1_entry.place(x=600, y=245)

pag1_label2 = Label(page1, text='Enter Teachers Answer', font=('Arial', 15, 'bold'))
pag1_label2.place(x=450, y=290)

pag1_entry2 = Entry(page1)
pag1_entry2.place(x=680, y=295)

pag1_label3 = Label(page1, text='Enter Keyword', font=('Arial', 15, 'bold'))
pag1_label3.place(x=450, y=350)

pag1_entry3 = Entry(page1)
pag1_entry3.place(x=600, y=355)

pg1_button = Button(page1, text='Submit', font=('Arial', 13, 'bold'),command=lambda : getvals())
pg1_button.place(x=450, y=400)

pg1_button1 = Button(page1, text='Next', font=('Arial', 13, 'bold'),command=lambda : show_frame(page2))
pg1_button1.place(x=800, y=400)

pg1_button2 = Button(page1, text='Confirm Ans', font=('Arial', 13, 'bold'),command=lambda : getvals3())
pg1_button2.place(x=550, y=400)

pg1_button3 = Button(page1, text='Confirm Key', font=('Arial', 13, 'bold'),command=lambda : getvals4())
pg1_button3.place(x=670, y=400)
ab=getvals3()
print(ab)
# ======== Page 2 ===========
pag2_label = Label(page2, text='Students Section', font=('Arial', 30, 'bold'))
pag2_label.place(x=50, y=100)

pag2_label = Label(page2, text='Enter Students Answer', font=('Arial', 15, 'bold'))
pag2_label.place(x=70, y=150)

pag2_entry = Entry(page2)
pag2_entry.place(x=300, y=156)

pg2_button = Button(page2, text='Submit', font=('Arial', 13, 'bold'), command=lambda: getvals1())
pg2_button.place(x=190, y=200)

pg2_button1 = Button(page2, text='Next', font=('Arial', 13, 'bold'), command=lambda: show_frame(page3))
pg2_button1.place(x=300, y=200)

# ======== Page 3 ===========
pag3_label = Label(page3, text='Marks Awarded!!', font=('Arial', 30, 'bold'))
pag3_label.place(x=50, y=100)

pag3_label2 = Label(page3, text=mark(), font=('Arial', 20, 'bold'))
pag3_label2.place(x=50, y=150)

pg3_button = Button(page3, text='Recheck', font=('Arial', 13, 'bold'), command=lambda: show_frame(page1))
pg3_button.place(x=50, y=300)

    
window.mainloop()