from flask import Flask, jsonify, request
from flask_cors import CORS
import db_util

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/employees', methods=['GET'])
def all_employees():
    return jsonify({
        'status': 'success',
        'data': db_util.get_all("employees")
    })

@app.route('/addEmployee', methods=['POST'])
def add_employee():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        response_object['data'] = db_util.add_record("employees",post_data)
        response_object['message'] = 'Employee added!'
    return jsonify(response_object)

@app.route('/searchEmployee', methods=['POST'])
def search_employee():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        response_object['data'] = db_util.search_record("employees",post_data)
        response_object['message'] = ''
    return jsonify(response_object)

@app.route('/removeEmployee/<employee_id>', methods=['GET'])
def remove_employee(employee_id):
    response_object = {'status': 'success'}
    db_util.delete_record("employees",employee_id)
    response_object['message'] = 'Employee removed!'
    return jsonify(response_object)



if __name__ == '__main__':
    db_util = db_util.Db_Util("test")
    app.run()