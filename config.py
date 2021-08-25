from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'sql6432877'
app.config['MYSQL_DATABASE_PASSWORD'] = 'VDx3sl5DZS'
app.config['MYSQL_DATABASE_DB'] = 'sql6432877'
app.config['MYSQL_DATABASE_HOST'] = 'sql6.freemysqlhosting.net'
mysql.init_app(app)