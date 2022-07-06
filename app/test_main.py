from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


# TODO: make patent_code and id_code random

class TestPatent:

    _url = 'http://localhost:8000/api/v1/patent/'

    def _post(self, payload):
        response = client.post(
            self._url,
            headers={'Content-Type': 'application/json'},
            json=payload,
        )
        return response

    def test_convert_success(self):
        response = self._post({'patent_code': 'AGGC214'})

        assert response.status_code == 200
        assert response.json() == {'id_code': 4214215}

    def test_convert_fail(self):
        response = self._post({'patent_code': 'AFSC221'})

        assert response.status_code == 200
        assert response.json() != {'id_code': 4214215}

    def test_length_fail(self):
        response = self._post({'patent_code': 'AGGC'})

        assert response.status_code == 422
        assert response.json()[
            'detail'][0]['msg'] == "ensure this value has at least 7 characters"

    def test_format_fail(self):
        response = self._post({'patent_code': 'AAAAAAA'})

        assert response.status_code == 422
        assert response.json()[
            'detail'][0]['msg'] == "string does not match regex \"^[A-Z]{4}[0-9]{3}$\""

    def test_type_fail(self):
        response = self._post({'patent_code': 1242421})

        assert response.status_code == 422
        assert response.json()['detail'][0]['type'] == "value_error.str.regex"


class TestId:
    _url = 'http://localhost:8000/api/v1/id/'

    def _post(self, payload):
        response = client.post(
            self._url,
            headers={'Content-Type': 'application/json'},
            json=payload,
        )
        return response

    def test_convert_success(self):
        response = self._post({'id_code': 4214215})

        assert response.status_code == 200
        assert response.json() == {'patent_code': 'AGGC214'}

    def test_convert_fail(self):
        response = self._post({'id_code': 424215})

        assert response.status_code == 200
        assert response.json() != {'patent_code': 'AGGC214'}

    def test_type_fail(self):
        response = self._post({'id_code': "fsaf"})

        assert response.status_code == 422
        assert response.json()[
            'detail'][0]['msg'] == "value is not a valid integer"
