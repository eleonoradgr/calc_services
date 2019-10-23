from flakon import JsonBlueprint
from flask import Flask, request, jsonify
from myservice.classes.foocalculator import FooCalculator

calc = JsonBlueprint('calc', __name__)


@calc.route('/calc/sum', methods=['GET'])
def sum():
    m = int(request.args.get('m'))
    if(request.args.get('n') != None):
        n = int(request.args.get('n'))
    else:
        n = 0
    calc = FooCalculator()
    m = calc.sum(m, n)
    return jsonify({'result': str(m)})


@calc.route('/calc/diff', methods=['GET'])
def diff():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    calc = FooCalculator()
    m = calc.subtract(m, n)
    return jsonify({'result': str(m)})


@calc.route('/calc/multiply', methods=['GET'])
def multiply():
    m = int(request.args.get('m'))
    n = int(request.args.get('n'))
    calc = FooCalculator()
    m = calc.multiply(m, n)
    return jsonify({'result': str(m)})


@calc.route('/calc/divide', methods=['GET'])
def divide():
    m = int(request.args.get('m'))
    n = -int(request.args.get('n'))
    calc = FooCalculator()
    m = calc.divide(m, n)
    return jsonify({'result': str(m)})
