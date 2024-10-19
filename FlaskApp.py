from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/calculate/<operation>/<int:numberA>/<int:numberB>', methods=['GET'])
def calculate(operation, numberA, numberB):
    """
    Performs the specified operation (add, subtract, multiply, divide) 
    on two numbers and returns the result as JSON.
    """

    
    if operation == 'add':
        result = numberA + numberB
    elif operation == 'subtract':
        result = numberA - numberB
    elif operation == 'multiply':
        result = numberA * numberB
    elif operation == 'divide':

        #division by 0  exception handling 
        if numberB == 0:
            return jsonify({'status': 400, 'error': 'Division by zero is not allowed!'})
        result = numberA / numberB
    else:

        #invalid operator exception handling 
        return jsonify({'status': 400, 'error': 'Invalid operation!'})  

    return jsonify({'status': 200, 'result': result})

