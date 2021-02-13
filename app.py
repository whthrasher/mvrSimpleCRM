import os
from flask import Flask, request, abort, jsonify
from models import setup_db, Business, Member, Customer_Relationship
from flask_cors import CORS
from datetime import datetime

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def get_greeting():
        greeting = "Hello"
        return greeting

    @app.route('/businesses', methods=['GET'])
    def get_businesses():
        businesses = Business.query.all()
        formatted_businesses = [business.format() for business in
                               businesses]

        return jsonify({
            'success': True,
            'businesses': formatted_businesses
        })


    @app.route('/businesses/add', methods=['POST'])
    def add_business():
        body = request.get_json()
        if not request.get_json():
            abort(400)

        name = body['name']
        description = body['description']
        date_added = datetime.today()

        business = Business(name=name, description=description,
                            date_added=date_added)

        Business.insert(business)

        # TODO: return the id of the business that was just created in
        #  the response.
        return jsonify({
            'success': True
        })

    @app.route('/businesses/<business_id>/remove', methods=['DELETE'])
    def delete_business(business_id):
        business = Business.query.get(business_id)

        # TODO: Add more specific error handling for this error.
        if business is None:
            abort(404)
        business.delete()

        return jsonify({
            'success': True,
            'deleted': business_id
        })

    # TODO: implement the update endpoint for the business.
    @app.route('/businesses/<business_id>/update', methods=['PATCH'])
    def update_business(business_id):
        business = Business.get(business_id)
        jsonify({
            'success': True,
            'business': business
        })

    # TODO: implement the create endpoint for the member.
    @app.route('/members/add', methods=['POST'])
    def add_member():
        body = request.get_json()

        if not request.get_json():
            abort(400)

        first_name = body['first_name']
        last_name = body['last_name']
        membership_type = body['membership_type']
        address = body['address']
        city = body['city']
        state = body['state']
        phone = body['phone']
        email_address = body['email_address']

        member = Member(first_name=first_name, last_name=last_name,
                            membership_type=membership_type,
                        address=address, city=city, state=state,
                        phone=phone, email_address=email_address)

        Member.insert(member)

    # TODO: implement the remove endpoint for the customer.
    @app.route('/members/<member_id>/remove', methods=['DELETE'])
    def delete_member():
        return "Update a business here"

    # TODO: implement the update endpoint for the customer.
    @app.route('/members/<member_id>/update', methods=['PATCH'])
    def update_member():
        return "Update a business here"

    # TODO: implement the create endpoint for the business/customer
    #  relationship.
    @app.route('/relationships/create', methods=['POST'])
    def create_relationship():
        return "Create a customer business relationship here"

    # TODO: implement the delete endpoint for the business/customer
    #  relationship.
    @app.route('/relationships/<customer_id>/remove', methods=['DELETE'])
    def delete_relationship():
        return "Update a customer business relationship here"

    # TODO: implement the update method for the business/customer
    #  relationship.
    @app.route('/relationships/<customer_id>/update', methods=['PATCH'])
    def update_relationship():
        return "Update a customer business relationship here"

    # TODO: implement the error handling for this application.

    return app

app = create_app()

if __name__ == '__main__':
    app.run()