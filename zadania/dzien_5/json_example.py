"""
    jak korzystac z plikow jsonowych w Pythonie?
"""

import json

# jak otwierac i czytac
# with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\example.json') as file:
#
#     data = json.load(file)
#     print(data['cats'][0]['name'])
#     print(type(data))

obj = [{'name': 'Bob'}, {'name': 'Bonifacy'}]

# jak zapisywac
with open(r'C:\Users\lukie\OneDrive\Dokumenty\SDA\zajecia_repos\ZDPYTpol56\materialy\example_writer.json', 'w') as file:
    json.dump(obj, file, indent=4)
