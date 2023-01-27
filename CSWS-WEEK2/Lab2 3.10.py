countries = ["Algeria","Brazil","USA","China","Japan"]
print(countries)

print("The length of the list is")
print(len(countries))

countries.append("Morocco")
print(countries)

print("The length of the list is")
print(len(countries))

countries.insert(2, "Wales")
print(countries)

countries.remove("Brazil")
print(countries)

x = countries.pop(2)
print(countries)

del countries[1]
print(countries)