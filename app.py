import os
from flask import Flask, request, abort, jsonify
from models import \
    setup_db, \
    Business, \
    Member, \
    Member_Relationship, Membership_Type
from flask_cors import CORS
from datetime import datetime

# TODO: Implement the OAuth authentication for this application
# TODO: Implement the frontend for this application
# TODO: Create Readme for this API
# TODO: Create the tests for this API
# TODO: Create the Heroku Code Pipeline for this application
# TODO: Add pagination when all of the members or businesses are returned
# TODO: Ensure that all of the information that is transferred is secure
# TODO: Add a GET request for each endpoint to access the individual id
# TODO: Make sure that there are no print items that will reveal
#  important information into the logs.

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

        if 'name' in body:
            name = body['name']
        if 'description' in body:
            description = body['description']

        business = Business.query.filter(Business.id == business_id).one_or_none()

        if business is None:
            abort(404)
        else:
            if 'name' in body:
                business.name = name
            if 'description' in body:
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

    @app.route('/members/<int:member_id>', methods=['DELETE'])
    def delete_member(member_id):
        member = Member.query.filter(Member.id == member_id).one_or_none()

        if member is None:
            abort(404)

        member.delete()

        return jsonify({
            'success': True,
            'deleted': member.format()
        })

    @app.route('/members/<int:member_id>', methods=['PATCH'])
    def update_member(member_id):
        body = request.get_json()
        address_in_dict = 'address' in body
        if 'first_name' in body:
            first_name = body['first_name']
        if 'last_name' in body:
            last_name = body['last_name']
        if 'address' in body:
            address = body['address']
        if 'city' in body:
            city = body['city']
        if 'state' in body:
            state = body['state']
        if 'phone' in body:
            phone = body['phone']
        if 'email_address' in body:
            email_address = body['email_address']

        member = Member.query.filter(
        Member.id == member_id).one_or_none()

        if member is None:
            abort(404)

        else:
            if 'first_name' in body:
                member.first_name = first_name
            if 'last_name' in body:
                member.last_name = last_name
            if 'address' in body:
                member.address = address
            if 'city' in body:
                member.city = city
            if 'state' in body:
                member.state = state
            if 'phone' in body:
                member.phone = phone
            if 'email_address' in body:
                member.email_address = email_address

            member.update()

        return jsonify({
            'success': True,
            'updated': member.format()
        })

    @app.route('/relationships/add', methods=['POST'])
    def create_relationship():
        body = request.get_json()

        if not request.get_json():
            abort(400)

        business_id = body['business_id']
        member_id = body['member_id']
        active = body['active']
        membership_type = body['membership_type']

        member_relationship = Member_Relationship(business_id=business_id,
                                                  member_id=member_id,
                                                  active=active,
                                                  membership_type=membership_type
                                                  )

        Member_Relationship.insert(member_relationship)

        return jsonify({
            'success': True,
            'member': member_relationship.format()
        })

    @app.route('/relationships/<int:relationship_id>', methods=['DELETE'])
    def delete_relationship(relationship_id):
        member_relationship = Member_Relationship.query.filter(
            Member_Relationship.id == relationship_id).one_or_none()

        if member_relationship is None:
            abort(404)

        member_relationship.delete()

        return jsonify({
            'success': True,
            'deleted': member_relationship.format()
        })

    @app.route('/relationships', methods=['GET'])
    def get_relationships():
        member_relationships = Member_Relationship.query.all()
        formatted_relationships = [member_relationship.format() for
                                   member_relationship in
                                   member_relationships]

        return jsonify({
            'success': True,
            'businesses': formatted_relationships
        })

    # TODO: implement the update method for the business/customer
    #  relationship.
    @app.route('/relationships/<customer_id>/update', methods=['PATCH'])
    def update_relationship():
        return "Update a customer business relationship here"

    @app.route('/memberships/types/add', methods=['POST'])
    def add_membership_type():
        body = request.get_json()

        if not request.get_json():
            abort(400)

        name = body['name']
        description = body['description']
        active = body['active']

        membership_type = Membership_Type(
            name=name,
            description=description,
            active=active,
            )

        Membership_Type.insert(membership_type)

        return jsonify({
            'success': True,
            'membership_type': membership_type.format()
        })
    # TODO: implement the error handling for this application.

    return app

app = create_app()

if __name__ == '__main__':
    app.run()