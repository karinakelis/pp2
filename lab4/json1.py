import json

f = open('data.json', 'r')
text = f.read()
name = json.loads(text)
print(
    "Interface Status" "\n"
    "================================================================================" "\n"
    "DN                                                 Description           Speed    MTU" "\n"
    "-------------------------------------------------- --------------------  ------  ------")
date = name['imdata']
for i in date:
    dn = i["l1PhysIf"]["attributes"]["dn"]
    description = i["l1PhysIf"]["attributes"]["descr"]
    speed = i["l1PhysIf"]["attributes"]["speed"]
    mtu = i["l1PhysIf"]["attributes"]["mtu"]
    print("{0:51} {1:20} {2:4} {3:9}".format(dn, description, speed, mtu))