import pytest
import json

from api.target_client import ApiClient

class TestApi():

    @pytest.fixture(scope = 'function')
    def api_client(self):
        return ApiClient('twi.lek@yandex.ru', '123456a')

    @pytest.mark.API
    def test_create_segment(self, api_client):
        resp = api_client.create_segment('NewSegment')
        id = json.loads(resp.text)['id']

        resp = api_client.get_segment_by_id(id)
        name = json.loads(resp.text)['name']

        assert name == 'NewSegment'

    @pytest.mark.API
    def test_delete_segment(self, api_client):
        resp = api_client.create_segment('NewSegmentForDelete')
        id = json.loads(resp.text)['id']
        api_client.delete_segment(id)

        resp = api_client.get_all_segments()
        segments = json.loads(resp.text)['items']

        res = True
        for segment in segments:
            if segment['id'] == id:
                res = False
                break

        assert res