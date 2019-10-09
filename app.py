from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.errorhandler(404)
def page_not_found():
    # note that we set the 404 status explicitly
    return "síða fanst ekki 404"





if __name__ == "__main__":
    app.run()
    app.run(debug=True, use_reloader = True)
