from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cx_Oracle as con


connString = 'FRAS/FRAS@localhost:1521/xe'
class Report3:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1530x790+0+0')
        self.root.title("Face Recoganization System")


        img3=Image.open(r"D:\MCA_II\Project\IMG\img18.JFIF")
        img3=img3.resize((1500,790),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1500,height=790)

        title_lb=Label(bg_img,text="Report",font=("times new roman",20,"bold"),bg="white",fg="black")
        title_lb.place(x=0,y=0,width=1500,height=60)
        # report table frame
        R_frame=LabelFrame(bg_img,bd=2,bg="white",relief=RIDGE,text="Report Details",font=("times new roman",10,"bold"))
        R_frame.place(x=5,y=45,width=1485,height=740)

       #buttons frame

        search_label=Label(R_frame,text="Search By:",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=40,pady=40,sticky=W)

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(R_frame,variable=self.var_radio1,text="Student Wise",value="Yes")
        radiobtn1.grid(row=0,column=3)

        radiobtn2=ttk.Radiobutton(R_frame,variable=self.var_radio1,text="Date Wise",value="No")
        radiobtn2.grid(row=0,column=8)

        radiobtn3=ttk.Radiobutton(R_frame,variable=self.var_radio1,text="Course Wise",value="No")
        radiobtn3.grid(row=0,column=13)

        search_btn=Button(R_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="pink",fg="black")
        search_btn.grid(row=0,column=17,padx=10)

        graph_btn=Button(R_frame,text="Graph",width=12,font=("times new roman",12,"bold"),bg="pink",fg="black")
        graph_btn.grid(row=0,column=18,padx=5)

        ex_btn=Button(R_frame,text="Export",width=12,font=("times new roman",12,"bold"),bg="pink",fg="black")
        ex_btn.grid(row=0,column=19,padx=5)
        
