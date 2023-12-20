import unittest
import requests

class WeatherTestCase(unittest.TestCase):
    def test_call_view_weather(self):
        response = requests.get('http://127.0.0.1:8000/api/weather?city=Москва')
        self.assertEqual(response.status_code, 200)
        self.assertIn('temperature', response.json())
        self.assertIn('wind_speed', response.json())
        self.assertIn('humidity', response.json())


if __name__ == '__main__':
    unittest.main()
