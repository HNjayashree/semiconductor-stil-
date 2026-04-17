from flask import Flask, render_template
from parser import parse_stil

app = Flask(__name__)

@app.route("/")
def home():
    file_path = r"C:\Users\dhanyashree\Downloads\Production_SCAN_stuck_at_Example (3).stil"
    data = parse_stil(file_path)
    return render_template("index.html", data=data)


# 🔥 THIS IS REQUIRED
if __name__ == "__main__":
    app.run(debug=True)