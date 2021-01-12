import dvc.api
import requests


def download_file_from_repository(filename, repository_url):
    with dvc.api.open(filename, repo=repository_url) as file_descriptor:
        return file_descriptor.read()


def download_regular_file_from_repository(filename, repository_id):
    url = "https://neemgit.informatik.uni-bremen.de/api/v4/projects/{}/repository/files/{}/raw?ref=master"\
        .format(repository_id,filename)

    return requests.get(url, allow_redirects=True)
