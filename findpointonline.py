# function "find point on line"

def receive_tuples():
    tuple_x1 = float(input("Enter x1:"))
    tuple_y1 = float(input("Enter y1:"))
    tuple1 = (tuple_x1, tuple_y1)
    tuple_x2 = float(input("Enter x2:"))
    tuple_y2 = float(input("Enter y2:"))
    tuple2 = (tuple_x2, tuple_y2)
    return tuple1, tuple2
 

def receive_x():
    x = float(input("Enter your new value x:"))
    return x


def calculate_y(tuple1, tuple2, x):
    slope = (tuple2[1] - tuple1[1]) / (tuple2[0] - tuple1[0])
    b = tuple2[1] - (slope * tuple2[0])
    y = (slope * x) + b
    return y


def find_y():
    tuple1, tuple2 = receive_tuples()
    x = receive_x()
    y = calculate_y(tuple1, tuple2, x)
    return y


def determine_point(tuple1, tuple2, tuple3):
    expected_y = calculate_y(tuple1, tuple2, tuple3[0])
    if expected_y == tuple3[1]:
        return True
    else:
        return False


def check_point():
    tuple1, tuple2 = receive_tuples()
    tuple_x3 = float(input("Enter x3:"))
    tuple_y3 = float(input("Enter y3:"))
    tuple3 = (tuple_x3, tuple_y3)
    if_on_line = determine_point(tuple1, tuple2, tuple3)
    return if_on_line


if __name__ == "__main__":
    print(find_y())
    print(check_point())
