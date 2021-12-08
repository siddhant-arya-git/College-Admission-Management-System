from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as mcon
from tkinter import messagebox
from tkinter import filedialog
import uuid

mydb=mcon.connect(host="localhost", user="root", passwd="sqlsid", database="college")
c=mydb.cursor()
query1="Create table if not exists student_login(username varchar(100) primary key, password varchar(100));"
query2="Create table if not exists staff_login(username varchar(100) primary key, password varchar(100));"
c.execute(query1)
c.execute(query2)
mydb.commit()


student_photo_path="D:/Programs/tkinter_project/student_photo"
student_aadhar_path="D:/Programs/tkinter_project/student_aadhar"
student_signature_path="D:/Programs/tkinter_project/student_signature"
parent_signature_path="D:/Programs/tkinter_project/parent_signature"
transfer_certificate_path="D:/Programs/tkinter_project/transfer_certificate"
result_12_path="D:/Programs/tkinter_project/result_12"
result_10_path="D:/Programs/tkinter_project/result_10"


root=Tk()
root.state("zoomed")
root.title("College Admission Management System")
root.iconbitmap("D:/Programs/tkinter_project/logo.ico")

main_frame=Frame(root)
main_frame.pack(side="top", expand=True, fill="both")

def dest():
    for widgets in main_frame.winfo_children():
        widgets.destroy()


