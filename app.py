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

        return jsonify({
            'success': True
        })



    @app.route('/businesses/<business_id>/remove', methods=['DELETE'])
    def delete_business():
        return "Delete a business here"

    @app.route('/businesses/<business_id>/update', methods=['PATCH'])
    def update_business():
        return "Update a business here"

    @app.route('/customers/create', methods=['POST'])
    def create_customer():
        return "Create a customer here"

    @app.route('/customers/<customer_id>/remove', methods=['DELETE'])
    def delete_customer():
        return "Update a business here"

    @app.route('/customers/<customer_id>/update', methods=['PATCH'])
    def update_customer():
        return "Update a business here"

    @app.route('/relationships/create', methods=['POST'])
    def create_relationship():
        return "Create a customer business relationship here"

    @app.route('/relationships/<customer_id>/remove', methods=['DELETE'])
    def delete_relationship():
        return "Update a customer business relationship here"

    @app.route('/relationships/<customer_id>/update', methods=['PATCH'])
    def update_relationship():
        return "Update a customer business relationship here"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()