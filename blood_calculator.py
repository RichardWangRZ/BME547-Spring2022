print("This is the blood_calculator module and python"
      " calls it {}".format(__name__))


def interface():
    print("Blood Test Analysis")
    keep_running = True
    while keep_running:
        print("Options:")
        print("1-HDL")
        print("2-LDL")
        print("3-Total Cholesterol")
        print("9-Quit")
        choice = input("Enter your choice:")
        if choice == "9":
            keep_running = False
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            TC_driver()
    return


def accept_input(test_name):
    entry = input("Enter the {} test result:".format(test_name))
    return int(entry)


def print_result(test_name, test_value, test_class):
    out_string = "The test value of {} for {} is {}".format(test_value, test_name, test_class)
    print(out_string)
    return


# Functions for HDL
def check_HDL(HDL_value):
    if HDL_value >= 60:
        answer = "Normal"
    elif 60 > HDL_value >= 40:
        answer = "Borderline Low"
    else:
        answer = "Low"
    return answer


def HDL_driver():
    HDL_value = accept_input("HDL")
    classification = check_HDL(HDL_value)
    print_result("HDL", HDL_value, classification)


# Functions for LDL
def check_LDL(LDL_value):
    if LDL_value >= 190:
        answer = "Very High"
    elif 160 <= LDL_value < 190:
        answer = "High"
    elif 130 <= LDL_value < 160:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer


def LDL_driver():
    LDL_value = accept_input("LDL")
    classification = check_LDL(LDL_value)
    print_result("LDL", LDL_value, classification)


# Functions for Total Cholesterol
def check_TC(TC_value):
    if TC_value >= 240:
        answer = "High"
    elif 200 <= TC_value < 240:
        answer = "Borderline High"
    else:
        answer = "Normal"
    return answer


def TC_driver():
    TC_value = accept_input("Total Cholesterol")
    classification = check_TC(TC_value)
    print_result("Total Cholesterol", TC_value, classification)



if __name__ == "__main__":
    interface()
