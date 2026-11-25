from flask import Flask, render_template

# Create flask application
app=Flask(__name__)

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/comics")
def comics():
    return render_template("comics.html")

@app.route("/comics/1to25")
def comics1to25():
    return render_template("comics1to25.html")

# Other pages routes


# Run the application
if __name__ == "__main__":
    app.run(debug=True)
