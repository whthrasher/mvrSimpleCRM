# Most Valuable Resource Simple CRM

## Getting Started
###Authentication

####JSON for the admin role is: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVkcG1KTDJwLXd4WnFKdVNIVHAwXyJ9.eyJpc3MiOiJodHRwczovL2NwcmVzb3VyY2UudXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTAzMzAwNTU4OTg2NDQ4MzcyMTAxIiwiYXVkIjpbIm12cl9hcGkiLCJodHRwczovL2NwcmVzb3VyY2UudXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYxNDA0NTgxOSwiZXhwIjoxNjE0MDUzMDE5LCJhenAiOiJHM3FYcGRQM25KY2Z1MHhFQnozaUJNaEtjOG5oOTNaaCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YnVzaW5lc3NlcyIsImRlbGV0ZTptZW1iZXJzIiwiZGVsZXRlOm1lbWJlcnNoaXBfdHlwZXMiLCJkZWxldGU6cmVsYXRpb25zaGlwcyIsImdldDpidXNpbmVzc2VzIiwiZ2V0Om1lbWJlcnMiLCJnZXQ6bWVtYmVyc2hpcF90eXBlcyIsImdldDpyZWxhdGlvbnNoaXBzIiwicGF0Y2g6YnVzaW5lc3NlcyIsInBhdGNoOm1lbWJlcnMiLCJwYXRjaDptZW1iZXJzaGlwX3R5cGVzIiwicGF0Y2g6cmVsYXRpb25zaGlwcyIsInBvc3Q6YnVzaW5lc3NlcyIsInBvc3Q6bWVtYmVycyIsInBvc3Q6bWVtYmVyc2hpcF90eXBlcyIsInBvc3Q6cmVsYXRpb25zaGlwcyJdfQ.pBQIR3fiZx0m7mRF9KKi4BeeQYvVGdbJxLD3Rxww9nTQQLdhp1c9LZ2iSD9pSrkaSUL6UYUiqu_4XHdNqCiU2hx_n4YLM9OtIQeWDmj4cojCaGyODmsN5Eg_ZaUq5YQHZQeIYPJ_uA2q_70rbSAw5iEUV9-yFhfzRxBfzha0vXKPRPIKNfXebZsrFwdrvHx762zhV2hdLXrIALZBzJZprxp0uIP6emCH0cGAH7T_97M3i6-eWGLWiKFl3R-F8m5ERprWK__So1H3030p6etI5TgFr-GJEy3sSYRXMgz46G8olhdf6iQXzTSUF53bjFPKNr3Vot2cxF-tl1S6W2kmvg

####JSON for the standard viewer role is: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVkcG1KTDJwLXd4WnFKdVNIVHAwXyJ9.eyJpc3MiOiJodHRwczovL2NwcmVzb3VyY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVmZjBjYmMwNTY5NmFlMDA3MTJlYmVkYiIsImF1ZCI6Im12cl9hcGkiLCJpYXQiOjE2MTQwNDYyNDIsImV4cCI6MTYxNDA1MzQ0MiwiYXpwIjoiRzNxWHBkUDNuSmNmdTB4RUJ6M2lCTWhLYzhuaDkzWmgiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpidXNpbmVzc2VzIiwiZ2V0Om1lbWJlcnMiLCJnZXQ6bWVtYmVyc2hpcF90eXBlcyIsImdldDpyZWxhdGlvbnNoaXBzIl19.aVqBZMwVodE5KCdPLsTPiuSrN1l0HGibNKD0YGsOESZ74IBGt9CqpsaPp9l6HpVj8E0bPgb0DNrLC8E_H5LuWEEElP90Sk0Z_ov-Hzp8yt9PgZAuP7dOXpqBAJZ7LFKhmjhuFCEWR1-pSUbgdGqFjMfuyxrKo4H315bkwopZMWFqjywSEtGySjvza-ISKI7o2yC-bnlrdjpmWqJML0_nF4kpTgAVLN-t5OdZp1eF9ef__3QSw9fQFTdljFODw6mJgzcMquQTlVwlUsxTXSwFKJwxHe_zbSMGK-ZIv99FHrluzfyNvbdkNrJ5R3TmfxExxESw6lBkQ3c0yPvfoVB_Bg

####The application is currently live at:
https://mostvaluableresource.herokuapp.com

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### PIP Dependencies

Once you have your virtual environment setup and running, install
 dependencies by navigating to the directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.y
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the
file to find the application. 

