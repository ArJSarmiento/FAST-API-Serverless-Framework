# from .test_person_test import client, database

# # class TestCreatePerson(TestPerson):
# #     def test_create_person(self):
# #         response = self.client.post("/api/person/", json=self.test_data)
# #         self.assertEqual(response.status_code, 200)
# #         self.assertTrue(all(person in response.json().items() for person in self.test_data.items()))

# #     def test_create_person_with_missing_data(self):
# #         missing_test_data = self.test_data.copy()
# #         missing_test_data.pop("firstName")
# #         response = self.client.post("/api/person/", json=missing_test_data)
# #         self.assertEqual(response.status_code, 422)

# #     def test_create_person_with_invalid_data_type(self):
# #         invalid_test_data = self.test_data.copy()
# #         invalid_test_data["firstName"] = 123
# #         response = self.client.post("/api/person/", json=invalid_test_data)
# #         self.assertEqual(response.status_code, 422)

# test_data = {
#             "firstName": "Arnel",
#             "lastName": "Sarmiento",
#             "preferredName": "Arnel Jan",
#             "dateOfBirth": "2021-12-01",
#             "gender": "Male",
#             "maritalStatus": "Single",
#             "mobileNumber": "+69123456789",
#             "homeEmail": "example@example.com",
#             "officeEmail": "example@example.com",
#             "homeAddress": "Example",
#             "officeAddress": "Example"
#         }

# def test_create_person(database, client):
#     response = client.post("/api/person/", json=test_data)
#     assert response.status_code == 200
#     assert all(person in response.json().items() for person in test_data.items())
#     # assertEqual(response.status_code, 200)
#     # assertTrue(all(person in response.json().items() for person in test_data.items()))

# def test_create_person_with_missing_data(database, client):
#     missing_test_data = test_data.copy()
#     missing_test_data.pop("firstName")
#     response = client.post("/api/person/", json=missing_test_data)
#     assert response.status_code == 422
#     # assertEqual(response.status_code, 422)

# def test_create_person_with_invalid_data_type(database, client):
#     invalid_test_data = test_data.copy()
#     invalid_test_data["firstName"] = 123
#     response = client.post("/api/person/", json=invalid_test_data)
#     assert response.status_code == 422
#     # assertEqual(response.status_code, 422)
