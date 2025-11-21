from flask import Flask, request, render_template

app = Flask(__name__) # please create the applicatin and use all the function in flask, so that you can run it from cloud

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    q = request.form.get("q")
    print(q)
    return(render_template("main.html"))


if __name__=="__main__":
    app.run(port=1111)
