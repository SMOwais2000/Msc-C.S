Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql.connector as m

db = 'test'

connection = m.connect(host='localhost', user='root',
					password='Omen1310', database=db)
cursor = connection.cursor()

cursor.execute('SHOW TABLES;')
table_names = []
for record in cursor.fetchall():
	table_names.append(record[0])

backup_test = db + '_backup'
try:
	cursor.execute(f'CREATE DATABASE {backup_test}')
except:
	pass

cursor.execute(f'USE {backup_test}')

for table_name in table_names:
	cursor.execute(
		f'CREATE TABLE {table_name} SELECT * FROM {db}.{table_name}')