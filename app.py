from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    """Returns a welcome message for the calculator."""
    return "Welcome to the Flask Calculator! Use the /calculate endpoint for arithmetic operations."

# Define the addition route
@app.route('/add/<int:numberA>/<int:numberB>', methods=['GET'])
def add(numberA, numberB):
    result = numberA + numberB
    return jsonify({'status': 200, 'result': result})

# Define the subtraction route
@app.route('/minus/<int:numberA>/<int:numberB>', methods=['GET'])
def minus(numberA, numberB):
    result = numberA - numberB
    return jsonify({'status': 200, 'result': result})

# Define the multiplication route
@app.route('/multiply/<int:numberA>/<int:numberB>', methods=['GET'])
def multiply(numberA, numberB):
    result = numberA * numberB
    return jsonify({'status': 200, 'result': result})

# Define the division route
@app.route('/divide/<int:numberA>/<int:numberB>', methods=['GET'])
def divide(numberA, numberB):
    if numberB == 0:
        return jsonify({'status': 400, 'error': 'Division by zero is not allowed!'})
    result = numberA / numberB
    return jsonify({'status': 200, 'result': result})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

