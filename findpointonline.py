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


def find_y(tuple1, tuple2, x):
    slope = (tuple2[1] - tuple1[1]) / (tuple2[0] - tuple1[0])
    b = tuple2[1] - (slope * tuple2[0])
    y = (slope * x) + b
    return y


if __name__ == "__main__":
    tuple1, tuple2 = receive_tuples()
    x = receive_x
    y1 = find_y(tuple1, tuple2, x)
