import os
from flask import Flask, request, abort, jsonify
from models import setup_db, Business, Member, Member_Relationship
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
        print(body)
        if not request.get_json():
            abort(400)

        name = body['name']
        description = body['description']
        date_added = datetime.today()

        business = Business(name=name, description=description,
                            date_added=date_added)

        Business.insert(business)

        return jsonify({
            'success': True,
            'new_business': business.format()
        })

    @app.route('/businesses/<int:business_id>', methods=['DELETE'])
    def delete_business(business_id):
        business = Business.query.filter(Business.id == business_id).one_or_none()

        if business is None:
            abort(404)

        business.delete()

        return jsonify({
            'success': True,
            'deleted': business.format()
        })

    @app.route('/businesses/<int:business_id>', methods=['PATCH'])
    def update_business(business_id):
        body = request.get_json()
        print(body)

        name = body['name']
        description = body['description']

        business = Business.query.filter(Business.id == business_id).one_or_none()

        if business is None:
            abort(404)
        else:
            business.name = name
            business.description = description
            business.update()

        return jsonify({
            'success': True,
            'business': business.format()
        })

    @app.route('/members', methods=['GET'])
    def get_members():
        members = Member.query.all()
        formatted_members = [member.format() for member in
                               members]

        return jsonify({
            'success': True,
            'members': formatted_members
        })

    @app.route('/members/add', methods=['POST'])
    def add_member():
        body = request.get_json()
        if not request.get_json():
            abort(400)
        # TODO: check to ensure that the member does not already exist.
        date_added = datetime.today()
        first_name = body['first_name']
        last_name = body['last_name']
        address = body['address']
        city = body['city']
        state = body['state']
        phone = body['phone']
        email_address = body['email_address']

        member = Member(first_name=first_name, last_name=last_name,
                        address=address, city=city, state=state,
                        phone=phone, email_address=email_address,
                        date_added=date_added)

        Member.insert(member)

        return jsonify({
            'success': True,
            'member': member.format()
        })

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