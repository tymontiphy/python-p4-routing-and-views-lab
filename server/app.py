#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    # Generate a list of numbers from 0 to parameter-1
    numbers = '\n'.join(str(i) for i in range(parameter))
    
    # Add a trailing newline if the parameter is greater than 0
    if parameter > 0:
        numbers += '\n'
    
    return numbers  


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    
    # Perform the appropriate math operation
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Cannot divide by zero', 400
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation', 400
    
    return str(result)  

if __name__ == '__main__':
    app.run(port=5555, debug=True)
