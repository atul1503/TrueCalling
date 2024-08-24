a REST API to help yourself to stay away from unwanted calls and disturbance in your stress filled life.



Steps to run the app:



0. Get python 3

1. create virtual env on top of the extracted project:
    `python3 -m venv .venv`

2. install all packages in requirement.txt:
 `pip3 install -r requirements.txt`

3. install postgres on local setup.

4. login to postgres with super user and create below user and create the database:
 `CREATE ROLE truecalling WITH LOGIN PASSWORD 'truecalling';`
 `CREATE DATABASE truecalling OWNER truecalling;`

5. activate virual env :
    `source .venv/bin/activate`

6. change into the project folder:
    `cd Truecalling` 
 
7. make migrations and migrate
  `python3 manage.py makemigration ; python3 manage.py migrate`

8. run the tests first, which are there to validate the correct run of the server:
    `python3 manage.py test`

9. run the server:
   `python3 manage.py runserver`

Tip: Use postman



API DOCUMENTATION:
-------------------

1. Search records by name:

    GET /caller/search/name/: 

        post request to register the user and return token for the remaining api unrestricted usage
        accepts username,password and phonenumber as body param
        email is optional
        
        saves the registered user records in the caller model


2. search records by phone:

    POST /caller/search/phone/:

        get request to search by phone number. If in case, phone number is more reliable than name.
        expects phonenumber as query param. 

3. Report phonenumber:

    POST /caller/report/
 
        post request , reports the phone number with the provided label type
        for eg, it will label any present `phonenumber` to the `label` provided in request

4. Register user:

    POST /api/token/

        post request to register the user and return token for the remaining api unrestricted usage
        accepts username,password and phonenumber as body param
        email is optional
            
        saves the registered user records in the caller model


5. Refresh token:

    POST /api/token/refresh/

        post request to refresh the auth token for a registered user
        accepts username and password as body params
        returns token


        
