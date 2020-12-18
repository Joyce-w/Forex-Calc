from app import app
from unittest import TestCase
from flask import session, request
from forex import Forex

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class appTestCase(TestCase):
    
    #test session 
    def test_session(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['convert_from'] = 'USD'
                change_session['convert_to'] = 'AUD'
                change_session['convert_amt'] = 1

            res = client.get("/")

            self.assertEqual(res.status_code, 200)
            self.assertEqual(session['convert_from'], 'USD')
            self.assertEqual(session['convert_to'], 'AUD')

    #test html data
    def test_html(self):
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h3 class="currency-heading">Currency Converter</h3>', html)
            self.assertIn('<div class="result_msg">', html)

    #test submissions
    def test_submission(self):
        with app.test_client() as client:
            res = client.get('?convert_from=AUD&convert_to=AUD&amt=')
            self.assertEqual(request.args['convert_from'], 'AUD')
            self.assertEqual(request.args['convert_to'], 'AUD')
            self.assertEqual(request.args['amt'], '')
            
            print(dir(res))