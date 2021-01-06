import requests as curl

NEEM_REPOS_URL = 'https://neemgit.informatik.uni-bremen.de/api/v4/groups/9/projects'


def get_all_public_repos():
    return _get_request_as_json_(NEEM_REPOS_URL)


def get_name_for_user_id(id):
    user = _get_request_as_json_('https://neemgit.informatik.uni-bremen.de/api/v4/users/{}'.format(id))
    return user.get('name', '')


def _get_request_as_json_(url):
    return curl.get(url).json()