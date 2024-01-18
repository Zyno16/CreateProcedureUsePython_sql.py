import mysql.connector
try:
    conn = mysql.connector.connect(
        host ="localhost",
        user ="userpython",
        passwd ="123456",
        database ="arabicinfo"
        )
    cur =conn.cursor()
    cur.execute("""create procedure emp_all()
                   BEGIN
                        set names utf8;
                        select * from emp;
                   END
               """)
    
except mysql.connector.Error as e:
      print(e)



call emp_all();