def student(user):

    root.state('normal')
    main_frame.configure(bg='black')
    root.iconbitmap("D:/Programs/tkinter_project/logo.ico")

    #logo:
    logo=ImageTk.PhotoImage(Image.open("D:/Programs/tkinter_project/logo_image_black.png").resize((100,100),Image.ANTIALIAS))
    logo_label=Label(main_frame,image=logo)
    logo_label.logo=logo
    logo_label.grid(row=0,column=0)

    main_header=Label(main_frame,text="STUDENT'S PROFILE",font=("helvetica",40),bg="black",fg="white")
    main_header.grid(row=0,column=1,sticky=W+E,columnspan=2)
    
    student_profile_bar=Label(main_frame,text="Personal Details",font=("helvetica",20),bg="#484a4d",fg="white",anchor=W)
    student_profile_bar.grid(row=1,column=0,columnspan=3,sticky=W+E)


    ##################################################################################################################

    name_label=Label(main_frame,text="Student's Name: ",font=("helvetica",13),bg="black",fg="white",anchor=W)
    name_label.grid(row=2,column=0)

    query="select name from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=2,column=1,sticky=W+E)



    label=Label(main_frame,text="Student's Phone:",font=("helvetica",13),bg="black",fg="white",anchor=W)
    label.grid(row=3,column=0)

    query="select phone_number from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=3,column=1,sticky=W+E)

    

    label=Label(main_frame,text="Aadhar Number:",font=("helvetica",13),bg="black",fg="white",anchor=W)
    label.grid(row=4,column=0)

    query="select aadhar_no from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=4,column=1,sticky=W+E)



    label=Label(main_frame,text="Student's email:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=5,column=0)

    query="select email from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=5,column=1,sticky=W+E)
    

    
    label=Label(main_frame,text="Address:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=6,column=0,rowspan=5)

    query="select a_1 from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=6,column=1,sticky=W+E)

    query="select a_2 from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=7,column=1,sticky=W+E)

    query="select a_3 from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=8,column=1,sticky=W+E)

    query="select a_4 from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=9,column=1,sticky=W+E)

    query="select a_5 from student_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=10,column=1,sticky=W+E)

    #####################################################################################################3

    student_academic_bar=Label(main_frame,text="Academic Details",font=("helvetica",20),bg="#484a4d",fg="white",anchor=W)
    student_academic_bar.grid(row=11,column=0,columnspan=3,sticky=W+E)

    
    label=Label(main_frame,text="Marks in class 12th:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=12,column=0)

    query="select marks_12 from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=12,column=1,columnspan=2,sticky=W+E)



    label=Label(main_frame,text="Marks in class 10th:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=13,column=0)

    query="select marks_10 from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=13,column=1,columnspan=2,sticky=W+E)



    label=Label(main_frame,text="Marks in JEE:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=14,column=0)

    query="select marks_jee from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=14,column=1,columnspan=2,sticky=W+E)



    label=Label(main_frame,text="Stream:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=15,column=0)

    query="select stream from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=15,column=1,columnspan=2,sticky=W+E)



    label=Label(main_frame,text="Specialisation:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=16,column=0)

    query="select subject from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=16,column=1,columnspan=2,sticky=W+E)



    label=Label(main_frame,text="Name of class 12th Board:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=17,column=0)

    query="select board_name from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=17,column=1,columnspan=2,sticky=W+E)



    label=Label(main_frame,text="Board Roll Number:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=18,column=0)

    query="select board_roll from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=18,column=1,columnspan=2,sticky=W+E)



    label=Label(main_frame,text="JEE Roll number:",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=19,column=0)

    query="select jee_roll from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=19,column=1,columnspan=2,sticky=W+E)



    label=Label(main_frame,text="Name of school (class 12th):",font=("helvetica",13),bg="black",fg="white",anchor=W,background="black")
    label.grid(row=20,column=0)

    query="select name_school from academic_data where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    name=Label(main_frame,text=db,font=("helvetica",13),bg="grey",fg="white",anchor=W,borderwidth=1)
    name.grid(row=20,column=1,columnspan=2,sticky=W+E)


    ##################################################################################################################

    uploaded_bar=Label(main_frame,text="Uploaded Documents",font=("helvetica",20),bg="#484a4d",fg="white",anchor=W)
    uploaded_bar.grid(row=21,column=0,columnspan=3,sticky=W+E)

    global image_1
    query="select stu_photo from uploaded_doc where email=%s"
    c.execute(query,(user,))
    db=c.fetchone()
    for a in db:
        db=a
    image_1=ImageTk.PhotoImage(Image.open(db).resize((120,120),Image.ANTIALIAS))
    photo=Label(main_frame,image=image_1)
    photo.grid(row=2,column=2,rowspan=8)



    def fun_1():
        image_window=Toplevel()
        image_window.iconbitmap("D:/Programs/tkinter_project/logo.ico")
        global image_2
        query="select aadhar_doc from uploaded_doc where email=%s"
        c.execute(query,(user,))
        db=c.fetchone()
        for a in db:
            db=a
        image_2=ImageTk.PhotoImage(Image.open(db).resize((720,720),Image.ANTIALIAS))
        Label(image_window,image=image_2).pack()

        image_window.mainloop()
    
    def fun_2():
        image_window=Toplevel()
        image_window.iconbitmap("D:/Programs/tkinter_project/logo.ico")
        global image_2
        query="select result12_doc from uploaded_doc where email=%s"
        c.execute(query,(user,))
        db=c.fetchone()
        for a in db:
            db=a
        image_2=ImageTk.PhotoImage(Image.open(db).resize((720,720),Image.ANTIALIAS))
        Label(image_window,image=image_2).pack()

        image_window.mainloop()
    
    def fun_3():
        image_window=Toplevel()
        image_window.iconbitmap("D:/Programs/tkinter_project/logo.ico")
        global image_2
        query="select result10_doc from uploaded_doc where email=%s"
        c.execute(query,(user,))
        db=c.fetchone()
        for a in db:
            db=a
        image_2=ImageTk.PhotoImage(Image.open(db).resize((720,720),Image.ANTIALIAS))
        Label(image_window,image=image_2).pack()

        image_window.mainloop()
    
    def fun_4():
        image_window=Toplevel()
        image_window.iconbitmap("D:/Programs/tkinter_project/logo.ico")
        global image_2
        query="select transfer_doc from uploaded_doc where email=%s"
        c.execute(query,(user,))
        db=c.fetchone()
        for a in db:
            db=a
        image_2=ImageTk.PhotoImage(Image.open(db).resize((720,720),Image.ANTIALIAS))
        Label(image_window,image=image_2).pack()

        image_window.mainloop()
    
    def fun_5():
        image_window=Toplevel()
        image_window.iconbitmap("D:/Programs/tkinter_project/logo.ico")
        global image_2
        query="select sign_stu from uploaded_doc where email=%s"
        c.execute(query,(user,))
        db=c.fetchone()
        for a in db:
            db=a
        image_2=ImageTk.PhotoImage(Image.open(db).resize((720,720),Image.ANTIALIAS))
        Label(image_window,image=image_2).pack()

        image_window.mainloop()
    
    def fun_6():
        image_window=Toplevel()
        image_window.iconbitmap("D:/Programs/tkinter_project/logo.ico")
        global image_2
        query="select sign_pa from uploaded_doc where email=%s"
        c.execute(query,(user,))
        db=c.fetchone()
        for a in db:
            db=a
        image_2=ImageTk.PhotoImage(Image.open(db).resize((720,720),Image.ANTIALIAS))
        Label(image_window,image=image_2).pack()

        image_window.mainloop()



    button_1=Button(main_frame,text="Aadhar Card",command=fun_1)
    button_1.grid(row=22,column=0,padx=7,pady=7)

    button_2=Button(main_frame,text="Class 12th Result",command=fun_2)
    button_2.grid(row=22,column=1,padx=7,pady=7)

    button_3=Button(main_frame,text="Class 10th Result",command=fun_3)
    button_3.grid(row=22,column=2,padx=7,pady=7)

    button_4=Button(main_frame,text="Transfer Certificate",command=fun_4)
    button_4.grid(row=23,column=0,padx=7,pady=7)

    button_5=Button(main_frame,text="Personal Signature",command=fun_5)
    button_5.grid(row=23,column=1,padx=7,pady=7)

    button_6=Button(main_frame,text="Guardian Signature",command=fun_6)
    button_6.grid(row=23,column=2,padx=7,pady=7)


def staff_check(user):
    user=(str(user))
    query_exists="select count(username) from student_login where username=%s;"
    c.execute(query_exists,(user,))
    exists=c.fetchone()
    for a in exists:
        if a==0:
            messagebox.showwarning("Invalid","Student doesn't exist!")

        else:
            dest()
            student(user)


def administrator():
    root.state('normal')
    main_frame.configure(bg='black')
    root.iconbitmap("D:/Programs/tkinter_project/logo.ico")

    #logo:
    logo=ImageTk.PhotoImage(Image.open("D:/Programs/tkinter_project/logo_image_black.png").resize((100,100),Image.ANTIALIAS))
    logo_label=Label(main_frame,image=logo)
    logo_label.logo=logo
    logo_label.grid(row=0,column=0)

    main_header=Label(main_frame,text="Administrator Page",font=("helvetica",40),bg="black",fg="white")
    main_header.grid(row=0,column=1,sticky=W+E)
    
    find_label=Label(main_frame,text="Please enter the student's name:",font=("helvetica",13),bg="black",fg="white")
    find_label.grid(row=1,column=0,padx=10,pady=10)

    find_entry=Entry(main_frame,font=("helvetica",13),highlightthickness=1,width=40)
    find_entry.config(highlightbackground = "black", highlightcolor= "black")
    find_entry.grid(row=1,column=1,padx=10,pady=10)

    
    find_label_1=Label(main_frame,text="Please enter the student's email :",font=("helvetica",13),bg="black",fg="white")
    find_label_1.grid(row=2,column=0,padx=10,pady=10)

    find_entry_1=Entry(main_frame,font=("helvetica",13),highlightthickness=1,width=40)
    find_entry_1.config(highlightbackground = "black", highlightcolor= "black")
    find_entry_1.grid(row=2,column=1,padx=10,pady=10)

    new_button=Button(main_frame,text="Search",pady=5,padx=10,command=lambda:staff_check(find_entry_1.get()))
    new_button.grid(row=3,column=0,columnspan=2,padx=10)


def database_check(user, pword,user_type):

    user=(str(user))
    pword=(str(pword))
    user_type=str(user_type)
    flag_exist=1

    #For students:
    if user_type=="Student":
        query_exists="select count(username) from student_login where username=%s;"
        c.execute(query_exists,(user,))
        exists=c.fetchone()
        for a in exists:
            if a==0:
                messagebox.showwarning("Login Error","Student ID doesn't exist!")
                flag_exist=0
        
        if flag_exist!=0:
            query="select password from student_login where username=%s"
            c.execute(query,(user,))
            fetched_pass=c.fetchone()
            for a in fetched_pass:
                if pword!=a:
                    messagebox.showwarning("Login Error","Invalid Login Credentials!")
                else:
                    messagebox.showinfo("Success","Login Successful")
                    dest()
                    student(user)
    
    #For college staff:
    if user_type=="Staff":
        query_exists="select count(username) from staff_login where username=%s;"
        c.execute(query_exists,(user,))
        exists=c.fetchone()
        for a in exists:
            if a==0:
                messagebox.showwarning("Login Error","Staff ID doesn't exist!")
                flag_exist=0
        
        if flag_exist!=0:
            query="select password from staff_login where username=%s"
            c.execute(query,(user,))
            fetched_pass=c.fetchone()
            for a in fetched_pass:
                if pword!=a:
                    messagebox.showwarning("Login Error","Invalid Login Credentials!")
                else:
                    messagebox.showinfo("Success","Login Successful")
                    dest()
                    administrator()
                                      

def checkStore(name,phone,email,addr_1,addr_2,addr_3,addr_4,addr_5,aadhar_card,\
                marks_12,marks_10,marks_jee,stream,subject,board_name,board_roll,jee_roll,name_school,\
                student_p,aadhar_p,signature_p,signature_g,transfer,result12,result10,root1):

                query="Create table if not exists student_data(name varchar(50),phone_number varchar(20),email varchar(100) primary key, a_1 varchar(60),\
                            a_2 varchar(60),a_3 varchar(60),a_4 varchar(60),a_5 varchar(60),aadhar_no varchar(30));"
                c.execute(query)
                query="Create table if not exists academic_data(email varchar(100),marks_12 varchar(10),marks_10 varchar(10),marks_jee varchar(10),\
                    stream varchar(20),subject varchar(20),board_name varchar(40),board_roll varchar(40),jee_roll varchar(40),name_school varchar(60),\
                        constraint foreign key(email) references student_data(email));"
                c.execute(query)
                query="Create table if not exists uploaded_doc(email varchar(100),stu_photo varchar(1000),aadhar_doc varchar(1000),sign_stu varchar(1000),\
                    sign_pa varchar(1000),transfer_doc varchar(1000),result12_doc varchar(1000), result10_doc varchar(1000),\
                        constraint foreign key(email) references student_data(email));"
                c.execute(query)
                mydb.commit()

                if len(email)!=0:
                    query="select count(username) from student_login where username=%s;"
                    c.execute(query,(email,))
                    yes_or_no=c.fetchone()
                    for a in yes_or_no:
                        if a==1:
                            messagebox.showwarning("Invalid","E-mail already in use!",parent=root1)

                if len(name)==0:
                    messagebox.showwarning("Invalid","Name can't be empty!",parent=root1)
                elif len(phone)==0:
                    messagebox.showwarning("Invalid","Phone number can't be empty!",parent=root1)
                elif len(email)==0:
                    messagebox.showwarning("Invalid","E-mail can't be empty!",parent=root1)
                elif email.find("@")==-1 or email.find(".")==-1:
                    messagebox.showwarning("Invalid","Please include '@' and '.' in e-mail",parent=root1)
                elif len(addr_1)==0:
                    messagebox.showwarning("Invalid","Address line 1 can't be empty!",parent=root1)
                elif len(addr_3)==0:
                    messagebox.showwarning("Invalid","City can't be empty!",parent=root1)
                elif len(addr_4)==0:
                    messagebox.showwarning("Invalid","State can't be empty!",parent=root1)
                elif len(addr_5)==0:
                    messagebox.showwarning("Invalid","Zip code can't be empty!",parent=root1)
                elif len(aadhar_card)==0:
                    messagebox.showwarning("Invalid","Aadhar number can't be empty!",parent=root1)
                elif len(marks_12)==0:
                    messagebox.showwarning("Invalid","Class 12th marks can't be empty!",parent=root1)
                elif len(marks_10)==0:
                    messagebox.showwarning("Invalid","Class 10th marks can't be empty!",parent=root1)
                elif len(stream)==0:
                    messagebox.showwarning("Invalid","Stream can't be empty!",parent=root1)
                elif len(subject)==0 or subject=="--":
                    messagebox.showwarning("Invalid","Fill Subject Preference Correctly!",parent=root1)
                elif len(board_name)==0:
                    messagebox.showwarning("Invalid","Class 12th board name can't be empty!",parent=root1)
                elif len(board_roll)==0:
                    messagebox.showwarning("Invalid","Board roll number of class 12th can't be empty!",parent=root1)
                elif len(name_school)==0:
                    messagebox.showwarning("Invalid","Please provide school name!",parent=root1)
                elif len(student_p)==0:
                    messagebox.showwarning("Invalid","Please upload your photograph!",parent=root1)
                elif len(aadhar_p)==0:
                    messagebox.showwarning("Invalid","Please upload your aadhar card!",parent=root1)
                elif len(signature_p)==0:
                    messagebox.showwarning("Invalid","Please upload your signature!",parent=root1)
                elif len(signature_g)==0:
                    messagebox.showwarning("Invalid","Please upload your parent's signature!",parent=root1)
                elif len(transfer)==0:
                    messagebox.showwarning("Invalid","Please upload your transfer certificate!",parent=root1)
                elif len(result12)==0:
                    messagebox.showwarning("Invalid","Please upload your class 12th result!",parent=root1)
                elif len(result10)==0:
                    messagebox.showwarning("Invalid","Please upload your class 10th result!",parent=root1)
                else:
                    
                    values=(str(name),str(phone),str(email),str(addr_1),str(addr_2),str(addr_3),str(addr_4),str(addr_5),str(aadhar_card))
                    query="insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    c.execute(query, values)
                    mydb.commit()

                    values=(str(email),str(marks_12),str(marks_10),str(marks_jee),str(stream),str(subject),str(board_name),str(board_roll),str(jee_roll),str(name_school))
                    query="insert into academic_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                    c.execute(query, values)
                    mydb.commit()

                    #for all documents:
                    image=Image.open(student_p)
                    st_photo_store=f"{student_photo_path}/{str(uuid.uuid4())}.jpg"
                    image = image.save(st_photo_store)

                    image=Image.open(aadhar_p)
                    st_aadhar_store=f"{student_aadhar_path}/{str(uuid.uuid4())}.jpg"
                    image = image.save(st_aadhar_store)

                    image=Image.open(signature_p)
                    st_sign_store=f"{student_signature_path}/{str(uuid.uuid4())}.jpg"
                    image = image.save(st_sign_store)

                    image=Image.open(signature_g)
                    pa_sign_store=f"{parent_signature_path}/{str(uuid.uuid4())}.jpg"
                    image = image.save(pa_sign_store)
                    
                    image=Image.open(transfer)
                    st_tc_store=f"{transfer_certificate_path}/{str(uuid.uuid4())}.jpg"
                    image = image.save(st_tc_store)

                    image=Image.open(result12)
                    st_12_store=f"{result_12_path}/{str(uuid.uuid4())}.jpg"
                    image = image.save(st_12_store)

                    image=Image.open(result10)
                    st_10_store=f"{result_10_path}/{str(uuid.uuid4())}.jpg"
                    image = image.save(st_10_store)

                    values=(str(email),st_photo_store,st_aadhar_store,st_sign_store,pa_sign_store,st_tc_store,st_12_store,st_10_store)
                    query="insert into uploaded_doc values(%s,%s,%s,%s,%s,%s,%s,%s);"
                    c.execute(query, values)
                    mydb.commit()

                    messagebox.showinfo("Success!","You have successfully signed up, your login-id is your email address and password is your aadhar number",parent=root1)

                    query="Insert into student_login values(%s,%s);"
                    values=(str(email),str(aadhar_card))
                    c.execute(query, values)
                    mydb.commit()


def signup():
    root1=Toplevel()
    root1.title("College Admission Management System")
    root1.iconbitmap("D:/Programs/tkinter_project/logo.ico")
    root1.state("zoomed")
    root1.configure(background="grey")
    
    #logo:
    logo=ImageTk.PhotoImage(Image.open("D:/Programs/tkinter_project/logo_image_black.png").resize((100,100),Image.ANTIALIAS))
    logo_label=Label(root1,image=logo)
    logo_label.logo=logo
    logo_label.place(x=0,y=0)

    main_header=Label(root1,text="New Admission Registration",font=("helvetica",40),bg="black",fg="white",padx=385,pady=17)
    main_header.place(x=105,y=3)

    #code for Student Details:
    f_student_details=LabelFrame(root1,bg="#494646",fg="white",padx=10,pady=10,bd=3,relief=GROOVE)
    f_student_details.place(x=10,y=115)
    
    header_student_detail=Label(f_student_details,text="Student Details",font=("helvetica",18),padx=100)
    header_student_detail.grid(row=0,column=0,columnspan=3)

    name_label=Label(f_student_details,text="Enter Name: *",bg="#494646",fg="White",font=("helvetica",11))
    name_label.grid(row=1,column=0,padx=10,pady=10)

    name_entry=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    name_entry.config(highlightbackground = "black", highlightcolor= "black")
    name_entry.grid(row=1,column=1,padx=10,pady=10)

    phone_label=Label(f_student_details,text="Phone number: *",bg="#494646",fg="White",font=("helvetica",11))
    phone_label.grid(row=2,column=0)
    info_label=Label(f_student_details,text="(Include country code as well)",bg="#494646",fg="White")
    info_label.grid(row=3,column=1)

    phone_entry=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    phone_entry.config(highlightbackground = "black", highlightcolor= "black")
    phone_entry.grid(row=2,column=1,padx=10,pady=5)

    email_label=Label(f_student_details,text="E-mail address: *",bg="#494646",fg="White",font=("helvetica",11))
    email_label.grid(row=4,column=0,padx=10,pady=10)

    email_entry=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    email_entry.config(highlightbackground = "black", highlightcolor= "black")
    email_entry.grid(row=4,column=1,padx=10,pady=5)

    line_break=Label(f_student_details,pady=10,bg="#494646",font=("helvetica",11))
    line_break.grid(row=5,column=0)

    address_label_1=Label(f_student_details,text="Address Line 1: *",bg="#494646",fg="White",font=("helvetica",11))
    address_label_1.grid(row=6,column=0)
    info_label_1=Label(f_student_details,text="(Street Address/ Company Name/ Colony)",bg="#494646",fg="White")
    info_label_1.grid(row=7,column=1)

    address_label_2=Label(f_student_details,text="Address Line 2:",bg="#494646",fg="White",font=("helvetica",11))
    address_label_2.grid(row=8,column=0)
    info_label_2=Label(f_student_details,text="(House No./ Flat No./ Apartment/ Building/ Floor)",bg="#494646",fg="White")
    info_label_2.grid(row=9,column=1)


    address_label_3=Label(f_student_details,text="City: *",bg="#494646",fg="White",font=("helvetica",11))
    address_label_3.grid(row=10,column=0)

    address_label_4=Label(f_student_details,text="State: *",bg="#494646",fg="White",font=("helvetica",11))
    address_label_4.grid(row=11,column=0)

    address_label_5=Label(f_student_details,text="Zip Code: *",bg="#494646",fg="White",font=("helvetica",11))
    address_label_5.grid(row=12,column=0)

    address_entry_1=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    address_entry_1.config(highlightbackground = "black", highlightcolor= "black")
    address_entry_1.grid(row=6,column=1,pady=4)

    address_entry_2=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    address_entry_2.config(highlightbackground = "black", highlightcolor= "black")
    address_entry_2.grid(row=8,column=1,pady=4)

    address_entry_3=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    address_entry_3.config(highlightbackground = "black", highlightcolor= "black")
    address_entry_3.grid(row=10,column=1,pady=4)

    address_entry_4=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    address_entry_4.config(highlightbackground = "black", highlightcolor= "black")
    address_entry_4.grid(row=11,column=1,pady=4)

    address_entry_5=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    address_entry_5.config(highlightbackground = "black", highlightcolor= "black")
    address_entry_5.grid(row=12,column=1,pady=4)

    line_break_2=Label(f_student_details,pady=10,bg="#494646")
    line_break_2.grid(row=13,column=0)

    aadhar_label=Label(f_student_details,text="Aadhar Number/Passport Number: *",bg="#494646",fg="White",font=("helvetica",11))
    aadhar_label.grid(row=14,column=0)

    aadhar_entry=Entry(f_student_details,highlightthickness=1,width=30,font=("helvetica",11))
    aadhar_entry.config(highlightbackground = "black", highlightcolor= "black")
    aadhar_entry.grid(row=14,column=1,padx=10,pady=13)    



    #Code for Academic Details:
    f_academic_details=LabelFrame(root1,bg="#494646",fg="white",padx=10,pady=10,bd=3,relief=GROOVE)
    f_academic_details.place(x=550,y=115)

    header_academic_detail=Label(f_academic_details,text="Academic Details",font=("helvetica",18),padx=100)
    header_academic_detail.grid(row=0,column=0,columnspan=3)

    class_12_label=Label(f_academic_details,text=r"%age of marks in Class 12th: *",bg="#494646",fg="White",font=("helvetica",11))
    class_12_label.grid(row=1,column=0,padx=10,pady=10)

    class_12_entry=Entry(f_academic_details,highlightthickness=1,width=30,font=("helvetica",11))
    class_12_entry.config(highlightbackground = "black", highlightcolor= "black")
    class_12_entry.grid(row=1,column=1,pady=10,columnspan=2)
    
    class_10_label=Label(f_academic_details,text=r"%age of marks in Class 10th: *",bg="#494646",fg="White",font=("helvetica",11)) #marked raw to use %
    class_10_label.grid(row=2,column=0,padx=10,pady=10)

    class_10_entry=Entry(f_academic_details,highlightthickness=1,width=30,font=("helvetica",11))
    class_10_entry.config(highlightbackground = "black", highlightcolor= "black")
    class_10_entry.grid(row=2,column=1,pady=10,columnspan=2)

    jee_label=Label(f_academic_details,text=r"%ile in JEE:",bg="#494646",fg="White",font=("helvetica",11))
    jee_label.grid(row=3,column=0,padx=10,pady=10)

    jee_entry=Entry(f_academic_details,highlightthickness=1,width=30,font=("helvetica",11))
    jee_entry.config(highlightbackground = "black", highlightcolor= "black")
    jee_entry.grid(row=3,column=1,pady=10,columnspan=2)

    preference_label=Label(f_academic_details,text="Select Preference: *",bg="#494646",fg="White",font=("helvetica",11))
    preference_label.grid(row=4,column=0,padx=10,pady=10)

    clicked=StringVar()
    sub_clicked=StringVar()
    def sub_preference(self):
        global options_list
        stream=clicked.get()
        if stream=="B.Tech":
            sub_clicked.set("--")
            options_list=OptionMenu(f_academic_details,sub_clicked,"Computer Science","Electrical","Mechanical","Civil")
        if stream=="B.Com":
            sub_clicked.set("--")
            options_list=OptionMenu(f_academic_details,sub_clicked,"Economics","Marketing","Finance","Accounting")
        if stream=="B.A":
            sub_clicked.set("--")
            options_list=OptionMenu(f_academic_details,sub_clicked,"Literature","History","Journalism","Civics")
        if stream=="B.Sc":
            sub_clicked.set("--")
            options_list=OptionMenu(f_academic_details,sub_clicked,"Maths","Agriculture","Zoology","Biotechnology")
        options_list.grid(row=4,column=2)
        
    preference_list=OptionMenu(f_academic_details,clicked,"B.Tech","B.Sc","B.Com","B.A",command=sub_preference)
    preference_list.grid(row=4,column=1,pady=10)

    
    boards_label=Label(f_academic_details,text="Class 12th board name: *",bg="#494646",fg="White",font=("helvetica",11))
    boards_label.grid(row=5,column=0,padx=10,pady=10)
    
    boards_entry=Entry(f_academic_details,highlightthickness=1,width=30,font=("helvetica",11))
    boards_entry.config(highlightbackground = "black", highlightcolor= "black")
    boards_entry.grid(row=5,column=1,pady=10,columnspan=2)

    line_break_3=Label(f_academic_details,pady=10,bg="#494646")
    line_break_3.grid(row=6,column=0)

    board_rollnumber_label=Label(f_academic_details,text="Enter class 12th Board roll number: *",bg="#494646",fg="White",font=("helvetica",11))
    board_rollnumber_label.grid(row=7,column=0,padx=10,pady=10)

    board_rollnumber_entry=Entry(f_academic_details,highlightthickness=1,width=30,font=("helvetica",11))
    board_rollnumber_entry.config(highlightbackground = "black", highlightcolor= "black")
    board_rollnumber_entry.grid(row=7,column=1,pady=10,columnspan=2)

    jee_rollnumber_label=Label(f_academic_details,text="Enter JEE roll number:",bg="#494646",fg="White",font=("helvetica",11))
    jee_rollnumber_label.grid(row=8,column=0,padx=10,pady=10)

    jee_rollnumber_entry=Entry(f_academic_details,highlightthickness=1,width=30,font=("helvetica",11))
    jee_rollnumber_entry.config(highlightbackground = "black", highlightcolor= "black")
    jee_rollnumber_entry.grid(row=8,column=1,pady=10,columnspan=2)

    name_of_school_label=Label(f_academic_details,text="Enter Name of school (class 12th): *",bg="#494646",fg="White",font=("helvetica",11))
    name_of_school_label.grid(row=9,column=0,padx=10,pady=10)

    name_of_school_entry=Entry(f_academic_details,highlightthickness=1,width=30,font=("helvetica",11))
    name_of_school_entry.config(highlightbackground = "black", highlightcolor= "black")
    name_of_school_entry.grid(row=9,column=1,pady=10,columnspan=2)

    line_break_4=Label(f_academic_details,pady=29,bg="#494646")
    line_break_4.grid(row=10,column=0)



    #Upload Documents: 
    f_upload_documents=LabelFrame(root1,bg="#494646",fg="white",padx=10,pady=10,bd=3,relief=GROOVE)
    f_upload_documents.place(x=1090,y=115)
    
    header_student_detail=Label(f_upload_documents,text="Upload Documents",font=("helvetica",18),padx=100)
    header_student_detail.grid(row=0,column=0)  
    
    personal_photo_label=Label(f_upload_documents,text="Upload your own photograph (.jpg, .jpeg) *",bg="#494646",fg="White",font=("helvetica",11))
    personal_photo_label.grid(row=1,column=0)

    global personal_photo
    personal_photo=""
    def photo_student():
        global personal_photo
        personal_photo=filedialog.askopenfilename(initialdir="/Downloads",title="Student's Photograph",parent=root1,filetypes=(("Photograph",("*.jpg","*.jpeg")),))

    photo_button=Button(f_upload_documents,text="Click here!",command=photo_student)
    photo_button.grid(row=2,column=0)

    line_break_5=Label(f_upload_documents,pady=1,bg="#494646")
    line_break_5.grid(row=3,column=0)

    aadhar_label=Label(f_upload_documents,text="Upload Aadhar Card (.jpg, .jpeg) *",bg="#494646",fg="White",font=("helvetica",11))
    aadhar_label.grid(row=4,column=0)

    global aadhar
    aadhar=""
    def aadhar_student():
        global aadhar
        aadhar=filedialog.askopenfilename(initialdir="/Downloads",title="Student's Aadhar Card",parent=root1,filetypes=(("Photograph",("*.jpg","*.jpeg")),))

    aadhar_button=Button(f_upload_documents,text="Click here!",command=aadhar_student)
    aadhar_button.grid(row=5,column=0)

    line_break_6=Label(f_upload_documents,pady=1,bg="#494646")
    line_break_6.grid(row=6,column=0)

    personal_signature_label=Label(f_upload_documents,text="Upload student's Signature(.jpg, .jpeg,) *",bg="#494646",fg="White",font=("helvetica",11))
    personal_signature_label.grid(row=7,column=0)

    global personal_signature
    personal_signature=""
    def signature_student():
        global personal_signature
        personal_signature=filedialog.askopenfilename(initialdir="/Downloads",title="Student's Signature",parent=root1,filetypes=(("Photograph",("*.jpg","*.jpeg")),))

    personal_signature_button=Button(f_upload_documents,text="Click here!",command=signature_student)
    personal_signature_button.grid(row=8,column=0)

    line_break_7=Label(f_upload_documents,pady=1,bg="#494646")
    line_break_7.grid(row=9,column=0)

    parent_signature_label=Label(f_upload_documents,text="Upload parent's Signature(.jpg, .jpeg) *",bg="#494646",fg="White",font=("helvetica",11))
    parent_signature_label.grid(row=10,column=0)

    global parent_signature
    parent_signature=""
    def signature_parent():
        global parent_signature
        parent_signature=filedialog.askopenfilename(initialdir="/Downloads",title="Parent's Signature",parent=root1,filetypes=(("Photograph",("*.jpg","*.jpeg")),))

    parent_signature_button=Button(f_upload_documents,text="Click here!",command=signature_parent)
    parent_signature_button.grid(row=11,column=0)

    line_break_8=Label(f_upload_documents,pady=1,bg="#494646")
    line_break_8.grid(row=12,column=0)

    tc_label=Label(f_upload_documents,text="Upload Transfer Certificate(.jpg, .jpeg) *",bg="#494646",fg="White",font=("helvetica",11))
    tc_label.grid(row=13,column=0)

    global tc
    tc=""
    def transfer_certificate():
        global tc
        tc=filedialog.askopenfilename(initialdir="/Downloads",title="Transfer Certificate",parent=root1,filetypes=(("Photograph",("*.jpg","*.jpeg")),))

    tc_button=Button(f_upload_documents,text="Click here!",command=transfer_certificate)
    tc_button.grid(row=14,column=0)

    line_break_9=Label(f_upload_documents,pady=1,bg="#494646")
    line_break_9.grid(row=15,column=0)

    label_12=Label(f_upload_documents,text="Upload class 12th result(.jpg, .jpeg) *",bg="#494646",fg="White",font=("helvetica",11))
    label_12.grid(row=16,column=0)

    global result_12
    result_12=""
    def result_12_function():
        global result_12
        result_12=filedialog.askopenfilename(initialdir="/Downloads",title="Class 12th Result",parent=root1,filetypes=(("Photograph",("*.jpg","*.jpeg")),))

    button_12=Button(f_upload_documents,text="Click here!",command=result_12_function)
    button_12.grid(row=17,column=0)

    line_break_10=Label(f_upload_documents,pady=1,bg="#494646")
    line_break_10.grid(row=18,column=0)

    label_10=Label(f_upload_documents,text="Upload class 10th result(.jpg, .jpeg) *",bg="#494646",fg="White",font=("helvetica",11))
    label_10.grid(row=19,column=0)

    global result_10
    result_10=""
    def result_10_function():
        global result_10
        result_10=filedialog.askopenfilename(initialdir="/Downloads",title="Class 10th Result",parent=root1,filetypes=(("Photograph",("*.jpg","*.jpeg")),))

    button_10=Button(f_upload_documents,text="Click here!",command=result_10_function)
    button_10.grid(row=20,column=0)

    def submit_all_information():
        checkStore(name_entry.get(), phone_entry.get(), email_entry.get(), address_entry_1.get(), address_entry_2.get(),\
                    address_entry_3.get(), address_entry_4.get(), address_entry_5.get(), aadhar_entry.get(),\
                    class_12_entry.get(), class_10_entry.get(), jee_entry.get(), clicked.get(), sub_clicked.get(),\
                    boards_entry.get(), board_rollnumber_entry.get(), jee_rollnumber_entry.get(), name_of_school_entry.get(),\
                    personal_photo, aadhar,personal_signature, parent_signature, tc, result_12, result_10, root1)

    #The submit button:
    submit_button=Button(root1,text="Submit",bg="#f5738b",fg="white",padx=120,font=("Times",14,"bold"),\
                        command=submit_all_information)
    submit_button.place(x=650,y=700)

    
    root1.mainloop()


def password_page():
    #Background:
    image_path='D:/Programs/tkinter_project/password_background.jpg'
    img = ImageTk.PhotoImage(Image.open(image_path).resize((1920,1080), Image.ANTIALIAS))
    lbl = Label(main_frame, image=img)
    lbl.img = img  
    lbl.place(relx=0.5, rely=0.5, anchor='center')

    #logo+Header:
    logo=ImageTk.PhotoImage(Image.open("D:/Programs/tkinter_project/logo_image_black.png").resize((100,100),Image.ANTIALIAS))
    logo_label=Label(main_frame,image=logo)
    logo_label.logo=logo
    logo_label.place(x=0,y=0)

    header=Label(main_frame,text="College Admission Management System",font=("helvetica",40),bg="black",fg="white",padx=242,pady=18)
    header.place(x=105,y=3)

    #Names of both group members:
    names=Label(main_frame,text="Developed by Siddhant Arya and Abinash Patra",relief=SUNKEN)
    names.place(rely=1,relx=0.085,anchor=S)

    #code for the password frame:
    main=Label(main_frame,text="User Login ",font=("helvetica",18),relief=GROOVE,bg="#494646",fg="white",padx=230,pady=8,bd=3)
    main.place(x=480,y=185)

    login_frame=LabelFrame(main_frame,bg="#494646",fg="white",padx=10,pady=10,bd=3,relief=GROOVE)
    login_frame.grid(row=0,column=0,padx=480,pady=230)

    username=Label(login_frame,text="Username:",font=("helvetica",13),bg="#494646",fg="White")
    username.grid(row=0,column=0,pady=10,padx=10)
    
    username_entry=Entry(login_frame,font=("helvetica",13),highlightthickness=1,width=40)
    username_entry.config(highlightbackground = "black", highlightcolor= "black")
    username_entry.grid(row=0,column=1,padx=10,pady=10)

    password=Label(login_frame,text="Password:",font=("helvetica",13),bg="#494646",fg="White")
    password.grid(row=1,column=0,pady=10,padx=10)

    password_entry=Entry(login_frame,font=("helvetica",13),highlightthickness=1,show="*",width=40)
    password_entry.config(highlightbackground = "black", highlightcolor= "black")
    password_entry.grid(row=1,column=1,padx=10,pady=10)

    def show_password():
        password_entry.configure(show="")

    eye="D:/Programs/tkinter_project/show_password_button.jpg"
    show_password_img=ImageTk.PhotoImage(Image.open(eye).resize((15,15),Image.ANTIALIAS))
    show_password_button=Button(login_frame,image=show_password_img,command=show_password)
    show_password_button.show_password_img=show_password_img
    show_password_button.grid(row=1,column=2)

    user_type=Label(login_frame,text="Select User type: ",font=("helvetica",13),bg="#494646",fg="White")
    user_type.grid(row=2,column=0,pady=10,padx=10)

    clicked=StringVar()
    clicked.set("Student")
    drop_list=OptionMenu(login_frame,clicked,"Student","Staff")
    drop_list.grid(row=2,column=1,padx=10,pady=10)

    submit_button=Button(login_frame,text="Sign In",bg="#4383D4",fg="white",padx=120,font=("Times",12,"bold"),\
                        command=lambda:database_check(username_entry.get(),password_entry.get(),clicked.get()))
    submit_button.grid(row=3,column=0,columnspan=3,pady=10,padx=10)

    new=Label(login_frame,text="New Student? Click the below button:",font=("helvetica",13),bg="#494646",fg="White")
    new.grid(row=4,column=0,columnspan=3,pady=10,padx=10)

    new_button=Button(login_frame,text="Sign-Up",pady=5,padx=10,command=signup)
    new_button.grid(row=5,column=0,columnspan=3,padx=10)


password_page()
root.mainloop()