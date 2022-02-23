import requests


"""
r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(r)
print(type(r))
answer = r.json()
print(answer)
for branch in answer:
    print(branch["name"])
"""
"""
out_data = {
    "name": "Richard Wang",
    "net_id": "rw252",
    "e-mail": "rw252@duke.edu"
    }
r = requests.post("http://vcm-21170.vm.duke.edu:5000/student", json=out_data)
print(r.text)

r = requests.get("http://vcm-21170.vm.duke.edu:5000/list")
print(r.text)
"""

r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/rw252")
print(r.text)
Donor = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6")
Recipient = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M8")
print(Donor.text)
print(Recipient.text)
result = {"Name": "rw252", "Match": "Yes"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=result)
print(r.text)
