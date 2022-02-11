import json


def create_person():
    new_person = {"First Name": "Anna",
                  "Last Name": "Ables",
                  "Age": 35,
                  "Visits": ["1/1/2020", "2/3/2020", "3/15/2020"]
                  }
    return new_person


def create_list():
    return [True, False, True]


def input_json(filename):
    in_file = open(filename, 'r')
    new_variable = json.load(in_file)
    in_file.close()
    return new_variable


def output_json(my_dict):
    # filename = "patient.json"
    filename = "my_boolean.json"
    out_file = open(filename, 'w')
    json.dump(my_dict, out_file)
    out_file.close()


def output_json_with(output_data):
    filename = "my_output.txt"
    with open(filename, 'w') as out_file:
        json.dump(output_data, out_file)
    print("The output is finished")


if __name__ == "__main__":
    """
    person = create_person()
    print(person)
    output_json(person)
    """

    # filename = "patient.json"
    filename = "my_boolean.json"
    x = input_json(filename)
    print(x)
    print(type(x))

    """
    data_to_output = create_list()
    output_json(data_to_output)
    """
