import pymysql

# 전역변수 선언부
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row=None

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='sqlDB', charset='utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM usertbl")

print("사용자ID    사용자이름      출생연도    지역")
print("----------------------------------------------------")

while (True) :
    row = cur.fetchone()
    if row== None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s   %10s   %10s   %5s" % (data1, data2, data3, data4))

conn.close()
