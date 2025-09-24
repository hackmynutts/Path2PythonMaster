import os, csv
ruta=r"C:/Users/jorge/OneDrive/Escritorio/DEV/Path2PythonMaster/REAL PYTHON BOOK/csv files/"

with open(ruta +"movies.csv", "r") as myInput:
    myFileReader = csv.reader(myInput)
    myFileReader.__next__()
    for movie, rating in myFileReader:
        highestRated = 0
        if float(rating) > highestRated:
            highestRated = float(rating)
            bestMovie = movie

print(f"The highest rated movie is {bestMovie} with a rating of {highestRated}")