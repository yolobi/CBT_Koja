from app import app
import sys
import MySQLdb
import time

def connect():
	return (MySQLdb.connect(host="mysql", user="root", passwd="PlantZo@123", auth_plugin='mysql_native_password', db="koja"))
