import pymysql

database=pymysql.connect(host='sever', port=3306, user='username', passwd='password',db='dbname', charset='utf8',
 cursorclass=pymysql.cursors.DictCursor)
 
