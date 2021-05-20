from pyramid import testing
from zope.interface.interface import Method
from pyramid_api.views import CountryViews

def test_welcome():
    request = testing.DummyRequest()
    response = CountryViews(request).welcome()
    assert response['content'] == 'Bem vindo !!!'

def test_create_country():
    request = testing.DummyRequest(method='POST', json_body={"name": "Brasil"})
    response = CountryViews(request).create_country()
    assert response['content'] ==  'Criou'
    assert response['body']['name'] == 'Brasil'

def test_get_country():
    request = testing.DummyRequest()
    response = CountryViews(request).get_country()
    assert response['content'] ==  'Retornou'

def test_update_country():
    request = testing.DummyRequest(method='PUT', json_body={"name": "Argentina"})
    response = CountryViews(request).update_country()
    assert response['content'] ==  'Atualizou !!'
    assert response['body']['name'] == 'Argentina'

def test_delete_country():
    request = testing.DummyRequest(method='DELETE', json_body={"id": 1})
    response = CountryViews(request).delete_country()
    assert response['content'] ==  'Apagou !!'
    assert response['body']['id'] == 1
