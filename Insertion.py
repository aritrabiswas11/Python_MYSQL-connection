Import mysql.connector as c
Con=c.connect (host=’localhost’ ,   user=’root’,  passwd='******’, database=’********’)
Cursor=con.cursor()
while True:
Col1=int(input(‘enter’))
Col2=(input(‘enter’)
Col3=(input(‘enter’)
Col4=int(input(‘enter’))
Query=”insert into <t_name>values({},{},{}, {})” .format(col1,col2,col3,col4)
Cursor.execute(query)
Con.commit()
Print(‘successful’)
x=int(input (“1>>Enter more\n2>>EXIT\nEnter choice”))
if x==2:
	break
