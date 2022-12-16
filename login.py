from tkinter import*
from tkinter import ttk
from turtle import bgcolor
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()



class Login_Window:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1360x688+0+0")



        # Background Shade
        root['bg'] = 'black'


        #User & Login Frame
        frame = Frame(self.root,bg='#011f4b')
        frame.place(x=510, y=90, width=340, height=480)   


        #User Icon
        img = Image.open(r"images/user_vector1.png")
        img = img.resize((80,80),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        bg_img =  Label(image=self.photoimg, bg='#011f4b', borderwidth=0)
        bg_img.place(x=640,y=105,width=80,height=80)

        #User Login Text
        get_str = Label(frame, text="User Login", font = ("cursive", 20, "bold"), bg ='#011f4b', fg = '#f8ae97' )
        get_str.place(x=97, y=97)

        #label- Username & Entry
        username_lbl = Label(frame, text="Username", font = ("cursive", 14, "bold"), bg ='#011f4b', fg = '#f8ae97')
        username_lbl.place(x=40, y=160)

        self.txtuser = ttk.Entry(frame, font = ("cursive", 14, "italic"))
        self.txtuser.place(x=40, y=190, width=270)

        #label - Password & Entry
        password_lbl = Label(frame, text="Password", font = ("cursive", 14, "bold"), bg ='#011f4b', fg = '#f8ae97')
        password_lbl.place(x=40, y=230)

        self.txtpassword = ttk.Entry(frame, font = ("cursive", 14, "italic"))
        self.txtpassword.place(x=40, y=260, width=270)

        #Login Button
        loginbtn=Button(frame,  text="Login", command=self.login, font = ("cursive", 14, "bold"), bd=3, relief=RIDGE, bg ='#FF0000', fg='#FFFFFF', activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        #Create A New Account Button
        registerbtn=Button(frame, command=self.register_window, text="Create New Account", font = ("cursive", 13, "italic"), borderwidth=0, bg ='#011f4b', fg = '#f8ae97', activeforeground='#f8ae97', activebackground='#011f4b')
        registerbtn.place(x=5, y=380, width=200)

        #Forgot Password Button
        forgetbtn=Button(frame, command=self.forgot_password_window,  text="Forgot Password?", font = ("cursive", 13, "italic"), borderwidth=0, bg ='#011f4b', fg = '#f8ae97', activeforeground='#f8ae97', activebackground='#011f4b')
        forgetbtn.place(x=5, y=405, width=180)


    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpassword.get()=="":
            messagebox.showerror("Error", "All Fields are Required!")

        #elif self.txtuser.get()=="gp24@gmail.com" and self.txtpassword.get()=="g123":
          #messagebox.showinfo("Success", "You have successfully Login")

        else:
            conn = mysql.connector.connect(host = "localhost", user = "user", password = "root@123", database = "user_login")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s" , (

                                                                                            self.txtuser.get(),
                                                                                            self.txtpassword.get()
                                                                                                ))

            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid Username or Password!")

            else:
                open_main = messagebox.askyesno("Confirm", "Access only Admin")
                if open_main>0:
                    self.new_window = Toplevel(self.new_window)
                   #----------To Add A Project-----------
                   #self.app = class_name(self.new_window)

                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email Address!")

        else:
            conn = mysql.connector.connect(host = "localhost", user = "user", password = "root@123", database = "user_login")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s",)
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)

            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Invalid Username!!")

            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450 + 610 + 170")



