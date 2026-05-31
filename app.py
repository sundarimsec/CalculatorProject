from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        a = int(request.form["num1"])
        b = int(request.form["num2"])
        result = a + b

        return f"""
        <h1>Calculator Result</h1>
        <h2>{a} + {b} = {result}</h2>
        <a href="/">Back</a>
        """

    return """
    <h1>Simple Calculator</h1>
    <form method="POST">
        Number 1: <input type="number" name="num1"><br><br>
        Number 2: <input type="number" name="num2"><br><br>
        <input type="submit" value="Add">
    </form>
    """

if __name__ == "__main__":
    app.run()
