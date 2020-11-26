from os import system
from flask import Flask, send_file, request

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
    app.run(port=1338,debug=True)