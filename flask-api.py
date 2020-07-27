#!/usr/bin/env python3
# USAGE: curl "127.0.0.1:1234?token=dude&shell=pwsh"
# import subprocess
from subprocess import Popen, PIPE, call, run
from flask import Flask, request, abort
import random
app = Flask(__name__)
token = "dude"

# methods=('get', 'post'
@app.route('/item1')
def item1():
    # token = "dude"
    if request.args.get("token") != token:
        # return "Denied!"
        abort(404, description="Resource not found")
    else:
        return str(random.randint(1,10))
@app.route('/hello')


def bash_pwsh():
    # r = subprocess.call(["ls", "-lhat"])

    # p = Popen(['ls', '-lat'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    # output, err = p.communicate(b"input data that is passed to subprocess' stdin")
    # rc = p.returncode
    # return output

    # r = subprocess.run(["ls", "-l", "/dev/null"], capture_output=True) # python 3.7
    # name = request.args.get("name", default=None, type=str)
    token = "dude"
    if request.args.get("token") != token:
        return "Denied!"
    if request.args.get("shell") == "pwsh":
        r = run(["pwsh", "-command", "dir", "/dev/null"], stdout=PIPE, stderr=PIPE)
    elif request.args.get("shell") == "bash":
        r = run(["ls", "-l", "/dev/null"], stdout=PIPE, stderr=PIPE)
    else:
        return "no match"

    # return "Hello World!"
    return r.stdout


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1234, ssl_context='adhoc')
