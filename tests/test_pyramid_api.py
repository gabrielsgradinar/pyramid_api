from pyramid import testing
from pyramid_api.api.resources.country import CountryViews


def test_welcome():
    request = testing.DummyRequest()
    response = CountryViews(request).hello()

    print("content", response)

    assert response.status_code == 200


def test_create_country():
    request = testing.DummyRequest(
        method='POST',
        json_body={
            "name": "Brasil",
            "official_language": "Português",
            "population": 4321
        }
    )
    response = CountryViews(request).create_country()
    assert response['content'] == 'Criou'
    assert response['body']['name'] == 'Brasil'


def test_get_country():
    request = testing.DummyRequest()
    response = CountryViews(request).get_country()
    assert response['content'] == 'Retornou'


def test_update_country():
    request = testing.DummyRequest(
        method='PUT', json_body={"name": "Argentina"})
    response = CountryViews(request).update_country()
    assert response['content'] == 'Atualizou !!'
    assert response['body']['name'] == 'Argentina'


def test_delete_country():
    request = testing.DummyRequest(method='DELETE', json_body={"id": 1})
    response = CountryViews(request).delete_country()
    assert response['content'] == 'Apagou !!'
    assert response['body']['id'] == 1
