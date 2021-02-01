from app import app
from unittest import TestCase
from flask import session, request
from forex import Forex

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class appTestCase(TestCase):

    #test html data
    def test_html(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3 class="currency-heading">Currency Converter</h3>', html)
            self.assertIn('<div class="result_msg">', html)
            self.assertIn('<label for="amt_input">Amount to convert</label>', html)

    #test submissions
    def test_submission(self):
        with app.test_client() as client:
            res = client.get('?convert_from=AUD&convert_to=AUD&amt=')

            self.assertEqual(request.args['convert_from'], 'AUD')
            self.assertEqual(request.args['convert_to'], 'AUD')
            self.assertEqual(request.args['amt'], '')
             