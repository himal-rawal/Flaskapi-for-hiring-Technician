
# Api_Hireme

This projects main goal is to hire technician. For that We are creating  Api to connect our frontend with backend. 
The api link https://hireme007.herokuapp.com will not work as I have hosted it in https://www.freemysqlhosting.net/ and its trial had ended. 
you can run it in local host

## Technologies
  - Frontend
      - any
   
  - Backend
      - Flask
      - Mysql

## Api Documentation :

## Table Of Content:
  * [1. Register Employee](#1-register-employee)
  * [2. View employees](#2-view-employees)
  * [3. Get Single Employee](#3-get-single-employee)
  * [3. To Update Employee Info By Admin](#3-to-update-employee-info-by-admin)
  * [4. To Update Employee Info By Employee From Setting](#4-to-update-employee-info-by-employee-from-setting)
  * [5. To Delete Employee](#5-to-delete-employee)
  * [6. Login for Employee](#6-login-for-employee)
  * [7. View all admin Users](#7-view-all-admin-users)
  * [8. To register client](#8-to-register-client)
  * [9. Login for client](#9-login-for-client)
  * [10. View all client Users](#10-view-all-client-users)
  * [11. To Delete Client](#11-to-delete-client)
  * [12. To Update client info By client From Setting](#12-to-update-client-info-by-client-from-setting)
  * [13. To Filter employee info](#13-to-filter-employee-info)
  * [14. To Sort technicians wrt charge](#14-to-sort-technicians-wrt-charge)
- [Maintainers](#maintainers)


(Note admin and  employee will share same table  there is coloumn in the database named **admin**  which is TINYINT data type . and we will set ** admin=1** in database manually to make any employee admin. Default value will be 0 i.e false.)

### 1. Register Employee
**Request**
```
POST /api/register/employee HTTP/1.1
Host: hireme007.herokuapp.com
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: becc2534-ddb9-9344-f53a-65a9573e91d0

{
  "name": "Dani Dany",
  "skill": "Electrician",
  "experience": "1 years",
  "gender": "Female",
  "email": "dani@gmail.com",
  "password": "test",
  "phone": "9878664554",
  "address": "Deheradun,India" ,
  "zipcode":"6547",
  "charge": "10000"
}
```
**Response** 
``` "Employee added sucessfully" ```

### 2. View employees

**Request**

```
GET /api/view/employees HTTP/1.1
Host: hireme007.herokuapp.com
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
        "name": "Dani Dany,
        "phone": "9878664554",
        "skill": "Electrician",
        "zipcode":"6547",
        "charge": "10000"
    }
]
```

### 3. Get Single Employee
**Request**
```
GET /api/view/employee/11 HTTP/1.1
Host: hireme007.herokuapp.com
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
        "name": "Dani Dany",
        "phone": "9878664554",
        "skill": "Electrician",
        "zipcode":"6547",
        "charge": "10000"
    }
]
```

### 3. To Update Employee Info By Admin
Admins token needed
**Request**
```
PUT /api/update/employee/byadmin HTTP/1.1
Host: hireme007.herokuapp.com
Content-Type: application/json
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjEsImV4cCI6MTYzMDA0MjU5M30.1GfXiVTq7vIevOZp9LlBFJUoTTEv8ee-3SUY_ZzOSCA
Cache-Control: no-cache
Postman-Token: 664cbe5a-a79f-ed1d-c34a-4ff046f2e235

{
  "id":11,
  "name": "Danni Donken",
  "skill": "Electrician",
  "experience": "4yr",
  "gender": "female",
  "email": "dani@gmail.com",
  "phone": "9878664565",
  "address": "USA",
  "zipcode":"6547",
  "charge": "10000"
}
```


**Response**

``` sucess ```

### 4. To Update Employee Info By Employee From Setting
This will update that employee whose acess token is provided
**Request**
```
PUT /api/update/employee HTTP/1.1
Host: hireme007.herokuapp.com
Content-Type: application/json
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUsImV4cCI6MTYzMDA0Mjc2N30.q8Ciwt5-cnPjb3A7HAzQnfW6rpf0Tq0IG4zOWbmm8Y4
Cache-Control: no-cache
Postman-Token: b00111ab-99b8-9970-2f7b-31132b1537b0

{
  "name": "Dani Donken",
  "skill": "Electrician",
  "experience": "3yr",
  "gender": "female",
  "email": "dani1@gmail.com",
  "password":"",
  "phone": "9878664565",
  "address": "USA",
  "zipcode":"6547",
  "charge": "10000"
}
```


**Response**

``` sucess ```

### 5. To Delete Employee
only Admins Token

**Request**

```
DELETE /api/delete/employee/10 HTTP/1.1
Host: hireme007.herokuapp.com
Cache-Control: no-cache
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OSwiZXhwIjoxNjI3MTQyODk4fQ.YSfk_VSc98dqfyY2VoCCAESsOJhArFbFw05407Jx_cE
Postman-Token: 28206cea-c4f0-0e8a-b53e-b00a30fb7ad1
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
```


**Response**

```If Employee exist on our database than employee deleted Sucessfully ```



### 6. Login for Employee

**Request**

```
POST /api/login HTTP/1.1
Host: hireme007.herokuapp.com
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

### 7. View all admin Users

**Request**

```
GET /api/view/addmin HTTP/1.1
Host: hireme007.herokuapp.com
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwiZXhwIjoxNjI3MTI5ODE1fQ.CMBrvZpZAscrfXQTYMOk0f22VvM3JyNsYd7M1NK0tEI
Cache-Control: no-cache
Postman-Token: 0f5f3403-d4ba-4b76-d93a-28d98b5363db
```


**Response**

```
[
    {
        "address": "USA",
        "email": "admin@gmail.com",
        "experience": "15 years",
        "gender": "Female",
        "name": "admin",
        "phone": "9878664554",
        "skill": "admin"
    }
]
```

### 8. To register client

**Request**
```
POST /api/register/client HTTP/1.1
Host: hireme007.herokuapp.com
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: 5c9c5c60-93d0-1e65-f336-675751dd6829

{
  "name": "shivali Bhatt",
  "gender": "Female",
  "email": "shivu@gmail.com",
  "password": "test",
  "phone": "9878664554",
  "address": "Deheradun,India" ,
  "zipcode":"6547"
}
```


**Response**

```
"client created sucessfully"
```

### 9. Login for client
**Request**
```
POST /api/login/client HTTP/1.1
Host: hireme007.herokuapp.com
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: 4660f824-f39d-c793-b74c-1f51ca67a17b

{
 "email": "shuvu@gmail.com",
  "password": "test"
}
```


**Response**

```
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NywiZXhwIjoxNjI2OTM5MzgzfQ.UyNsGPq0sim6rf1pN8MX39vuTGtx-t8r9DMUCOhLHrI"
}
```

### 10. View all client Users
Admin Token Needed
**Request**
```
GET /api/view/clients HTTP/1.1
Host: hireme007.herokuapp.com
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjIsImV4cCI6MTYzMDA0NTY5NH0.lT7_4CpqmD9xXWDUM3pCcyLTQDXn-ClpD_5jK1fVa88
Cache-Control: no-cache
Postman-Token: df7a0718-3b5f-8095-3bda-f1d0a2b4935e

```


**Response**

```
[
    {
        "address": "USA",
        "email": "shivu@gmail.com",
        "gender": "Female",
        "name": "shiivali Bhatt",
        "phone": "9878664554",
    }
]
```



### 11. To Delete Client

 Admin Token Needed
**Request**
```
DELETE /api/delete/client/1 HTTP/1.1
Host: hireme007.herokuapp.com
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjIsImV4cCI6MTYzMDA0NjYxNH0.ZsP0ROryTjNjKvsSX8MOM9CNNRCUL_USvQlFF-TfWus
Cache-Control: no-cache
Postman-Token: 2ce8687f-3786-ff22-ebc7-3b731a035a17
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
```


**Response**
```If Employee exist on our database than employee deleted Sucessfully ```


### 12. To Update client info By client From Setting
This will update that client whose acess token is provided
**Request**
```
PUT /api/update/account HTTP/1.1
Host: hireme007.herokuapp.com
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MCwiZXhwIjoxNjMwMDQ2MDU1fQ.kzK2724_87n2qwUjj0HM8JZehPfqzptiehwaGVHkuWE
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: dbb0d2ae-bfb6-edea-1591-4c03a012c03f

[
    {
        "address": "Deheradun,India",
        "email": "shivu@gmail.com",
        "gender": "Female",
        "password":"howdy",
        "name": "shivali Bhatacharya",
        "phone": "9878664554",
        "zipcode": "6547"
    }
]
```


**Response**
``` sucess ```


### 13. To Filter employee info

**Request**
```
GET /api/filterby/skill=Electrician&amp;zipcode=null&amp;charge=null HTTP/1.1
Host: hireme007.herokuapp.com
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MCwiZXhwIjoxNjMwMDQ2MDU1fQ.kzK2724_87n2qwUjj0HM8JZehPfqzptiehwaGVHkuWE
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: 664443b8-4e8c-4bbe-5449-4d19089cbcd6
```


**Response**
```
[
    {
        "address": "Usa",
        "charge": "",
        "email": "danny@gmail.com",
        "experience": "9years",
        "gender": "female",
        "name": "danny donken",
        "phone": "83459878768",
        "skill": "Electrician",
        "zipcode": "1435"
    }
]
```

### 14. To Sort technicians wrt charge
**Request**
```
GET /api/sortby/charge/acending HTTP/1.1
Host: hireme007.herokuapp.com
x-acess-token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MCwiZXhwIjoxNjMwMDQ2MDU1fQ.kzK2724_87n2qwUjj0HM8JZehPfqzptiehwaGVHkuWE
Content-Type: application/json
Cache-Control: no-cache
Postman-Token: 9f3c0d72-e7d9-4de8-ea87-8d47b3a1c468
```


**Response**
```
[ {
        "address": "India",
        "charge": "",
        "email": "hello@gmail.com",
        "experience": "B tech 4 year",
        "gender": "male",
        "name": "Hello Kumar",
        "phone": "9006575707",
        "skill": "Plumber",
        "zipcode": ""
    },
    {
        "address": "USA",
        "charge": "10000",
        "email": "dani@gmail.com",
        "experience": "3yr",
        "gender": "female",
        "name": "dani donken",
        "phone": "9878664565",
        "skill": "Electrician",
        "zipcode": "6547"
    }]
```
## Maintainers 

 :pouting_man:` people Contributing to this project : `
 
- [paranoid0x0x](https://github.com/Traitor00)
- [Mobambo](https://github.com/Mobambo)  both are my accounts

