import tkinter.messagebox
import PIL.Image
from PIL import Image, ImageTk

import os
from shutil import copyfile
from tkinter import filedialog

try:
	import tkinter as tk                # python 3
	from tkinter import font as tkfont  # python 3
	
	from PIL import Image, ImageTk
	from tkinter import ttk
	from tkinter import *
	from tkinter import messagebox
	from acct import Account
except ImportError:
	import Tkinter as tk     # python 2
	import tkFont as tkfont  # python 2
from PIL import Image, ImageTk

Profile = {1:""}
Profile2 = {1:""}
account=Account("member.db")

LARGEFONT =("Verdana", 35) 
p=1
class tkinterApp(tk.Tk): 
	
	# __init__ function for class tkinterApp 
	def __init__(self, *args, **kwargs): 
		
		# __init__ function for class Tk 
		tk.Tk.__init__(self, *args, **kwargs)
		self.geometry("1500x750+5+5")
		self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic") 

		
		
		# creating a container 
		container = tk.Frame(self) 
		container.pack(side = "top", fill = "both", expand = True) 

		container.grid_rowconfigure(0, weight = 1) 
		container.grid_columnconfigure(0, weight = 1) 

		# initializing frames to an empty array 
		self.frames = {} 

		# iterating through a tuple consisting 
		# of the different page layouts 
		for F in (LoginPage,StartPage, PageOne, PageTwo, PageThree,PageFour): 

			frame = F(container, self) 

			# initializing frame of that object from 
			# startpage, page1, page2 respectively with 
			# for loop 
			self.frames[F] = frame 

			frame.grid(row = 0, column = 0, sticky ="nsew") 

		self.show_frame(LoginPage) 

	# to display the current frame passed as 
	# parameter 
	def show_frame(self, cont): 
		frame = self.frames[cont] 
		frame.tkraise() 

# first window frame startpage 


class LoginPage(tk.Frame):    
	def __init__(self, parent, controller):		
		tk.Frame.__init__(self, parent,bg="darkorange")
		# tk.Frame.bg_login=ImageTk.PhotoImage(file="12.png")
		# tk.Frame.bg_image=Label(self,image=self.bg_login,bg="darkorange")
		# tk.Frame.bg_image.place(x=300,y=0,relwidth=1,relheight=1)
		img1=ImageTk.PhotoImage(Image.open("6.png"))
		img2=ImageTk.PhotoImage(Image.open("7.png"))
		img3=ImageTk.PhotoImage(Image.open("8.png"))
		img4=ImageTk.PhotoImage(Image.open("6.png"))

		l = tk.Label(self, text ="EVERGREEN INTERNATIONAL! The Right Place!",fg="#00ff00",bg="darkorange") 
		# l.pack( fill="x", pady=50,padx=700)
		l.place(x=650,y=70)

		
		
		def move():
			global p
			# p=1
			if p==4:
				p=1
			if p==1:
				l.config(image=img1)
			elif p==2:
				l.config(image=img2)
			elif p==3:
				l.config(image=img3)
			elif p==4:
				l.config(image=img4)
			p+=1
			self.after(2000,move)

		move()
		
		self.controller = controller
		# ====Login Frame=========
		Frame_login=tk.Frame(self,bg="navy",)
		Frame_login.place(x=0,y=0,height=750,width=600)
		title=tk.Label(Frame_login,text="Login Here",font=("impact",28,"bold"),fg="#d77337",bg="navy")
		title.place(x=210,y=50)
		desc=tk.Label(Frame_login,text="Admin Login Area",font=("Goudy old style",20,"bold"),fg="#d77337",bg="navy")
		desc.place(x=200,y=110)

		l_user=tk.Label(Frame_login,text="Username",font=("Goudy old style",16,"bold"),fg="#d77337",bg="navy")
		l_user.place(x=250,y=180)
		self.txt_user=tk.Entry(Frame_login,font=("times new roman",15))
		self.txt_user.place(x=170,y=220,width=250,height=30)

		l_user=tk.Label(Frame_login,text="Password",font=("Goudy old style",16,"bold"),fg="#d77337",bg="navy")
		l_user.place(x=250,y=300)
		self.txt_passw=tk.Entry(Frame_login,font=("times new roman",15))
		self.txt_passw.place(x=170,y=340,width=250,height=30)

		
		def login_function():
			if self.txt_user.get()=="" or self.txt_passw.get()=="":
			    messagebox.showerror("Error","All fields are required",parent=self)
			elif self.txt_user.get()!="marcel" or self.txt_passw.get()!="pass111":
			    messagebox.showerror("Error","Invalid Username/Password",parent=self)
			else:
			    messagebox.showinfo("Welcome",f"Welcome to Evergreen {self.txt_user.get()}",parent=self)
			    self.controller.show_frame(StartPage)
			# self.controller.show_frame(StartPage)
			
		login_bn=Button(Frame_login,text="Login",command=login_function,width=10,font=("Goudy old style",16,"bold"),fg="#d77337",bg="navy")
		login_bn.place(x=230,y=450)
		forget_paasw_bn=Button(Frame_login,text="Forget Password?",bd=0,width=15,height=1,font=("Goudy old style",16,"bold"),fg="#d77337",bg="navy")
		forget_paasw_bn.place(x=200,y=580)

		l_user=Label(self,text="EVERGREEN? The Right Place!",font=("times new roman",32,"bold"),fg="#00ff00",bg="darkorange")
		l_user.place(x=720,y=5)


class StartPage(tk.Frame): 
	def __init__(self, parent, controller): 
		tk.Frame.__init__(self, parent,bg="darkred")

		img1=ImageTk.PhotoImage(Image.open("13.png"))
		img2=ImageTk.PhotoImage(Image.open("15.png"))
		img3=ImageTk.PhotoImage(Image.open("121.png"))
		img4=ImageTk.PhotoImage(Image.open("13.png"))

		l_heading = tk.Label(self, text ="EVERGREEN INTERNATIONAL! The Right Place!",font=("times new roman",25,"bold"),fg="#00ff00",bg="darkred") 
		l_heading.place(x=150,y=5)

		l = tk.Label(self, text ="EVERGREEN INTERNATIONAL! The Right Place!",fg="#00ff00",bg="darkorange") 
		l.pack( fill="x", pady=50)
		# l.pack(side="top", fill="x", pady=10)
		# l.grid(row = 0, column = 4, padx = 10, pady = 10) 

		button1 = tk.Button(self, text="Account",bg="blue",fg="white",font=("bold",10),
							command=lambda: controller.show_frame(PageOne))
		button2 = tk.Button(self, text="PayDues",bg="blue",fg="white",font=("bold",10),
							command=lambda: controller.show_frame(PageTwo))
		button3 = tk.Button(self, text="Register Member",bg="blue",fg="white",font=("bold",10),
							command=lambda: controller.show_frame(PageThree))
		button4 = tk.Button(self, text="Munite",bg="blue",fg="white",font=("bold",10),
							command=lambda: controller.show_frame(PageFour))
		button1.place(x=1400, y=10)
		button2.place(x=1320,y=10)
		button3.place(x=1200, y=10)
		button4.place(x=1120,y=10)

		

		def move():
			global p
			# p=1
			if p==4:
				p=1
			if p==1:
				l.config(image=img1)
			elif p==2:
				l.config(image=img2)
			elif p==3:
				l.config(image=img3)
			elif p==4:
				l.config(image=img4)
			p+=1
			self.after(2000,move)

		move()


