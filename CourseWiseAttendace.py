from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
#from FRWindo import face_recoganization
import cx_Oracle as con
from tkcalendar import Calendar, DateEntry
import tkinter as tk
from datetime import date
connString = 'FRAS/FRAS@localhost:1521/xe'
class CourseWiseAttendace:
    def __init__(self,root):
        self.root=root
        #self.root.geometry('400x400+0+0')
        width= self.root.winfo_screenwidth() 
        height= self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (width/1.2, height/1.2-10))

        #back img3
        img3=Image.open(r"IMG\Grey.jpg")
        img3=img3.resize((1530,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=(width/1.2)-10,height=(height/1.2-20))
        
        #main frame for stud details
        main_frame =Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=1,y=45,width=(width/1.2)-10,height=(height/1.2-20))
        
        #Right Side Teacher Fram
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Faculty Operations",font=("times new roman",15,"bold"))
        right_frame.place(x=750,y=0,width=340,height=500)
        
        #Attendace Date
        todays_date = date.today()
        # fetching the current year, month and day of today
        curnt_yr=todays_date.year #cmnth=todays_date.month, cday=todays_date.day
        lblDate=Label(right_frame,text="Date: ",font=("times new roman",15,"bold"),bg="white",fg="black")
        lblDate.place(x=5,y=15)
                
        self.curAttendaceDt = DateEntry(right_frame, width=12, background='darkblue', foreground='white', borderwidth=1, year=int(curnt_yr),  locale='en_US', date_pattern='dd-mm-y')
        self.curAttendaceDt.place(x=100, y=15, height=21, width=180)
           
        #Select Course
        CourseVal=self.Get_Course_data()
        lblCourse=Label(right_frame,text="Course: ",font=("times new roman",15,"bold"),bg="white",fg="black")
        lblCourse.place(x=5,y=60)
        self.course_combo=ttk.Combobox(right_frame,font=("times new roman",12,"bold"),width=20)
        self.course_combo["values"]=CourseVal
        print(CourseVal)
        self.course_combo.current(0)
        self.course_combo.place(x=100,y=60,width=180,height=21)
        
        #Enter Passcode / Optional
        lblPssKey=Label(right_frame,text="Pass Key: ",font=("times new roman",13,"bold"),bg="white")
        lblPssKey.place(x=5,y=100,height=21)
        self.txtPassKey=ttk.Entry(right_frame,width=20,font=("times new roman",13,"bold"))
        self.txtPassKey.place(x=100,y=100,width=180,height=21)

        #Submit & Cancel Button
        btnSubmit=Button(right_frame,text="Submit",command=self.add_dataAttndace,font=("times new roman",13,"bold"),bg="white")
        btnSubmit.place(x=80,y=180,height=30)
        btnCancel=Button(right_frame,text="Cancel",command=self.exit, font=("times new roman",13,"bold"),bg="white")
        btnCancel.place(x=160,y=180,height=30)
         
        self.root.title("Subject/Course Wise Attendace")
        #back img3
        title_lb=Label(root,text="Course Wise Attendace",font=("times new roman",15,"bold"),bg="white",fg="red")
        title_lb.place(x=00,y=10,width=(width/1.2))                

        #================Present Student Table Frame==============
        left_frame=Label(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendace",font=("times new roman",15,"bold"))
        left_frame.place(x=5,y=2,width=725,height=650)

        lblAbsStud=Label(left_frame,bd=2,bg="white",relief=RIDGE,text="Today's Present Student's",font=("times new roman",15,"bold"))
        lblAbsStud.place(x=5,y=2,width=710)
        
        table_frame=Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=3,y=35,width=710,height=235)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.stud_table=ttk.Treeview(table_frame,column=("Studid","RollNo","Name","Div","Sem"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)#"Dep",,"Course"
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)
        
        self.stud_table.heading("Studid",text="StudentID")
        self.stud_table.heading("RollNo",text="RollNo")
        self.stud_table.heading("Name",text="Name")
        #self.stud_table.heading("Dep",text="Department")
        self.stud_table.heading("Div",text="Division")
        self.stud_table.heading("Sem",text="Semester")
        #self.stud_table.heading("Course",text="Course")
        self.stud_table["show"]="headings"
        self.stud_table.column("Studid",width=100)
        self.stud_table.column("RollNo",width=100)
        self.stud_table.column("Name",width=100)
        #self.stud_table.column("Dep",width=100)    
        self.stud_table.column("Div",width=100)
        self.stud_table.column("Sem",width=100)   
        #self.stud_table.column("Course",width=100)        
        self.stud_table.pack(fill=BOTH,expand=1)
        ##self.getmxsrno()
        self.PresentStud_data()

              #=============Absent Student Details=====================
        lblAbsStud=Label(left_frame,bd=2,bg="white",relief=RIDGE,text="Today's Absent Student's",font=("times new roman",15,"bold"))
        lblAbsStud.place(x=5,y=310,width=710)
        
        table_absframe=Frame(left_frame,bd=2,bg="white",relief=RIDGE)
        table_absframe.place(x=3,y=340,width=710,height=235)
        scroll_x=ttk.Scrollbar(table_absframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_absframe,orient=VERTICAL)
        self.ABSstud_table=ttk.Treeview(table_absframe,column=("Studid","RollNo","Name","Div","Sem"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)#"Dep",,"Course"
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.ABSstud_table.xview)
        scroll_y.config(command=self.ABSstud_table.yview)        
        self.ABSstud_table.heading("Studid",text="StudentID")
        self.ABSstud_table.heading("RollNo",text="RollNo")
        self.ABSstud_table.heading("Name",text="Name")
        #self.ABSstud_table.heading("Dep",text="Department")
        self.ABSstud_table.heading("Div",text="Division")
        self.ABSstud_table.heading("Sem",text="Semester")
        #self.ABSstud_table.heading("Course",text="Course")
        self.ABSstud_table["show"]="headings"
        self.ABSstud_table.column("Studid",width=100)
        self.ABSstud_table.column("RollNo",width=100)
        self.ABSstud_table.column("Name",width=100)
        #self.ABSstud_table.column("Dep",width=100)    
        self.ABSstud_table.column("Div",width=100)
        self.ABSstud_table.column("Sem",width=100)   
        #self.ABSstud_table.column("Course",width=100)        
        self.ABSstud_table.pack(fill=BOTH,expand=1)
        self.AbsStud_data()

          ##Manipulate Student Present And Absent Student
        imgprs=Image.open(r"IMG\Arrow_DOWAN.png")
        imgprs=imgprs.resize((15,15),Image.ANTIALIAS)
        self.photoimgprs=ImageTk.PhotoImage(imgprs)

        btnAddAsPresent=Button(left_frame,image=self.photoimgprs,cursor="hand2", command=self.addPresentiToabasent)
        btnAddAsPresent.place(x=200,y=275,width=80, height=30)#

        imgabs=Image.open(r"IMG\Arrow_UP.png")
        imgabs=imgabs.resize((15,15),Image.ANTIALIAS)
        self.photoimgabs=ImageTk.PhotoImage(imgabs)

        btnAddAsAbsent=Button(left_frame,image=self.photoimgabs,cursor="hand2", command=self.addAbsentiToPresenti)
        btnAddAsAbsent.place(x=385,y=275,width=80, height=30) 
         
    def addPresentiToabasent(self):
        print("Presenti std list")
        item_count = len(self.stud_table.get_children())
        if(item_count==0):
            return
        curItem = self.stud_table.focus()
        item=(self.stud_table.item(curItem)['values'])
        if(item_count==0 or self.stud_table.focus()==""):
            return
        self.ABSstud_table.insert("",'end',text=str(item[0]),values=(str(item[0]),str(item[1]),str(item[2]), str(item[3]),str(item[4])))
        self.stud_table.delete(self.stud_table.selection()[0])
        
    def addAbsentiToPresenti(self):
        print("Absenty Stdents")
        item_count = len(self.ABSstud_table.get_children())
        if(item_count==0):
            return
        curItem = self.ABSstud_table.focus()
        item=(self.ABSstud_table.item(curItem)['values'])
        print(item)
        print( "****----"+self.ABSstud_table.focus())
        if(item_count==0 or self.ABSstud_table.focus()==""):
            return
        self.stud_table.insert("",'end',text=str(item[0]),values=(str(item[0]),str(item[1]),str(item[2]), str(item[3]),str(item[4])))
        self.ABSstud_table.delete(self.ABSstud_table.selection()[0])
     
    def SaveAttendace(self): #this function called in sysytem login button 
         self.new_window=Toplevel(self.root)
         self.SD=face_recoganization(self.new_window)
         
         #Get Present Students List
    def PresentStud_data(self):
        try:
            self.stud_table.delete(*self.stud_table.get_children())# 
            query2="select s.SRNO,s.ROLLNO,s.FULLNAME,s.div,s.SEM from student_mst s,attendace a where a.rollno=s.rollno"
            query2=query2+" and a.odt=(select to_char(NVL(max(adt),SYSDATE),'dd-mon-yyyy') from doc where nvl(STATUS,'B')='B') ORDER BY ROLLNO"            
            print("*********Present Students**********")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            db_connection.close()
            for row in rows:
                 print("**Data Found***** ")
                 self.stud_table.insert("",'end',text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2]), str(row[3]),str(row[4])))
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             db_connection.close()
             messagebox.showinfo('Information', "Data fetching error!!!")
        #finally:
            #db_connection.close()

    #Get Absent Student List
    def AbsStud_data(self):
        try:
            self.ABSstud_table.delete(*self.ABSstud_table.get_children())
            query2=" select std.SRNO,std.ROLLNO,std.FULLNAME,std.div,std.SEM from student_mst std where std.srno not in( "            
            query2=query2+" select a.SRNO from attendace a where a.odt=(select to_char(NVL(max(adt),SYSDATE),'dd-mon-yyyy') from doc where nvl(STATUS,'B')='B')) ORDER BY STD.ROLLNO "
            
            print("**********Absent Student List*********")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            db_connection.close()
            for row in rows:
                 print("**********Got Data Happy Na*********")
                 self.ABSstud_table.insert("",'end',text=str(row[0]),values=(str(row[0]),str(row[1]),str(row[2]), str(row[3]),str(row[4])))
        except con.DatabaseError as e:
            print(e)
            db_connection.rollback()
            db_connection.close()
            messagebox.showinfo('Information', "Data fetching error!!!")
        #finally:
            #db_connection.close()

    #Course...
    def Get_Course_data(self):
        try:
            deprtValue=()
            query2="  select '--Select--' CO_NAME from dual union all select CO_NAME from COURSE where NVL(stats,'A')='A' "
            print("*******************")
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            db_connection.close()
            if(db_cursor.rowcount>1):
                deprtValue=rows
            else:
                deprtValue=["--Select--","Python","ADBMS","AIT","OT","SMP"]
            return deprtValue
        except con.DatabaseError as e:
            print(e)
            db_connection.rollback()
            db_connection.close()
            messagebox.showinfo('Information', "Data fetching error!!!")
            return deprtValue
        #finally:
            #db_connection.close()

    #Department..
    def Get_DeprtsList(self):
        try:
            deprtValue=()
            query2=" select '--Select--' DEPART_NAME from dual union all select DEPART_NAME from DEPART where Stats='A'"
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            db_connection.close()
            if(db_cursor.rowcount>1):
                deprtValue=rows
            else:
                deprtValue=["--Select--","MCA","MBA","BCA","BBA"]
            return deprtValue
        except con.DatabaseError as e:
            print(e)
            db_connection.rollback()
            db_connection.close()
            deprtValue=["--Select--","MCA","MBA","BCA","BBA"]
            messagebox.showinfo('Information', "Department Feaching Error!!!")
            return deprtValue
        #finally:
            #db_connection.close()
        
    def exit(self):
        root.destroy()

    def add_dataAttndace(self):
        if self.course_combo.get()=="--Select--":
           messagebox.showerror("Error","Select Course Name",parent=self.root)
           return
        
        try:
            #keyverify
            deprtValue=()
            query2=" select FACULTY_ID from  FACULTY where PASSKEY ='"+self.txtPassKey.get()+"' and CO_NAME like '%"+self.course_combo.get()+"%'"
            print(query2)
            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
            rows=db_cursor.fetchall()
            db_connection.close()
            if(db_cursor.rowcount>0):
                deprtValue=rows
            else:
                messagebox.showinfo('Information',"Invalid Pass Key !!",parent=self.root)
                return
            
            sn=0
            StudID="0"
            RollNo="0"
            query2 = "insert  all "
            for row_id in self.ABSstud_table.get_children():
                sn=sn+1
                row = self.ABSstud_table.item(row_id)['values']
                print('save row:', row[0])
                StudID=str(row[0])
                RollNo=str(row[1])
                query2 = query2 +" INTO CWA(sn,DT,CORSNM,ATIME,ABS_SID,ABS_ROLL_NO,CRSEID) "
                query2 = query2 +" VALUES ("+str(sn)+",(select to_Char(TO_DATE('"+self.curAttendaceDt.get()+"','dd-mm-yyyy'),'dd-MON-yyyy') from DUAL),'"+self.course_combo.get()+"', (select to_Char(sysdate,'hh:mi') from DUAL),'"+str(StudID)+"'"
                query2 = query2 +" ,"+str(row[1])+",( select nvl(max(CO_ID),'0') from course where stats='A' and CO_NAME like '%"+self.course_combo.get()+"%'))"
                print(query2)
            query2=query2+" SELECT * FROM dual "
            print(query2)
            # implement query Sentence
            print("*******************")
            print(query2)
            if(sn==0):
                query2="insert INTO CWA(sn,DT,CORSNM,ATIME,ABS_SID,ABS_ROLL_NO,CRSEID)"
                query2 = query2 +" VALUES ("+str(1)+",(select to_Char(TO_DATE('"+self.curAttendaceDt.get()+"','dd-mm-yyyy'),'dd-MON-yyyy') from DUAL),'"+self.course_combo.get()+"', (select to_Char(sysdate,'hh:mi') from DUAL),'"+str(0)+"'"
                query2 = query2 +" ,"+str(0)+",( select nvl(max(CO_ID),'0') from course where stats='A' and CO_NAME like '%"+self.course_combo.get()+"%'))"

            db_connection = con.connect(connString)
            db_cursor = db_connection.cursor()
            db_cursor.execute(query2)
           
        # Submit to database for execution
            db_connection.commit()
            messagebox.showinfo('Information', "Student Attendace Submited Successfully")
            root.destroy()            
           
        except con.DatabaseError as e:
             print(e)
             db_connection.rollback()
             messagebox.showinfo('Information', "Failed To Submit Attendace failed!!!")
        #finally:
            #db_connection.close()
     

if __name__ == "__main__":
    root=Tk()
    obj=CourseWiseAttendace(root)
    root.mainloop()
