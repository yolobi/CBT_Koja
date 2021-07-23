from app import app
import sys
import mysql.connector
import time

def MysqlConnection():
	time.sleep(0.5)
	return (mysql.connector.connect(host="mysql", user="root", password="PlantZo@123", auth_plugin='mysql_native_password', database="koja", pool_size=20))


mysql = MysqlConnection()
