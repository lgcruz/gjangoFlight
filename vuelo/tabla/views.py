from django.shortcuts import render
from pymongo import MongoClient

# DB connectivity

# Create your views here.
def tabla(request):
    client = MongoClient('localhost', 27017)
    db = client.get_database(name="daw")
    #collection = db.get_collection(name="aerolineas")
    #rutas = db.get_collection(name="routes")
    #puertos = db.get_collection(name="aeropuertos")
    dicci = {}
    listaO = []

    listaAli=[]
    listaAliP = []
    listaAeropO =[]
    listaAeropD=[]
    for i in db.aerolineas.find():
        if (( not i["Country"].isupper())and(len(i["Country"]) != 0) and (i["Country"] not in listaO)):
            listaO.append(i["Country"])

    dicci["countriesO"]=listaO
    dicci["countriesD"] = listaO
    if request.method == "POST":

        origen = request.POST["origen"]
        destino = request.POST["destino"]
        stops = int(request.POST["vuelo"])
        aeropuertosOrigen={}
        aeropuertosDestino = {}

        for aeropuerto in db.aeropuertos.find({'Country':origen}):
            aeropuertosOrigen[aeropuerto['Airport ID']]=aeropuerto['Name of airport']
        for aeropuerto in db.aeropuertos.find({'Country':destino}):
            aeropuertosDestino[aeropuerto['Airport ID']] = aeropuerto['Name of airport']

        for i in db.routes.find({'Stops':stops,'Source airport ID': { '$in' :list(aeropuertosOrigen.keys())},
                'Destination airport ID': { '$in': list(aeropuertosDestino.keys())}}):
            if i['Airline ID'] != '\\N' and i['Airline ID'] not in listaAli:
                listaAli.append(i['Airline ID'])
        #for i in db.aerolineas.find({'Airline ID':{'$in':listaAli}}):
            #print(i['Name']+" "+ i['IATA']+" "+ i['Country'])
        #    listaAliP.append([i['Airline ID'],i['Name'], i['IATA'], i['Country'],origen,destino])

        dicci["aerolineas"]=db.aerolineas.find({'Airline ID':{'$in':listaAli}})
        #print(origen+" "+destino+" ",stops)


    return render(request,"html/Flying.html",dicci)