#==========================First Table================================================

        table_frame=Frame(R_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=80,width=900,height=500)
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.stud_table=ttk.Treeview(table_frame,column=("roll","name","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud_table.xview)
        scroll_y.config(command=self.stud_table.yview)
        
        self.stud_table.heading("roll",text="RollNo")
        self.stud_table.heading("name",text="Name")
        self.stud_table.heading("1",text="1")
        self.stud_table.heading("2",text="2")
        self.stud_table.heading("3",text="3")
        self.stud_table.heading("4",text="4")
        self.stud_table.heading("5",text="5")
        self.stud_table.heading("6",text="6")
        self.stud_table.heading("7",text="7")
        self.stud_table.heading("8",text="8")
        self.stud_table.heading("9",text="9")
        self.stud_table.heading("10",text="10")
        self.stud_table.heading("11",text="11")
        self.stud_table.heading("12",text="12")
        self.stud_table.heading("13",text="13")
        self.stud_table.heading("14",text="14")
        self.stud_table.heading("15",text="15")
        self.stud_table.heading("16",text="16")
        self.stud_table.heading("17",text="17")
        self.stud_table.heading("18",text="18")
        self.stud_table.heading("19",text="19")
        self.stud_table.heading("20",text="20")
        self.stud_table.heading("21",text="21")
        self.stud_table.heading("22",text="22")
        self.stud_table.heading("23",text="23")
        self.stud_table.heading("24",text="24")
        self.stud_table.heading("25",text="25")
        self.stud_table.heading("26",text="26")
        self.stud_table.heading("27",text="27")
        self.stud_table.heading("28",text="28")
        self.stud_table.heading("29",text="29")
        self.stud_table.heading("30",text="30")
        self.stud_table.heading("31",text="31")
        
        self.stud_table["show"]="headings"
        self.stud_table.column("roll",width=100)
        self.stud_table.column("name",width=150)
        self.stud_table.column("1",width=50)    
        self.stud_table.column("2",width=50)
        self.stud_table.column("3",width=50)   
        self.stud_table.column("4",width=50)
        self.stud_table.column("5",width=50)
        self.stud_table.column("6",width=50)
        self.stud_table.column("7",width=50)
        self.stud_table.column("8",width=50)
        self.stud_table.column("9",width=50)
        self.stud_table.column("10",width=50)
        self.stud_table.column("11",width=50)
        self.stud_table.column("12",width=50)
        self.stud_table.column("13",width=50)
        self.stud_table.column("14",width=50)
        self.stud_table.column("15",width=50)
        self.stud_table.column("16",width=50)
        self.stud_table.column("17",width=50)
        self.stud_table.column("18",width=50)
        self.stud_table.column("19",width=50)
        self.stud_table.column("20",width=50)
        self.stud_table.column("21",width=50)
        self.stud_table.column("22",width=50)
        self.stud_table.column("23",width=50)
        self.stud_table.column("24",width=50)
        self.stud_table.column("25",width=50)
        self.stud_table.column("26",width=50)
        self.stud_table.column("27",width=50)
        self.stud_table.column("28",width=50)
        self.stud_table.column("29",width=50)
        self.stud_table.column("30",width=50)
        self.stud_table.column("31",width=50)
       
        self.stud_table.pack(fill=BOTH,expand=1)
#====================================Second table========================================

        table1_frame=Frame(R_frame,bd=2,bg="white",relief=RIDGE)
        table1_frame.place(x=5,y=80,width=900,height=500)
        scroll_x=ttk.Scrollbar(table1_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table1_frame,orient=VERTICAL)
        
        self.stud1_table=ttk.Treeview(table1_frame,column=("roll","name","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.stud1_table.xview)
        scroll_y.config(command=self.stud1_table.yview)
        
        self.stud1_table.heading("roll",text="RollNo")
        self.stud1_table.heading("name",text="name")
        self.stud1_table.heading("1",text="1")
        self.stud1_table.heading("2",text="2")
        self.stud1_table.heading("3",text="3")
        self.stud1_table.heading("4",text="4")
        self.stud1_table.heading("5",text="5")
        self.stud1_table.heading("6",text="6")
        self.stud1_table.heading("7",text="7")
        self.stud1_table.heading("8",text="8")
        self.stud1_table.heading("9",text="9")
        self.stud1_table.heading("10",text="10")
        self.stud1_table.heading("11",text="11")
        self.stud1_table.heading("12",text="12")
        self.stud1_table.heading("13",text="13")
        self.stud1_table.heading("14",text="14")
        self.stud1_table.heading("15",text="15")
        self.stud1_table.heading("16",text="16")
        self.stud1_table.heading("17",text="17")
        self.stud1_table.heading("18",text="18")
        self.stud1_table.heading("19",text="19")
        self.stud1_table.heading("20",text="20")
        self.stud1_table.heading("21",text="21")
        self.stud1_table.heading("22",text="22")
        self.stud1_table.heading("23",text="23")
        self.stud1_table.heading("24",text="24")
        self.stud1_table.heading("25",text="25")
        self.stud1_table.heading("26",text="26")
        self.stud1_table.heading("27",text="27")
        self.stud1_table.heading("28",text="28")
        self.stud1_table.heading("29",text="29")
        self.stud1_table.heading("30",text="30")
        self.stud1_table.heading("31",text="31")
        
        self.stud1_table["show"]="headings"
        self.stud1_table.column("roll",width=100)
        self.stud1_table.column("name",width=150)
        self.stud1_table.column("1",width=50)    
        self.stud1_table.column("2",width=50)
        self.stud1_table.column("3",width=50)   
        self.stud1_table.column("4",width=50)
        self.stud1_table.column("5",width=50)
        self.stud1_table.column("6",width=50)
        self.stud1_table.column("7",width=50)
        self.stud1_table.column("8",width=50)
        self.stud1_table.column("9",width=50)
        self.stud1_table.column("10",width=50)
        self.stud1_table.column("11",width=50)
        self.stud1_table.column("12",width=50)
        self.stud1_table.column("13",width=50)
        self.stud1_table.column("14",width=50)
        self.stud1_table.column("15",width=50)
        self.stud1_table.column("16",width=50)
        self.stud1_table.column("17",width=50)
        self.stud1_table.column("18",width=50)
        self.stud1_table.column("19",width=50)
        self.stud1_table.column("20",width=50)
        self.stud1_table.column("21",width=50)
        self.stud1_table.column("22",width=50)
        self.stud1_table.column("23",width=50)
        self.stud1_table.column("24",width=50)
        self.stud1_table.column("25",width=50)
        self.stud1_table.column("26",width=50)
        self.stud1_table.column("27",width=50)
        self.stud1_table.column("28",width=50)
        self.stud1_table.column("29",width=50)
        self.stud1_table.column("30",width=50)
        self.stud1_table.column("31",width=50)
       
        self.stud1_table.pack(fill=BOTH,expand=1)

        

        

        



if __name__ == "__main__":
    root=Tk()
    obj=Report3(root)
    root.mainloop()


