from flask import Flask, request, render_template

app = Flask(__name__) # please create the applicatin and use all the function in flask, so that you can run it from cloud

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__=="__main__":
    app.run(port=1111)
