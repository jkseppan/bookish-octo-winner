import io
from urllib import request

def test_fetching():
    url = 'https://matplotlib.org/1.5.0/_static/logo2.png'
    with request.urlopen(url) as response:
        response = io.BytesIO(response.read())
        assert len(response.getbuffer()) == 19496
