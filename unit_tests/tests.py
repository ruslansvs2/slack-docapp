import sys
sys.path.append('./')
from app import app
import unittest


class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_add(self):
        rv = self.app.post('/add', data = { 'token':'111', 'text':'test data' })
        #print(rv.data)
        assert rv.status == '200 OK'
        #assert b'data' in rv.data

    def test_doc(self):
        rv = self.app.post('/doc', data = { 'token':'111', 'text':'test' })
        #print(rv.data)
        assert rv.status == '200 OK'
        #assert b' data' == rv.data
        self.assertEqual(b' data', rv.data)
        #assert False

if __name__ == '__main__':
    unittest.main()
