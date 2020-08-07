import io
import urllib

def test_fetching():
    url = 'https://matplotlib.org/1.5.0/_static/logo2.png'
    with urllib.request.urlopen(parsed) as response:
        response = io.BytesIO(response.read())
        assert len(response) > 0
