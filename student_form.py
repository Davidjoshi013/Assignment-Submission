from tkinter import *
import mysql.connector
from tkinter import ttk


try:
    con=mysql.connector.connect(host='localhost',
                                user='root',
                                password='root',
                                database='student')

    cur=con.cursor()
except mysql.connector.Error as E:
    print ("Database Error")


def add_info():
    student_id=int(entrystudent_id.get())
    first_name=entryfirst_name.get()
    last_name=entrylast_name.get()
    degree=entrydegree.get()
    address=entryaddress.get()
    contact_no=int(entrycontact_no.get())

    query='insert into student_table values(%s,%s,%s,%s,%s,%s)'
    values=(student_id,first_name,last_name,degree,address,contact_no)
    cur.execute(query,values)
    print('Data saved successfully')
    con.commit()
    show()
    clear()

def show():
    query='select * from student_table'
    cur.execute(query)
    result=cur.fetchall()
    if len(result)!=0:
        student_table.delete(*student_table.get_children())
        for row in result:
            student_table.insert('',END,values=row)
            con.commit()



def delete_data():
    student_id=int(entrystudent_id.get())
    query='delete from student_table where stu_id=%s'
    values=(student_id,)
    cur.execute(query,values)
    print('data deleted successfully')
    con.commit()
    show()

def clear():
    entrystudent_id.delete(0,END)
    entryfirst_name.delete(0,END)
    entrylast_name.delete(0,END)
    entrydegree.delete(0,END)
    entryaddress.delete(0,END)
    entrycontact_no.delete(0,END)


def pointer(event):
    point=student_table.focus()
    content=student_table.item(point)
    row=content['values']
    clear()
    if len(row) !=0:
        entrystudent_id.insert(0,row[0])
        entryfirst_name.insert(0,row[1])
        entrylast_name.insert(0,row[2])
        entrydegree.insert(0,row[3])
        entryaddress.insert(0,row[4])
        entrycontact_no.insert(0,row[5])

def update():
    query='update student_table set Fname=%s,Lname=%s,course=%s,address=%s,contact_no=%s where stu_id=%s'
    student_id=int(entrystudent_id.get())
    first_name=entryfirst_name.get()
    last_name=entrylast_name.get()
    degree=entrydegree.get()
    address=entryaddress.get()
    contact_no=int(entrycontact_no.get())
    values=(first_name,last_name,degree,address,contact_no,student_id)
    cur.execute(query,values)
    con.commit()
    show()
    clear()


window=Tk()
window.title('Student Management')
size=window.geometry('800x700')
window.configure(bg='#6D9B9B')

#Lables
title=Label(window,text='Student Management System',font=('Montserrat',25),bg='#6D9B9B')
student_id=Label(window,text='Id:',bg='#6D9B9B',font=('Arial',12,'bold'))
first_name=Label(window,text='First Name:',bg='#6D9B9B',font=('Arial',12,'bold'))
last_name=Label(window,text='Last Name:',bg='#6D9B9B',font=('Arial',12,'bold'))
degree=Label(window,text='Degree:',bg='#6D9B9B',font=('Arial',12,'bold'))
address=Label(window,text='Address:',bg='#6D9B9B',font=('Arial',12,'bold'))
contact_no=Label(window,text='Contact Number:',bg='#6D9B9B',font=('Arial',12,'bold'))


title.place(x=200,y=20)
student_id.place(x=50,y=100)
first_name.place(x=50,y=150)
last_name.place(x=50,y=200)
degree.place(x=400,y=100)
address.place(x=400,y=150)
contact_no.place(x=400,y=200)

#Entry
entrystudent_id=Entry(window,width=23)
entryfirst_name=Entry(window,width=23)
entrylast_name=Entry(window,width=23)
entrydegree=ttk.Combobox(window,values=['Bsc(Hons)computing','Ethical Hacking'])
entryaddress=Entry(window,width=23)
entrycontact_no=Entry(window,width=23)

entrystudent_id.place(x=200,y=100)
entryfirst_name.place(x=200,y=150)
entrylast_name.place(x=200,y=200)
entrydegree.place(x=600,y=100)
entryaddress.place(x=600,y=150)
entrycontact_no.place(x=600,y=200)

btn_frame=Frame(window,bd=4,relief=RIDGE,bg='#9966ff')
btn_frame.place(x=40,y=650,width=720,height=50)

