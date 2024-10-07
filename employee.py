from tkinter import *
from tkinter import messagebox
import pymysql
import time


class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1920x1080+0+0")
        self.root.config(bg="White")
        title = Label(self.root, text="Employee Payroll Management System", font=("times new roman", 30, "bold"),
                      bg="#262626", fg="white").place(x=0, y=0, relwidth=1)

        # ===================FRAME1==========================
        # ==================VARIABLES========================
        self.var_emp_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hr_location = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_id_proof = StringVar()
        self.var_contact = StringVar()
        self.var_status = StringVar()
        self.var_experience = StringVar()

        Frame1 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=70, width=780, height=700)
        title2 = Label(Frame1, text="Employee Details", font=("times new roman", 20,), bg="lightgrey",
                       fg="black").place(x=0, y=0, relwidth=1)

        lbl_code = Label(Frame1, text="Employee Code", font=("times new roman", 20,), bg="white", fg="black").place(
            x=10, y=70)
        txt_dob = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_emp_code, bg="light yellow",
                        fg="black").place(x=220, y=74, width=200)
        btn_search = Button(Frame1, text="Search",command=self.search, font=("times new roman", 20,), bg="grey", fg="black").place(x=440,
                                                                                                               y=72,
                                                                                                               height=30)

        # ================ROW1===================
        lbl_designation = Label(Frame1, text="Designation", font=("times new roman", 20,), bg="white",
                                fg="black").place(x=10, y=120)
        txt_designation = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_designation,
                                bg="light yellow", fg="black").place(x=170, y=125, width=200)
        lbl_dob = Label(Frame1, text="D.O.B", font=("times new roman", 20,), bg="white", fg="black").place(x=390, y=120)
        txt_dob = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_dob, bg="light yellow",
                        fg="black").place(x=520, y=125)

        # ================ROW2===================
        lbl_Name = Label(Frame1, text="Name", font=("times new roman", 20,), bg="white", fg="black").place(x=10, y=170)
        txt_name = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_name, bg="light yellow",
                         fg="black").place(x=170, y=175, width=200)
        lbl_doj = Label(Frame1, text="D.O.J", font=("times new roman", 20,), bg="white", fg="black").place(x=390, y=170)
        txt_doj = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_doj, bg="light yellow",
                        fg="black").place(x=520, y=175)

        # ================ROW3===================
        lbl_Age = Label(Frame1, text="Age", font=("times new roman", 20,), bg="white", fg="black").place(x=10, y=220)
        txt_age = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_age, bg="light yellow",
                        fg="black").place(x=170, y=225, width=200)
        lbl_Experience = Label(Frame1, text="Experience", font=("times new roman", 20,), bg="white", fg="black").place(
            x=390, y=220)
        txt_experience = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_experience,
                               bg="light yellow", fg="black").place(x=520, y=225)

        # ================ROW4===================
        lbl_gender = Label(Frame1, text="Gender", font=("times new roman", 20,), bg="white", fg="black").place(x=10,
                                                                                                               y=270)
        txt_gender = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_gender, bg="light yellow",
                           fg="black").place(x=170, y=275, width=200)
        lbl_proof = Label(Frame1, text="ID Proof", font=("times new roman", 20,), bg="white", fg="black").place(x=390,
                                                                                                                y=270)
        txt_proof = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_id_proof, bg="light yellow",
                          fg="black").place(x=520, y=275)

        # ================ROW5===================
        lbl_email = Label(Frame1, text="Email", font=("times new roman", 20,), bg="white", fg="black").place(x=10,
                                                                                                             y=320)
        txt_email = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_email, bg="light yellow",
                          fg="black").place(x=170, y=325, width=200)
        lbl_contact = Label(Frame1, text="Contact", font=("times new roman", 20,), bg="white", fg="black").place(x=390,
                                                                                                                 y=320)
        txt_contact = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_contact, bg="light yellow",
                            fg="black").place(x=520, y=325)

        # ================ROW6===================
        lbl_hired = Label(Frame1, text="Hired Location", font=("times new roman", 18,), bg="white", fg="black").place(
            x=10, y=372)
        txt_hired = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_hr_location, bg="light yellow",
                          fg="black").place(x=170, y=375, width=200)
        lbl_status = Label(Frame1, text="Status", font=("times new roman", 20,), bg="white", fg="black").place(x=390,
                                                                                                               y=370)
        txt_status = Entry(Frame1, font=("times new roman", 15,), textvariable=self.var_status, bg="light yellow",
                           fg="black").place(x=520, y=375)
        #====================Row7=================
        lbl_address = Label(Frame1, text="Address", font=("times new roman", 20,), bg="white", fg="black").place(x=10,
                                                                                                                 y=425)
        self.txt_address = Text(Frame1, font=("times new roman", 15,), bg="light yellow", fg="black")
        self.txt_address.place(x=170, y=425, width=550, height=150)

        # ===================FRAME2==========================
        #====================VARIABLES=======================
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_t_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()

        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_sal = StringVar()

        Frame2 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame2.place(x=800, y=70, width=720, height=350)
        title3 = Label(Frame2, text="Employee Salary Details", font=("times new roman", 20,), bg="lightgrey",
                       fg="black").place(x=0, y=0, relwidth=1)

        lbl_month = Label(Frame2, text="Month", font=("times new roman", 18,), bg="white", fg="black").place(x=10, y=60)
        txt_month = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_month, bg="light yellow",
                          fg="black").place(x=90, y=62, width=100)

        lbl_year = Label(Frame2, text="Year", font=("times new roman", 18,), bg="white", fg="black").place(x=200, y=60)
        txt_year = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_year, bg="light yellow",
                         fg="black").place(x=270, y=62, width=100)

        lbl_salary = Label(Frame2, text="Basic Salary", font=("times new roman", 18,), bg="white", fg="black").place(
            x=380, y=60)
        txt_salary = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_salary, bg="light yellow",
                           fg="black").place(x=520, y=62, width=180)

        lbl_t_days = Label(Frame2, text="Total Days", font=("times new roman", 20,), bg="white", fg="black").place(x=10,
                                                                                                                   y=120)
        txt_t_days = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_t_days, bg="light yellow",
                           fg="black").place(x=170, y=125, width=100)

        lbl_absent = Label(Frame2, text="Absents", font=("times new roman", 20,), bg="white", fg="black").place(x=450,
                                                                                                                y=120)
        txt_absent = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_absent, bg="light yellow",
                           fg="black").place(x=550, y=125, width=120)

        lbl_medical = Label(Frame2, text="Medical", font=("times new roman", 20,), bg="white", fg="black").place(x=10,
                                                                                                                 y=150)
        txt_medical = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_medical, bg="light yellow",
                            fg="black").place(x=170, y=155, width=100)

        lbl_pf = Label(Frame2, text="Proviedent Fund", font=("times new roman", 20,), bg="white", fg="black").place(
            x=360, y=150)
        txt_pf = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_pf, bg="light yellow",
                       fg="black").place(x=550, y=155, width=120)

        lbl_convence = Label(Frame2, text="Convence", font=("times new roman", 18,), bg="white", fg="black").place(
            x=10, y=180)
        txt_convence = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_convence, bg="light yellow",
                             fg="black").place(x=170, y=185, width=100)

        lbl_netsalary = Label(Frame2, text="Net Salary", font=("times new roman", 20,), bg="white", fg="black").place(
            x=410, y=180)
        txt_netsalary = Entry(Frame2, font=("times new roman", 15,), textvariable=self.var_net_sal,state='readonly', bg="light yellow",
                              fg="black").place(x=550, y=185, width=120)

        btn_calculate = Button(Frame2, text="Calculate", command=self.calculate, font=("times new roman", 20,),
                               bg="grey", fg="black").place(x=150, y=230, height=30, width=120)
        btn_save = Button(Frame2, text="Save", command=self.add, font=("times new roman", 20,), bg="green",
                         fg="white").place(x=280, y=230, height=30, width=120)
        btn_clear = Button(Frame2, text="Clear",command=self.clear, font=("times new roman", 20,), bg="orange",
                          fg="black").place(x=420, y=230, height=30, width=120)
        btn_update = Button(Frame2, text="Update", command=self.calculate, font=("times new roman", 20,),
                               bg="yellow", fg="black").place(x=150, y=280, height=30, width=120)
        btn_delete = Button(Frame2, text="Delete", command=self.delete, font=("times new roman", 20,), bg="brown",
                         fg="white").place(x=280, y=280, height=30, width=120)

        # ================FRAME3==================
        Frame3 = Frame(self.root, bd=5, relief=RIDGE, bg="white")
        Frame3.place(x=800, y=420, width=720, height=350)

        # =================CALCULATOR FRAME===================
        self.var_txt = StringVar()
        self.var_operator = ''

        def btn_click(num):
            self.var_operator = self.var_operator + str(num)
            self.var_txt.set(self.var_operator)

        def result():
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator =''

        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''

        Cal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        Cal_Frame.place(x=5, y=5, width=247, height=320)

        txt_result = Entry(Cal_Frame, bg="lightyellow",state='readonly', textvariable=self.var_txt, font=("times new roman", 20, "bold"),
                           justify=RIGHT)
        txt_result.place(x=0, y=0, relwidth=1, height=70)

        # ================ROW1==================
        btn_7 = Button(Cal_Frame, text='7', command=lambda: btn_click(7), font=("times new roman", 15, "bold")).place(
            x=0, y=72, w=60, h=60)
        btn_8 = Button(Cal_Frame, text='8', command=lambda: btn_click(8), font=("times new roman", 15, "bold")).place(
            x=61, y=72, w=60, h=60)
        btn_9 = Button(Cal_Frame, text='9', command=lambda: btn_click(9), font=("times new roman", 15, "bold")).place(
            x=122, y=72, w=60, h=60)
        btn_div = Button(Cal_Frame, text='/', command=lambda: btn_click('/'),
                         font=("times new roman", 15, "bold")).place(x=183, y=72, w=60, h=60)

        # ================ROW2==================
        btn_4 = Button(Cal_Frame, text="4", command=lambda: btn_click(4), font=("times new roman", 15, "bold")).place(
            x=0, y=133, w=60, h=60)
        btn_5 = Button(Cal_Frame, text="5", command=lambda: btn_click(5), font=("times new roman", 15, "bold")).place(
            x=61, y=133, w=60, h=60)
        btn_6 = Button(Cal_Frame, text="6", command=lambda: btn_click(6), font=("times new roman", 15, "bold")).place(
            x=122, y=133, w=60, h=60)
        btn_mul = Button(Cal_Frame, text="*", command=lambda: btn_click('*'),
                         font=("times new roman", 15, "bold")).place(x=183, y=133, w=60, h=60)

        # ================ROW3==================
        btn_1 = Button(Cal_Frame, text="1", command=lambda: btn_click(1), font=("times new roman", 15, "bold")).place(
            x=0, y=194, w=60, h=60)
        btn_2 = Button(Cal_Frame, text="2", command=lambda: btn_click(2), font=("times new roman", 15, "bold")).place(
            x=61, y=194, w=60, h=60)
        btn_3 = Button(Cal_Frame, text="3", command=lambda: btn_click(3), font=("times new roman", 15, "bold")).place(
            x=122, y=194, w=60, h=60)
        btn_sub = Button(Cal_Frame, text="-", command=lambda: btn_click('-'),
                         font=("times new roman", 15, "bold")).place(x=183, y=194, w=60, h=60)

        # ================ROW3==================
        btn_0 = Button(Cal_Frame, text="0", command=lambda: btn_click(0), font=("times new roman", 15, "bold")).place(
            x=0, y=255, w=60, h=60)
        btn_dot = Button(Cal_Frame, text="C", command=clear_cal, font=("times new roman", 15, "bold")).place(x=61,
                                                                                                             y=255,
                                                                                                             w=60, h=60)
        btn_sum = Button(Cal_Frame, text="+", command=lambda: btn_click('+'),
                         font=("times new roman", 15, "bold")).place(x=122, y=255, w=60, h=60)
        btn_equal = Button(Cal_Frame, text="=", command=result, font=("times new roman", 15, "bold")).place(x=183,
                                                                                                            y=255, w=60,
                                                                                                            h=60)
        #===========Salary Frame=====================
        sal_Frame = Frame(Frame3, bg="white", bd=2, relief=RIDGE)
        sal_Frame.place(x=260, y=4, width=445, height=320)
        title_sal = Label(sal_Frame, text="Salary Receipt", font=("times new roman", 20,), bg="lightgrey",
                          fg="black").place(x=0, y=0, relwidth=1)

        sal_Frame2 = Frame(sal_Frame, bg='white', bd=2, relief=RIDGE)
        sal_Frame2.place(x=0, y=30, relwidth=1, height=245)

        self.sample = f'''   \t  Company Name, XYZ\n\t  Address: Xyz, Floor4
-------------------------------------------------
Empolyee ID\t\t:  
Salary of \t\t:  MON-YYYY
Generated On \t\t:  DD-MM-YYYY
--------------------------------------------------
Total Days\t\t:  DD
Total Present \t\t:  DD
Total Absent \t\t :  DD
Convence \t\t:  Rs.----
Medical \t\t:  Rs.----
PF \t\t:  Rs.----
Gross Payment \t\t:  Rs.-------
Net Salary \t\t:  Rs.--------
--------------------------------------------------
This is computer generated slip, not required any signature'''
        scroll_y = Scrollbar(sal_Frame2, orient=VERTICAL)
        scroll_y.pack(fill=Y, side=RIGHT)

        self.txt_salary_receipt = Text(sal_Frame2, font=("times new roman", 17), bg="lightyellow",
                                       yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=BOTH, expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(END, self.sample)
        btn_print = Button(sal_Frame, text="Print", font=("times new roman", 20,), bg="lightblue", fg="black").place(
            x=300, y=278, height=30, width=120)

        self.check_connection()

    def search(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))

            # print(rows)
            row = cur.fetchone()
            if row == None:
                messagebox.showerror("Error",
                                     "Invalid Empolyee ID,Please try with another empolyee Id",
                                     parent=self.root)
            else:
                print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_id_proof.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert( END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_t_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_net_sal.set(row[22])
                file_ = open('salary_receipt' + str(row[23]),'r')
                self.txt_salary_receipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_receipt.insert( END,i)
                file_.close()


        except Exception as ex:

                messagebox.showerror("Error", f"Error due to: {str(ex)}")
    def clear(self):

        self.var_emp_code.set('')
        self.var_designation.set(r'')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_experience.set('')
        self.var_id_proof.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0', END)

        self.var_month.set('')
        self.var_year.set('')
        self.var_salary.set('')
        self.var_t_days.set('')
        self.var_absent.set('')
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('')
        self.var_net_sal.set('')
        self.txt_salary_receipt.delete('1.0',END)
        self.txt_salary_receipt.insert(END,self.sample)

    def delete(self):

        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Emmployee ID must be required")
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
                # print(rows)
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error",
                                         "Invalid Empolyee ID,Please try with another empolyee Id",
                                         parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_salary where e_id= %s", (self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete", "Emmployee Record Deleted Successfully",parent=self.root)
                        self.clear()


            except Exception as ex:
                    messagebox.showerror("Error", f"Error due to: {str(ex)}")
    def add(self):
        # Add employee to the database
        if self.var_emp_code.get() == '' or self.var_net_sal.get() == '' or self.var_name.get() == '':
            messagebox.showerror("Error", "Empolyee Details Are required")
        else:

            try:
                con = pymysql.connect(host='localhost', user='root', password='', db='ems')
                cur = con.cursor()
                cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))

                # print(rows)
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error",
                                         "This Employee ID is already available in our record,try again with another id",
                                         parent=self.root)
                else:
                    cur.execute(
                        "insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.var_emp_code.get(),
                            self.var_designation.get(),
                            self.var_name.get(),
                            self.var_age.get(),
                            self.var_gender.get(),
                            self.var_email.get(),
                            self.var_hr_location.get(),
                            self.var_doj.get(),
                            self.var_dob.get(),
                            self.var_experience.get(),
                            self.var_id_proof.get(),
                            self.var_contact.get(),
                            self.var_status.get(),
                            self.txt_address.get('1.0', END),
                            self.var_month.get(),
                            self.var_year.get(),
                            self.var_salary.get(),
                            self.var_t_days.get(),
                            self.var_absent.get(),
                            self.var_medical.get(),
                            self.var_pf.get(),
                            self.var_convence.get(),
                            self.var_net_sal.get(),
                            self.var_emp_code.get() + ".txt"
                        ))
                    con.commit()
                    con.close()

                    file_=open('salary_receipt' +str(self.var_emp_code.get())+".txt",'w')
                    file_.write(self.txt_salary_receipt.get('1.0',END))
                    file_.close()
                messagebox.showinfo("Success", "Record added successfully!")
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}")



    def calculate(self):
        if self.var_month.get()=='' or self.var_year.get()==''or self.var_salary.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            #self.var_netSalary.set("RESULT")
            per_day=int(self.var_salary.get())/int(self.var_t_days.get())
            work_day=int(self.var_t_days.get())-int(self.var_absent.get())
            sal=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal-deduct+addition
            self.var_net_sal.set(str(round(net_sal,2)))
            #================Update the receipt

            new_sample = f'''   \t  Company Name, XYZ\n\t  Address: Xyz, Floor4
            ------------------------------------------
            Empolyee ID\t\t:  {self.var_emp_code.get()}  
            Salary of \t\t:  {self.var_month.get()}-{self.var_year.get()}
            Generated On \t\t:  {str(time.strftime("%d-%m-%Y"))}
            ------------------------------------------
            Total Days\t\t:  {self.var_t_days.get()}
            Total Present \t\t:  {str(int(self.var_t_days.get())-int(self.var_absent.get()))}
            Total Absent \t\t :  {self.var_absent.get()}
            Convence \t\t:  Rs.{self.var_convence.get()}
            Medical \t\t:  Rs.{self.var_medical.get()}
            PF \t\t:  Rs.{self.var_pf.get()}
            Gross Payment \t\t:  Rs.{self.var_salary.get()}
            Net Salary \t\t:  Rs.{self.var_net_sal.get()}
            ------------------------------------------
            This is computer generated slip, not required any signature'''

            self.txt_salary_receipt.delete('1.0',END)
            self.txt_salary_receipt.insert(END,new_sample)




    def check_connection(self):
        try:
            con = pymysql.connect(host='localhost', user='root', password='', db='ems')
            cur = con.cursor()
            cur.execute("select * from emp_salary where e_id=%s", (self.var_emp_code.get()))
            row = cur.fetchall()
            print(row)



        except Exception as ex:
            messagebox.showerror("Error", f'Error due to: {str(ex)}')


root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
