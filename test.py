import unittest
import json
from main import app

class FlaskApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def testSuma_ShouldReturn_IntFive(self):
        response = self.app.get("/suma?a=2&b=3")
        data = json.loads(response.data)
        self.assertEqual(data.get("result", 0), 5)

    def testProduct_ShouldReturn_IntSix(self):
        response = self.app.get("/multiplica?a=2&b=3")
        data = json.loads(response.data)
        self.assertEqual(data.get("result", 0), 6)

if __name__ == "__main__":
    unittest.main()
