# from .test_person_test import TestPerson
# from fastapi.testclient import TestClient
# from .test_person_test import database, client
# # class TestGetPerson(TestPerson):
# #     def test_get_person(self):
# #         response = self.client.get("/api/person/")
# #         self.assertEqual(response.status_code, 200)
# #         self.assertEqual(response.json(), [])

# def test_get_person(database, client):
#     response = client.get("/api/person/")
#     assert response.status_code == 200
#     assert response.json() == []
