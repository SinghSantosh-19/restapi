import unittest
import json
import requests

class TestRequest(unittest.TestCase):
    def test_add_product(self):
        r = {"name": "cake"}
        x = requests.post('http://127.0.0.1:5000/product/',data=r).json()
        self.assertEqual(r['name'], json.loads(x)['name'], "Name returned should be cake")

    def test_add_purchser(self):
        r = {"name": "bob"}
        x = requests.post('http://127.0.0.1:5000/purchaser/',data=r).json()
        self.assertEqual(r['name'], json.loads(x)['name'], "Name returned should be bob")

    def test_add_transaction(self):
        r = {"purchaser-id":1, "product-id":4, "purchased-timestamp":'2019/08/27 10:00:00'}
        i = {"transaction_id": 4, "created_timestamp": "2019-08-27T10:00:00"}
        x = requests.post('http://127.0.0.1:5000/purchaser-product/',data=r).json()
        #self.assertEqual(r['name'], json.loads(x)['name'], "Name returned should be bob")
        self.assertDictEqual(i, json.loads(x), "Transaction id should be 4 and timestamp 2019-08-27T10:00:00")

    def test_get_result_all(self):
        x = requests.get('http://127.0.0.1:5000/purchaser/1/product/').json()
        self.assertEqual(3, len(json.loads(x)["purchases"]), "Should have returned 3 dates")

    def test_get_result_between_dates(self):
        i = {'start_date':'2019/08/27 09:00:00', 'end_date':'2019/08/28 09:00:00'}
        x = requests.get('http://127.0.0.1:5000/purchaser/1/product/', data=i).json()
        self.assertEqual(2, len(json.loads(x)["purchases"]), "Should have returned 2 dates")


if __name__ == '__main__':
    unittest.main()