class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1360x688+0+0")

        #========Variables=========
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        

        # Background Shade
        root['bg'] = 'black'

        #Logo
        img = Image.open(r"bg_images/topic.png")
        img = img.resize((180,100),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)


        first_label =  Label(self.root, image=self.photoimg)
        first_label.place(x=0,y=0,width=180,height=100)

        #Title Of Institute
        #title_lable = Label(text = "SHREE SWAMINARAYAN INSTITUTE OF TECHNOLOGY", font = ("palatino", 30, "bold"),bg ='#282b30', fg = '#f5f5f5') 
        #title_lable.place(x=180, y=0, width = 1180, height = 100)

        # Main Register Frame
        frame = Frame(self.root, bg ="white")
        frame.place(x=300, y=100,  width=800, height=588)

        #Register Label
        register_lbl = Label(frame, text="Create A New Account", font = ("palatino", 20, "bold"), fg="black", bg = "white")
        register_lbl.place(x=10, y=10)

        #=======Labels And Entry========

        #-----------ROW 1----------
        #First Name
        fname = Label(frame, text="First Name", font = ("cursive", 14, "bold"), bg="white", fg ='#011f4b')
        fname.place(x=50, y=60)

        self.txt_fname = ttk.Entry(frame,textvariable=self.var_fname, font = ("palatino", 14, "italic") )        
        self.txt_fname.place(x=50, y=90, width=250)

        #Last Name
        lname = Label(frame, text="Last Name", font = ("cursive", 14, "bold"), bg="white", fg ='#011f4b')
        lname.place(x=410, y=60)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, font = ("palatino", 14, "italic") )        
        self.txt_lname.place(x=410, y=90, width=250)

        
        #------------ROW 2----------
        #Contact Number
        contact = Label(frame, text="Contact No.", font = ("cursive", 14, "bold"), bg="white", fg ='#011f4b')
        contact.place(x=50, y=140)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, font = ("palatino", 14, "italic") )        
        self.txt_contact.place(x=50, y=170, width=250)

        #Email
        email = Label(frame, text="Email", font = ("cursive", 14, "bold"), bg="white", fg ='#011f4b')
        email.place(x=410, y=140)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font = ("palatino", 14, "italic") )        
        self.txt_email.place(x=410, y=170, width=250)

        
        #------------ROW 3----------
        #Security Question
        security_Q = Label(frame, text="Select Security Question", font = ("cursive", 14, "bold"), bg="white", fg ='#011f4b')
        security_Q.place(x=50, y=230)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font = ("palatino", 14, "italic"), state="readonly")
        self.combo_security_Q["values"] = ["Select", "Your favourite Book", "Your favourite Animal", "Your favourite food"]
        self.combo_security_Q.place(x=50, y=260, width=250)
        self.combo_security_Q.current(0) 

        
        #Security Answer
        security_A = Label(frame, text="Security Answer", font = ("cursive", 14, "bold"), bg="white", fg ='#011f4b')
        security_A.place(x=410, y=230)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_securityA, font = ("palatino", 14, "italic") )        
        self.txt_email.place(x=410, y=260, width=250)


         #------------ROW 4----------
        #Password
        password = Label(frame, text="Password", font = ("cursive", 14, "bold"), bg="white", fg ='#011f4b')
        password.place(x=50, y=325)

        self.txt_password = ttk.Entry(frame, textvariable=self.var_pass, font = ("palatino", 14, "italic") )        
        self.txt_password.place(x=50, y=355, width=250)

        #Confirm Password
        cf_pass = Label(frame, text="Confirm Password", font = ("cursive", 14, "bold"), bg="white", fg ='#011f4b')
        cf_pass.place(x=410, y=325)

        self.txt_cf_pass = ttk.Entry(frame, textvariable=self.var_confpass, font = ("palatino", 14, "italic") )        
        self.txt_cf_pass.place(x=410, y=355, width=250)


        # Check Button - Terms & Condition
        self.var_check = IntVar()
        check_btn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font = ("cursive", 12, "bold"), onvalue=1, offvalue=0, bg="white")
        check_btn.place(x=50, y=410)

        # Button - Register
        save_btn =Button(frame, command=self.register_data, text="Register",width=11, height=1, font = ("cursive", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground='#011f4b', activeforeground='#f8ae97')
        save_btn.place(x=50, y=480)
        #save_btn.grid(row=5, column=5, padx=5, pady=10)

        # Button - Login
        login_btn =Button(frame, text="Login",width=11, height=1, font = ("cursive", 14, "bold"),bg ='#011f4b', fg = '#f8ae97', activebackground='#011f4b', activeforeground='#f8ae97')
        login_btn.place(x=230, y=480)

    #======Function Declaration===============

    def register_data(self):
        if self.var_fname.get() == "" or self.var_contact.get() == "" or self.var_pass.get() == "" or self.var_confpass.get() == "" or self.var_securityQ.get() == "Select" or self.var_email.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!")

        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password Does Not Match!!")

        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Agree Our Terms & Conditions!")

        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="root@123", database="user_login")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row != None:
                messagebox.showerror("Error", "This Email is already in use")

            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (
                                                                                                self.var_fname.get(),
                                                                                                self.var_lname.get(),
                                                                                                self.var_contact.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_securityQ.get(),
                                                                                                self.var_securityA.get(),
                                                                                                self.var_pass.get()

                                                                                                ))

            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "You have registered Successfully!")








if __name__ == "__main__":
   main()