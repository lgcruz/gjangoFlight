import csv

def csv_to_dict():
    reader = (open("Flying//aeropuertos.dat"))
    writer = open("Flying//aeropuertos2.dat","w")
    result = {}
    for row in reader:
        if ("\"" in row):
           row=row.replace("\"","")
        writer.write(row)
    reader.close()
    writer.close()