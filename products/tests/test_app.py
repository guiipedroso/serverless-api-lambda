from chalice.test import Client
from app import app
import json

def test_create_product():
    with Client(app) as client:
        response = client.http.post(
                        '/product',
                        body=json.dumps({"product": "arroz", "amount": "2"}),
                        headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_update_product():
    with Client(app) as client:
        response = client.http.put(
                        '/product',
                        body=json.dumps({"product": "arroz", "amount": "2"}),
                        headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_delete_product():
    with Client(app) as client:
        response = client.http.delete(
                        '/product',
                        body=json.dumps({"product": "arroz", "amount": "2"}),
                        headers={"Content-Type": "application/json"}
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_products():
    with Client(app) as client:
        response = client.http.get(
                        '/products'
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200


def test_get_product():
    with Client(app) as client:
        response = client.http.get(
                        '/product/1'
                    )
        print(response.json_body)
        assert response.json_body["statusCode"] == 200