import mysql.connector

connection = mysql.connector.connect(
    host = "HostName",
    user = "UserName",
    password = "YourPassword",
    auth_plugin = "mysql_native_password",
    database = "YourDbName"
)