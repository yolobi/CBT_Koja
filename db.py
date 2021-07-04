from app import app
import sys
import mysql.connector

def MysqlConnection():
	return (mysql.connector.connect(host="172.17.0.1", user="root", password="PlantZo@123", auth_plugin='mysql_native_password', database="koja"))


mysql = MysqlConnection()
