# Most Valuable Resource Simple CRM
## Motivation For Project
My wife runs a small business and I wanted to create a simple CRM that
 she can use to keep up with her customers. 
## Getting Started
###Authentication

####JSON for the admin role is: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVkcG1KTDJwLXd4WnFKdVNIVHAwXyJ9.eyJpc3MiOiJodHRwczovL2NwcmVzb3VyY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImNjeTI2M0tsM3A5bkI2SVE2SGpEVDZQbDVuMHNqajI4QGNsaWVudHMiLCJhdWQiOiJtdnJfYXBpIiwiaWF0IjoxNjE1ODU3NTAzLCJleHAiOjE2MTU5NDM5MDMsImF6cCI6ImNjeTI2M0tsM3A5bkI2SVE2SGpEVDZQbDVuMHNqajI4Iiwic2NvcGUiOiJnZXQ6YnVzaW5lc3NlcyBnZXQ6bWVtYmVycyBnZXQ6cmVsYXRpb25zaGlwcyBnZXQ6bWVtYmVyc2hpcF90eXBlcyBwb3N0OmJ1c2luZXNzZXMgcG9zdDptZW1iZXJzIHBvc3Q6cmVsYXRpb25zaGlwcyBwb3N0Om1lbWJlcnNoaXBfdHlwZXMgcGF0Y2g6bWVtYmVycyBwYXRjaDpyZWxhdGlvbnNoaXBzIHBhdGNoOmJ1c2luZXNzZXMgcGF0Y2g6bWVtYmVyc2hpcF90eXBlcyBkZWxldGU6YnVzaW5lc3NlcyBkZWxldGU6bWVtYmVycyBkZWxldGU6cmVsYXRpb25zaGlwcyBkZWxldGU6bWVtYmVyc2hpcF90cGVzIGRlbGV0ZTptZW1iZXJzaGlwX3R5cGVzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmJ1c2luZXNzZXMiLCJnZXQ6bWVtYmVycyIsImdldDpyZWxhdGlvbnNoaXBzIiwiZ2V0Om1lbWJlcnNoaXBfdHlwZXMiLCJwb3N0OmJ1c2luZXNzZXMiLCJwb3N0Om1lbWJlcnMiLCJwb3N0OnJlbGF0aW9uc2hpcHMiLCJwb3N0Om1lbWJlcnNoaXBfdHlwZXMiLCJwYXRjaDptZW1iZXJzIiwicGF0Y2g6cmVsYXRpb25zaGlwcyIsInBhdGNoOmJ1c2luZXNzZXMiLCJwYXRjaDptZW1iZXJzaGlwX3R5cGVzIiwiZGVsZXRlOmJ1c2luZXNzZXMiLCJkZWxldGU6bWVtYmVycyIsImRlbGV0ZTpyZWxhdGlvbnNoaXBzIiwiZGVsZXRlOm1lbWJlcnNoaXBfdHBlcyIsImRlbGV0ZTptZW1iZXJzaGlwX3R5cGVzIl19.MktqKK5u57cU9A2Lu20Hv7KwLm9nmrOuB7ebFvyVnaJF0jnoi3aHNGEd-2q98a2aqH4598JYGE3gx9XRW5XKAT4MP51mLrSlKoPDvXrjkb2Tv2LTZWII7nef9x7EDnrlYWuaCMgJ0IH-jayeEXlIryvJQXFEP3n5ae4Kf6aP26wo_r1HCjITi8jsidLRcp8KCDI50wLj7VtNhHXQPo7FBaFA7dXoBiZJyn2rfnkgf56zYHkgBLlHtcRMevfS4_jZq2wIg-ZPD5DB2l1a2uLcI1X6deW-NthFYP3YmKOBDJh9YxJvDgmH4WMyDNLTckziR-5JnHcncAed93YPB1Vmmg
#####Permissions for the admin role includes: 
* delete:business
* delete:members
* delete:membership_types
* delete:relationships
* get:businesses
* get:members
* get:membership_types
* get:relationships
* patch:businesses
* patch:members
* patch:membership_types
* patch:relationship
* post:businesses
* post:members
* post:membership_types
* post:relationships

####JSON for the standard viewer role is: 
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVkcG1KTDJwLXd4WnFKdVNIVHAwXyJ9.eyJpc3MiOiJodHRwczovL2NwcmVzb3VyY2UudXMuYXV0aDAuY29tLyIsInN1YiI6ImFTQjZXUzZNdlNsYjYwRVBmY3ZOOFV0c0xCZnAzRGhZQGNsaWVudHMiLCJhdWQiOiJtdnJfYXBpIiwiaWF0IjoxNjE1ODU3NDUyLCJleHAiOjE2MTU5NDM4NTIsImF6cCI6ImFTQjZXUzZNdlNsYjYwRVBmY3ZOOFV0c0xCZnAzRGhZIiwic2NvcGUiOiJnZXQ6YnVzaW5lc3NlcyBnZXQ6bWVtYmVycyBnZXQ6cmVsYXRpb25zaGlwcyBnZXQ6bWVtYmVyc2hpcF90eXBlcyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDpidXNpbmVzc2VzIiwiZ2V0Om1lbWJlcnMiLCJnZXQ6cmVsYXRpb25zaGlwcyIsImdldDptZW1iZXJzaGlwX3R5cGVzIl19.dwDRAskGbuH0D6iKZDLsZPUOE_Tfm1-hiPf0OqfZK1yTJv1aCvAWEVFAHV0qKK9e84-eI2iNt61TwBawJ9cgYcvh3VT1yhlawGmumsP-Fv3WQhcRLSHiQWiy8olL7BKV2Yy19kHrIIB0EXHJLrbm5u4e_YVAoo5V0dvhPTIXp1_0fDAQaTMyGh47FlYJgYXmnc1EOPAY8TZjJ2da52E8UPlgdUigud3BSbH26AUyRQ7m-sJzlesgSzT0cI4eSlc28HxfixzQa-GZwnT9WOIoRa5WyNFe3otHKjQcz9HuxLcXUSyjpHrS6XhvL7m8T2Ve6-C72p290Q-J5f9TQFla-w
#####Permissions for the standard viewer role includes: 
* get:businesses
* get:members
* get:membership_types
* get:relationships

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