```
Endpoints
GET '/businesses'
POST '/businesses/add'
PATCH '/businesses/1'
DELETE '/businesses/1'

GET '/members'
POST '/members/add'
PATCH '/members/1'
DELETE '/members/1'

GET '/relationships'
POST '/relationships/add'
PATCH '/relationships/1'
DELETE '/relationships/1'

GET '/relationships/types'
POST '/relationships/types/add'
PATCH '/relationships/types/1'
DELETE '/relationships/types/1'


GET '/businesses'
- Fetches an array of the businesses
- Request Arguments: None
- Returns: An object with an array of all businesses. 

            "businesses": [
                "added": "Fri, 19 Feb 2021 21:20:10 GMT",
                "description": "Business Description",
                "id": 10,
                "name": "Business Name"
            ], 
            "success": True,
        })
POST '/businesses/add'
- Adds a new business to the businesses table.
- Request Arguments: name, description
- Returns: An object with an array of all businesses. 

            "businesses": [
                "added": "Fri, 19 Feb 2021 21:20:10 GMT",
                "description": "Business Description",
                "id": 10,
                "name": "Business Name"
            ], 
            "success": True,
        })
PATCH '/businesses/1'
- Updates a specified business in the business table..
- Request Arguments: name, description, id
- Returns: An object with the business that ws updated. 

            "updated": [
                "added": "Fri, 19 Feb 2021 21:20:10 GMT",
                "description": "Business Description",
                "id": 10,
                "name": "Business Name"
            ], 
            "success": True,
        })
DELETE '/businesses/1'
- Removes a business from the businesses table.
- Request Arguments: id
- Returns: An object with an array of the business that was deleted. 

            "businesses": [
                "added": "Fri, 19 Feb 2021 21:20:10 GMT",
                "description": "Business Description",
                "id": 10,
                "name": "Business Name"
            ], 
            "success": True,
        })
GET '/members'
- Gets a list of the members that exist in the members table. 
- Request Arguments: None
- Returns: An object with an array of all members. 

            "members": [
        {
            "address": "Address, NC",
            "email_address": "email@gmail.com",
            "id": 2,
            "name": "first_name last_name",
            "phone": "333-333-3333"
        }
            ], 
            "success": True,
        })
POST '/members/add'
- Adds a new member to the members table. 
- Request Arguments: first_name, last_name, address, city, state, phone
, email_address
- Returns: An object with an array of the member that was added. 

            "new_member": [
        {
            "address": "Address, NC",
            "email_address": "email@gmail.com",
            "id": 2,
            "name": "first_name last_name",
            "phone": "333-333-3333"
        }
            ], 
            "success": True,
        })
PATCH '/members/1'
- Gets a list of the members that exist in the members table. 
- Request Arguments: id, first_name, last_name, address, city, state
, phone, email_address
- Returns: An object with an array of the updated member. 

            "updated": [
        {
            "address": "Address, NC",
            "email_address": "email@gmail.com",
            "id": 2,
            "name": "first_name last_name",
            "phone": "333-333-3333"
        }
            ], 
            "success": True,
DELETE '/members/1'
- Removes a specified member from the members table. 
- Request Arguments: id
- Returns: An object with an array of the member that was deleted. 

            "deleted": [
        {
            "address": "Address, NC",
            "email_address": "email@gmail.com",
            "id": 2,
            "name": "first_name last_name",
            "phone": "333-333-3333"
        }
            ], 
            "success": True,
        })
GET '/relationships'
- Gets a list of the relationships that exist in the relationships table. 
- Request Arguments: None
- Returns: An object with an array of all relationships. 

            "relationships": [
        {
            "active": true,
            "business_id": 3,
            "date_added": "Sun, 14 Feb 2021 14:51:08 GMT",
            "id": 1,
            "member_id": 1,
            "membership_type_id": 3
        }
            ], 
            "success": True,
        })
POST '/relationships/add'
- Create a new relationship between the business and the member in the
 rleationships table. 
- Request Arguments: active, business_id, member_id, membership_type_id
- Returns: An object with an array of the relationship that was created. 

            "new_relationship": [
        {
            "active": true,
            "business_id": 3,
            "date_added": "Sun, 14 Feb 2021 14:51:08 GMT",
            "id": 1,
            "member_id": 1,
            "membership_type_id": 3
        }
            ], 
            "success": True,
        })
PATCH '/relationships/1'
- Updates a specified relationship in the relationship table. 
- Request Arguments: id, business_id, member_id, membership_type_id
- Returns: An object with relationships that was updated. 

            "updated": [
        {
            "active": true,
            "business_id": 3,
            "date_added": "Sun, 14 Feb 2021 14:51:08 GMT",
            "id": 1,
            "member_id": 1,
            "membership_type_id": 3
        }
            ], 
            "success": True,
        })
DELETE '/relationships/id'
- Deletes a specified relationship from the relationship table.  
- Request Arguments: id
- Returns: An object with the relationship that was deleted.  

            "deleted": [
        {
            "active": true,
            "business_id": 3,
            "date_added": "Sun, 14 Feb 2021 14:51:08 GMT",
            "id": 1,
            "member_id": 1,
            "membership_type_id": 3
        }
            ], 
            "success": True,
        })
