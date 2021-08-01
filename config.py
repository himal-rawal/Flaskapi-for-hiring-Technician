from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'sql6428663'
app.config['MYSQL_DATABASE_PASSWORD'] = 'VkAiediWZC'
app.config['MYSQL_DATABASE_DB'] = 'sql6428663'
app.config['MYSQL_DATABASE_HOST'] = 'sql6.freemysqlhosting.net'
mysql.init_app(app)