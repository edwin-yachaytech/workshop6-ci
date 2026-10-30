from app import app


def client():
    return app.test_client()


def test_hello_returns_greeting():
    response = client().get('/hello/Ana')
    assert response.status_code == 200
    assert response.content_type == 'application/json'
    assert response.get_json() == {'message': 'Hello, Ana!'}


def test_square_returns_number_and_square():
    response = client().get('/api/square/4')
    assert response.status_code == 200
    assert response.get_json() == {'number': 4, 'square': 16}


def test_unknown_route_returns_404():
    assert client().get('/unknown').status_code == 404


def test_health_returns_ok():
    response = client().get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}