class PageOne(tk.Frame):  #ACCOUNT

	# =========Account Function========================


	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		tk.Frame.bg_pageone=Label(self,bg="teal",height=600,width=1400)
		tk.Frame.bg_pageone.place(x=0,y=0)
		# tk.Frame.bg1=ImageTk.PhotoImage(file="12.png")
		# tk.Frame.bg_image=Label(self,image=self.bg1)
		# tk.Frame.bg_image.place(x=300,y=0,relwidth=1,relheight=1)

		self.controller = controller
		label = tk.Label(self, text="Finance / Account Section", fg='darkorange',bg="#3EFF15",font=("Arial",24,))
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Back",bg="red",fg="white",bd=0,
						   command=lambda: controller.show_frame(StartPage))
		button.place(x=5,y=20)

		def get_selected_row1(event):
			e1.configure(state=tk.NORMAL)
			e2.configure(state=tk.NORMAL)
			e4.configure(state=tk.NORMAL)
			e5.configure(state=tk.NORMAL)
			
			global selected_tuple
			index=list1.curselection()[0]
			selected_tuple=list1.get(index)
			#====to display selected tuple in the entry box====
			e1.delete(0,END)
			e1.insert(END,selected_tuple[1])
			e2.delete(0,END)
			e2.insert(END,selected_tuple[2])
			# e3.delete(0,END)
			# e3.insert(END,selected_tuple[3])
			e1.configure(state=tk.DISABLED)
			e2.configure(state=tk.DISABLED)
			e4.configure(state=tk.DISABLED)
			e5.configure(state=tk.DISABLED)

		def get_selected_row2(event):
			e4.configure(state=tk.NORMAL)
			e5.configure(state=tk.NORMAL)
			e1.configure(state=tk.NORMAL)
			e2.configure(state=tk.NORMAL)
			
			global selected_tuple2
			index2=list2.curselection()[0]
			selected_tuple2=list2.get(index2)
			#====to display selected tuple in the entry box====
			e4.delete(0,END)
			e4.insert(END,selected_tuple2[1])
			e5.delete(0,END)
			e5.insert(END,selected_tuple2[2])
			# e6.delete(0,END)
			# e6.insert(END,selected_tuple2[3])
			e4.configure(state=tk.DISABLED)
			e5.configure(state=tk.DISABLED)
			e1.configure(state=tk.DISABLED)
			e2.configure(state=tk.DISABLED)

		def view_member_command():
			list1.delete(0,END)
			for row in account.view_member():
				list1.insert(END,row)
				b1.configure(state=tk.NORMAL)
				
		def deposit_command():
			if(e3.get()).isdigit():
				depo=tkinter.messagebox.askyesno("Validate", "Are you sure to deposit?")
				if depo > 0:
					account.insert_member_deposit(selected_tuple[0],firstname_text.get(),lastname_text.get(),amount_text.get())
					list1.delete(0,END)
					list1.insert(END,(firstname_text.get(),lastname_text.get(),amount_text.get()))
					e3.delete(0,END)
					acct_msg1.delete(0, END)
					acct_msg1.insert(0, 'Deposit SUCCESSFUL!')

		def view_member_deposit_command():
			list1.delete(0,END)
			for row in account.view_member_deposit():
				list1.insert(END,row)
				b1.configure(state=tk.DISABLED)

		def view_member_deposit_command2():
			list2.delete(0,END)
			for row in account.view_member_deposit():
				list2.insert(END,row)
				b1.configure(state=tk.DISABLED)

		def update_member_deposit_command():
			if (e3.get()).isdigit():
				account.credit_member(selected_tuple[0],selected_tuple[1],selected_tuple[2],amount_text.get())
				e3.delete(0,END)
				acct_msg1.delete(0, END)
				acct_msg1.insert(0, 'Update SUCCESSFUL!')
				return True

			else:
				tkinter.messagebox.showwarning("Caution", "Invalid Data, Numbers Only")
				e3.delete(0,END)        
				return True

		def transfer_command():
			if (e3.get()).isdigit():
				account.debit_one_member(selected_tuple[0],selected_tuple[1],selected_tuple[2],amount_text.get())
				account.credit_member(selected_tuple2[0],selected_tuple2[1],selected_tuple2[2],amount_text.get())        
				e3.delete(0,END)
				acct_msg1.delete(0, END)
				acct_msg1.insert(0, 'Transfer SUCCESSFUL!')
				return True

			else:
				tkinter.messagebox.showwarning("Caution", "Invalid Data, Numbers Only")
				e3.delete(0,END)        
				return True
		
		# ========DEPOSIT=============================================
		deposit_frame=Frame(self,bd=10,relief=RIDGE,width=640,height=220,bg='darkgreen')
		deposit_frame.place(x=0,y=65)
		
		view_member_frame=Frame(self,bd=10,relief=RIDGE,width=640,height=80,bg='darkgreen')
		view_member_frame.place(x=0,y=285)

		transfer_frame=Frame(self,bd=10,relief=RIDGE,width=640,height=320,bg='darkgreen')
		transfer_frame.place(x=0,y=365)
		self.imgg=ImageTk.PhotoImage(file="6.png")
		frm_image=Label(self,image=self.imgg,height=620,width=800)
		frm_image.place(x=660,y=60)

		l2=Label(self,text="Credit Member Account",font=('arial',14,'bold'),bg='darkgreen',fg='darkorange')
		l2.place(x=200,y=90) 

		l2_0=Label(self,text="Member Fund Transfer",font=('arial',14,'bold'),bg='darkgreen',fg='darkorange')
		l2_0.place(x=200,y=380) 

		l3=Label(self,text="FirstName",font=('arial',12,'bold'),bg='darkgreen',fg='cyan')
		l3.place(x=70,y=150)

		l4=Label(self,text="LastName",font=('arial',12,'bold'),bg='darkgreen',fg='cyan')
		l4.place(x=70,y=210)

		l5=Label(self,text="Amount",font=('arial',12,'bold'),bg='darkgreen',fg='cyan')
		l5.place(x=350,y=150)
		
		firstname_text=StringVar()
		e1=Entry(self,textvariable=firstname_text,font=('arial',16,'bold'),width=10)
		e1.place(x=160,y=150)

		lastname_text=StringVar()
		e2=Entry(self,textvariable=lastname_text,font=('arial',16,'bold'),width=10)
		e2.place(x=160,y=210)

		amount_text=StringVar()
		e3=Entry(self,textvariable=amount_text,font=('arial',16,'bold'),width=10)
		e3.place(x=430,y=150)

		b1=Button(self,text='Deposit',command=deposit_command,width=15,height=2,font=('arial',12,'bold'),#
		bg='darkgreen',fg='cyan',relief='solid')
		b1.place(x=395,y=200)
	#=======================================================================================================
		b2=Button(self,text='View Members',command=view_member_command,width=15,height=2,font=('arial',12,'bold'),#
		bg='darkgreen',fg='cyan',relief='solid')
		b2.place(x=120,y=300)

		b3=Button(self,text='View 1\n Members Deposit',command=view_member_deposit_command,width=19,height=3,font=('arial',10,'bold'),#
		bg='darkgreen',fg='cyan',relief='solid')
		b3.place(x=780,y=610)

		b4=Button(self,text='Update \n Member Deposit',command=update_member_deposit_command,width=19,height=3,font=('arial',10,'bold'),#
		bg='darkgreen',fg='cyan',relief='solid')
		b4.place(x=400,y=295)

		
		b6=Button(self,text='View 2\n Members Deposit',command=view_member_deposit_command2,width=19,height=3,font=('arial',10,'bold'),#command=view_member_deposit_command2,
		bg='darkgreen',fg='cyan',relief='solid')
		b6.place(x=1180,y=610)
		# ====================TRANSFER=================================================

		l6=Label(self,text="FirstName",font=('arial',12,'bold'),bg='darkgreen',fg='cyan')
		l6.place(x=70,y=470)

		l7=Label(self,text="LastName",font=('arial',12,'bold'),bg='darkgreen',fg='cyan')
		l7.place(x=70,y=560)

		l8=Label(self,text="Amount",font=('arial',12,'bold'),bg='darkgreen',fg='cyan')
		l8.place(x=350,y=470)

		firstname2_text=StringVar()
		e4=Entry(self,textvariable=firstname2_text,font=('arial',16,'bold'),width=10)
		e4.place(x=185,y=465)

		lastname2_text=StringVar()
		e5=Entry(self,textvariable=lastname2_text,font=('arial',16,'bold'),width=10)
		e5.place(x=185,y=555)

		amount2_text=StringVar()
		e6=Entry(self,textvariable=amount2_text,font=('arial',16,'bold'),width=10)
		e6.place(x=440,y=470)

		acct_msg1_text=StringVar()
		acct_msg1=Entry(self,textvariable=acct_msg1_text,bd=0,font=('arial',25,'bold'),width=50,bg="teal",fg="#3EFF15")
		acct_msg1.place(x=460,y=695)

		b5=Button(self,text='Transfer',command=transfer_command,width=15,height=2,font=('arial',12,'bold'),#
		bg='darkred',fg='cyan',relief='solid')
		b5.place(x=410,y=540)
# ============================================================================================
		
		list1=Listbox(self,height=22,width=35,
		bg='lightblue',fg='red',font=('arial',13,'bold'))
		list1.place(x=700,y=120)

		list1.bind('<<ListboxSelect>>', get_selected_row1)

		sb1=Scrollbar(self)
		sb1.place(x=1030,y=330)

		list1.configure(yscrollcommand=sb1.set)
		sb1.configure(command=list1.yview)              

		list2=Listbox(self,height=22,width=35,
		bg='lightblue',fg='red',font=('arial',13,'bold'))
		list2.place(x=1080,y=120)

		list2.bind('<<ListboxSelect>>', get_selected_row2)

		sb2=Scrollbar(self)
		sb2.place(x=1405,y=330)
		
		list2.configure(yscrollcommand=sb2.set)
		sb2.configure(command=list2.yview)
		

