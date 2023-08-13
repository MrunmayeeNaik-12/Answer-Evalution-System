
from tkinter import *
from difflib import SequenceMatcher
from PIL import ImageTk,Image


window = Tk()
window.title('Answer Evalution System')
image1=Image.open("M:\Vartak Clg\Sem 4\Mini Project\Code\\image.jpg")
back_img=ImageTk.PhotoImage(image1)
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')
page1 = Frame(window)
page2 = Frame(window)
page3 = Frame(window)

for frame in (page1, page2, page3):
    frame.grid(row=0, column=0, sticky='nsew')
def show_frame(frame):
    frame.tkraise()

show_frame(page1)

def similar(a,b):
     return SequenceMatcher(None,a,b).ratio()

def getvals():
    
    teachersanswer=pag1_entry2.get()
    keyword=pag1_entry3.get()
    studentsanswer=pag1_entry4.get()
    a=similar(teachersanswer,studentsanswer)
    if keyword in studentsanswer:

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

    pag2_label0=Label(page2,image=back_img)
    pag2_label0.place(x=40,y=10)
    pag2_label = Label(page2, text='Marks Awarded !', font=('Arial', 30, 'bold'))
    pag2_label.place(x=50, y=20)

    pag2_label = Label(page2, text=marks, font=('Arial', 25, 'bold'))
    pag2_label.place(x=60, y=80)

    pag2_label1 = Label(page2, text='Correct Answer:', font=('Arial', 15, 'bold'))
    pag2_label1.place(x=50, y=550)

    pag2_label2 = Label(page2, text=teachersanswer, font=('Arial', 10, 'bold'))
    pag2_label2.place(x=50, y=600)

    return None


pag1_label0=Label(page1,image=back_img)
pag1_label0.place(x=40,y=10)

pag1_label10 = Label(page1, text="Teacher's Section", font=('Arial', 30, 'bold'))
pag1_label10.place(x=45, y=20)

pag1_label = Label(page1, text='Enter Question :', font=('Arial', 15, 'bold'))
pag1_label.place(x=60, y=80)

pag1_entry1 = Entry(page1)
pag1_entry1.place(x=60, y=120)

pag1_label2 = Label(page1, text='Enter Teachers Answer:', font=('Arial', 15, 'bold'))
pag1_label2.place(x=60, y=160)

pag1_entry2 = Entry(page1)
pag1_entry2.place(x=60, y=200)

pag1_label3 = Label(page1, text='Enter Keyword:', font=('Arial', 15, 'bold'))
pag1_label3.place(x=60, y=240)

pag1_entry3 = Entry(page1)
pag1_entry3.place(x=60, y=280)

pag1_label = Label(page1, text='Students Section', font=('Arial', 30, 'bold'))
pag1_label.place(x=60, y=550)

pag1_label = Label(page1, text='Enter Students Answer', font=('Arial', 15, 'bold'))
pag1_label.place(x=60, y=600)

pag1_entry4 = Entry(page1)
pag1_entry4.place(x=60, y=640)

pg1_button1 = Button(page1, text='Next', font=('Arial', 13, 'bold'),command=lambda : show_frame(page2))
pg1_button1.place(x=450, y=600)

pg1_button = Button(page1, text='Submit', font=('Arial', 13, 'bold'),command=lambda : getvals())
pg1_button.place(x=450, y=550)


window.mainloop()