from tkinter import *
from tkinter import ttk
import mysql.connector
import pymysql
from tkinter import messagebox

class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title_label = Label(self.root, text = "Student Management System", bd=10, relief=GROOVE, font = ("Cambria",28,'bold'), bg = 'cyan', fg='black')
        title_label.pack(side = TOP, fill=X)
        
        #Assiginig Variables
        self.Roll_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_var = StringVar()
        self.txt_add_var = StringVar()

        #Manage Students
        F1 = Frame(self.root, bd=5, relief=RIDGE, bg = 'crimson')
        F1.place(x=15, y=70, width=470, height=600)

        l1 = Label(F1, text= "Manage Students", font=("Comic Sans MS",16,'bold'),bg = 'Crimson', fg='white')
        l1.grid(row=0, columnspan = 2, pady=20)

        lf1 = Label(F1, text = "Roll No.", bg = 'crimson', fg='white', font=('Cambria', 14, 'bold')).grid(row=1, column =0, padx=10, pady=10, sticky ='w')
        e1 = Entry(F1, textvariable = self.Roll_var, width = 20, font = 'arial 12', bd=5, relief=GROOVE).grid(row=1, column=1, padx=10, pady=10, sticky='w')

        lf2 = Label(F1, text = "Student Name", bg = 'crimson', fg= 'white', font=("Cambria", 14,'bold')).grid(row=2, column=0, padx=10, pady=10, sticky='w')
        e2 = Entry(F1, textvariable = self.name_var, width= 20, font='arial 12', bd=5, relief = GROOVE).grid(row=2, column=1, padx = 10, pady=10, sticky='w')

        lf3 = Label(F1, text = "Student Email Id", bg = 'crimson', fg= 'white', font=("Cambria", 14,'bold')).grid(row=3, column=0, padx=10, pady=10, sticky='w')
        e3 = Entry(F1, textvariable = self.email_var, width= 20, font='arial 12', bd=5, relief = GROOVE).grid(row=3, column=1, padx = 10, pady=10, sticky='w')

        lf4 = Label(F1, text = "Gender", bg = 'crimson', fg= 'white', font=("Cambria", 14,'bold')).grid(row=4, column=0, padx=10, pady=10, sticky='w')
        
        #e2 = Entry(F1, width= 20, font='arial 12', bd=5, relief = GROOVE).grid(row=4, column=1, padx = 10, pady=10, sticky='w')
        box_gender = ttk.Combobox(F1, font = ("Cambria", 10, 'bold'), textvariable = self.gender_var, state = 'readonly')
        box_gender['values']=("Male", "Female", "Other")
        box_gender.grid(row=4, column=1, padx=11, pady=10, sticky='w')

        lf5 = Label(F1, text = "Contact No.", bg = 'crimson', fg= 'white', font=("Cambria", 14,'bold')).grid(row=5, column=0, padx=10, pady=10, sticky='w')
        e5 = Entry(F1, textvariable = self.contact_var, width= 20, font='arial 12', bd=5, relief = GROOVE).grid(row=5, column=1, padx = 10, pady=10, sticky='w')

        lf6 = Label(F1, text = "Student D.O.B.", bg = 'crimson', fg= 'white', font=("Cambria", 14,'bold')).grid(row=6, column=0, padx=10, pady=10, sticky='w')
        e6 = Entry(F1, textvariable = self.dob_var, width= 20, font='arial 12', bd=5, relief = GROOVE).grid(row=6, column=1, padx = 10, pady=10, sticky='w')

        lf7 = Label(F1, text = "Residential Address", bg = 'crimson', fg= 'white', font=("Cambria", 14,'bold')).grid(row=7, column=0, padx=10, pady=10, sticky='w')
        #e2 = Entry(F1, width= 20, font='arial 12', bd=5, relief = GROOVE).grid(row=7, column=1, padx = 10, pady=10, sticky='w')
        self.txt_add = Text(F1, width=27, height=5, font = ("", 10))
        self.txt_add.grid(row=7, column=1, padx=10, pady=15, sticky = 'w')

        #border buttons
        new_frame = Frame(F1,relief = RIDGE, bg='crimson', bd=5)
        new_frame.place(x=10, y=500, width = 380, height = 55)

        b1 = Button(new_frame, width=5, text = "Add",command = self.add_students, bg = 'white',bd=3, fg='black', font=("Cambria",14, 'bold'))
        b1.grid(row=0, column=0, padx=12)
        
        b2 = Button(new_frame, width=5, text = "Update", bg = 'white',bd=3, fg='black', font=("Cambria",14, 'bold'))
        b2.grid(row=0, column=1, padx=13)

        b3 = Button(new_frame, width=5, text = "Delete", bg = 'white',bd=3, fg='black', font=("Cambria",14, 'bold'))
        b3.grid(row=0, column=2, padx=12)

        b4 = Button(new_frame, width=5, text = "Clear", command = self.clear_students, bg = 'white',bd=3, fg='black', font=("Cambria",14, 'bold'))
        b4.grid(row=0, column=3, padx=12)

        #second frame
        F2 = Frame(self.root, bd=5, relief=RIDGE, bg = 'crimson')
        F2.place(x = 500, y=70, width=835, height= 600)

        search_label = Label(F2, text = "Search By", bg = 'crimson', fg='white', font=("Comic Sans MS",14,'bold')).grid(row=0, column=0, padx=10, pady=10)
        
        opt_l1 = Label(F2, text = "Select Options :-", bg = 'crimson', fg= 'white', font=("Cambria", 14,'bold')).grid(row=0, column=1, padx=5, pady=5)
        box_select = ttk.Combobox(F2, font = ("Cambria", 10, 'bold'), state = 'readonly')
        box_select['values']=("Roll No.", "Student Name", "Contact No.")
        box_select.grid(row=0, column=2, padx=5, pady=5)

        search_entry = Entry(F2, textvariable = self.search_var, width=10, bd =5, relief = GROOVE, font = ('arial',12, 'bold')).grid(row=0, column=3, padx=5, pady=5)

        b5 = Button(F2, text = 'Search', bd=5, fg = 'black', width = 10, font = ('Cambria', 12, 'bold')).grid(row=0, column=4, padx=5, pady=3)

        b6 = Button(F2, text = 'Show All', bd =5, fg='black', width= 10, font = ('cambria', 12, 'bold')).grid(row=0, column=5, padx=5, pady=3)
        
        #table form
        
        table_frame = Frame(F2, bd=4, relief = RIDGE, bg = 'white')
        table_frame.place(x=9, y=70, width=800, height=520)

        scroll_x = Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient = VERTICAL)
        self.student_table = ttk.Treeview(table_frame, columns = ("roll", "name","Email Id", "Gender", "Contact No.", "DOB", "Address"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill=X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)
        self.student_table.heading("roll", text = "Roll No.")
        self.student_table.heading("name", text = "Student Name")
        self.student_table.heading("Email Id", text = "Student Email Id")
        self.student_table.heading("Gender", text = "Gender")
        self.student_table.heading("Contact No.", text = "Contact No.")
        self.student_table.heading("DOB", text = "Studetn D.O.B.")
        self.student_table.heading("Address", text = "Residential Address")
        self.student_table['show'] = 'headings'
        self.student_table.column("roll", width = 100)
        self.student_table.column("name", width=100)
        self.student_table.column("Email Id", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Contact No.", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Address", width=150)
        self.student_table.pack(fill = BOTH, expand = 1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_all()

        


    def add_students(self):
        #if self.Roll_var.get() == "" or self.name_var.get() == "", or self.email_var.get() == "":
         #   tkinter.messagebox.showerror("Enter Correct Details")
        
        #else:
            mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = "password", database = "manage")
            cur = mydb.cursor()
            cur.execute("insert into users values (%s, %s, %s, %s, %s, %s, %s)", (self.Roll_var.get(), 
                                                                                 self.name_var.get(), 
                                                                                 self.email_var.get(), 
                                                                                 self.gender_var.get(),   
                                                                                 self.contact_var.get(), 
                                                                                 self.dob_var.get(),  
                                                                                 self.txt_add.get("1.0", END)
            ))   
            mydb.commit()
            mydb.close()

    def fetch_all(self):
        mydb = mysql.connector.connect(host = 'localhost', user = 'root', password = 'password', database = 'manage')
        cur = mydb.cursor()
        cur.execute("select * from users")
        rows = cur.fetchall()
        if len(rows) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END,values=row)
                mydb.commit()
                mydb.close()


    

    def clear_students(self):
        self.Roll_var.set(" ")
        self.name_var.set(" ")
        self.email_var.set(" ")
        self.gender_var.set(" ")
        self.contact_var.set(" ")
        self.dob_var.set(" ")
        self.txt_add.delete("1.0", END)

    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.Roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_add.set.delete("1.0", END)
        self.txt_add.set.insert(END,row[6])

        
        #def delete_students(self):
        #pass



    #def update_students(self):
        #pass  

root=Tk()
ob = Student(root)
root.mainloop()                                                                                                                                                 