class PageTwo(tk.Frame):
		
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		tk.Frame.bg_pageone=Label(self,bg="darkred",height=600,width=1400)
		tk.Frame.bg_pageone.place(x=0,y=0)      
				
		# tk.Frame.bg2=ImageTk.PhotoImage(file="12.png")
		# tk.Frame.bg_image=Label(self,image=self.bg2)
		# tk.Frame.bg_image.place(x=0,y=0,relwidth=1,relheight=1)

		self.controller = controller
		label = tk.Label(self, text="Member Dues Management Panel",bg="teal",font=controller.title_font,fg="darkorange")
		label.pack(side="top", fill="x", pady=10)
		button_2 = tk.Button(self, text="Back",bg="red",fg="white",bd=0,command=lambda: controller.show_frame(StartPage))
		button_2.place(x=5,y=20)

		#=========Dues Function=========================
		def treeActionSelect2(event):
			pass
		#     # load image
		#     global idSelect
		#     global firstNameSelect
		#     global lastNameSelect
		#     global addressSelect
		#     global genderSelect
		#     global dobSelect
		#     global igdgdgdgd
		#     idSelect = tree.item(tree.selection())['values'][0]
		#     firstNameSelect = tree.item(tree.selection())['values'][1]
		#     lastNameSelect = tree.item(tree.selection())['values'][2]
		#     addressSelect = tree.item(tree.selection())['values'][3]
		#     genderSelect = tree.item(tree.selection())['values'][4]
		#     dobSelect = tree.item(tree.selection())['values'][5]
		#     imgBlopSelect = tree.item(tree.selection())['values'][6]
		#     igdgdgdgd = tree.item(tree.selection())['values'][7]


		def get_selected_row3(event):
			e05.configure(state=tk.NORMAL)
			e06.configure(state=tk.NORMAL)
			global selected_tuple3
			index3=list3.curselection()[0]
			selected_tuple3=list3.get(index3)
			e05.delete(0,END)
			e05.insert(END,selected_tuple3[1])
			e06.delete(0,END)
			e06.insert(END,selected_tuple3[2])
			e05.configure(state=tk.DISABLED)
			e06.configure(state=tk.DISABLED)
			
		def view_member_dues_command():
			due_heading.delete(0,END)
			due_heading.insert(END,"      MEMBERS CURRENT DUES")
			list3.delete(0,END)
			for row in account.view_member_due():
				list3.insert(END,row)
				# b1.configure(state=tk.NORMAL) 

		def view_member_dues_all_command():
			due_heading.delete(0,END)
			due_heading.insert(END,"      ALL MEMBERS DUES")
			list3.delete(0,END)
			for row in account.view_member_due_all():                
				list3.insert(END,row)

		def update_one_member_dues_command(): #Pay for one member
			due_heading.delete(0,END)
			due_heading.insert(END,"      MEMBER PAID DUE")
			account.pay_one_member_dues(selected_tuple3[0],due_due_text.get(),month_due_text.get(),
			info_due_text.get())
			account.debit_one_member(selected_tuple3[0],firstname_due_text.get(),lastname_due_text.get(),due_due_text.get())
			list3.delete(0,END)
			list3.insert(END,(selected_tuple3[0],selected_tuple3[1],selected_tuple3[2],due_due_text.get(),month_due_text.get(),info_due_text.get()))
			due_msg.delete(0,END)
			due_msg.insert(0,selected_tuple3[1]+"  Due Paid Successfuly!")
			e05.delete(0,END)
			e06.delete(0,END)
			# e7.delete(0,END)
			# e8.delete(0,END)
			# e9.delete(0,END)
		
		def pay_all_member_dues_command(): #Pay for all members
			due_heading.delete(0,END)
			due_heading.insert(END,"MEMBERS PAID DUES")
			account.debit_all_member(firstname_due_text.get(),lastname_due_text.get(),due_due_text.get())
			list3.delete(0,END)                        
			for row in account.view_member_due():
				account.pay_all_dues(due_due_text.get(),month_due_text.get(),
				info_due_text.get())       
									   
				list3.insert(END,row) 
				e7.configure(state=tk.DISABLED)
				e8.configure(state=tk.DISABLED)
				e9.configure(state=tk.DISABLED)
				
			due_msg.delete(0,END)
			due_msg.insert(0,"All Member Due Paid Successfuly!")
			# e_rev_total.delete(0,END)
			# e_rev_total.insert(0,totalamt)
			account.create_file()
			
			# for d in account.view_member_due():
			#     totalpay.append(int(due_due_text.get()))
			#     totalamt=sum(totalpay)
			 


		def submit_member_dues_command():
			due_heading.delete(0,END)
			due_heading.insert(END,"      ALL MEMBERS DUES")
			list3.delete(0,END)
			account.submit_member_dues()
			account.create_file()
			due_msg.delete(0, END)
			for row in account.view_member_due():
				list3.insert(END,row)
			due_msg.insert(0, 'Dues SUBMITED!')

		def get_total_due_command():
			e_rev_monthlydue.delete(0,END)
			e_rev_monthlydue.insert(0,account.get_sum_monthlydue())
			mdue=monthlydue_rev_text.get()
			grandtotal = int(mdue) + int(other_rev_amt_text.get())     
			e_rev_otherdue.delete(0,END)
			e_rev_otherdue.insert(0,other_rev_amt_text.get())
			e_rev_total.delete(0,END)
			e_rev_total.insert(0,grandtotal)
			other_rev_textbox.configure(state=tk.DISABLED)
			e_other_rev_amt.configure(state=tk.DISABLED)
			e_rev_monthlydue.configure(state=tk.DISABLED) 
			e_rev_otherdue.configure(state=tk.DISABLED)
			e_rev_total.configure(state=tk.DISABLED) 
			e_rev_exp.configure(state=tk.NORMAL)
			e_rev_bal.configure(state=tk.NORMAL)
			
		def activate_dues_fields_command():
			e7.configure(state=tk.NORMAL)
			e8.configure(state=tk.NORMAL)
			e9.configure(state=tk.NORMAL)
			
			
		def view_total_dues_command():
			pass
			# e_rev_total.delete(0,END)
			# e_rev_total.insert(0,account.get_sum_monthlydue())
			# e_rev_total.configure(state=tk.DISABLED) 
			# e_rev_exp.configure(state=tk.NORMAL)
			# e_rev_bal.configure(state=tk.NORMAL)

		def get_balance_command():
			totl=e_rev_total.get()
			balance=int(totl) - int(e_rev_exp.get())
			e_rev_bal.delete(0,END)
			e_rev_bal.insert(0,balance)
			e_rev_bal.configure(state=tk.DISABLED)

		def submit_balance_command():
			account.update_all_due_revenue_temp(month_due_text.get(),monthlydue_rev_text.get(),
			other_rev_amt_text.get(),other_rev_textbox.get(1.0,END),due_total_text.get(),due_exp_text.get(),
			due_bal_text.get())
			due_msg.delete(0,END)
			due_msg.insert(0, 'Finance Account Submitted Successfully!')
			e7.configure(state=tk.DISABLED)
			e8.configure(state=tk.DISABLED)
			e9.configure(state=tk.DISABLED)
			account.submit_due_revenue_all(month_due_text.get(),monthlydue_rev_text.get(),
			other_rev_amt_text.get(),other_rev_textbox.get(1.0,END),due_total_text.get(),due_exp_text.get(),
			due_bal_text.get())
			account.insert_due_revenue_temp("",None,None,"",None,None,None)

		def view_monthly_finance_command():
			list3.delete(0,END)
			for row in account.view_due_revenue_all():
				list3.insert(END,row)
			

		# ========DUES=============================================
		Dues_frame=Frame(self,bd=10,relief=RIDGE,width=460,height=430,bg='navy')
		Dues_frame.place(x=20,y=65)
		
		Dues_frame_button=Frame(self,bd=10,relief=RIDGE,width=460,height=200,bg='navy')
		Dues_frame_button.place(x=20,y=495)

		Dues_frame_list=Frame(self,bd=10,relief=RIDGE,width=660,height=630,bg='#00ff00')
		Dues_frame_list.place(x=480,y=65)

		Dues_frame_other=Frame(self,bd=10,relief=RIDGE,width=340,height=630,bg='darkorange')
		Dues_frame_other.place(x=1140,y=65)

		Dues_frame_list2=Frame(self,bd=0,width=640,height=50,bg='navy')
		Dues_frame_list2.place(x=490,y=75)

		Dues_frame_list3=Frame(self,bd=0,width=640,height=59,bg='darkorange')
		Dues_frame_list3.place(x=490,y=345)

		l0=Label(self,text="Dues Payment Platform",font=('arial',18,'bold'),bg='navy',fg='cyan')
		l0.place(x=130,y=90)

		l0=Label(self,text="Revenue Detailed Information",font=('arial',22,'bold'),bg='navy',fg='cyan')
		l0.place(x=620,y=80)

		l80=Label(self,text="FirstName :",font=('arial',11,'bold'),bg='navy',fg='orange')
		l80.place(x=70,y=160)

		l81=Label(self,text="LastName :",font=('arial',11,'bold'),bg='navy',fg='orange')
		l81.place(x=70,y=230)

		l82=Label(self,text="Amount:",font=('arial',12,'bold'),bg='navy',fg='orange')
		l82.place(x=70,y=300)

		l83=Label(self,text="Date:",font=('arial',12,'bold'),bg='navy',fg='orange')
		l83.place(x=70,y=370)

		l8=Label(self,text="Due Info :",font=('arial',12,'bold'),bg='navy',fg='orange')
		l8.place(x=70,y=440)

		l_other_rev_acct=Label(self,text="Other Revenue",font=('arial',20,'bold'),bd=10,bg='#00ff00',fg='navy')
		l_other_rev_acct.place(x=700,y=485)

		l_other_rev_amt=Label(self,text="Amount",font=('arial',18,'bold'),bd=10,bg='#00ff00',fg='cyan')
		l_other_rev_amt.place(x=590,y=525)

		l_other_rev_source=Label(self,text="Source",font=('arial',18,'bold'),bd=10,bg='#00ff00',fg='cyan')
		l_other_rev_source.place(x=890,y=525)

		l_rev_acct=Label(self,text="Dues Account",font=('arial',19,'bold'),bd=10,bg='darkorange',fg='navy')
		l_rev_acct.place(x=1210,y=90)

		l_rev_total=Label(self,text="Month Due",font=('arial',15,'bold'),bd=10,bg='darkorange',fg='cyan')
		l_rev_total.place(x=1160,y=165)

		l_rev_exp=Label(self,text="Other Rev.",font=('arial',15,'bold'),bd=10,bg='darkorange',fg='cyan')
		l_rev_exp.place(x=1160,y=220)

		l_rev_total=Label(self,text="Total Revenue",font=('arial',17,'bold'),bd=10,bg='darkorange',fg='cyan')
		l_rev_total.place(x=1210,y=285)

		l_rev_exp=Label(self,text="Total Expenditure",font=('arial',17,'bold'),bd=10,bg='darkorange',fg='cyan')
		l_rev_exp.place(x=1190,y=405)

		l_rev_bal=Label(self,text="Balance",font=('arial',19,'bold'),bd=10,bg='darkorange',fg='cyan')
		l_rev_bal.place(x=1240,y=520)

		firstname_due_text=StringVar()
		e05=Entry(self,textvariable=firstname_due_text,font=('arial',14,'bold'),width=22)
		e05.place(x=175,y=155)

		lastname_due_text=StringVar()
		e06=Entry(self,textvariable=lastname_due_text,font=('arial',14,'bold'),width=22)
		e06.place(x=175,y=225)

		due_due_text=StringVar()
		e7=Entry(self,textvariable=due_due_text,font=('arial',14,'bold'),width=22)
		e7.place(x=170,y=295)
		e7.configure(state=tk.DISABLED)

		month_due_text=StringVar()
		e8=Entry(self,textvariable=month_due_text,font=('arial',14,'bold'),width=22)
		e8.place(x=170,y=365)
		e8.configure(state=tk.DISABLED)

		info_due_text=StringVar()
		e9=Entry(self,textvariable=info_due_text,font=('arial',14,'bold'),width=22)
		e9.place(x=170,y=435)
		e9.configure(state=tk.DISABLED)

		other_rev_amt_text=StringVar()
		e_other_rev_amt=Entry(self,textvariable=other_rev_amt_text,font=('arial',16,'bold'),width=17)
		e_other_rev_amt.place(x=550,y=575)
		# e_other_rev_amt.configure(state=tk.DISABLED)
		e_other_rev_amt

		due_heading_text=StringVar()
		due_heading=Entry(self,textvariable=due_heading_text,font=('arial',23,'bold'),width=36,bg="teal",fg="#3EFF15")
		due_heading.place(x=500,y=355)

		due_msg_text=StringVar()
		due_msg=Entry(self,textvariable=due_msg_text,font=('arial',22,'bold'),width=42,bg="darkred",fg="yellow",bd=0)
		due_msg.place(x=170,y=705)

		monthlydue_rev_text=StringVar()
		e_rev_monthlydue=Entry(self,textvariable=monthlydue_rev_text,font=('arial',22,'bold'),width=10,fg='darkred',bg='darkorange')
		e_rev_monthlydue.place(x=1280,y=170)

		due_other_text=StringVar()
		e_rev_otherdue=Entry(self,textvariable=due_other_text,font=('arial',22,'bold'),width=10,fg='darkred',bg='darkorange')
		e_rev_otherdue.place(x=1280,y=220)
		# e_rev_exp.configure(state=tk.DISABLED)

		due_total_text=StringVar()
		e_rev_total=Entry(self,textvariable=due_total_text,font=('arial',22,'bold'),width=15,fg='darkred',bg='darkorange')
		e_rev_total.place(x=1185,y=330)

		due_exp_text=StringVar()
		e_rev_exp=Entry(self,textvariable=due_exp_text,font=('arial',22,'bold'),width=15,fg='darkred',bg='darkorange')
		e_rev_exp.place(x=1185,y=450)
		e_rev_exp.configure(state=tk.DISABLED)

		due_bal_text=StringVar()
		e_rev_bal=Entry(self,textvariable=due_bal_text,font=('arial',22,'bold'),width=15,fg='darkred',bg='darkorange')
		e_rev_bal.place(x=1185,y=570)

		other_rev_textbox=Text(self,width=35,height=6,font=('arial',12))
		other_rev_textbox.place(x=800,y=570)
		
		b7=Button(self,text='Pay One Dues',command=update_one_member_dues_command,width=15,height=2,font=('arial',10,'bold'),#
		bg='navy',fg='white',relief='solid')
		b7.place(x=40,y=525)

		b7=Button(self,text='Pay All Dues',command=pay_all_member_dues_command,width=15,height=2,font=('arial',10,'bold'),#
		bg='navy',fg='white',relief='solid')
		b7.place(x=185,y=525)
		
		view_due_b1=Button(self,text='View All Dues',command=view_member_dues_command,width=15,height=2,font=('arial',10,'bold'),#
		bg='navy',fg='white',relief='solid')
		view_due_b1.place(x=330,y=525)

		b7=Button(self,text='Activate Fields',command=activate_dues_fields_command,width=15,height=2,font=('arial',10,'bold'),#
		bg='blue',fg='white',relief='solid')
		b7.place(x=40,y=595)

		b7=Button(self,text='View Total Dues',command=view_total_dues_command,width=15,height=2,font=('arial',10,'bold'),#
		bg='navy',fg='white',relief='solid')
		b7.place(x=185,y=595)

		b7_01=Button(self,text='Submit Dues',command=submit_member_dues_command,width=15,height=2,font=('arial',10,'bold'),#
		bg='darkorange',fg='white',relief='solid')
		b7_01.place(x=330,y=595)

		other_rev_due_b=Button(self,text='Submit Dues',command=get_total_due_command,width=25,height=1,font=('arial',10,'bold'),#
		bg='purple',fg='white',relief='solid')
		other_rev_due_b.place(x=550,y=640)

		get_bal=Button(self,text='Get Balance',command=get_balance_command,width=12,height=1,font=('arial',10,'bold'),#
		bg='blue',fg='white',relief='solid')
		get_bal.place(x=1180,y=655)

		submit_bal=Button(self,text='Submit Balance',command=submit_balance_command,width=13,height=1,font=('arial',10,'bold'),#
		bg='teal',fg='white',relief='solid')
		submit_bal.place(x=1330,y=655)

		view_mdue_b1=Button(self,text='View Monthly Finance',command=view_monthly_finance_command,width=19,height=2,font=('arial',10,'bold'),#command=view_monthly_dues_all_command,
		bg='blue',fg='white',relief='solid')
		view_mdue_b1.place(x=860,y=700)

		view_fdue_b1=Button(self,text='View Function Dues',width=19,height=2,font=('arial',10,'bold'),#command=view_function_dues_all_command,
		bg='blue',fg='white',relief='solid')
		view_fdue_b1.place(x=1030,y=700)

		view_due_all_b1=Button(self,text='View All Paid Dues',command=view_member_dues_all_command,width=25,height=2,font=('arial',10,'bold'),#
		bg='blue',fg='white',relief='solid')
		view_due_all_b1.place(x=1230,y=700)

		tree = ttk.Treeview(Dues_frame_list, columns =(1,2,3,4,5,6,7,8), height = 5 , show ="headings")
		tree.place(x=0, y=50, width = 640, height = 220)
		tree.tag_configure('oddrow',background='#E8E8E8')
		tree.tag_configure('evenrow',background='#DFDFDF')
		tree.bind("<<TreeviewSelect>>", treeActionSelect2)
		# Add scrollbar
		vsb = ttk.Scrollbar(Dues_frame_list , orient="vertical",command=tree.yview)
		vsb.place(x=620, y=160, height=50)
		tree.configure(yscrollcommand=vsb.set)

		# Add headings
		tree.heading(1, text ="Id" )
		tree.heading(2, text = "Date")
		tree.heading(3, text = "Month-Rev")
		tree.heading(4, text ="Other-Rev" )
		tree.heading(5, text = "Other-Rev-Info")
		tree.heading(6, text = "Total-Rev")
		tree.heading(7, text = "Expenses")
		tree.heading(8, text = "Balance")
		#Define column width
		tree.column(1, width=20)
		tree.column(2, width=50)
		tree.column(3, width=50)
		tree.column(4, width=50)
		tree.column(5, width=70)
		tree.column(6, width=50)
		tree.column(7, width=50)
		tree.column(8, width=50)

		select2=account.view_due_revenue_all()
		for row in select2:
			if row[0]%2==0:
				tree.insert('',END,values=row,tags=("even",))
			else:
				tree.insert('',END,values=row,tags=("odd",))

		tree.tag_configure("even",foreground="black",background="white")
		tree.tag_configure("odd",foreground="white",background="black")

		list3=Listbox(self,height=4,width=58,bg='lightblue',
		fg='red',font=('arial',14,'bold'))
		list3.place(x=490,y=403)

		list3.bind('<<ListboxSelect>>', get_selected_row3)

		sb3=Scrollbar(self)
		sb3.place(x=1110,y=425)

		list3.configure(yscrollcommand=sb3.set)
		sb3.configure(command=list3.yview)
		#=================================================================================

