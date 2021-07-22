
# Api_Hireme

We are doing college project whose goal is to hire technician. For that We are creating  Api to connect our frontend with backend. 

## Technologies
  - Frontend
      - React native
   
  - Backend
      - Flask
      - Mysql

## Api Documentation :

## Table Of Content:
- [1. Register Employee](#1-register-employee)
- [2. View employees](#2-view-employees-)
- [3. Get Single Employee](#3-get-single-employee-)
- [3. To Update Employee Info](#3-to-update-employee-info-)
- [4. To Delete Employee](#4-to-delete-employee-)
- [5. Login for Employee](#5-login-for-employee)


(Note admin and  employee will share same database but it there is coloumn in the database named **admin**  which is TINYINT data type . and we will set ** admin=1** in database manually to make any employee admin. Default value will be 0 i.e false.)

### 1. Register Employee
**Request**
```
POST /api/register/employee HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: 84b21adf-5ea7-b9f7-915f-2f506e64cddd

{
  "name": "Dani Daniel",
  "skill": "Blow Job",
  "experience": "15 years",
  "gender": "Female",
  "email": "dani@gmail.com",
  "password": "test",
  "phone": "9878664554",
  "address": "USA"
}
```
**Response** 
``` "Employee added sucessfully" ```

### 2. View employees

**Request**

```
GET /api/view/employees HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: 44a64360-8999-1515-2e43-cf81e9014cf9

```
**Response**
```
[
    {
        "address": "USA",
        "email": "dani@gmail.com",
        "experience": "15 years",
        "gender": "Female",
        "name": "Dani Daniel",
        "phone": "9878664554",
        "skill": "Blow Job"
    }
]
```

### 3. Get Single Employee
**Request**
```
GET /api/view/employee/6 HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: 65d95c1e-4ee5-1c4f-b698-b3737fd0b926
```
**Response**
```
[
    {
        "address": "USA",
        "email": "dani@gmail.com",
        "experience": "15 years",
        "gender": "Female",
        "name": "Dani Daniel",
        "phone": "9878664554",
        "skill": "Blow Job"
    }
]
```

### 3. To Update Employee Info
**Request**
```
PUT /api/update/employee HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: a37cbb6b-fe7a-8263-8e6e-993a83aa3331

{
  "id":1,
  "name": "Mia Khalifa",
  "skill": "Glasses and acting",
  "experience": "4yr",
  "gender": "female",
  "email": "mia@gmail.com",
  "phone": "9878664565",
  "address": "USA"
}
```

**Response**
``` If user exist  than information updated Sucessfully ```

### 4. To Delete Employee
**Request**
```
DELETE /api/delete/employee/1 HTTP/1.1
Host: 127.0.0.1:5000
Cache-Control: no-cache
Postman-Token: 28206cea-c4f0-0e8a-b53e-b00a30fb7ad1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
```
**Response**
```If Employee exist on our database than employee deleted Sucessfully ```

### 5. Login for Employee
**Request**
```
POST /api/login HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: 4660f824-f39d-c793-b74c-1f51ca67a17b

{
 "email": "dani@gmail.com",
  "password": "test"
}
```

**Response**

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjI2OTM5MzgzfQ.UyNsGPq0sim6rf1pN8MX39vuTGtx-t8r9DMUCOhLHrI"
}
```
## Maintainers 

 :pouting_man:` people Contributing to this project : `

- [Mobambo](https://github.com/Mobambo) 
- [Ankit Kumar](https://github.com/Robust-sketch) 
- [Babin Manyal](https://github.com/BabinManyal)  
- [Chandan Kumar](https://github.com/)  
- [Santosh](https://github.com/)  
