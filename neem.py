from neem_hub_caller import get_name_for_user_id


class NEEM(object):
    def __init__(self, repo_as_json):
        self.repo_id = repo_as_json.get('id')
        self.user = get_name_for_user_id(repo_as_json.get('creator_id'))
        self.created_at = repo_as_json.get('created_at')
        self.last_activity_at = repo_as_json.get('last_activity_at')
        self.url = repo_as_json.get('web_url')