class PageThree(tk.Frame):

	def __init__(self, parent, controller):
		s=ttk.Style()
		s.theme_use("clam")
		s.configure(".",font=('Helvetica',11))
		tk.Frame.__init__(self, parent)
		tk.Frame.bg_pageone=Label(self,bg="#3EFF15",height=600,width=1400)
		tk.Frame.bg_pageone.place(x=0,y=0)
				
		# tk.Frame.bg1=ImageTk.PhotoImage(file="12.png")
		# tk.Frame.bg_image=Label(self,image=self.bg1)
		# tk.Frame.bg_image.place(x=300,y=0,relwidth=1,relheight=1)

		Reg_frame1=Frame(self,bd=10,relief=RIDGE,width=660,height=430,bg='navy')
		Reg_frame1.place(x=20,y=65)
		
		Reg_frame1_button=Frame(self,bd=10,relief=RIDGE,width=660,height=200,bg='navy')
		Reg_frame1_button.place(x=20,y=495)

		Reg_frame1_list=Frame(self,bd=10,relief=RIDGE,width=460,height=630,bg='#00ff00')
		Reg_frame1_list.place(x=680,y=65)

		Reg_frame1_other=Frame(self,bd=10,relief=RIDGE,width=340,height=630,bg='darkorange')
		Reg_frame1_other.place(x=1140,y=65)

		self.controller = controller
		label = tk.Label(self, text="Member Registration Platform", fg='darkorange',bg="navy",font=("Arial",24,))
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Back",bg="red",fg="white",bd=0,
						   command=lambda: controller.show_frame(StartPage))
		button.place(x=5,y=20)

	  
		def treeActionSelect(event):
			# load image
			global idSelect
			global firstNameSelect
			global lastNameSelect
			global addressSelect
			global genderSelect
			global dobSelect
			global imgProfile2
			idSelect = tree.item(tree.selection())['values'][0]
			firstNameSelect = tree.item(tree.selection())['values'][1]
			lastNameSelect = tree.item(tree.selection())['values'][2]
			addressSelect = tree.item(tree.selection())['values'][3]
			genderSelect = tree.item(tree.selection())['values'][4]
			dobSelect = tree.item(tree.selection())['values'][5]
			imgBlopSelect = tree.item(tree.selection())['values'][6]
			imgProfile2 = "images/profile_"+firstNameSelect+"_"+lastNameSelect+"_" + str(idSelect) + "." + "jpg"
			load2 = Image.open(imgProfile2)
			load2.thumbnail((250,250))
			photo2 = ImageTk.PhotoImage(load2)
			Profile2[1] = photo2
			lblImage2 = Label(self ,  image = photo2,width=180,height=180)
			lblImage2.place(x=1200 , y=90)
			lid = Label(self, text = "Club ID : " + str(idSelect),bg='darkorange',fg='blue',font=('arial',16,'bold'))
			lid.place(x = 1150, y =280 , width = 300)
			fname = Label(self, text = " FirstName : " + firstNameSelect,bg='darkorange',fg='blue',font=('arial',16,'bold'))
			fname.place(x=1150 , y = 330 , width = 300)
			lname = Label(self, text = "LastName : " + lastNameSelect,bg='darkorange',fg='blue',font=('arial',16,'bold'))
			lname.place(x = 1150 , y = 380 , width = 300)
			addr = Label(self, text = " Address : " + addressSelect,bg='darkorange',fg='blue',font=('arial',16,'bold'))
			addr.place(x=1150 , y = 430 , width = 300)
			gnder = Label(self, text = "Gender : " + genderSelect,bg='darkorange',fg='blue',font=('arial',16,'bold'))
			gnder.place(x = 1150 , y = 480 , width = 300)
			dob = Label(self, text = " DOB : " + dobSelect,bg='darkorange',fg='blue',font=('arial',16,'bold'))
			dob.place(x=1150 , y = 530 , width = 300)
			iblp = Label(self, text = "ImgBlop : " + str(imgBlopSelect),bg='darkorange',fg='blue',font=('arial',16,'bold'))
			iblp.place(x = 1150 , y = 580 , width = 300)            
			# Tmore.insert(END , "More Info : " +  moreInfoSelect)
			e10.delete(0,END)
			e10.insert(END,firstNameSelect)
			e11.delete(0,END)
			e11.insert(END,lastNameSelect)
			e12.delete(0,END)
			e12.insert(END,addressSelect)
			e13.delete(0,END)
			e13.insert(END,genderSelect)
			e14.delete(0,END)
			e14.insert(END,dobSelect)
			#Replace image
			imgProfile = "images/profile_"+firstNameSelect+"_" +lastNameSelect+"_" + str(idSelect) + "." + "jpg"
			load = Image.open(imgProfile)
			load.thumbnail((150,150))
			photo = ImageTk.PhotoImage(load)
			Profile[1] = photo
			lblImage = Label(Reg_frame1 ,  image = photo)
			lblImage.place(x=440 , y=80)

			# path = imgBlopSelect
			# img = ImageTk.PhotoImage(Image.open(path).resize((150,150),Image.ANTIALIAS))
			# panel = Label(Reg_frame1, image = img,)
			# panel.image = img # keep a reference!
			# panel.place(x=440, y=75,)

	
	   
	   

		def BrowsePhoto():
			entryPhoto.delete(0, END)
			filedirr = filedialog.askopenfilename(initialdir= "/",title="Select File")
			print(filedirr)  
			entryPhoto.insert(END , filedirr)                     
		
		def member_reg_command():                   
			# Photo profile
			filename = entryPhoto.get()
			with open(filename,'rb') as fl:
				m=fl.read()
			filenew="temp_image/profile"+ ".jpg"
			with open(filenew,"wb") as k:
				img=k.write(m)
			if filenew != None:
				#place image
				img = ImageTk.PhotoImage(Image.open(filenew).resize((150,150),Image.ANTIALIAS))
				panel = Label(Reg_frame1, image = img)
				panel.image = img # keep a reference!
				panel.place(x=440, y=80,)
			
			if account.view_member() == []:
				with open(filenew,'rb') as fl:
					m=fl.read()
				with open("images/profile_"+firstname_reg_text.get()+"_"+lastname_reg_text.get()+"_" +str(1) + ".jpg","wb") as k:
					img=k.write(m)
					account.insert_member(firstname_reg_text.get(),lastname_reg_text.get(),address_reg_text.get(),
					gender_reg_text.get(),dob_reg_text.get(),img)
					select = account.view_member_reg()
					select = list(select)
					tree.insert('' , END , values = select[0] )
					account.register_member_for_deposit(firstname_reg_text.get(),lastname_reg_text.get(),"")
					# list4.delete(0,END)
					# list4.insert(END,(firstname_reg_text.get(),lastname_reg_text.get(),address_reg_text.get(),
					# gender_reg_text.get(),dob_reg_text.get(),img))
					e15.delete(0,END) 
					e15.insert(0,"New Member Registration SUCCESSFUL!")
			else:
				select=account.view_member_reg()
				select = list(select)
				id = select[0][0]
				with open(filenew,'rb') as fl:
					m=fl.read()
				with open("images/profile_"+firstname_reg_text.get()+"_"+lastname_reg_text.get()+"_" +str(id + 1) + ".jpg","wb") as k:
					img=k.write(m)

					account.insert_member(firstname_reg_text.get(),lastname_reg_text.get(),address_reg_text.get(),
					gender_reg_text.get(),dob_reg_text.get(),img)
					account.register_member_for_deposit(firstname_reg_text.get(),lastname_reg_text.get(),"")
					select = account.view_member_reg()
					select = list(select)
					tree.insert('' , END , values = select[0] )
					# list4.delete(0,END)
					# list4.insert(END,(firstname_reg_text.get(),lastname_reg_text.get(),address_reg_text.get(),
					# gender_reg_text.get(),dob_reg_text.get(),img))
					e15.delete(0,END) 
					e15.insert(0,"New Member Registration SUCCESSFUL!")

		def update_member_reg_command():
			select=account.view_member_reg()
			select = list(select)
			id = select[0][0]
			if entryPhoto.get() != "":
				filename = entryPhoto.get()
				with open(filename,'rb') as fl:
					m=fl.read()
				filenew="temp_image/profile"+ ".jpg"
				with open(filenew,"wb") as k:
					img=k.write(m)
				if filenew != None:
					#place image
					imag = ImageTk.PhotoImage(Image.open(filenew).resize((150,150),Image.ANTIALIAS))
					panel = Label(Reg_frame1, image = imag)
					panel.image = imag # keep a reference!
					panel.place(x=440, y=80,)                   

					file2="temp_image/profile"+ ".jpg"                    
					with open(file2,'rb') as fl:
						m=fl.read()
					fileupdate="images/profile_"+firstNameSelect+"_" +lastNameSelect+"_" + str(idSelect) +".jpg"
					with open(fileupdate,"wb") as k:
						img=k.write(m)
						account.update_member_reg(str(idSelect),firstname_reg_text.get(),lastname_reg_text.get(),
						address_reg_text.get(),gender_reg_text.get(),dob_reg_text.get(),img)

			else:
				filename="images/profile_"+firstNameSelect+"_" +lastNameSelect+"_" + str(idSelect) +".jpg"
				with open(filename,'rb') as fl:
					m=fl.read()
				fileupdate="temp_image/profile"+ ".jpg"
				with open(fileupdate,"wb") as k:
					img=k.write(m)

				if fileupdate != "":                    
					os.remove(filename)
					fileupdate="temp_image/profile"+ ".jpg"
					with open(fileupdate,'rb') as fl:
						m=fl.read()
					finalupdate="images/profile_"+firstname_reg_text.get()+"_" +lastname_reg_text.get()+"_" + str(idSelect) +".jpg"
					with open(finalupdate,"wb") as k:
						img=k.write(m)

						imag = ImageTk.PhotoImage(Image.open(fileupdate).resize((150,150),Image.ANTIALIAS))
						panel = Label(Reg_frame1, image = imag)
						panel.image = imag # keep a reference!
						panel.place(x=440, y=80,)

						account.update_member_reg(str(idSelect),firstname_reg_text.get(),lastname_reg_text.get(),
						address_reg_text.get(),gender_reg_text.get(),dob_reg_text.get(),img)
						select = account.view_member_reg()
						select = list(select)
						tree.insert('' , END , values = (idSelect,firstname_reg_text.get(),lastname_reg_text.get(),
						address_reg_text.get(),gender_reg_text.get(),dob_reg_text.get(),img))
						
						e15.delete(0,END) 
						e15.insert(0,"Member Details Update SUCCESSFUL!")
			

		
		def delete_member_reg_command():
			account.delete_member(idSelect,)
			tree.delete(tree.selection())
			e15.delete(0,END) 
			e15.insert(0,"Member Deleted SUCCESSFULLY!")
			

		tree = ttk.Treeview(Reg_frame1_list, columns =(1,2,3,4,5,6,7), height = 5 , show ="headings")
		tree.place(x=0, y=50, width = 440, height = 555)
		tree.tag_configure('oddrow',background='#E8E8E8')
		tree.tag_configure('evenrow',background='#DFDFDF')
		tree.bind("<<TreeviewSelect>>", treeActionSelect)
		# Add scrollbar
		vsb = ttk.Scrollbar(Reg_frame1_list , orient="vertical",command=tree.yview)
		vsb.place(x=420, y=200, height=175)
		tree.configure(yscrollcommand=vsb.set)

		# Add headings
		tree.heading(1, text ="Id" )
		tree.heading(2, text = "Firstname")
		tree.heading(3, text = "Lastname")
		tree.heading(4, text ="Address" )
		tree.heading(5, text = "Gender")
		tree.heading(6, text = "DOB")
		tree.heading(7, text = "ImgBLOP")
		#Define column width
		tree.column(1, width=20)
		tree.column(2, width=50)
		tree.column(3, width=50)
		tree.column(4, width=50)
		tree.column(5, width=50)
		tree.column(6, width=50)
		tree.column(7, width=50)
		
		select=account.view_member()
		for row in select:
			if row[0]%2==0:
				tree.insert('',END,values=row,tags=("even",))
			else:
				tree.insert('',END,values=row,tags=("odd",))

		tree.tag_configure("even",foreground="black",background="white")
		tree.tag_configure("odd",foreground="white",background="black")

		#===================Registration=====================================================================
							 
		l9=Label(self,text="Member Personal Details",font=('arial',16,'bold'),bg='navy',fg='cyan')
		l9.place(x=195,y=90)

		l10=Label(self,text="Firstname :",font=('arial',12,'bold'),bg='navy',fg='white')
		l10.place(x=70,y=150)

		l11=Label(self,text="Lastname:",font=('arial',12,'bold'),bg='navy',fg='white')
		l11.place(x=70,y=210)

		l12=Label(self,text="Address :",font=('arial',12,'bold'),bg='navy',fg='white')
		l12.place(x=70,y=270)

		l13=Label(self,text="Gender:",font=('arial',12,'bold'),bg='navy',fg='white')
		l13.place(x=70,y=330)

		l14=Label(self,text="DOB :",font=('arial',12,'bold'),bg='navy',fg='white')
		l14.place(x=70,y=390)

		l14=Label(Reg_frame1_list,text="Registered Members",font=('arial',23,'bold'),bg='navy',fg='cyan')
		l14.place(x=69,y=4)

		firstname_reg_text=StringVar()
		e10=Entry(self,textvariable=firstname_reg_text,font=('arial',16,'bold'),width=15)
		e10.place(x=170,y=148)

		lastname_reg_text=StringVar()
		e11=Entry(self,textvariable=lastname_reg_text,font=('arial',16,'bold'),width=15)
		e11.place(x=170,y=205)

		address_reg_text=StringVar()
		e12=Entry(self,textvariable=address_reg_text,font=('arial',16,'bold'),width=15)
		e12.place(x=170,y=265)

		gender_reg_text=StringVar()
		e13=Entry(self,textvariable=gender_reg_text,font=('arial',16,'bold'),width=15)
		e13.place(x=170,y=325)

		dob_reg_text=StringVar()
		e14=Entry(self,textvariable=dob_reg_text,font=('arial',16,'bold'),width=15)
		e14.place(x=170,y=385)

		info_text=StringVar()
		e15=Entry(self,textvariable=info_text,bd='0',font=('arial',22,'bold'),width=40,bg='#3EFF15',fg='darkorange')
		e15.place(x=250,y=700)

		entryPhoto=StringVar()
		entryPhoto = Entry(self,textvariable=entryPhoto)
		entryPhoto.place(x = 410,  y =330 , width=150)

		#place image
		path = "profile.png"
		img = ImageTk.PhotoImage(Image.open(path).resize((150,150),Image.Resampling.LANCZOS))
		panel = Label(Reg_frame1, image = img,)
		panel.image = img # keep a reference!
		panel.place(x=440, y=75,)





		# path = "profile.png"
		img = ImageTk.PhotoImage(Image.open(path))
		 
		# label_image = Label(Dues_frame,width=100,height=100,image = img)
		# label_image.place(x=440, y=125) 
		# Add Treeview
	   
		# ======================================================================================
		reg_1=Button(self,text='Add Member',command=member_reg_command,width=15,height=2,font=('arial',12,'bold'),#command=member_reg_command,
		bg='darkgreen',fg='white',relief='solid')
		reg_1.place(x=50,y=520)

		reg_2=Button(self,text='View Members',width=15,height=2,font=('arial',12,'bold'),#command=view_reg_member_command,
		bg='darkgreen',fg='white',relief='solid')
		reg_2.place(x=50,y=590)

		reg_3=Button(self,text='Update Entry',command=update_member_reg_command,width=15,height=2,font=('arial',12,'bold'),#
		bg='darkorange',fg='white',relief='solid')
		reg_3.place(x=270,y=520)

		reg_4=Button(self,text='Delete Member',command=delete_member_reg_command,width=15,height=2,font=('arial',12,'bold'),#
		bg='red',fg='white',relief='solid')
		reg_4.place(x=270,y=590)

		reg_5=Button(self,text='Search',width=15,height=2,font=('arial',12,'bold'),padx=0,#command=search_member_reg_command,
		bg='grey',fg='white',relief='solid')
		reg_5.place(x=490,y=520)

		browse_img_b=Button(self,text='Browse',command=BrowsePhoto,width=8,height=1,font=('arial',10,'bold'),padx=0,#command = BrowsePhoto 
		bg='blue',fg='white',relief='solid')
		browse_img_b.place(x=590,y=330)

		browse_img_b2=Button(self,text='View Members',width=15,height=2,font=('arial',12,'bold'),padx=0,#command=view_member_reg_command,
		bg='blue',fg='white',relief='solid')
		browse_img_b2.place(x=490,y=590)

		# list4=Listbox(self,height=30,width=48,bg='#00ff00',fg='red',font=('arial',12,'bold'))
		# list4.place(x=690,y=75)

		# sb4=Scrollbar(self)
		# sb4.place(x=1100,y=400)


