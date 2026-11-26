from flask import Flask, render_template

# Create flask application
app=Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Other pages routes
@app.route("/comics")
def comics():
    return render_template("comics.html")

@app.route("/comics/1to25")
def comics1to25():
    return render_template("1to25.html")

@app.route("/comics/26to50")
def comics26to50():
    return render_template("26to50.html")

@app.route("/ingredients")
def ingredients():
    return render_template("ingredients.html")

@app.route("/locations")
def locations():
    return render_template("locations.html")

@app.route("/merch")
def merch():
    return render_template("merch.html")
# Run the application
if __name__ == "__main__":
    app.run(debug=True)
