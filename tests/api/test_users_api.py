import pytest
from pytest import mark
from utils.api_client import APIClient

@mark.api
class TestUsersAPI:
    """API tests for users endpoints"""

    @pytest.fixture
    def api_client(self, config, api_session):
        return APIClient(config['base_url'], api_session)

    @pytest.mark.testomatio("@Tb088df60")
    @mark.smoke
    def test_get_all_users(self, api_client):
        """Test getting all users"""
        response = api_client.get('/users')

        assert response.status_code == 200
        users = response.json()
        assert isinstance(users, list)
        assert len(users) == 10

        user = users[0]
        required_fields = ['id', 'name', 'username', 'email']
        for field in required_fields:
            assert field in user

    @pytest.mark.testomatio("@Tc549a3f6")
    def test_get_user_by_id(self, api_client):
        """Test getting a specific user by ID"""
        user_id = 1
        response = api_client.get(f'/users/{user_id}')

        assert response.status_code == 200
        user = response.json()
        assert user['id'] == user_id
        assert 'name' in user
        assert 'email' in user
        assert 'address' in user
        assert 'company' in user

    @pytest.mark.testomatio("@T84cf4535")
    def test_user_address_structure(self, api_client):
        """Test user address has correct structure"""
        response = api_client.get('/users/1')

        assert response.status_code == 200
        user = response.json()
        address = user['address']

        required_address_fields = ['street', 'suite', 'city', 'zipcode', 'geo']
        for field in required_address_fields:
            assert field in address

        geo = address['geo']
        assert 'lat' in geo
        assert 'lng' in geo

    @pytest.mark.testomatio("@Tefe27560")
    @mark.regression
    def test_user_company_structure(self, api_client):
        """Test user company has correct structure"""
        response = api_client.get('/users/1')

        assert response.status_code == 200
        user = response.json()
        company = user['company']

        required_company_fields = ['name', 'catchPhrase', 'bs']
        for field in required_company_fields:
            assert field in company
            assert isinstance(company[field], str)
            assert len(company[field]) > 0