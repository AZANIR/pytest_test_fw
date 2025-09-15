import pytest
from pytest_bdd import scenarios, given, when, then, parsers
import requests
from pytest import mark


scenarios('../features/api_operations.feature')


@pytest.fixture
def api_context():
    return {
        'base_url': 'https://jsonplaceholder.typicode.com',
        'response': None,
        'post_data': {},
        'posts': []
    }


@given('the API is available')
def api_available(api_context):
    response = requests.get(f"{api_context['base_url']}/posts/1")
    assert response.status_code == 200


@given('the API has existing posts')
def api_has_posts(api_context):
    response = requests.get(f"{api_context['base_url']}/posts")
    assert response.status_code == 200
    assert len(response.json()) > 0


@given(parsers.parse('a post exists with id {post_id:d}'))
def post_exists(api_context, post_id):
    response = requests.get(f"{api_context['base_url']}/posts/{post_id}")
    assert response.status_code == 200
    api_context['existing_post'] = response.json()


@when(parsers.parse('I create a post with title "{title}" and body "{body}" for user {user_id:d}'))
def create_post(api_context, title, body, user_id):
    post_data = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    api_context['post_data'] = post_data

    response = requests.post(
        f"{api_context['base_url']}/posts",
        json=post_data
    )
    api_context['response'] = response


@when(parsers.parse('I retrieve posts for user {user_id:d}'))
def retrieve_posts_for_user(api_context, user_id):
    response = requests.get(f"{api_context['base_url']}/posts?userId={user_id}")
    api_context['response'] = response
    api_context['posts'] = response.json() if response.status_code == 200 else []


@when(parsers.parse('I update the post with title "{new_title}" and body "{new_body}"'))
def update_post(api_context, new_title, new_body):
    post_id = api_context['existing_post']['id']
    update_data = {
        'id': post_id,
        'title': new_title,
        'body': new_body,
        'userId': api_context['existing_post']['userId']
    }

    response = requests.put(
        f"{api_context['base_url']}/posts/{post_id}",
        json=update_data
    )
    api_context['response'] = response
    api_context['updated_data'] = update_data


@then('the post should be created successfully')
def post_created_successfully(api_context):
    assert api_context['response'].status_code == 201


@then('the response should contain the post details')
def response_contains_post_details(api_context):
    response_data = api_context['response'].json()
    assert response_data['title'] == api_context['post_data']['title']
    assert response_data['body'] == api_context['post_data']['body']
    assert response_data['userId'] == api_context['post_data']['userId']


@then(parsers.parse('I should get {expected_count:d} posts'))
def should_get_expected_posts(api_context, expected_count):
    assert len(api_context['posts']) == expected_count


@then(parsers.parse('all posts should belong to user {user_id:d}'))
def posts_belong_to_user(api_context, user_id):
    for post in api_context['posts']:
        assert post['userId'] == user_id


@then('the post should be updated successfully')
def post_updated_successfully(api_context):
    assert api_context['response'].status_code == 200


@then(parsers.parse('the response should contain the updated title "{expected_title}"'))
def response_contains_updated_title(api_context, expected_title):
    response_data = api_context['response'].json()
    assert response_data['title'] == expected_title