import pytest
from pytest import mark
from utils.api_client import APIClient

@mark.api
@mark.smoke
class TestJSONPlaceholderAPI:
    """Example API test class using JSONPlaceholder service"""

    @pytest.fixture
    def api_client(self, config, api_session):
        return APIClient(config['base_url'], api_session)

    @pytest.mark.testomatio("@T9ecb0d39")
    def test_get_all_posts(self, api_client):
        """Test getting all posts"""
        response = api_client.get('/posts')

        assert response.status_code == 200
        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) == 100

    @pytest.mark.testomatio("@T9ebc34f9")
    def test_get_single_post(self, api_client):
        """Test getting a single post by ID"""
        post_id = 1
        response = api_client.get(f'/posts/{post_id}')

        assert response.status_code == 200
        post = response.json()
        assert post['id'] == post_id
        assert 'title' in post
        assert 'body' in post
        assert 'userId' in post

    @pytest.mark.testomatio("@T7f3cf5ef")
    def test_create_post(self, api_client):
        """Test creating a new post"""
        new_post = {
            'title': 'Test Post Title',
            'body': 'This is a test post body content',
            'userId': 1
        }

        response = api_client.post('/posts', json=new_post)

        assert response.status_code == 201
        created_post = response.json()
        assert created_post['title'] == new_post['title']
        assert created_post['body'] == new_post['body']
        assert created_post['userId'] == new_post['userId']
        assert 'id' in created_post

    @pytest.mark.testomatio("@T12ac14e8")
    def test_update_post(self, api_client):
        """Test updating an existing post"""
        post_id = 1
        updated_data = {
            'id': post_id,
            'title': 'Updated Title',
            'body': 'Updated body content',
            'userId': 1
        }

        response = api_client.put(f'/posts/{post_id}', json=updated_data)

        assert response.status_code == 200
        updated_post = response.json()
        assert updated_post['title'] == updated_data['title']
        assert updated_post['body'] == updated_data['body']

    @pytest.mark.testomatio("@Taab69a7a")
    def test_delete_post(self, api_client):
        """Test deleting a post"""
        post_id = 1
        response = api_client.delete(f'/posts/{post_id}')

        assert response.status_code == 200

    @pytest.mark.testomatio("@T5f604568")
    @mark.regression
    def test_get_user_posts(self, api_client):
        """Test getting posts for a specific user"""
        user_id = 1
        response = api_client.get('/posts', params={'userId': user_id})

        assert response.status_code == 200
        user_posts = response.json()
        assert isinstance(user_posts, list)
        assert len(user_posts) > 0

        for post in user_posts:
            assert post['userId'] == user_id

    @pytest.mark.testomatio("@T96d4201b")
    def test_get_nonexistent_post(self, api_client):
        """Test getting a non-existent post returns 404"""
        response = api_client.get('/posts/99999')
        assert response.status_code == 404