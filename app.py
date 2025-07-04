from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = ""
    expression = ""
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            # Safely evaluate the expression
            result = eval(expression, {"__builtins__": None}, {})
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result, expression=expression)

if __name__ == "__main__":
    app.run(debug=True)
