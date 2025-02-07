import json

def load_json(file):
    with open(file, "r") as f:
        return json.load(f)

data = load_json("json_file.json")
print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<21} {'Speed':<9} {'MTU':<5}")
print("-" * 50 + " " + "-" * 20 + " " * 2 + "-" * 7 + " " * 2 + "-" * 6)
for i in data["imdata"]:
    attributes = i["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]
    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<5}")