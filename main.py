from os import system
from flask import Flask, send_file, request
import requests as curl
import json

from neem import NEEM
from neem_hub_caller import get_all_public_repos
from neem_hub_downloader import download_regular_file_from_repository

app = Flask(__name__)
import dvc.api

@app.route('/download')
def download_file ():
    repo = request.args.get('repo')
    print(repo)
    #system("echo $HADOOP_HOME")
    #system("dvc get https://neemgit.informatik.uni-bremen.de/data-collection/pr2.git pr2.urdf -o data/")
    with dvc.api.open(
        "pr2.urdf",
        repo='https://neemgit.informatik.uni-bremen.de/data-collection/pr2.git'
    ) as fd:
        print('test')
        new_file = open("data/pr2_test.urdf", mode="w")
        new_file.write(fd.read())
        new_file.close()
    path = "data/hello.txt"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    #app.run(port=1338,debug=True)
    neems = [NEEM(repo) for repo in get_all_public_repos()]

    for neem in neems:
        data = download_regular_file_from_repository("meta.json", neem.repo_id)
        if data.status_code == 200:
            print(data.content)
    print('END')