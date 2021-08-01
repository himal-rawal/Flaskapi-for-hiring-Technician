from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = '3907626_hireme'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Test@981077'
app.config['MYSQL_DATABASE_DB'] = ' 3907626_hireme'
app.config['MYSQL_DATABASE_HOST'] = 'fdb32.awardspace.net'
mysql.init_app(app)