from flask import Flask, request, jsonify


app = Flask(__name__)

db = []


def add_patient_to_db(name, id, blood_type):
    new_patient = {"name": name, "id": id,
                   "blood_type": blood_type, "tests": {}}
    db.append(new_patient)
    return True


def init_server():
    add_patient_to_db("Ann Ables", 101, "A+")
    add_patient_to_db("Bob Boyles", 202, "B-")
    # Start logging functionality


@app.route("/add_patient", methods=["POST"])
def add_patient():
    # Get the data form the request
    in_data = request.get_json()
    # Call other function to do the request
    answer, status_code = add_patient_driver(in_data)
    # Provide a response
    return jsonify(answer), status_code


def add_patient_driver(in_data):
    answer, status_code = validate_add_patient_input(in_data)
    if status_code != 200:
        return answer, status_code
    add_patient_to_db(in_data["name"], in_data["id"], in_data["blood_type"])
    return db, 200


def validate_add_patient_input(in_data):
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, expected_type in zip(expected_keys, expected_types):
        if key not in in_data:
            error_massage = "Key {} is missing.".format(key)
            return error_massage, 400
        if type(in_data[key]) is not expected_type:
            error_massage = "Value of key {} is not of type {}"\
                            .format(key, expected_type)
            return error_massage, 400
    return True, 200


@app.route("/get_results/<patient_id>", methods=["GET"])
def get_results(patient_id):
    answer, status_code = get_results_driver(patient_id)
    return answer, status_code


def get_results_driver(patient_id):
    answer, status_code = validate_patient_id(patient_id)
    if status_code != 200:
        return answer, status_code
    for patient in db:
        if patient["id"] == int(patient_id):
            return jsonify(patient["tests"]), 200
    return "Patient id {} is not in database.".format(patient_id), 400


def validate_patient_id(patient_id):
    try:
        patient_id_int = int(patient_id)
        return True, 200
    except ValueError:
        return "Patient_id was not an integer.", 400


if __name__ == "__main__":
    init_server()
    app.run()
