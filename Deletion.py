Import mysql.connector as c
Con=c.connect (host=’localhost’ ,   user=’root’,  passwd=’Momita_1969’, database=’namegiven’)
Cursor=con.cursor()
Col4=int(input(‘enter’))
Query=”delete from<t_name> where col4={}” .format(col4)
Cursor.execute(query)
Con.commit()
If cursor.rowcount>0:
	Print(“successful”)
Else:
	Print(“denied”)
