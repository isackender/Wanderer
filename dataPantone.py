data = []
pantone_aliases = []
pantone_codes = []
pantone_hex = []
pantone_rgb = []

databasePantone = "database-pantone.txt"

with open(databasePantone) as datafile:
    megalist = list(zip(*(line.strip().split(' \t') for line in datafile)))

# Aliases
for dat in list(megalist[0]):                       # Pantone names
    pantone_aliases.append(dat.strip().lower())     # Removes white spaces and transform to lowercase

# Codes
for dat in list(megalist[1]):                       # Pantone names
    pantone_codes.append(dat.strip().lower())       # Removes white spaces and transform to lowercase

# Hexadecimal
for dat in list(megalist[2]):                       # Pantone names
    pantone_hex.append(dat.strip().lower())         # Removes white spaces and transform to lowercase

pantone_rgb = list(zip(megalist[3], megalist[4], megalist[5]))
