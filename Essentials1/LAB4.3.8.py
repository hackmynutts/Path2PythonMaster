# Tu tarea es escribir un par de funciones que conviertan l/100km a mpg (milas por galón), y viceversa.

# Las funciones:

# se llaman liters_100km_to_miles_gallon y miles_gallon_to_liters_100km respectivamente;
# toman un argumento (el valor correspondiente a sus nombres)


def liters_100km_to_miles_gallon(liters):
    galon = liters / 3.78541
    milla = 100 * 1000 / 1609.34
    return milla / galon

def miles_gallon_to_liters_100km(miles):
    galon = 3.78541
    milla = 1609.34
    return galon * miles / (100 * 1000 / milla)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))