# sample Dictionary

##Al = [
##        {'Baldwin': {'tracts': 31, 'pop': 182265},
##         'Autauga': {'tracts': 12, 'pop': 54571},
##         'Barbour': {'tracts': 8, 'pop': 22874}}
##      ]

county = [
    {"county": "Baldwin", "pop": 182265},
    {"county": "Autuga", "pop": 54571},
    {"county": "Barbour", "tracts": 8, "pop": 22874},
]


def search(name):
    for c in county:
        if c["county"] == name:
            return c


x = search("Barbour")
print(x["tracts"])

