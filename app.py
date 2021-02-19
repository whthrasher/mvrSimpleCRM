import os
from flask import Flask, \
    request, \
    abort, \
    jsonify, \
    redirect
from models import \
    setup_db, \
    Business, \
    Member, \
    Member_Relationship, Membership_Type
from flask_cors import CORS
from datetime import datetime
from auth.auth import AuthError, requires_auth


# TODO: Implement the OAuth authentication for this application
# TODO: Implement the frontend for this application
# TODO: Create Readme for this API
# TODO: Create the tests for this API
# TODO: Create the Heroku Code Pipeline for this application
# TODO: Add pagination when all of the members or businesses are returned
# TODO: Ensure that all of the information that is transferred is secure

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

    @app.route('/login')
    def auth0_redirect():
        AUTH0_AUTHORIZE_URL = os.environ['AUTH0_AUTHORIZE_URL']
        print(AUTH0_AUTHORIZE_URL)
        return redirect(AUTH0_AUTHORIZE_URL)

#-------------------
# Business Endpoints
#-------------------

    @app.route('/businesses', methods=['GET'])
    @requires_auth('get:businesses')
    def get_businesses(payload):
        businesses = Business.query.all()
        formatted_businesses = [business.format() for business in
                               businesses]

        return jsonify({
            'success': True,
            'businesses': formatted_businesses
        })
    @app.route('/businesses/<int:business_id>', methods=['GET'])
    @requires_auth('get:businesses')
    def get_business(business_id, payload):
        business = Business.query.filter(Business.id == business_id).one_or_none()

        if business is None:
            abort(404)

        return jsonify({
            'success': True,
            'business': business.format()
        })

    @app.route('/businesses/add', methods=['POST'])
    @requires_auth('post:businesses')
    def add_business(payload):
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
            'success': True,
            'new_business': business.format()
        })

    @app.route('/businesses/<int:business_id>', methods=['DELETE'])
    @requires_auth('delete:businesses')
    def delete_business(business_id, payload):
        business = Business.query.filter(Business.id == business_id).one_or_none()

        if business is None:
            abort(404)

        business.delete()

        return jsonify({
            'success': True,
            'deleted': business.format()
        })

    @app.route('/businesses/<int:business_id>', methods=['PATCH'])
    @requires_auth('patch:businesses')
    def update_business(business_id, payload):
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

# -------------------
# Members Endpoints
# -------------------
    @app.route('/members', methods=['GET'])
    @requires_auth('get:members')
    def get_members(payload):
        members = Member.query.all()
        formatted_members = [member.format() for member in
                               members]

        return jsonify({
            'success': True,
            'members': formatted_members
        })

    @app.route('/members/<int:member_id>', methods=['GET'])
    @requires_auth('get:members')
    def get_member(member_id, payload):
        member = Member.query.filter(Member.id == member_id).one_or_none()

        if member is None:
            abort(404)

        return jsonify({
            'success': True,
            'members': member.format()
        })

    @app.route('/members/add', methods=['POST'])
    @requires_auth('post:members')
    def add_member(payload):
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
    @requires_auth('delete:members')
    def delete_member(member_id, payload):
        member = Member.query.filter(Member.id == member_id).one_or_none()

        if member is None:
            abort(404)

        member.delete()

        return jsonify({
            'success': True,
            'deleted': member.format()
        })

    @app.route('/members/<int:member_id>', methods=['PATCH'])
    @requires_auth('patch:members')
    def update_member(member_id, payload):
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

