from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <html>
        <head>
            <title>Calculator</title>
        </head>
        <body>
            <form action="/calculate" method="post">
                <input type="text" name="first_number">
                <input type="text" name="second_number">
                <select name="operation">
                    <option value="add">+</option>
                    <option value="subtract">-</option>
                    <option value="multiply">*</option>
                    <option value="divide">/</option>
                </select>
                <input type="submit" value="Calculate">
            </form>
        </body>
    </html>
    """

@app.route("/calculate", methods=["POST"])
def calculate():
    first_number = request.form.get("first_number")
    second_number = request.form.get("second_number")
    operation = request.form.get("operation")

    if operation == "add":
        result = int(first_number) + int(second_number)
    elif operation == "subtract":
        result = int(first_number) - int(second_number)
    elif operation == "multiply":
        result = int(first_number) * int(second_number)
    elif operation == "divide":
        result = int(first_number) / int(second_number)

    return f"The result is {result}"

if __name__ == "__main__":
    app.run()
