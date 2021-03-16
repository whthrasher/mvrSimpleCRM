import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import os
from app import create_app
from models import setup_db,\
    Business, \
    Member, \
    Membership_Type, \
    Member_Relationship


class mvrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ.get('DATABASE_URL')
        self.admin_account = os.environ.get('ADMIN_ACCOUNT')
        self.standard_account = os.environ.get('STANDARD_ACCOUNT')
        if not self.database_path:
            database_name = "test_mvrdb"
            database_path = "postgres://{}/{}".format(
                'localhost:5432', database_name)
        self.database_path = database_path

        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

        self.new_business = {
            "name": "name",
            "description": "description"
        }
        self.patch_business = {
            "name": "new name",
            "description": "new description"
        }
        self.new_member = {
            "first_name": "Firstname",
            "last_name": "Lastname",
            "address": "1971 Test Blvd",
            "city": "testcity",
            "state": "NC",
            "phone": "333-333-3333",
            "email_address": "test@test.copm"
        }
        self.patch_member = {
            "first_name": "new_Firstname",
            "last_name": "new_Lastname",
            "address": "1971 Test Blvd",
            "city": "testcity",
            "state": "NC",
            "phone": "333-333-3333",
            "email_address": "test@test.copm"
        }
        self.new_membership_type = {
                "name": "new membership",
                "description": "new membership description",
                "active": True
            }
        self.patch_membership_type = {
                "name": "new membership",
                "description": "new membership description",
                "active": False
            }

    def tearDown(self):
        pass

    def test_create_new_business(self):
        res = self.client().post('/businesses/add', headers={
                                 'Authorization': 'Bearer '
                                 + str(self.admin_account)},
                                 json=self.new_business)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_business_standard(self):
        res = self.client().post('/businesses/add', headers={
                                 'Authorization': 'Bearer '
                                 + str(self.standard_account)},
                                 json=self.new_business)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_new_member(self):
        res = self.client().post('/members/add', headers={
                                    'Authorization': 'Bearer '
                                    + str(self.admin_account)},
                                 json=self.new_member)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_member_standard(self):
        res = self.client().post('/members/add', headers={
                                    'Authorization': 'Bearer '
                                    + str(self.standard_account)},
                                 json=self.new_member)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_new_membership_type(self):
        res = self.client().post('/memberships/types/add', headers={
                                    'Authorization': 'Bearer '
                                    + str(self.admin_account)},
                                 json=self.new_membership_type)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_membership_type_standard(self):
        res = self.client().post('/memberships/types/add', headers={
                                    'Authorization': 'Bearer '
                                    + str(self.standard_account)},
                                 json=self.new_membership_type)

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_create_new_relationship(self):
        business = Business.query.first()
        member = Member.query.first()
        membership_type = Membership_Type.query.first()

        self.new_relationship = {
            "business_id": business.id,
            "member_id": member.id,
            "active": True,
            "membership_type_id": membership_type.id
        }

        res = self.client().post('/relationships/add', headers={
                                    'Authorization': 'Bearer '
                                    + str(self.admin_account)},
                                 json=self.new_relationship)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_new_relationship_standard(self):
        business = Business.query.first()
        member = Member.query.first()
        membership_type = Membership_Type.query.first()

        self.new_relationship = {
            "business_id": business.id,
            "member_id": member.id,
            "active": True,
            "membership_type_id": membership_type.id
        }

        res = self.client().post('/relationships/add', headers={
                                    'Authorization': 'Bearer '
                                    + str(self.standard_account)},
                                 json=self.new_relationship)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_get_businesses(self):
        res = self.client().get('/businesses',
                                headers={'Authorization': 'Bearer '
                                         + str(self.admin_account)})
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['businesses']))

    def test_get_businesses_standard(self):
        res = self.client().get('/businesses',
                                headers={'Authorization': 'Bearer '
                                         + str(self.standard_account)})
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['businesses']))

    def test_get_members(self):
        res = self.client().get('/members',
                                headers={'Authorization': 'Bearer '
                                         + str(self.admin_account)})
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['members']))

    def test_get_members_standard(self):
        res = self.client().get('/members',
                                headers={'Authorization': 'Bearer '
                                         + str(self.standard_account)})
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['members']))

    def test_get_membership_types(self):
        res = self.client().get('/memberships/types',
                                headers={'Authorization': 'Bearer '
                                         + str(self.admin_account)})
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['membership_types']))

    def test_get_membership_types_standard(self):
        res = self.client().get('/memberships/types',
                                headers={'Authorization': 'Bearer '
                                         + str(self.standard_account)})
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['membership_types']))

    def test_get_relationships(self):
        res = self.client().get('/relationships',
                                headers={'Authorization': 'Bearer '
                                         + str(self.admin_account)})
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['relationships']))

    def test_get_relationships_standard(self):
        res = self.client().get('/relationships',
                                headers={'Authorization': 'Bearer '
                                         + str(self.standard_account)})
        data = res.json

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['relationships']))

    def test_update_member(self):
        member = Member.query.first()
        res = self.client().patch('/members/' + str(member.id),
                                  headers={
                                            'Authorization': 'Bearer '
                                            + str(self.admin_account)},
                                  json=self.patch_member)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated']['name'],
                         'new_Firstname new_Lastname')

    def test_update_member_standard(self):
        member = Member.query.first()
        res = self.client().patch('/members/' + str(member.id),
                                  headers={
                                            'Authorization': 'Bearer '
                                            + str(self.standard_account)},
                                  json=self.patch_member)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_update_business(self):
        business = Business.query.first()
        res = self.client().patch('/businesses/' + str(business.id),
                                  headers={'Authorization': 'Bearer '
                                           + str(self.admin_account)},
                                  json=self.patch_business)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated']['name'],
                         'new name')
    def test_update_business_standard(self):
        business = Business.query.first()
        res = self.client().patch('/businesses/' + str(business.id),
                                  headers={'Authorization': 'Bearer '
                                           + str(self.standard_account)},
                                  json=self.patch_business)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_update_relationship(self):
        relationship = Member_Relationship.query.first()
        business = Business.query.first()
        member = Member.query.first()
        membership_type = Membership_Type.query.first()\

        self.patch_relationship = {
            "business_id": business.id,
            "member_id": member.id,
            "active": False,
            "membership_type_id": membership_type.id
        }

        res = self.client().patch('/relationships/' + str(
                                  relationship.id),
                                  headers={
                                           'Authorization': 'Bearer '
                                           + str(self.admin_account)},
                                  json=self.patch_relationship)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated']['active'],
                         False)

    def test_update_relationship_standard(self):
        relationship = Member_Relationship.query.first()
        business = Business.query.first()
        member = Member.query.first()
        membership_type = Membership_Type.query.first()\

        self.patch_relationship = {
            "business_id": business.id,
            "member_id": member.id,
            "active": False,
            "membership_type_id": membership_type.id
        }

        res = self.client().patch('/relationships/' + str(
                                  relationship.id),
                                  headers={
                                           'Authorization': 'Bearer '
                                           + str(self.standard_account)},
                                  json=self.patch_relationship)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_update_membership_type(self):
        membership_type = Membership_Type.query.first()
        res = self.client().patch('/memberships/types/' + str(
                                  membership_type.id),
                                  headers={'Authorization': 'Bearer '
                                           + str(self.admin_account)},
                                  json=self.patch_membership_type)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated']['active'], False)

    def test_update_membership_type_standard(self):
        membership_type = Membership_Type.query.first()
        res = self.client().patch('/memberships/types/' + str(
                                  membership_type.id),
                                  headers={'Authorization': 'Bearer '
                                           + str(self.standard_account)},
                                  json=self.patch_membership_type)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_relationship(self):
        relationship = Member_Relationship.query.first()
        res = self.client().delete('/relationships/' + str(
                                    relationship.id), headers={
                                    'Authorization': 'Bearer '
                                    + str(self.admin_account)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_relationship_standard(self):
        relationship = Member_Relationship.query.first()
        res = self.client().delete('/relationships/' + str(
                                    relationship.id), headers={
                                    'Authorization': 'Bearer '
                                    + str(self.standard_account)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

    def test_delete_business(self):
        business = Business.query.first()
        res = self.client().delete('/businesses/' + str(business.id),
                                   headers={
                                    'Authorization': 'Bearer '
                                    + str(self.admin_account)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_business_standard(self):
        business = Business.query.first()
        res = self.client().delete('/businesses/' + str(business.id),
                                   headers={
                                    'Authorization': 'Bearer '
                                    + str(self.standard_account)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)

if __name__ == "__main__":
    unittest.main()