class PageFour(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		tk.Frame.bg_pageone=Label(self,bg="teal",height=600,width=1400)
		tk.Frame.bg_pageone.place(x=0,y=0)
				
		# tk.Frame.bg1=ImageTk.PhotoImage(file="12.png")
		# tk.Frame.bg_image=Label(self,image=self.bg1)
		# tk.Frame.bg_image.place(x=300,y=0,relwidth=1,relheight=1)

		self.controller = controller
		label = tk.Label(self, text="Records / Munite Section", fg='darkorange',bg="#3EFF15",font=("Arial",24))
		label.pack(side="top", fill="x", pady=10)
		button = tk.Button(self, text="Back",bg="red",fg="white",bd=0,
						   command=lambda: controller.show_frame(StartPage))
		button.place(x=5,y=20)

		def get_selected_row6(event):
			global selected_tuple6
			index=list_minute.curselection()[0]
			selected_tuple6=list_minute.get(index)
			minute_e8.delete(0,END)
			minute_e8.insert(END,selected_tuple6[1])

		# def get_agenda(index):
			
		#     minute_e8.delete(0,END)
		#     minute_e8.insert(END,agenda[index])

		# agendadetail=""
		# aobdetail=""
		
		def submit_munite_1_command():
			minute_file="minute.txt"            
			with open(minute_file,"a+") as file:
				file.write("This meeting was held on "+date_minute_text.get()+" ")

			with open(minute_file,"a+") as file:
				file.write("at about "+time_minute_text.get()+"\n")

			with open(minute_file,"a+") as file:
				file.write("The venue of the days meeting was "+venue_minute_text.get()+"\n")

			with open(minute_file,"a+") as file:
				file.write("and it was hosted by "+host_minute_text.get()+"\n")

			with open(minute_file,"a+") as file:
				file.write(chaired_minute_text.get()+" presided over the meeting as the chairman"+"\n")

			with open(minute_file,"a+") as file:
				file.write("while "+sec_minute_text.get()+" was the secretary who read the minute of the last meeting"+"\n")

			with open(minute_file,"a+") as file:
				file.write("After no ammendment the minute was endorsed by "+endorsed_minute_text.get()+"\n")
				minute_e1.delete(0,END)
				minute_e2.delete(0,END)
				minute_e3.delete(0,END)
				minute_e4.delete(0,END)
				minute_e5.delete(0,END)
				minute_e6.delete(0,END)
				minute_e7.delete(0,END)
				minute_e06.configure(state=tk.DISABLED)


		def submit_munite_2_command():
			minute_file="minute.txt"            
			with open(minute_file,"a+") as file:
				file.write("\n")
				file.write("The opening remark was as follows:\n "+remark_textbox.get(1.0,END)+" ")
				file.write("\n")

			minute_file="minute.txt"            
			with open(minute_file,"a+") as file:
				file.write("\n")
				file.write("The Agenda are as follows:\n ")

				remark_textbox.delete(1.0,END)
				minute_e06.configure(state=tk.DISABLED)

			# account.add_minute_openremark(remark_textbox.get(1.0,END))
			# info_minute.delete(0,END)
			# info_minute.insert(0,"Open Remark SUBMITTED!")
			# remark_textbox.delete(0,END)
			# list_minute.delete(0,END)
			# for row in account.view_minute():
			#     list_minute.insert(END, row)

		index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
		agenda=[]

		def activate_agenda_command():
			minute_e06.configure(state=tk.NORMAL)
			minute_e9.configure(state=tk.DISABLED)
			aob_textbox.configure(state=tk.DISABLED)
		
			  
		def add_agenda_command():
			if agender_title_text.get() == "":
				pass
			else:
				account.add_agenda_title(agender_title_text.get())
				agenda.append(agender_title_text.get())  
				minute_file="minute.txt"            
				with open(minute_file,"a+") as file:
					file.write(agender_title_text.get() + "\n"+" ")        
				list_minute.delete(0,END)
				for i,j in zip(index,agenda):
					list_minute.insert(END,str(i)+" "+ j + "\n") 
					
					minute_e06.delete(0,END)
					info_minute.delete(0,END)
					info_minute.insert(0,"Aganda SUBMITTED!")
							   
					
		def submit_agenda_deli_command():
			minute_file="minute.txt"            
			with open(minute_file,"a+") as file:
				file.write(str(selected_tuple6[0])+". "+str(selected_tuple6[1])+":\n"+agenda_textbox.get(1.0,END)+" ")
				  

		def view_agenda_title_command():
			list_minute.delete(0,END)        
			for row in account.view_agenda_title():
				list_minute.insert(END,row)
			minute_file="minute.txt"            
			with open(minute_file,"a+") as file:
				file.write("\n")
				file.write("The Agenda are deliberated as follows :\n")
			minute_e9.configure(state=tk.DISABLED)
			aob_textbox.configure(state=tk.DISABLED)

		def activate_AOB_command():
			minute_e9.configure(state=tk.NORMAL)
			aob_textbox.configure(state=tk.NORMAL)
			minute_file="minute.txt"            
			with open(minute_file,"a+") as file:
				file.write("\n")
				file.write("The Club AOBs are deliberated as follows :\n")
			
		def submit_aob_deli_command():
			minute_file="minute.txt"            
			with open(minute_file,"a+") as file:
				file.write(aob_title_text.get()+":\n"+aob_textbox.get(1.0,END))  
			minute_e9.delete(0,END)
			aob_textbox.delete(1.0,END)                  
					  

		#==============Munites=============================================
		Dues_frame=Frame(self,bd=10,relief=RIDGE,width=660,height=480,bg='navy')
		Dues_frame.place(x=20,y=65)
		
		Dues_frame_button=Frame(self,bd=10,relief=RIDGE,width=660,height=150,bg='navy')
		Dues_frame_button.place(x=20,y=545)

		Dues_frame_list=Frame(self,bd=10,relief=RIDGE,width=460,height=630,bg='darkgreen')
		Dues_frame_list.place(x=680,y=65)

		Dues_frame_other=Frame(self,bd=10,relief=RIDGE,width=340,height=630,bg='darkorange')
		Dues_frame_other.place(x=1140,y=65)

		minute_l1=Label(self,text="Club Munite Book",font=('arial',16,'bold'),bg='navy',fg='cyan')
		minute_l1.place(x=245,y=90)

		minute_l2=Label(self,text="Date :",font=('arial',12,'bold'),bg='navy',fg='white')
		minute_l2.place(x=70,y=130)

		minute_l3=Label(self,text="Time:",font=('arial',12,'bold'),bg='navy',fg='white')
		minute_l3.place(x=250,y=130)

		minute_l4=Label(self,text="Venue :",font=('arial',12,'bold'),bg='navy',fg='white')
		minute_l4.place(x=430,y=130)

		minute_l5=Label(self,text="Host By:",font=('arial',12,'bold'),bg='navy',fg='white')
		minute_l5.place(x=70,y=180)

		minute_l6=Label(self,text="Chaired By:",font=('arial',12,'bold'),bg='navy',fg='white')
		minute_l6.place(x=270,y=180)

		minute_l7=Label(self,text="Secretary:",font=('arial',12,'bold'),bg='navy',fg='white')
		minute_l7.place(x=70,y=230)

		minute_l7=Label(self,text="Endorsed By:",font=('arial',12,'bold'),bg='navy',fg='white')
		minute_l7.place(x=290,y=230)
		
		minute_20=Label(self,text="Opening Remark:",font=('arial',12,'bold'),bg='navy',fg='darkorange')
		minute_20.place(x=50,y=310)

		minute_l8=Label(self,text="Enter Agender",font=('arial',14,'bold'),bg='navy',fg='cyan')
		minute_l8.place(x=280,y=440)

		minute_l9=Label(self,text="Agender Title:",font=('arial',12,'bold'),bg='navy',fg='darkorange')
		minute_l9.place(x=50,y=470)       

		minute_20=Label(self,text="Agender Deliberation Panel",font=('arial',15,'bold'),bg='darkgreen',fg='cyan')
		minute_20.place(x=770,y=90)

		minute_20=Label(self,text="Agender Title:",font=('arial',12,'bold'),bg='darkgreen',fg='white')
		minute_20.place(x=700,y=140)

		minute_20=Label(self,text="Agender Description:",font=('arial',12,'bold'),bg='darkgreen',fg='white')
		minute_20.place(x=700,y=175)

		minute_20=Label(self,text="AOB Deliberation Panel",font=('arial',15,'bold'),bg='darkorange',fg='cyan')
		minute_20.place(x=1190,y=90)

		minute_20=Label(self,text="AOB Title:",font=('arial',12,'bold'),bg='darkorange',fg='white')
		minute_20.place(x=1158,y=140)

		minute_20=Label(self,text="AOB Description:",font=('arial',12,'bold'),bg='darkorange',fg='white')
		minute_20.place(x=1158,y=175)

		date_minute_text=StringVar()
		minute_e1=Entry(self,textvariable=date_minute_text,font=('arial',14,'bold'),width=8)
		minute_e1.place(x=120,y=130)

		time_minute_text=StringVar()
		minute_e2=Entry(self,textvariable=time_minute_text,font=('arial',14,'bold'),width=8)
		minute_e2.place(x=300,y=130)

		venue_minute_text=StringVar()
		minute_e3=Entry(self,textvariable=venue_minute_text,font=('arial',14,'bold'),width=10)
		minute_e3.place(x=500,y=130)

		host_minute_text=StringVar()
		minute_e4=Entry(self,textvariable=host_minute_text,font=('arial',14,'bold'),width=10)
		minute_e4.place(x=150,y=180)

		chaired_minute_text=StringVar()
		minute_e5=Entry(self,textvariable=chaired_minute_text,font=('arial',14,'bold'),width=10)
		minute_e5.place(x=370,y=180)

		sec_minute_text=StringVar()
		minute_e6=Entry(self,textvariable=sec_minute_text,font=('arial',14,'bold'),width=10)
		minute_e6.place(x=160,y=230)

		endorsed_minute_text=StringVar()
		minute_e7=Entry(self,textvariable=endorsed_minute_text,font=('arial',14,'bold'),width=15)
		minute_e7.place(x=410,y=230)

		agender_title_text=StringVar()
		minute_e06=Entry(self,textvariable=agender_title_text,font=('arial',14,'bold'),width=44)
		minute_e06.place(x=165,y=470)

		# agender_desc_minute_text=StringVar()
		# minute_e7=Entry(self,textvariable=agender_desc_minute_text,font=('arial',14,'bold'),width=37)
		# minute_e7.place(x=225,y=430)

		agender_deli_title_text=StringVar()
		minute_e8=Entry(self,textvariable=agender_deli_title_text,font=('arial',14,'bold'),width=17)
		minute_e8.place(x=845,y=140)

		aob_title_text=StringVar()
		minute_e9=Entry(self,textvariable=aob_title_text,font=('arial',14,'bold'),width=19)
		minute_e9.place(x=1240,y=140)

		# agender_deli_desc_text=StringVar()
		# minute_e9=Entry(self,textvariable=agender_deli_desc_text,font=('arial',14,'bold'),width=17)
		# minute_e9.place(x=885,y=175)

		remark_textbox=Text(self,width=50,height=5,font=('arial',12))
		remark_textbox.place(x=200,y=305)

		agenda_textbox=Text(self,width=39,height=17,font=('arial',12))
		agenda_textbox.place(x=735,y=205)

   
		info_minute_text=StringVar()
		info_minute=Entry(self,textvariable=info_minute_text,font=('arial',22,'bold'),width=36,fg="darkred",bg="teal")
		info_minute.place(x=40,y=700)


		# aob_deli_desc_text=StringVar()
		aob_textbox=Text(self,width=32,height=17,font=('arial',12,))
		aob_textbox.place(x=1160,y=205)

	  

		minute_b1=Button(self,text='Submit',command=submit_munite_1_command,width=15,height=1,font=('arial',12,'bold'),padx=0,#
		bg='darkorange',fg='white',relief='solid')
		minute_b1.place(x=500,y=260)

		minute_b2=Button(self,text='Submit',command=submit_munite_2_command,width=15,height=1,font=('arial',12,'bold'),padx=0,#
		bg='darkorange',fg='white',relief='solid')
		minute_b2.place(x=500,y=405)

		minute_b3=Button(self,text='Club Agenda',width=15,command=activate_agenda_command,height=1,font=('arial',12,'bold'),padx=0,#command=view_minute_command,
		bg='green',fg='white',relief='solid')
		minute_b3.place(x=170,y=500)

		minute_b3=Button(self,text='Submit',width=15,command=add_agenda_command,height=1,font=('arial',12,'bold'),padx=0,#command=view_minute_command,
		bg='darkorange',fg='white',relief='solid')
		minute_b3.place(x=340,y=500)

		minute_b4=Button(self,text='View All Agenda',width=15,command=view_agenda_title_command,height=1,font=('arial',12,'bold'),padx=0,#command=view_minute_command,
		bg='blue',fg='white',relief='solid')
		minute_b4.place(x=500,y=500)

		minute_b4=Button(self,text='Club Agenda',width=12,height=1,font=('arial',10,'bold'),padx=0,#command=submit_munite_1_command,
		bg='blue',fg='white',relief='solid')
		minute_b4.place(x=740,y=530)

		minute_b4=Button(self,text='Submit',command=submit_agenda_deli_command,width=12,height=1,font=('arial',10,'bold'),padx=0,#command=submit_munite_1_command,
		bg='darkorange',fg='white',relief='solid')
		minute_b4.place(x=985,y=530)

		minute_b5=Button(self,text='Club AOBs',command=activate_AOB_command,width=12,height=1,font=('arial',10,'bold'),padx=0,#command=submit_munite_2_command,
		bg='blue',fg='white',relief='solid')
		minute_b5.place(x=1160,y=530)

		minute_b6=Button(self,text='Submit',command=submit_aob_deli_command,width=12,height=1,font=('arial',10,'bold'),padx=0,#command=submit_munite_2_command,
		bg='darkorange',fg='white',relief='solid')
		minute_b6.place(x=1350,y=530)

		minute_b7=Button(self,text='Submit All',width=17,height=2,font=('arial',12,'bold'),padx=0,#command=submit_munite_all_command,
		bg='blue',fg='black',relief='solid')
		minute_b7.place(x=1270,y=695)

		list_minute=Listbox(self,height=6,width=70,bg='#00ff00',fg='red',font=('arial',12,'bold'))
		list_minute.place(x=32,y=557)

		list_minute.bind('<<ListboxSelect>>', get_selected_row6)

		sb5=Scrollbar(self)
		sb5.place(x=640,y=600)

		list_minute.configure(yscrollcommand=sb5.set)
		sb5.configure(command=list_minute.yview)


if __name__ == "__main__":
	app = tkinterApp()
	app.mainloop()
