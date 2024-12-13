import json


f = open("sample.json")
data = json.load(f)
for k, v in data.items():
    if k == "projects":
        print(v)
f.close()

json_string = '{"name": "Alice", "age": 25, "isStudent": false}'
data_s = json.loads(json_string)
print(data_s)


ff = open("write_json.json", "w")
data_p = {
    "name": "Bob",
    "last_name": None,
    "age": 28,
    "isEmployed": True,
    "skills": ["Python", "Django", "Machine Learning"],
    "address": {
        "street": "456 Elm St",
        "city": "Metropolis",
        "state": "NY",
        "zip": "10118"
    }
}

dt = json.dump(data_p, ff, indent=4)
ff.close()
