import json


with open("digimon.json", "r", encoding="utf-8") as f: 
    digimon = json.load(f)

list_digimon={k + 1 : v for k, v in enumerate (digimon) }

print(list_digimon)