# -------------------
# Relationships Endpoints
# -------------------
    @app.route('/relationships/add', methods=['POST'])
    @requires_auth('post:relationships')
    def create_relationship(payload):
        body = request.get_json()

        if not request.get_json():
            abort(400)

        business_id = body['business_id']
        member_id = body['member_id']
        active = body['active']
        membership_type_id = body['membership_type_id']

        member_relationship = Member_Relationship(business_id=business_id,
                                                  member_id=member_id,
                                                  active=active,
                                                  membership_type_id=membership_type_id
                                                  )

        Member_Relationship.insert(member_relationship)

        return jsonify({
            'success': True,
            'member': member_relationship.format()
        })

    @app.route('/relationships/<int:relationship_id>', methods=['DELETE'])
    @requires_auth('delete:relationships')
    def delete_relationship(relationship_id, payload):
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
    @requires_auth('get:relationships')
    def get_relationships(payload):
        member_relationships = Member_Relationship.query.all()
        formatted_relationships = [member_relationship.format() for
                                   member_relationship in
                                   member_relationships]

        return jsonify({
            'success': True,
            'relationships': formatted_relationships
        })

    @app.route('/relationships/<int:relationship_id>', methods=['GET'])
    @requires_auth('get:relationships')
    def get_relationship(relationship_id, payload):
        member_relationship = Member_Relationship.query.filter(
            Member_Relationship.id == relationship_id).one_or_none()

        if member_relationship is None:
            abort(404)

        return jsonify({
            'success': True,
            'relationships': member_relationship.format()
        })

    @app.route('/relationships/<int:relationship_id>', methods=['PATCH'])
    @requires_auth('patch:businesses')
    def update_relationship(relationship_id, payload):
        body = request.get_json()
        if 'business_id' in body:
            business_id = body['business_id']
        if 'member_id' in body:
            member_id = body['member_id']
        if 'active' in body:
            active = body['active']
        if 'membership_type_id' in body:
            membership_type_id = body['membership_type_id']

        member_relationship = Member_Relationship.query.filter(
            Member_Relationship.id == relationship_id).one_or_none()

        if member_relationship is None:
            abort(404)

        else:
            if 'business_id' in body:
                member_relationship.business_id = business_id
            if 'member_id' in body:
                member_relationship.member_id = member_id
            if 'active' in body:
                member_relationship.active = active
            if 'membership_type_id' in body:
                member_relationship.membership_type_id = membership_type_id

            member_relationship.update()

        return jsonify({
            'success': True,
            'updated': member_relationship.format()
        })

# -------------------
# Membership Types Endpoints
# -------------------
    @app.route('/memberships/types/add', methods=['POST'])
    @requires_auth('post:membership_types')
    def add_membership_type(payload):
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

    @app.route('/memberships/types/<int:membership_type_id>', methods=[
        'PATCH'])
    @requires_auth('patch:membership_types')
    def update_membership_type(membership_type_id, payload):
        body = request.get_json()
        if 'name' in body:
            name = body['name']
        if 'description' in body:
            description = body['description']
        if 'active' in body:
            active = body['active']

        membership_type = Membership_Type.query.filter(
            Membership_Type.id == membership_type_id).one_or_none()

        if membership_type is None:
            abort(404)

        else:
            if 'name' in body:
                membership_type.name = name
            if 'description' in body:
                membership_type.description = description
            if 'active' in body:
                membership_type.active = active

            membership_type.update()

        return jsonify({
            'success': True,
            'updated': membership_type.format()
        })

    @app.route('/memberships/types', methods=['GET'])
    @requires_auth('get:membership_types')
    def get_membership_types(payload):
        membership_types = Membership_Type.query.all()
        formatted_types = [membership_type.format() for
                                   membership_type in
                                   membership_types]

        return jsonify({
            'success': True,
            'membership_types': formatted_types
        })

    @app.route('/memberships/types/<int:membership_type_id>', methods=[
        'GET'])
    @requires_auth('get:membership_types')
    def get_membership_type(membership_type_id, payload):
        membership_type = Membership_Type.query.filter(
            Membership_Type.id == membership_type_id).one_or_none()

        if membership_type is None:
            abort(404)

        return jsonify({
            'success': True,
            'membership_types': membership_type.format()
        })

    @app.route('/memberships/types/<int:membership_type_id>', methods=[
        'DELETE'])
    @requires_auth('delete:membership_types')
    def delete_membership_type(membership_type_id, payload):
        membership_type = Membership_Type.query.filter(
            Membership_Type.id == membership_type_id).one_or_none()

        if membership_type is None:
            abort(404)

        membership_type.delete()

        return jsonify({
            'success': True,
            'deleted': membership_type.format()
        })

    return app

app = create_app()

if __name__ == '__main__':
    app.run()