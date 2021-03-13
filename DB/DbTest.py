import pymysql # pymysql 임포트

# 전역변수 선언부
conn = None
cur = None

data1 = ""
data2 = ""
data3 = ""
data4 = ""

sql=""

# 메인 코드
conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='TEST', charset='utf8')
cur = conn.cursor()

sql = "SELECT * FROM USER" # sql변수에 SQL문 입력
cur.execute(sql) # 커서로sql 실행

while (True) : # 반복실행
    row = cur.fetchone() # row에 커서(테이블 셀렉트)를 한줄 입력하고 다음줄로 넘어감
    if row== None : # 커서(테이블 셀렉트)에 더이상 값이 없으면
        break # while문을 빠져나감
    data1 = row[0]
    data2 = row[1]
    print("%5s %5s" % (data1, data2))

conn.close() # 접속 종료