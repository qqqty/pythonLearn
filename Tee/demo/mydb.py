import psycopg2

conn = psycopg2.connect(database='testStudy', user='wenhuang', password='Wen2012', host='127.0.0.1', port='5432')

cur = conn.cursor()

#sql = "insert into student (id, name, age) VALUES (2, 'li si', 20)"
sql = "select * from student"
cur.execute(sql)
# print cur.rowcount
#
# print cur.description
# rows = cur.fetchall()
#
# print rows
# for row in rows:
#     print row[0]
#     print row[1]
#     print row[2]


info = cur.description
res = []
for item in cur.fetchall():
    row = {}
    for i in range(len(info)):
        row[info[i][0]] = item[i]
    res.append(row)

print res


conn.commit()
conn.close()