import unittest
import json
from flask import request, jsonify
from myservice.app import app as tested_app


class TestApp2(unittest.TestCase):

    def test1(self):  # allpolls
        app = tested_app.test_client()

        reply = app.get('/calc/sum?m=1&n=2')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body['result'], '3')

        reply = app.get('/calc/diff?m=1&n=2')
        body = json.loads(str(reply.data, 'utf8'))
        self.assertEqual(body['result'], '-1')
