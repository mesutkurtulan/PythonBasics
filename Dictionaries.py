countrycodes = {1: 'Adana', 3: 'Afyon', 5: 'Amasya', 6: "Ankara", 7: "Antalya"}
print(countrycodes)         # {1: 'Adana', 3: 'Afyon', 5: 'Amasya', 6: "Ankara", 7: "Antalya"}
print(countrycodes[1])      # Adana
print(countrycodes.get(3))  # Afyon
print(countrycodes.get(8, "Not Found"))     # Not Found

countrycodes[8] = "Artvin"
print(countrycodes)         # {1: 'Adana', 3: 'Afyon', 5: 'Amasya', 6: 'Ankara', 7: 'Antalya', 8: 'Artvin'}

print(countrycodes.keys())      # dict_keys([1, 3, 5, 6, 7, 8])
print(countrycodes.values())    # dict_values(['Adana', 'Afyon', 'Amasya', 'Ankara', 'Antalya', 'Artvin'])
print(countrycodes.items())     # dict_items([(1, 'Adana'), (3, 'Afyon'), (5, 'Amasya'), (6, 'Ankara'), (7, 'Antalya'), (8, 'Artvin')])

print(countrycodes.pop(9, "Not Found"))     # Not Found
print(countrycodes.pop(8, "Not Found"))     # Artvin
print(countrycodes)                         # {1: 'Adana', 3: 'Afyon', 5: 'Amasya', 6: 'Ankara', 7: 'Antalya'}
print(countrycodes.popitem())               # (7, 'Antalya')
print(countrycodes)                         # {1: 'Adana', 3: 'Afyon', 5: 'Amasya', 6: 'Ankara}

countrycodes.update({3: "AfyonKarahisar"})
print(countrycodes)                         # {1: 'Adana', 3: 'AfyonKarahisar', 5: 'Amasya', 6: 'Ankara'}

print(countrycodes.setdefault(6, "Not Found"))      # Ankara

print(countrycodes.clear())                         # None

#Empty Dictionary
newDistionary = {}
newDistionary['firstName'] = "John"
newDistionary['lastName'] = "Doe"