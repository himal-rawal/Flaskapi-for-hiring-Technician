import pymysql
from functools import  wraps
import jwt
import uuid
import  datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
app.config['SECRET_KEY']='confidential'

def token_required(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token= None
        if 'x-acess-token' in request.headers:
            token=request.headers['x-acess-token']
        if not token:
            return  jsonify("token not found")
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        try:
            data=jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            cursor.execute('SELECT  * FROM hireme_emp  WHERE id=%s ', (data['id'],))
            row=cursor.fetchone()
            current_user = row['id']
        except Exception as  e:
            print(e)
        finally:
            cursor.close()
            conn.close()
        return  f(current_user, *args, **kwargs)
    return decorated


@app.route('/api/register/employee', methods=['POST'])
def register_user():
    try:
        _json = request.json
        _name = _json['name']
        _skill = _json['skill']
        _experience= _json['experience']
        _gender = _json['gender']
        _email= _json['email']
        _password =  _json['password']
        _phone =  _json['phone']
        _address=  _json['address']
        if _name and _skill and _experience and _gender and _email and _password and _phone and _address and request.method=='POST':

            _password=generate_password_hash(_password)
            sql="INSERT INTO hireme_emp (name,skill,experience,gender,email,password,phone,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            data= (_name, _skill, _experience, _gender, _email, _password, _phone, _address)
            conn= mysql.connect()
            cursor=conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp=jsonify("Employee added sucessfully")
            resp.status_code=200
            return  resp
        else: return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#-----------------------------------------------------------------------
#To View Employee List eg carpenter
@app.route('/api/view/employees')
def view_employee():
    try:
        conn=mysql.connect()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name,skill,experience,gender,email,phone,address FROM hireme_emp WHERE admin=0")
        rows=cursor.fetchall()
        resp=jsonify(rows)
        resp.status_code=200
        return  resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#------------------------------------------------------------------------------------
#get Specific employee  with their id
@app.route('/api/view/employee/<int:id>', methods=['GET'])
def get_specific_user(id):
    try:
        conn=mysql.connect()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name,skill,experience,gender,email,phone,address FROM hireme_emp WHERE id=%s", id)
        emprow=cursor.fetchone()
        resp = jsonify(emprow)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#------------------------------------------------------------------------------------
#login User

@app.route('/api/login', methods=['POST'])
def login():
    try:
        _json= request.json
        _email=_json['email']
        _password= _json['password']
        if _email and _password:
            conn=mysql.connect()
            cursor= conn.cursor()
            sqlquery= "SELECT * FROM hireme_emp WHERE email=%s"
            data=( _email ,)
            cursor.execute(sqlquery,data)
            row= cursor.fetchone()
            if row:
                if check_password_hash(row[8],_password):
                    token=jwt.encode({'id':row[0],'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
                    return jsonify({"token":token})
                else:
                    reponse=jsonify({'message':'Bad Request we cant find username password in our database1'})
                    reponse.status_code=400
                    return reponse
            else:
                reponse = jsonify({'message': 'Bad Request we cant find username password in our database2'})
                reponse.status_code = 400
                return reponse
        else:
            reponse = jsonify({'message': 'Bad Request we cant find username password in our database 3'})
            reponse.status_code = 400
            return reponse
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



#------------------------------------------------------------------------------------
#update user info
@app.route('/api/update/employee',methods=['PUT'])
def update_user_info():
    try:
        _json = request.json
        _id = _json['id']
        _name = _json['name']
        _skill = _json['skill']
        _experience = _json['experience']
        _gender = _json['gender']
        _email = _json['email']
        _phone = _json['phone']
        _address = _json['address']
        if _id and _name and _skill and _experience and _gender and _email  and _phone and _address and request.method == 'PUT':
            sqlquery="UPDATE hireme_emp SET name=%s,skill=%s,experience=%s, gender=%s,email=%s,phone=%s,address=%s WHERE id=%s"
            binddata= (_name, _skill, _experience, _gender, _email, _phone, _address, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlquery, binddata)
            conn.commit()
            response=jsonify("sucess")
            response.status_code=200
            return response
        else:
            return  not_found()

    except  Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()



#------------------------------------------------------------------------------------
#delete  user
@app.route('/api/delete/employee/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        conn=mysql.connect()
        cursor=conn.cursor()
        cursor.execute("DELETE FROM hireme_emp WHERE id-%s", id)
        conn.commit()
        response=jsonify("If Employee exist on our database than employee deleted Sucessfully")
        response.status_code=200
        return  response
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#------------------------------------------------------------------------------------
#create Client accoount     this is incomplete
@app.route('/api/register/client', methods=['POST'])
def create_client():
    try:
        _json = request.json
        _name = _json['name']
        _gender = _json['gender']
        _email= _json['email']
        _password =  _json['password']
        _phone =  _json['phone']
        _address=  _json['address']
        if _name and _gender and _email and _password and _phone and _address and request.method=='POST':
            sql="INSERT INTO hireme_emp (name,gender,email,password,phone,address) VALUES (%s,%s,%s,%s,%s,%s)"
            data= (_name, _gender, _email, _password, _phone, _address)
            conn= mysql.connect()
            cursor=conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp=jsonify("client created sucessfully")
            resp.status_code=200
            return  resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


#------------------------------------------------------------------------------------
#show all admin users
@app.route('/api/view/addmin')
@token_required
def view_addmin(current_user):
    try:
        conn=mysql.connect()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT name,skill,experience,gender,email,phone,address FROM hireme_emp WHERE admin=1")
        rows=cursor.fetchall()
        resp=jsonify(rows)
        resp.status_code=200
        return  resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#------------------------------------------------------------------------------------
#Error Page
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

#-------------------------------------------------------------------------------------
if __name__=="__main__":
    app.run()
