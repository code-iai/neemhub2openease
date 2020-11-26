import dvc.api


def download_file_from_repository(filename, repository_url):
    with dvc.api.open(filename, repo=repository_url) as file_descriptor:
        return file_descriptor.read()
