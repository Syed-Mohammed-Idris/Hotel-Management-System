def addcustomer():
    def submitadd():
        roomno = roomnoval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        room = roomval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into customerdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(roomno,name,mobile,email,address,gender,room,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','RoomNo. {} Name {} Added sucessfully.. and want to clean the form?'.format(roomno,name),parent=addroot)
            if(res==True):
                roomnoval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                roomval.set('')
        except:
            messagebox.showerror('Notifications','RoomNo. is invalid or it already exists, try another room.no...',parent=addroot)
        strr = 'select * from customerdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        customerttable.delete(*customerttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            customerttable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Hotel Management System')
    addroot.config(bg='green2')
    addroot.iconbitmap('./res/I&U.ico')
    addroot.resizable(False,False)
    #--------------------------------------------------- Add customer Labels
    roomnolabel = Label(addroot,text='Enter Room.No : ',bg='green4',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    roomnolabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name : ',bg='green4',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile : ',bg='green4',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email : ',bg='green4',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text='Enter Address : ',bg='green4',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender : ',bg='green4',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    genderlabel.place(x=10,y=310)

    roomlabel = Label(addroot,text='Room & Price : ',bg='green4',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    roomlabel.place(x=10,y=370)

    ##----------------------------------------------------------- Add customer Entry
    roomnoval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    roomval = StringVar()

    roomnoentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=roomnoval)
    roomnoentry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(addroot,font=('times',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    roomentry = ttk.Combobox(addroot,font=('times',15,'bold') ,width=19, textvariable=roomval)
    roomentry['values'] = ('Single (Rs.1000)',
                           'Double (Rs.2000)',
                           'Twin (Rs.2000)',
                           'Duplex (Rs.2500)',
                           'Deluxe (Rs.3500)',
                           'Beach Cabana (Rs.5000)',
                           'Penthouse Suite (Rs.7500)',
                           'Presidential Suite (Rs.10000)')

    roomentry.grid(column=1, row=5)
    roomentry.current()
    roomentry.place(x=250,y=370)
    ############------------------------- add button
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)



    addroot.mainloop()

def searchcustomer():
    def search():
        roomno = roomnoval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        room = roomval.get()
        addeddate = addeddateval.get()
        if(roomno != ''):
            strr = 'select *from customerdata1 where roomno=%s'
            mycursor.execute(strr,(roomno))
            datas = mycursor.fetchall()
            customerttable.delete(*customerttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customerttable.insert('', END, values=vv)
        elif(name != ''):
            strr = 'select *from customerdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            customerttable.delete(*customerttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customerttable.insert('', END, values=vv)
        elif(mobile != ''):
            strr = 'select *from customerdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            customerttable.delete(*customerttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customerttable.insert('', END, values=vv)
        elif(email != ''):
            strr = 'select *from customerdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            customerttable.delete(*customerttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customerttable.insert('', END, values=vv)
        elif(address != ''):
            strr = 'select *from customerdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            customerttable.delete(*customerttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customerttable.insert('', END, values=vv)
        elif(gender != ''):
            strr = 'select *from customerdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            customerttable.delete(*customerttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customerttable.insert('', END, values=vv)
        elif(room != ''):
            strr = 'select *from customerdata1 where room=%s'
            mycursor.execute(strr,(room))
            datas = mycursor.fetchall()
            customerttable.delete(*customerttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customerttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select *from customerdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            customerttable.delete(*customerttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                customerttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Hotel Management System')
    searchroot.config(bg='gold4')
    searchroot.iconbitmap('./res/I&U.ico')
    searchroot.resizable(False,False)
    #--------------------------------------------------- Add customer Labels
    roomnolabel = Label(searchroot,text='Enter Room.No : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    roomnolabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Mobile : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter Email : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text='Enter Address : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text='Enter Gender : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    genderlabel.place(x=10,y=310)

    roomlabel = Label(searchroot,text='Room & Price : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    roomlabel.place(x=10,y=370)

    addeddatelabel = Label(searchroot,text='Enter Date : ',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    addeddatelabel.place(x=10,y=430)

    ##----------------------------------------------------------- Add customer Entry
    roomnoval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    roomval = StringVar()
    addeddateval = StringVar()

    roomnoentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=roomnoval)
    roomnoentry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    roomentry = ttk.Combobox(searchroot, font=('times', 15, 'bold'), width=19, textvariable=roomval)
    roomentry['values'] = ('Single (Rs.1000)',
                           'Double (Rs.2000)',
                           'Twin (Rs.2000)',
                           'Duplex (Rs.2500)',
                           'Deluxe (Rs.3500)',
                           'Beach Cabana (Rs.5000)',
                           'Penthouse Suite (Rs.7500)',
                           'Presidential Suite (Rs.10000)')
    roomentry.grid(column=1, row=5)
    roomentry.current()
    roomentry.place(x=250,y=370)

    addeddateentry = Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addeddateval)
    addeddateentry.place(x=250,y=430)
    ############------------------------- add button
    submitbtn = Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
    submitbtn.place(x=150,y=480)



    searchroot.mainloop()
def deletecustomer():
    cc = customerttable.focus()
    content = customerttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from customerdata1 where roomno=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Room.No {} deleted sucessfully...'.format(pp))
    strr = 'select *from customerdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    customerttable.delete(*customerttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        customerttable.insert('', END, values=vv)


def updatecustomer():
    def update():
        roomno = roomnoval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        room = roomval.get()
        addeddate = addeddateval.get()
        time = timeval.get()

        strr = 'update customerdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,room=%s,addeddate=%s,time=%s where roomno=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,room,addeddate,time,roomno))
        con.commit()
        messagebox.showinfo('Notifications', 'Room.No {} Modified sucessfully...'.format(roomno),parent=updateroot)
        strr = 'select *from customerdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        customerttable.delete(*customerttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            customerttable.insert('', END, values=vv)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+160')
    updateroot.title('Hotel Management System')
    updateroot.config(bg='firebrick1')
    updateroot.iconbitmap('./res/I&U.ico')
    updateroot.resizable(False,False)
    #--------------------------------------------------- Add customer Labels
    roomnolabel = Label(updateroot,text='Enter Room.No : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    roomnolabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Mobile : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter Email : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text='Enter Address : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text='Enter Gender : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    genderlabel.place(x=10,y=310)

    roomlabel = Label(updateroot,text='Room & Price : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    roomlabel.place(x=10,y=370)

    addeddatelabel = Label(updateroot,text='Enter Date : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    addeddatelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text='Enter Time : ',bg='gold',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    timelabel.place(x=10,y=490)

    ##----------------------------------------------------------- Add customer Entry
    roomnoval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    roomval = StringVar()
    addeddateval = StringVar()
    timeval = StringVar()

    roomnoentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=roomnoval)
    roomnoentry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)

    roomentry = ttk.Combobox(updateroot, font=('times', 15, 'bold'), width=19, textvariable=roomval)
    roomentry['values'] = ('Single (Rs.1000)',
                           'Double (Rs.2000)',
                           'Twin (Rs.2000)',
                           'Duplex (Rs.2500)',
                           'Deluxe (Rs.3500)',
                           'Beach Cabana (Rs.5000)',
                           'Penthouse Suite (Rs.7500)',
                           'Presidential Suite (Rs.10000)')

    roomentry.grid(column=1, row=5)
    roomentry.current()
    roomentry.place(x=250,y=370)

    addeddateentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=addeddateval)
    addeddateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('times',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)
    ############------------------------- add button
    submitbtn = Button(updateroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
    submitbtn.place(x=150,y=540)
    cc = customerttable.focus()
    content = customerttable.item(cc)
    pp = content['values']
    if(len(pp)!= 0):
        roomnoval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        roomval.set(pp[6])
        addeddateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
def showcustomer():
    strr = 'select *from customerdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    customerttable.delete(*customerttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        customerttable.insert('', END, values=vv)

def exportcustomer():
    ff = filedialog.asksaveasfilename()
    gg = customerttable.get_children()
    roomno,name,mobile,email,address,gender,room,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = customerttable.item(i)
        pp = content['values']
        roomno.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        room.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Room.No','Name','Mobile','Email','Address','Gender','Room_Type','Check-in Date','Added Time']
    df = pandas.DataFrame(list(zip(roomno,name,mobile,email,address,gender,room,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Customer data is Saved {}'.format(paths))


def exitcustomer():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()


###################################################################################Connecttion of Database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database hotelmanagementsystem'
            mycursor.execute(strr)
            strr = 'use hotelmanagementsystem'
            mycursor.execute(strr)
            strr = 'create table customerdata1(roomno int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),room varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table customerdata1 modify column roomno int not null'
            mycursor.execute(strr)
            strr = 'alter table customerdata1 modify column roomno int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Database created and now you are connected connected to the database ....',parent=dbroot)

        except:
            strr = 'use hotelmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database ....',parent=dbroot)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('./res/I&U.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='brown1')
    #-------------------------------Connectdb Labels
    hostlabel = Label(dbroot,text="Enter Host : ",bg='maroon1',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='maroon1',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='maroon1',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #-------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('times',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('times',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('times',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #-------------------------------- Connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('roman',15,'bold'),bg='red',bd=5,width=20,activebackground='blue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()
###########################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
#######################################INTRO SLIDER
import random
colors = ['blue2','red2']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200,IntroLabelTick)

##########################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
import pygame
file="./res/bgm2.mp3"
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.event.wait()

root = Tk()
root.title('Hotel Management System')
root.config(bg='DeepSkyBlue2')
root.geometry('1174x700+200+50')
root.iconbitmap('./res/I&U.ico')
root.resizable(False,False)
############################################################################################################  Frames
##---------------------------------------------------------------------------- dataentry frame

DataEntryFrame = Frame(root,bg='SlateBlue1',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel = Label(DataEntryFrame,text='--------------Welcome--------------',width=30,font=('arial',22,'italic bold'),bg='white')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add Customer',width=20,font=('century',17,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=addcustomer)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Customer',width=20,font=('century',17,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=searchcustomer)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Customer',width=20,font=('century',17,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=deletecustomer)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Customer',width=20,font=('century',17,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=updatecustomer)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Display All',width=20,font=('century',17,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=showcustomer)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Save Data',width=20,font=('century',17,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exportcustomer)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7.  Exit',width=20,font=('century',17,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exitcustomer)
exitbtn.pack(side=TOP,expand=True)

##-----------------------------------------------------------Show data frame
ShowDataFrame = Frame(root,bg='purple2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

##-------------------------------------------------  Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=('century',17,'bold'),foreground='red')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
customerttable = Treeview(ShowDataFrame,columns=('Room.No','Name','Mobile No','Email','Address','Gender','Room_Type & Price','Check-in Date','Added Time'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=customerttable.xview)
scroll_y.config(command=customerttable.yview)
customerttable.heading('Room.No',text='Room.No')
customerttable.heading('Name',text='Name')
customerttable.heading('Mobile No',text='Mobile No')
customerttable.heading('Email',text='Email')
customerttable.heading('Address',text='Address')
customerttable.heading('Gender',text='Gender')
customerttable.heading('Room_Type & Price',text='Room_Type & Price')
customerttable.heading('Check-in Date',text='Check-in Date')
customerttable.heading('Added Time',text='Added Time')
customerttable['show'] = 'headings'
customerttable.column('Room.No',width=125)
customerttable.column('Name',width=200)
customerttable.column('Mobile No',width=200)
customerttable.column('Email',width=250)
customerttable.column('Address',width=400)
customerttable.column('Gender',width=130)
customerttable.column('Room_Type & Price',width=260)
customerttable.column('Check-in Date',width=190)
customerttable.column('Added Time',width=190)
customerttable.pack(fill=BOTH,expand=1)

################################################################################################################  Slider
ss = 'I&U Hotel Management System'
count = 0
text = ''
##################################
SliderLabel = Label(root,text=ss,font=('century',24,'italic bold'),relief=RIDGE,borderwidth=4,width=27,bg='sky blue')
SliderLabel.place(x=260,y=0)
IntroLabelTick()
IntroLabelColorTick()
############################################################################################################### clock
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='yellow')
clock.place(x=0,y=0)
tick()
################################################################################################################## ConnectDatabaseButton
connectbutton = Button(root,text='Connect To Database',width=16,font=('century',15,'italic bold'),relief=RIDGE,borderwidth=4,bg='green2', activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=930,y=0)
root.mainloop()