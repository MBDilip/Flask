# import add
# Importing flask.
from flask import Flask, request, jsonify

# products = [{"name": "Coke",
#              "price": 20},
#             {"name": "pepsi",
#             "price": 30}]

students = [{"name": "Shreyas",
             "class": "10th A",
             "grade": "A"},
             {"name": "Ram",
             "class": "10th B",
             "grade": "B"}]
# Create the server
app = Flask(__name__)

# Root


@app.route("/")
def hello():
    print(" I am in hello function")
    return "<H1>Hello World</H1>"


@app.route("/api", methods=['GET', 'POST'])
def api():
    if (request.method == 'GET'):
        return (" You are getting a get request")
    elif (request.method == 'POST'):
        return jsonify("Post Request")


@app.route("/students", methods=['GET', 'POST'])
def product():
    if (request.method == 'GET'):
        return (students)
    elif (request.method == 'POST'):

        jsonData = request.get_json()
        print(request.get_json())
        students.append(jsonData)
        return jsonify("New Student is added")


if (__name__ == "__main__"):
    app.run(debug=True)


# 127.0.0.1:5000