btn_f2=Frame(window,bd=4,relief=RIDGE,bg='#9966ff')
btn_f2.place(x=40,y=250,width=720,height=100)

table_frame=Frame(window,bd=4,relief=RIDGE,bg='gray')
table_frame.place(x=40,y=350,width=720,height=300)

#scrollbar
scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
scroll_y=Scrollbar(table_frame,orient=VERTICAL)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)


#table
student_table=ttk.Treeview(table_frame,column=('stu_id','Fname','Lname','course','address','contact_no'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
student_table.heading('stu_id',text="Id")
student_table.heading('Fname',text="First Name")
student_table.heading('Lname',text="Last Name")
student_table.heading('course',text="Degree")
student_table.heading('address',text="Address")
student_table.heading('contact_no',text="Contact Number")
student_table['show']='headings'

student_table.column('stu_id',width=120)
student_table.column('Fname',width=120)
student_table.column('Lname',width=120)
student_table.column('course',width=120)
student_table.column('address',width=120)
student_table.column('contact_no',width=120)


scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
show()

student_table.bind(('<ButtonRelease-1>'),pointer)
student_table.pack(fill=BOTH,expand=True)

#Buttons
addbutton=Button(btn_frame,text='Add',command=add_info,width=8,height=2)
addbutton.grid(row=0,column=0,padx=60)

btn_update=Button(btn_frame,text='Update',width=8,height=2,command=update)
btn_update.grid(row=0,column=1,padx=60)

delete=Button(btn_frame,text='Delete',command=delete_data,width=8,height=2)
delete.grid(row=0,column=2,padx=60)

btn_clear=Button(btn_frame,text='Clear',width=8,height=2,command=clear)
btn_clear.grid(row=0,column=3,padx=60)

btn_show = Button(btn_f2,text='Show All',command=show)
btn_show.grid(row=2,column=3,padx=20)



def search(data,search_index,search_for):
    global search_results
    search_results = []
    for i in data:
        if str(search_for) in str(i[search_index]):
            search_results.append(i)
            return search_results

def search_fetch():
    query = "select * from student_table"
    cur.execute(query)
    data = cur.fetchall()
    test = combo_search.get()
    searching = Esearch.get()
    list = ('ID','First name','Last name','Course','Address','Contact no.')
    search_index = int()
    for i in list:
        if i == test:
            search_index = list.index(i)

    search(data,search_index,searching)
    student_table.delete(*student_table.get_children())
    if len(search_results) != 0:
        for i in search_results:
            student_table.insert('', END, values=i)
            con.commit()



def bubble_sort(result,sort_by):
    for i in range(0,len(result)-1):
        for j in range(0,len(result)-1-i):
            if result[j][sort_by]>result[j+1][sort_by]:
                result[j],result[j+1]=result[j+1],result[j]
    return result

def sorted():
    thelist = 'select * from student_table'
    cur.execute(thelist)
    result = cur.fetchall()
    entry = entry_sort.get()
    data = ('ID','First name','Last name','Course','Address','Contact no.')
    sort_by = int()
    for i in data:
        if i == entry:
            sort_by = data.index(i)
            break
    bubble_sort(result,sort_by)
    if len(result) != 0:
        student_table.delete(*student_table.get_children())
        for row in result:
            student_table.insert('', END, values=row)
            con.commit()

Esearch = Entry(btn_f2)
Esearch.grid(row=1, column=2, padx=10, pady=10)
combo_search = ttk.Combobox(btn_f2)
combo_search['values'] = ('ID', 'First name', 'Last name','Course', 'Address','Contact no.')
combo_search.set('ID')
combo_search.grid(row=1, column=1, padx=10, pady=10)
btn_search=Button(btn_f2,text='search',width=6,height=1,command=search_fetch)
btn_search.grid(row=1,column=3,padx=10)
entry_sort=ttk.Combobox(btn_f2,font=('arial',15),state='readonly',width=10)
entry_sort['values']=('ID','First name','Last name','Course','Address','Contact no.')
entry_sort.set('ID')
entry_sort.grid(row=2,column=1,padx=10,pady=10)
btn_sort=Button(btn_f2,text='sort',width=6,height=1,command=sorted)
btn_sort.grid(row=2,column=2,padx=10)
lbl_search = Label(btn_f2, text='Search By:')
lbl_search.grid(row=1, column=0, padx=10, pady=10)
window.resizable(0,0)
window.mainloop()
