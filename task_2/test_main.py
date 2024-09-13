import pytest
import requests
from http import HTTPStatus
from constant import SAVE_MES, BODY
from configuration import BASE_URL, API
from uuid import uuid4


class TestPositiveSave:
    """
    Позитивные проверки для ручки POST /api/1/item
    """

    def test_post(self, save):
        status = save.json()["status"]
        assert save.status_code == HTTPStatus.OK
        assert status.split(" - ")[0] == SAVE_MES


@pytest.mark.parametrize("status", [HTTPStatus.INTERNAL_SERVER_ERROR], scope="class")
class TestNegativeSave:
    """
    Негативные проверки для ручки POST /api/1/item
    """

    def test_body_without_body(self, status):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={},
        )

        assert response.status_code == status

    def test_without_name(self, status):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "price": 31313,
                "sellerId": 678654,
                "statistics": {"contacts": 1313, "like": 3, "viewCount": 4},
            },
        )

        assert response.status_code == status

    @pytest.mark.parametrize("name", [21, {"error": "error"}])
    def test_name(self, name, status):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "name": name,
                "price": 13131,
                "sellerId": 452342,
                "statistics": {"contacts": 32, "like": 35, "viewCount": 14},
            },
        )

        assert response.status_code == status

    def test_without_price(self, status):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "name": "Телефон",
                "sellerId": 123123,
                "statistics": {"contacts": 32, "like": 35, "viewCount": 14},
            },
        )
        assert response.status_code == status

    @pytest.mark.parametrize("price", [-500, "десять"])
    def test_incorrect_price(self, price, status):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "name": "Телефон",
                "price": price,
                "sellerId": 131123,
                "statistics": {"contacts": 32, "like": 35, "viewCount": 14},
            },
        )
        assert response.status_code == status

    def test_without_sellerid(self, status):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "name": "Телефон",
                "price": 500,
                "statistics": {"contacts": 32, "like": 35, "viewCount": 14},
            },
        )
        assert response.status_code == status

    @pytest.mark.parametrize("sellerId", [13.31, {"error": "error"}])
    def test_incorrect_sellerid(self, sellerId, status):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "name": "Телефон",
                "price": 500,
                "sellerId": sellerId,
                "statistics": {"contacts": 32, "like": 35, "viewCount": 14},
            },
        )
        assert response.status_code == status

    def test_without_statistics(self, status):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "name": "Телефон",
                "price": 500,
                "sellerId": 213131,
            },
        )
        assert response.status_code == status

    @pytest.mark.parametrize("statistics", [1, True, {"error": "error"}])
    def test_incorrect_statistic(self, status, statistics):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "name": "Телефон",
                "price": 500,
                "sellerId": 313131,
                "statistics": statistics,
            },
        )
        assert response.status_code == status

    @pytest.mark.parametrize("contacts", [-311, "contacts"])
    @pytest.mark.parametrize("like", [-13, "like"])
    @pytest.mark.parametrize("viewCount", [-12424, "viewCount"])
    def test_incorrect_statistics(self, status, contacts, like, viewCount):
        response = requests.request(
            "POST",
            f"{BASE_URL}{API}",
            json={
                "name": "Телефон",
                "price": 500,
                "sellerId": 324242,
                "statistics": {
                    "contacts": contacts,
                    "like": like,
                    "viewCount": viewCount,
                },
            },
        )
        assert response.status_code == status


class TestGetIdPositive:
    """
    Позитивные проверки для ручки GET /api/1/item/:id
    """

    def test_get_id(self, save):
        ids = save.json()["status"].split(" - ")[-1]
        response = requests.request("GET", f"{BASE_URL}{API}/{ids}")

        assert response.status_code == HTTPStatus.OK
        data_json = response.json()[0]
        assert data_json["id"] == ids
        assert data_json["name"] == BODY["name"]
        assert data_json["price"] == BODY["price"]
        assert data_json["sellerId"] == BODY["sellerId"]
        assert data_json["price"] == BODY["price"]
        assert data_json["statistics"]["contacts"] == BODY["statistics"]["contacts"]
        assert data_json["statistics"]["likes"] == BODY["statistics"]["like"]
        assert data_json["statistics"]["viewCount"] == BODY["statistics"]["viewCount"]


@pytest.mark.parametrize("status", [HTTPStatus.NOT_FOUND], scope="class")
class TestGetIdNegative:
    """
    Негативные проверки для ручки GET /api/1/item/:id
    """

    def test_notfound_id(self, status):
        response = requests.request(
            "GET",
            f"{BASE_URL}{API}/{uuid4()}",
        )
        assert response.status_code == status

    def test_incorrect_id(self, status):
        response = requests.request(
            "GET",
            f"{BASE_URL}{API}/324242121",
        )
        assert response.status_code == status

    def test_no_id(self, status):
        response = requests.request(
            "GET",
            f"{BASE_URL}{API}",
        )
        assert response.status_code == status


class TestSellerIdPositive:
    """
    Позитивные проверки для ручки GET /api/1/:sellerID/item
    """

    def test_seller_with_objects(self, save):
        response = requests.request(
            "GET",
            f"{BASE_URL}/api/1/{BODY["sellerId"]}/item",
        )
        assert response.status_code == HTTPStatus.OK

    @pytest.mark.parametrize("sellerId", [992131])
    def test_seller_without_objects(self, sellerId):
        response = requests.request(
            "GET",
            f"{BASE_URL}/api/1/{sellerId}/item",
        )
        assert response.status_code == HTTPStatus.OK

@pytest.mark.parametrize("status", [HTTPStatus.NOT_FOUND], scope="class")
class TestSellerIdNegative:
    """
    Негативные проверки для ручки GET /api/1/:sellerID/item
    """

    @pytest.mark.parametrize("sellerId", [-4242])
    def test_without_sellerid(self, status, sellerId):
        response = requests.request(
            "GET",
            f"{BASE_URL}/api/1/{sellerId}/item",
        )
        assert response.status_code == status

    @pytest.mark.parametrize("sellerId", ["error"])
    def test_incorrect_sellerid(self, status, sellerId):
        response = requests.request(
            "GET",
            f"{BASE_URL}/api/1/{sellerId}/item",
        )
        assert response.status_code == status