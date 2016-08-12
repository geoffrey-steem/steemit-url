from flask import Flask, redirect
import json

from steemapi.steemnoderpc import SteemNodeRPC

app = Flask(__name__)

@app.route("/")
def homepage():
    return('Go to /account_name to view their metadata webpage')

@app.route("/<account_name>")
def account_meta(account_name):
    rpc = SteemNodeRPC("wss://steemit.com/wspa")

    account_meta = json.loads(rpc.get_account(account_name)['json_metadata'])
    account_url = account_meta['url']
    
    return redirect(account_url, code=302)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
    #app.run()
