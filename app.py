from flask import Flask, render_template
import os
#idata["results"]
from datetime import datetime
import urllib.request, json
from jinja2 import ext

with urllib.request.urlopen("https://apis.is/petrol") as url:
    data = json.loads(url.read().decode())

stodvar = []
done = []
for i in data["results"]:
    if i["company"] not in done:
        done.append(i["company"])
        stodvar.append([i["company"],i["company"].lower()+".png"])

def getlowestprice(key,nafn):
    low = 10000000000000000000
    company = ""
    name = ""
    nafn = nafn
    for i in data["results"]:
        if i[key] < low:
            company = i["company"]
            name = i["name"]
            low = i[key]

    return f"Ódýrasta {nafn}: {low}kr. er hjá {company}, {name}"

print(getlowestprice("diesel","dísel"))



app = Flask(__name__)

def format_time(data):
    return datetime.strptime(data, "%Y-%m-%dT%H:%M:%S.%f").strftime("%d. %m. %Y Kl. %H: %M")

print(format_time(data["timestampPriceCheck"]))
app.jinja_env.filters["format_time"] = format_time


@app.route("/")
def index():
    return render_template("index.html",data = data, stodvar = stodvar, disel = getlowestprice("diesel","dísel"), bensin = getlowestprice("bensin95","bensín"), )


@app.route("/company/<name>")
def company(name):
    print(name)
    for items in data["results"]:
        if items["company"] == name:
            print(items["geo"]["lat"])
    return render_template("company.html", data = data, name = name)

@app.route("/moreinfo/<name>")
def moreinfo(name):
    print("kallli")
    return render_template("moreinfo.html", data = data , name = name)



#@app.errorhandler(404)
#def page_not_found():
    # note that we set the 404 status explicitly
    #return "síða fanst ekki 404"





if __name__ == "__main__":
    app.run()
    app.run(debug=True, use_reloader = True)
