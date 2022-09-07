1>>Import mysql.connector as c
Con=c.connect(host=’localhost’, user=’root’, passwd=’******’, database=”******”)
Cursor=con.cursor
Query=”select* from <t_name>
Cursor.execute(query)
Data=cursor.fetchone()
Print(data)
Data-cursor.fetchone()
Print(data)
Print(“total number of rows”,cursor.rowcount)
2>>Import mysql.connector as c
Con=c.connect(host=’localhost’, user=’root’, passwd=’******’, database=”******”)
Cursor=con.cursor
Query=”select* from <t_name>
Cursor.execute(query)
Data=cursor.fetchmany(4)
For I in data:
	Print(I)
Print(“total number of rows”, cursor.rowcount)
