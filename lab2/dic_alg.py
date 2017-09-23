def filter_emp(dic_empls):
        for emp in dic_empls:
            children = emp["children"]
            for child in children:
                if (child["age"]>=18):
                    print(emp["name"])
                    break
ivan = {
    "name": "ivan",
    "age": 46,
    "children": [
        {"name": "karen",
         "age": 12},
        {"name": "lip",
         "age": 20}
        ]
    }
rose = {
    "name": "rose",
    "age": 46,
    "children": [
        {"name": "rory",
         "age": 12},
        {"name": "emmy",
         "age": 1}
        ]
    }
jody = {
    "name": "jody",
    "age": 46,
    "children": [
        {"name": "debby",
         "age": 23},
        {"name": "karl",
         "age": 1}
        ]
    }

empls=[ivan, rose, jody]

filter_emp(empls)
