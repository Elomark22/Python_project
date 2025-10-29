import sqlite3
class Account:
  
    def __init__(self,db):
        self.conn=sqlite3.Connection(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS member_deposit (id INTEGER PRIMARY KEY, firstname TEXT, lastname text, amount INTEGER)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS member (id INTEGER PRIMARY KEY, firstname TEXT, lastname text,address text,gender text,dob text,img BLOP)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS member_dues (id INTEGER PRIMARY KEY, firstname TEXT, lastname text,due integer,month text,descrpt text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS member_dues_all (id INTEGER PRIMARY KEY, firstname TEXT, lastname text,due integer,month text,descrpt text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS minute (id INTEGER PRIMARY KEY, date TEXT, time text,venue text,host text,chairedby text,secby text,endorsedby text,openremark text,agendatitle text,agendadetail text,aobtitle text,aobdetail text)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS minute_agenda (id INTEGER PRIMARY KEY, agenda TEXT)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS due_revenue (id INTEGER PRIMARY KEY, date TEXT,monthlydue integer,otherdue integer,otherdueinfo text, total integer, expenditure integer,balance integer)")
        self.cur.execute("CREATE TABLE IF NOT EXISTS due_revenue_all (id INTEGER PRIMARY KEY, date TEXT,monthlydue integer,otherdue integer,otherdueinfo text, total integer, expenditure integer,balance integer)")

        self.conn.commit()

    def insert_member(self, firstname, lastname,address,gender,dob,img):
        # self.cur.execute("INSERT INTO member VALUES (NULL, ?, ?, ?, ?, ?)", (firstname,lastname,address,gender,dob))
        self.cur.execute("INSERT INTO member VALUES (NULL, ?, ?, ?, ?, ?,?)", (firstname,lastname,address,gender,dob,img))
        self.cur.execute("INSERT INTO member_dues VALUES (NULL, ?, ?, ?, ?, ?)", (firstname,lastname,address,gender,dob))
        self.conn.commit()

    def register_member_for_deposit(self, firstname, lastname,amount):
        self.cur.execute("INSERT INTO member_deposit VALUES (NULL, ?, ?, ?)", (firstname,lastname,amount))
        self.conn.commit()

    def search_member(self,firstname="",lastname="",address="",gender="",dob=""):
        self.cur.execute("SELECT * FROM member WHERE firstname=? OR lastname=? OR address=? OR gender=? OR dob=?",
         (firstname, lastname,address,gender,dob))
        rows=self.cur.fetchall()
        return rows
        #  # Photo profile
        # filename = entryPhoto.get() 
        # ext = filename.split(".")
        # id = select[0][0]
        # copyfile(filename, "images/profile_" +str(id) +"."+ext[len(ext)-1])
        # im = Image.open("images/profile_" +str(id) +"."+ext[len(ext)-1])
        # rgb_im = im.convert('RGB')
        # rgb_im.save("images/profile_" +str(id) + ".jpg")

    def view_member(self):
        self.cur.execute("SELECT * FROM member ")
        rows=self.cur.fetchall()
        return rows

    def view_member_reg(self):
        self.cur.execute("SELECT * FROM member order by id desc")
        rows=self.cur.fetchall()
        return rows

    def delete_member(self,id):
        self.cur.execute("DELETE FROM member WHERE id=?", (id,))
        self.conn.commit()

    def update_member_reg(self,id,firstname,lastname,address,gender,dob,img):
        self.cur.execute("UPDATE member SET firstname=?, lastname=?,address=?,gender=?,dob=?,img=? WHERE id=?", (firstname,lastname,address,gender,dob,img,id))
        self.conn.commit()
        
    def view_member_deposit(self):
        self.cur.execute("SELECT * FROM member_deposit")
        rows=self.cur.fetchall()
        return rows
    
    def search_member_deposit(self,firstname="",lastname="",amount=""):
        self.cur.execute("SELECT * FROM member_deposit WHERE firstname=? OR lastname=? OR amount=?", (firstname, lastname))
        rows=self.cur.fetchall()
        return rows

    def insert_member_deposit(self,id, firstname, lastname, amount):
        self.cur.execute("UPDATE member_deposit SET firstname=?,lastname=?, amount = amount+? WHERE Id = ?", (firstname,lastname,amount,id))
        self.conn.commit()

    def credit_member(self,id,firstname,lastname,amount):
        self.cur.execute("UPDATE member_deposit SET amount = amount+? WHERE Id = ?", (amount,id))
        self.conn.commit()

    def debit_one_member(self,id,firstname,lastname,amount):
        self.cur.execute("UPDATE member_deposit SET amount = amount-? WHERE Id = ?", (amount,id))
        self.conn.commit()

    def debit_all_member(self,firstname,lastname,due):
        self.cur.execute("UPDATE member_deposit SET amount = amount-?", (due,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

# =============Dues Functions===========================
    def pay_all_dues(self,due,month,descrpt):
        self.cur.execute("UPDATE member_dues SET due=?,month=?,descrpt=?",
        (due,month,descrpt))        
        self.conn.commit()

    def pay_one_member_dues(self,id,due,month,descrpt):
        self.cur.execute("UPDATE member_dues SET due=?,month=?,descrpt=? WHERE Id = ?",
        (due,month,descrpt,id))        
        self.conn.commit()

    def submit_member_dues(self):
        self.cur.execute("INSERT INTO member_dues_all (firstname, lastname, due, month, descrpt) SELECT firstname, lastname, due, month, descrpt FROM member_dues")
       
        self.conn.commit()

    def view_member_due_all(self):
        self.cur.execute("SELECT * FROM member_dues_all")
        rows=self.cur.fetchall()
        return rows

    # def update_member_deposit(self,id,amount):
    #     self.cur.execute("UPDATE member_deposit SET amount = amount-? WHERE Id = ?", (amount,id))              
    #     self.conn.commit()

    def view_member_due(self):
        self.cur.execute("SELECT * FROM member_dues")
        rows=self.cur.fetchall()
        return rows

    def delete_member_dues(self,id):
        self.cur.execute("DELETE FROM member_dues WHERE id=?", (id,))
        self.conn.commit()


    def create_file(self):
        self.filename=("emy.txt")
        self.filename2=("emyCsv.csv")
        self.filename3=("emy.xlsx")
        self.cur.execute("SELECT * FROM member_dues")
        rows=self.cur.fetchall()
        # return rows
        with open(self.filename,"a+") as file:
            file.write("\n")
            for row in rows:                
                file.write(str(row)+"\n")

        with open(self.filename2,"a+") as file:
            file.write("\n")
            for row in rows:                
                file.write(str(row)+"\n")

        with open(self.filename3,"a+") as file:
            file.write("\n")
            for row in rows:                
                file.write(str(row)+"\n")

    # =====================================================

    def insert_due_revenue_temp(self,date,monthlydue,otherdue,otherdueinfo,total,expenditure,balance):
        self.cur.execute("INSERT INTO due_revenue VALUES (NULL, ?, ?, ?, ?,?,?,?)", (date,monthlydue,otherdue,otherdueinfo,total,expenditure,balance))
        self.conn.commit()

    # def insert_other_due_revenue(self,otherdue,):
    #     self.cur.execute("UPDATE due_revenue SET otherdue=?", (otherdue,))
    #     self.conn.commit()

    def get_sum_monthlydue(self):
        self.cur.execute("SELECT SUM(due) FROM member_dues")
        rows=self.cur.fetchall()
        return rows

    def update_all_due_revenue_temp(self,date,monthlydue,otherdue,otherdueinfo,total,expenditure,balance):
        self.cur.execute("UPDATE due_revenue SET date=?,monthlydue=?,otherdue=?,otherdueinfo=?,total=?,expenditure=?,balance=? ",
        (date,monthlydue,otherdue,otherdueinfo,total,expenditure,balance))      
        self.conn.commit()

    def submit_due_revenue_all(self,date,monthlydue,otherdue,otherdueinfo,total,expenditure,balance):
        self.cur.execute("INSERT INTO due_revenue_all VALUES (NULL, ?, ?, ?, ?,?,?,?)", (date,monthlydue,otherdue,otherdueinfo,total,expenditure,balance))
        self.conn.commit()


    def view_due_revenue_all(self):
        self.cur.execute("SELECT * FROM due_revenue_all ")
        rows=self.cur.fetchall()
        return rows
        
#     def withdraw(self,amount):
#         self.balance=self.balance - amount

#     def deposit(self,amount):
#         self.balance=self.balance + amount

#     def commit(self):
#         with open(self.filepath,'w') as file:
#             file.write(str(self.balance))
# ==================================================================================
    def add_minute(self,date,time,venue,host,chairedby,secby,endorsedby,openremark,agendatitle,agendadetail,aobtitle,aobdetail):
        self.cur.execute("INSERT INTO minute VALUES (NULL,?, ?, ?, ?, ?, ?, ?,?, ?, ?,?, ?)",
        (date,time,venue,host,chairedby,secby,endorsedby,openremark,agendatitle,agendadetail,aobtitle,aobdetail))
        self.conn.commit()

    def add_minute_openremark(self,openremark):
        self.cur.execute("UPDATE minute SET openremark=?",
        (openremark,))        
        self.conn.commit()

    def add_agenda_title(self,agendatitle):
        self.cur.execute("INSERT INTO minute_agenda VALUES (NULL,?)",
        (agendatitle,))        
        self.conn.commit()

    def view_agenda_title(self):
        self.cur.execute("SELECT * FROM minute_agenda")
        rows=self.cur.fetchall()
        return rows
        
    def view_minute(self):
        self.cur.execute("SELECT * FROM minute")
        rows=self.cur.fetchall()
        return rows




    