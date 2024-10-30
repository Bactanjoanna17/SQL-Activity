from tkinter import*

import sqlite3

root=Tk()
root.title('MyCRUDProject')
root.geometry("500x500")

conn=sqlite3.connect('my_data.db')
c=conn.cursor()
'''
c.execute("""CREATE TABLE
"studentinfo
CREATE TABLE "mydata" (
	"f_name"	TEXT,
	"L_name"	TEXT,
	"Age"	INTEGER,
	"Address"	TEXT,
	"email"	TEXT
)""")
'''
f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20)
L_name=Entry(root,width=30)
L_name.grid(row=1,column=1,padx=20)
Age=Entry(root,width=30)
Age.grid(row=2,column=1,padx=20)
address=Entry(root,width=30)
address.grid(row=3,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=4,column=1,padx=20)
conn.commit()
conn.close()

root.mainloop()
