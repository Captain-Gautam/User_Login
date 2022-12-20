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


if __name__ == "__main__":
   main()