import json

x = open('/Users/Admin/DocumentsClone/Lab-python/lab-4/json/sample-data.json')

data = json.load(x)

print("Interface Status")
print("=" * 92)
print("DN                                                 Description           Speed       MTU")
print("-" * 50, "-" * 20,   "-" * 8, "  ",      "-" * 6)

for i in data['imdata']:
    print(i['l1PhysIf']['attributes']['dn'], '\t\t\t\t', i['l1PhysIf']['attributes']['descr'], i['l1PhysIf']['attributes']['speed'], '   ', i['l1PhysIf']['attributes']['mtu'])

x.close()