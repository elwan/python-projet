import pymongo as modb
myclient = modb.MongoClient("mongodb://10.1.5.20:27017")
apisdb = myclient["api"]
mydoc =apisdb["flights"]

#find_one()
#data = mydoc.find_one()
#print (type(data))
#print(len(data))
#print(data['passenger_count'])
#print(data['flightNumber'])
#print(data['flight_date'])
#print(data['FromAirport']['iata'])
#print(data['ToAirport']['iata'])
#print(len(data['passengers']))

paxquery = {"created_at" : {"$gte":"2020-03-01T00:00:00", "$lte":"2020-03-29T00:00:00"}}
data=mydoc.find(paxquery)
#print(len(data))

def get_fligthdata(flight):
    dataflight=flight #initialise flights
    numberchild = numberofchild(dataflight['passengers'])#compute number of child 
    dictdata = dict(NumberPax=dataflight['passenger_count'],NumberFlight=dataflight['flightNumber'],DateFlight=dataflight['flight_date'],FromAirport=dataflight['FromAirport']['iata'],ToAirport=dataflight['ToAirport']['iata'],NumberChild=numberchild)
    
    return dictdata

def numberofchild(paxdata):
    #iterateurs = len(data['passengers'])
    number_child =0
    passengers = paxdata
    iterateurs = len(passengers)
    for i in range(iterateurs):
        if int(passengers[i]['age']) <= 2:
            number_child +=1
    return number_child

#n=numberofchild(data['passengers'])
#print(n)
for x in data:
    print(get_fligthdata(x))
