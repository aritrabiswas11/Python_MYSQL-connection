Import mysql.connector as c
Con=c.connect (host=’localhost’ ,   user=’root’,  passwd=’*******’, database=’********’)
Cursor=con.cursor()
Col1=int(input(‘enter’))
Col4=int(input(‘enter’))
Query=”update<t_name>set col1={}where col4={}” .format(col1,col4)
Cursor.execute(query)
Con.commit()
If cursor.rowcount>0:
	Print(“successful”)
Else:
	Print(“denied”)
