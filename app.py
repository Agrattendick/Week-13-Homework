from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    #listings = mongo.db.listings.find_one()
    marsData = mongo.db.mars.find_one()
    print(marsData)
    return render_template("index.html", marsData = marsData)


@app.route("/scrape")
def scraper():
    mars = scrape_mars.scrape()
    mongoMars = mongo.db.mars
    mongoMars.update({},mars, upsert=True)
    #listings = mongo.db.listings
    #listings_data = scrape_craigslist.scrape()
    #listings.update({}, listings_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
