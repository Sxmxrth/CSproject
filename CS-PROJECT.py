from tkinter import *
import time
import datetime
from tkinter import messagebox
import mysql.connector as mysql
from PIL import  ImageTk, Image


home=Tk()
home.title("Database Manager")
home.iconbitmap('appimg.ico')
home.configure(bg="#FFCCBC")
#home.geometry('300x300')

def Admin():
    
    login_a=Toplevel()
    login_a.title("Admin Login")
    login_a.configure(bg='#FFEB3B')
    
    p="admin"
    
    def login():

        pas= passwd.get()
        
        if pas == p:
            
            login_a.destroy()
            
            root = Toplevel()
            root.title('Databases')
            root.iconbitmap('appimg.ico')
            root.configure(bg='#03A9F4')
            #root.geometry("400x400")
            
            def Attendance_record_delete():
                ID=Edit_ID.get()
                
                db = mysql.connect(host="localhost", user="root", passwd="Samarth2002#", database="emp_data")
                # Create cursor
                c = db.cursor()
           
                #Insert into tabel
                query="DROP TABLE `emp_data`.`emp_%s`;"%(ID)
                
                c.execute(query)
                
                db.commit()
                db.close()
                
                
            def Attendance_record():
                ID=Emp_ID.get()
                
                db = mysql.connect(host="localhost", user="root", passwd="Samarth2002#", database="emp_data")
                # Create cursor
                c = db.cursor()
           
                #Insert into tabel
                query="CREATE TABLE `emp_data`.`emp_%s` ( `Date` DATE NOT NULL, `In_time` TIME NOT NULL, `Out_time` TIME NULL, PRIMARY KEY (`Date`))"%(ID)
                
                c.execute(query)
                
                db.commit()
                db.close()
            
           #create Submit Function
            def submit():
                #connect to datbase
                db = mysql.connect(host="localhost", user="root", passwd="Samarth2002#", database="emp_data")
                # Create cursor
                c = db.cursor()
           
                #Insert into tabel
                query="insert into employee(Emp_ID, Emp_Name, Emp_Address, Emp_Status, Emp_DOB, Emp_Salary, Emp_Passwd, Emp_Remark) values (%s,%s,%s,%s,%s,%s,%s,%s)"
                
                value=[Emp_ID.get(),
                       Emp_Name.get(),
                       Emp_Address.get(),
                       Emp_Status.get(),
                       Emp_DOB.get(),
                       Emp_Salary.get(),
                       Emp_Passwd.get(),
                       Emp_Remark.get()
                       ]
                c.execute(query, value)
                
                
                db.commit()
                db.close()
                
                Attendance_record()
                
                #clear the box
                Emp_ID.delete(0,END)
                Emp_Name.delete(0,END)
                Emp_Address.delete(0,END)
                Emp_Status.delete(0,END)
                Emp_DOB.delete(0,END)
                Emp_Salary.delete(0,END)
                Emp_Passwd.delete(0,END)
                Emp_Remark.delete(0,END)
                
                print ("Employee Information Successfully added to records")
                                
            def query():
                            
                #connect to datbase
                db = mysql.connect(host="localhost", user="root", passwd="Samarth2002#", database="emp_data")
                # Create cursor
                c = db.cursor()
                
                c.execute("SELECT * from employee")
                d=c.fetchall()
                
                data=''  
                global root2
                
                root2 = Toplevel()
                root2.title('Databases')
                root2.iconbitmap('appimg.ico')
                root2.configure(bg='#03A9F4')
                
                rec = LabelFrame(root2, text="Employee Information", padx=70, pady=50, bg='#A9DFBF',  relief= RIDGE, bd=6)
                rec.grid(row=2, column=0)
               
                for i in d: 
                    for j in range(0,9):
                        data_1=str(i[0:3])
                        Dob=str(i[3])
                        data_2=str(Dob)
                        data_3=str(i[4:])
                        
                        data = (data_1+','+data_2+','+data_3)
                        
                    print (data,end="\n")
                    query_lbl = Label(rec, text = data, bg='#A9DFBF')
                    query_lbl.pack()
                    #query_lbl.(row=0, column=0)
                    #data += str(i)+"\n"+"\n"
                    #print ()
                    
                db.commit()
                db.close()
                
            def delete():
                
                #root2.destroy()
                
                db = mysql.connect(host="localhost", user="root", passwd="Samarth2002#", database="emp_data")
               
                # Create cursor
                c = db.cursor()
                
                ID=Edit_ID.get()
                print(ID ,"Record deleted")
                
                query = "DELETE FROM `emp_data`.`employee` WHERE (`Emp_ID` = %s); "%(ID)
                
                c.execute(query)
                
                db.commit()
                db.close()
                
                Attendance_record_delete()
            
            def update_screen():
                
                global Updt
                
                Updt = Toplevel()
                Updt.title('UPDATE')
                Updt.iconbitmap('appimg.ico')
                Updt.configure(bg="#F6DDCC")
                
                global ID
                
                ID=[Edit_ID.get()]
                
                db = mysql.connect(host="localhost", user="root", passwd="Samarth2002#", database="emp_data")
                c = db.cursor()
                
                query="Select * from `emp_data`.`employee` WHERE (`Emp_ID` = %s);"
                c.execute(query,ID)
                
                d=c.fetchall()
                for i in d:
                    print (i,end="\n")
                
                f_au = LabelFrame(Updt,padx=10, pady=10, bg='#FFFFCC',  relief= RIDGE, bd=6)
                f_au.grid(row=0, column=0)
                
                global Emp_ID_ed , Emp_Name_ed , Emp_Address_ed , Emp_Status_ed , Emp_DOB_ed , Emp_Salary_ed , Emp_Attend_ed , Emp_Passwd_ed , Emp_Remark_ed
                
                #Create text boxes
                
                Emp_ID_ed = Entry(f_au, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
                Emp_ID_ed.grid(row=0, column=1, padx=20)
                Emp_ID_ed.insert(0,  d[0][0])
                Emp_Name_ed = Entry(f_au, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
                Emp_Name_ed.grid(row=1, column=1, padx=20)
                Emp_Name_ed.insert(0,  d[0][1])
                Emp_Address_ed = Entry(f_au, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
                Emp_Address_ed.grid(row=2, column=1, padx=20)
                Emp_Address_ed.insert(0,  d[0][2])
                Emp_DOB_ed = Entry(f_au, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
                Emp_DOB_ed.grid(row=3, column=1, padx=20)
                Emp_DOB_ed.insert(0, str( d[0][3]))
                Emp_Status_ed = Entry(f_au, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
                Emp_Status_ed.grid(row=4, column=1, padx=20)
                Emp_Status_ed.insert(0,  d[0][4])
                Emp_Salary_ed = Entry(f_au, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
                Emp_Salary_ed.grid(row=5, column=1, padx=20)
                Emp_Salary_ed.insert(0,  d[0][5])
                Emp_Passwd_ed = Entry(f_au, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
                Emp_Passwd_ed.grid(row=7, column=1, padx=20)
                Emp_Passwd_ed.insert(0,  d[0][6])
                Emp_Remark_ed = Entry(f_au, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
                Emp_Remark_ed.grid(row=8, column=1, padx=20)
                Emp_Remark_ed.insert(0,  d[0][7])
                
                #Create Text Box Labels
                
                Emp_ID_lbl = Label(f_au, text="ID No.", bg='#FFFFCC')
                Emp_ID_lbl.grid(row=0, column=0)
                Emp_Name_lbl = Label(f_au, text="Name", bg='#FFFFCC')
                Emp_Name_lbl.grid(row=1, column=0)
                Emp_Address_lbl = Label(f_au, text="Address", bg='#FFFFCC')
                Emp_Address_lbl.grid(row=2, column=0)
                Emp_DOB_lbl = Label(f_au, text="Date of Birth", bg='#FFFFCC')
                Emp_DOB_lbl.grid(row=3, column=0)
                Emp_Status_lbl = Label(f_au, text="Position", bg='#FFFFCC')
                Emp_Status_lbl.grid(row=4, column=0)
                Emp_Salary_lbl = Label(f_au, text="Salary", bg='#FFFFCC')
                Emp_Salary_lbl.grid(row=5, column=0)
                Emp_Passwd_lbl = Label(f_au, text="Password", bg='#FFFFCC')
                Emp_Passwd_lbl.grid(row=7, column=0)
                Emp_Remark_lbl = Label(f_au, text="Remarks", bg='#FFFFCC')
                Emp_Remark_lbl.grid(row=8, column=0)
                
                save_btn = Button(f_au, text="Save Record", command = update , padx=5, pady=5, bd=8)
                save_btn.grid(row=10, column=1, columnspan=2, padx=10, pady=10, ipadx=98)
                
                                
                db.commit()
                db.close()
                
                
            def update():
                #connect to datbase
                db = mysql.connect(host="localhost", user="root", passwd="Samarth2002#", database="emp_data")
                # Create cursor
                c = db.cursor()
                
                value=[Emp_Name_ed.get(),
                       Emp_Address_ed.get(),
                       Emp_Status_ed.get(),
                       Emp_DOB_ed.get(),
                       Emp_Salary_ed.get(),
                       Emp_Passwd_ed.get(),
                       Emp_Remark_ed.get(),
                       Edit_ID.get()]
                
                #Insert into tabel
                print(value)
                

                query="UPDATE `emp_data`.`employee` SET  `Emp_Name`= '%s',  `Emp_Address`= '%s',  `Emp_Status`= '%s',  `Emp_DOB`= '%s',  `Emp_Salary`= '%s', `Emp_Passwd`= '%s',  `Emp_Remark`= '%s' WHERE (`Emp_ID` = '%s')"% (Emp_Name_ed.get(),Emp_Address_ed.get(),Emp_Status_ed.get(),str(Emp_DOB_ed.get()),Emp_Salary_ed.get(),Emp_Passwd_ed.get(),Emp_Remark_ed.get(),Edit_ID.get())
                
                c.execute(query)
                
                Updt.destroy()
                
                db.commit()
                db.close()
                
            def exit2():
                exit2=messagebox.askyesno("Employee system","Do you want to exit the system")
                if exit2==True:
                    root.destroy()
                    return
            
            f_a = LabelFrame(root,padx=10, pady=10, bg='#FFFFCC',  relief= RIDGE, bd=6)
            f_a.grid(row=0, column=0)
            
            
            #Create text boxes
            
            Emp_ID = Entry(f_a, width =30, font=('Courier New',16,'bold','italic',),bd=5,justify='left')
            Emp_ID.grid(row=0, column=1, padx=20)
            Emp_Name = Entry(f_a, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
            Emp_Name.grid(row=1, column=1, padx=20)
            Emp_Address = Entry(f_a, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
            Emp_Address.grid(row=2, column=1, padx=20)
            Emp_DOB = Entry(f_a, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
            Emp_DOB.grid(row=3, column=1, padx=20)
            Emp_DOB.insert(0, "yyyy-mm-dd")
            Emp_Status = Entry(f_a, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
            Emp_Status.grid(row=4, column=1, padx=20)
            Emp_Salary = Entry(f_a, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
            Emp_Salary.grid(row=5, column=1, padx=20)
            Emp_Passwd = Entry(f_a, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
            Emp_Passwd.grid(row=7, column=1, padx=20)
            Emp_Remark = Entry(f_a, width =30, font=('Courier New',16,'bold','italic'),bd=5,justify='left')
            Emp_Remark.grid(row=8, column=1, padx=20)
            
            #Create Text Box Labels
            
            Emp_ID_lbl = Label(f_a, text="ID No.", bg='#FFFFCC')
            Emp_ID_lbl.grid(row=0, column=0)
            Emp_Name_lbl = Label(f_a, text="Name", bg='#FFFFCC')
            Emp_Name_lbl.grid(row=1, column=0)
            Emp_Address_lbl = Label(f_a, text="Address", bg='#FFFFCC')
            Emp_Address_lbl.grid(row=2, column=0)
            Emp_DOB_lbl = Label(f_a, text="Date of Birth", bg='#FFFFCC')
            Emp_DOB_lbl.grid(row=3, column=0)
            Emp_Status_lbl = Label(f_a, text="Position", bg='#FFFFCC')
            Emp_Status_lbl.grid(row=4, column=0)
            Emp_Salary_lbl = Label(f_a, text="Salary", bg='#FFFFCC')
            Emp_Salary_lbl.grid(row=5, column=0)
            Emp_Passwd_lbl = Label(f_a, text="Password", bg='#FFFFCC')
            Emp_Passwd_lbl.grid(row=7, column=0)
            Emp_Remark_lbl = Label(f_a, text="Remarks", bg='#FFFFCC')
            Emp_Remark_lbl.grid(row=8, column=0)
            
            f_ab = LabelFrame(root,padx=70, pady=10, bg='#212121',  relief= GROOVE, bd=6)
            f_ab.grid(row=1, column=0)
            
            #Create Submit Button
            add_btn = Button(f_ab, text="Add Record", command=submit, padx=5, pady=5, bd=8)
            add_btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=88)
            #Create query Button
            query_btn = Button(f_ab, text="Show Records", command = query, padx=5, pady=5, bd=8)
            query_btn.grid(row=2, column=1, columnspan=2, padx=10, pady=10, ipadx=82)
            
            Edit_ID = Entry(f_ab, width =17, font=('Courier New',18,'bold','italic',), bd=5,justify='left')
            Edit_ID.grid(row=3, column=1, padx=20, columnspan=2)
            
            Edit_ID_lbl = Label(f_ab, text="Select ID", bg='#D5D8DC',fg='#455A64', font =('Book Antiqua',18))
            Edit_ID_lbl.grid(row=3, column=0)
            
            #Create Delete Button
            delete_btn = Button(f_ab, text="Delete Records", command = delete, padx=5, pady=5, bd=8)
            delete_btn.grid(row=4, column=1, columnspan=2, padx=10, pady=10, ipadx=80)
            #Create Update Button
            update_btn = Button(f_ab, text="Edit Record", command = update_screen, padx=5, pady=5, bd=8)
            update_btn.grid(row=5, column=1, columnspan=2, padx=10, pady=10, ipadx=90)

            #Create Exit button
            exit_btn = Button(f_ab, text="Exit", command = exit2, padx=5, pady=5, bd=8)
            exit_btn.grid(row=6, column=1, columnspan=2, padx=10, pady=10, ipadx=109)
            
            root.mainloop() 
            
        else:
            messagebox.showwarning("Login Error","Credentials are Incorrect")
        

    user_lbl = Label(login_a, text="User Name", bg='#FFEB3B')
    user_lbl.grid(row=0, column=0)
    passwd_lbl = Label(login_a, text="Password", bg='#FFEB3B')
    passwd_lbl.grid(row=1, column=0)
    
    user = Entry(login_a, width =20, font=('Courier New',16,'bold','italic',),bd=5,justify='left')
    user.grid(row=0, column=1, padx=20)
    user.insert(0, "ADMIN")
    
    passwd = Entry(login_a, show="*",  width =20, font=('Courier New',16,'bold','italic',),bd=5,justify='left')
    passwd.grid(row=1, column=1, padx=20)
    
    submit_btn = Button(login_a, text="Login", command=login, padx=5, pady=5, bd=8)
    submit_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10, ipadx=104)
        
    login_a.mainloop()
    
    

def Emp():

    conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
    c=conn.cursor()

    root=Toplevel                    ()
    root.title("EMPLOYEE")
    #root.geometry("300x300")
    root.configure(bg="#F38F3C",bd=5)
    root.iconbitmap("appimg.ico")


    def popup():
        m=messagebox.askyesno("confirmation","Are You Sure You Want To Exit")
        if(m==True):
            root.destroy()

    def update1():
        
        def check():
            
            k=0
            import mysql.connector as mysql
            conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
            c=conn.cursor()
            c.execute("SELECT Emp_ID,Emp_Passwd from employee")
            m=c.fetchall()
            #h.delete(0,END)
            f=h.get()
            g=p.get()
            x=(f,g)
            def update():
                conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
                c=conn.cursor()
                global hm
                hm=Toplevel()
                hm.title("Update")
                hm.geometry("390x200")
                hm.configure(bg="#AACFD1")
                hm.iconbitmap("appimg.ico")
            

                #creating entry widgets
                addup=Entry(hm,width=30,font=('Courier New',10,'bold'))
                #a=str(addup.get())

                def save():
                    conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
                    c=conn.cursor()
                
                    ID=int(h.get())
                
                    query= " UPDATE employee SET Emp_Address = %s  WHERE (Emp_ID= %s) "
                    value= (addup.get(),ID)
                    c.execute(query,value)
                    messagebox.showinfo("Success","Your address was successfully updated")
                

                    print(c.rowcount, "record(s) affected")
                    addup.delete(0,END)
                    conn.commit()
                    conn.close()
                    #creating labels
                l1=Label(hm,text="New Address*",bg="#AACFD1")
                save_bttn=Button(hm,text="Save",command=save)


                #placing labels/entry widget
                addup.grid(row=0,column=1,padx=10)
                l1.grid(row=0,column=0,padx=5)
                save_bttn.grid(row=1,column=1,padx=10)








            for i in m:
                if(int(f)==i[0]and g==i[1]):
                    update()

                else:
                    k=k+1
                    continue

            if(k==len(m)):
                m=messagebox.showinfo("ERROR","The entered ID/ Password is wrong",icon="warning")



    
        global hm1
        hm1=Toplevel()
        hm1.iconbitmap("appimg.ico")
        hm1.title("Authorisation")
        hm1.configure(bg="#E3E23C")
        hm1.geometry("330x100")
        h=Entry(hm1,width=30,font=('Courier New',10,'bold'))
        p=Entry(hm1,width=30,font=('Courier New',10,'bold'),show="*")
        h.grid(row=0,column=1)
        p.grid(row=1,column=1)
        l=Label(hm1,text="Employee ID:",bg="#E3E23C")
        n=Label(hm1,text="Password:",bg="#E3E23C")
        l.grid(row=0,column=0)
        n.grid(row=1,column=0)
        #x=h.get()
        ch=Button(hm1,text="Verify",command=check)
        ch.grid(row=2,column=1,columnspan=2)
    
    

    def tax():
        global hm1
        def check():
            k=0
            import mysql.connector as mysql
            conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
            c=conn.cursor()
            c.execute("SELECT Emp_ID,Emp_Passwd from employee")
            m=c.fetchall()
            #h.delete(0,END)
            f=h.get()
            g=p.get()
            x=(f,g)


            def calc():
                conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
                c=conn.cursor()
                query="SELECT Emp_Salary from employee WHERE (Emp_ID=%s)"
                a=(h.get(),)
                c.execute(query,a)
                m=c.fetchall()
                z=m[0][0]
               
                #y=0.123*z
                if(z<=200000 ):
                    messagebox.showinfo("TAX BILL","Sorry, you dont pay any tax")
                    hm1.destroy()
                if(z>200000 and z<=500000):
                    y=0.123*z
                    messagebox.showinfo("TAX BILL","The amount of tax you pay is: Rs."+str(y))
                    hm1.destroy()
                if(z>500000 and z<=1000000):
                    y=0.15*z
                    messagebox.showinfo("TAX BILL","The amount of tax you pay is: Rs."+str(y))
                    hm1.destroy()
                if(z>1000000 and z<=2000000):
                    y=0.20*z
                    messagebox.showinfo("TAX BILL","The amount of tax you pay is: Rs."+str(y))
                    hm1.destroy()
                if(z>2000000):
                    y=0.30*z
                    messagebox.showinfo("TAX BILL","The amount of tax you pay is: Rs."+str(y))
                    hm1.destroy()


            for i in m:
                if(int(f)==i[0]and g==i[1]):
                    calc()

                else:
                    k=k+1
                    continue
            if(k==len(m)):
                m=messagebox.showinfo("ERROR","The entered ID/ Password is wrong",icon="warning")


    
        hm1=Toplevel()
        hm1.iconbitmap("appimg.ico")
        hm1.title("Authorisation")
        hm1.configure(bg="#B4EFAE")
        hm1.geometry("330x100")
        h=Entry(hm1,width=30,font=('Courier New',10,'bold'))
        p=Entry(hm1,width=30,font=('Courier New',10,'bold'),show="*")
        h.grid(row=0,column=1)
        p.grid(row=1,column=1)
        l=Label(hm1,text="Employee ID:",bg="#B4EFAE")
        n=Label(hm1,text="Password:",bg="#B4EFAE")
        l.grid(row=0,column=0)
        n.grid(row=1,column=0)
        #x=h.get()
        ch=Button(hm1,text="Verify",command=check)
        ch.grid(row=2,column=1,columnspan=2)
    






    def att():
        from datetime import datetime
        import mysql.connector as mysql
        now = datetime.now()
        #b = now.strftime("%H:%M:%S")
        #print(current_time)
        import datetime
        a = datetime.date.today()
        #print(datetime.date.today())
        conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
        c=conn.cursor()
        def check():
            k=0
            import mysql.connector as mysql
            conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
            c=conn.cursor()
            c.execute("SELECT Emp_ID,Emp_Passwd from employee")
            m=c.fetchall()
            #h.delete(0,END)

            def attmark():

                def intime():
                    b = now.strftime("%H:%M:%S")
                    conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
                    c=conn.cursor()
                    query="INSERT INTO `emp_data`.`emp_%s` (`date`, `in_time`) VALUES (%s,%s);" 
                    value=(int(h.get()),a,b)
                    c.execute(query,value)
                    messagebox.showinfo("Attendence","In-time marked successfully")
                    conn.commit()
                    conn.close()
                def outtime():
                    z= now.strftime("%H:%M:%S")
                    conn=mysql.connect(host="localhost",user="root",passwd="Samarth2002#",database="emp_data")
                    d=conn.cursor()
                    query2="UPDATE `emp_data`.`emp_%s` SET `out_time` = '%s' WHERE (`date` = '%s')"%(int(h.get()),z,a)
    
                    d.execute(query2)
                    messagebox.showinfo("Attendence","Out-time marked successfully")
                    conn.commit()
                    conn.close()



                hm2=Toplevel()
                hm2.iconbitmap("appimg.ico")
                hm2.title("Attendence")
                hm2.configure(bg="#9CE8F5")
                hm2.geometry("400x300")
                frame1=LabelFrame(hm2,text="",padx=50,pady=30,bd=6,bg="#F7F1DE")
                #frame2=LabelFrame(hm2,text="",padx=50,pady=30,bd=6,bg="#F7F1DE")

                frame1.pack()
                frame2.pack()
                b1=Button(frame1,text="IN-TIME",command =intime,bd=8).grid(row=0,column=0,columnspan=2,ipadx=50,pady=10,padx=50)
                b2=Button(frame1,text="OUT-TIME",command=outtime,bd=8).grid(row=1,column=0,columnspan=2,ipadx=50,pady=10,padx=50)


                conn.commit()
                conn.close()
    
            f=h.get()
            g=p.get()
            x=(f,g)
            for i in m:
                if(int(f)==i[0]and g==i[1]):
                    attmark()
                else:
                    k=k+1
                    continue

            if(k==len(m)):
                messagebox.showinfo("ERROR","The entered ID/ Password is wrong",icon="warning")




    
        #creating a top level
        hm1=Toplevel()
        hm1.iconbitmap("appimg.ico")
        hm1.title("Authorisation")
        hm1.configure(bg="#9CE8F5")
        hm1.geometry("330x100")
        h=Entry(hm1,width=30,font=('Courier New',10,'bold'))
        p=Entry(hm1,width=30,font=('Courier New',10,'bold'),show="*")
        h.grid(row=0,column=1)
        p.grid(row=1,column=1)
        l=Label(hm1,text="Employee ID:",bg="#9CE8F5")
        n=Label(hm1,text="Password:",bg="#9CE8F5")
        l.grid(row=0,column=0)
        n.grid(row=1,column=0)
        #x=h.get()
        ch=Button(hm1,text="Verify",command=check)
        ch.grid(row=2,column=1,columnspan=2)
    
   
    
    
    
    #creating frames:
    frame1=LabelFrame(root,text="",padx=50,pady=30,bd=6,bg="#F7F1DE")
    frame2=LabelFrame(root,text="",padx=50,pady=30,bd=6,bg="#F7F1DE")

    frame1.pack()
    frame2.pack()


    #creating button
    upd_bttn=Button(frame1,text="Update Address",padx=28,pady=10,command=update1,bd=8)
    att_bttn=Button(frame1,text="Attendence",padx=50,pady=10,command=att,bd=8)
    tax_bttn=Button(frame1,text="Tax Info",command=tax,padx=50,pady=10,bd=8)
    exit_bttn=Button(frame2,text="EXIT",command=popup)

    #placing button
    upd_bttn.grid(row=1,column=0,columnspan=2,ipadx=60,pady=10)
    att_bttn.grid(row=0,column=0,columnspan=2,ipadx=49,pady=10)
    tax_bttn.grid(row=4,column=0,columnspan=2,ipadx=55,pady=10)
    exit_bttn.grid(row=0,column=5,ipadx=10)


    #end committment
    conn.commit()
    conn.close()
    


def exit():
    m=messagebox.askyesno("Employee system","Do you want to exit the system")
    if m==True:
        home.destroy()
        return

f_m = LabelFrame(home, padx=50, pady=50, bg='#BBDEFB', bd=6)
f_m.pack(padx=10, pady=10)



admin_btn = Button(f_m, text="ADMIN", command=Admin, padx=10, pady=10, bd=8)
#admin_btn.pack(padx=10, pady=10, ipadx=110)
admin_btn.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=110)

emp_btn = Button(f_m, text="EMPLOYEE", command=Emp, padx=10, pady=10, bd=8)
#emp_btn.pack(padx=10, pady=10, ipadx=105)
emp_btn.grid(row=2, column=1, columnspan=2, padx=10, pady=10, ipadx=105)

Date=StringVar()
Date.set(time.strftime("%d/%m/%Y"))
date=Label(f_m, textvariable=Date ,font=('Castellar',12,'italic'), fg="#546E7A",bg="#BBDEFB").grid(row=0, column=2)

exit_btn = Button(home, text="EXIT", command = exit, padx=10, pady=10, bd=8)
exit_btn.pack(side='top', padx=10, pady=10, ipadx=120)
#exit_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx=125)



home.mainloop()
