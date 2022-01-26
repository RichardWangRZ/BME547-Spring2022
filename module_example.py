print("This is the database module and python calls it {}".format(__name__))

import blood_calculator as bc



HDL_value = 55

classification = bc.check_HDL(HDL_value)
print("55 is {}".format(classification))

x = bc.check_LDL(200)
print(x)


