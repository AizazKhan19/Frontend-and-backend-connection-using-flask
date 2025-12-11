from flask import Flask, render_template, request
from logic import messege_printer   # Import your function

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    
    if request.method == "POST":
        name = request.form.get("name")
        message = messege_printer(name)

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
