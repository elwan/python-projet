from flask import Flask , request,jsonify,make_response
from flask_restplus import Api,Resource
import pymongo as modb

myclient = modb.MongoClient("") # acces to remote database apis backup

apisdb = myclient["api"] #acces to database

mydoc =apisdb["flights"] #acces to documents in database apis
code_iata_cdeao =['DSS','ABJ','OUA','COO','BJL','ACC','CKY','FNA','BKO','NIM','LOS','MLW','LFW','RAI','OXB']
#paxquery = {"created_at" : {"$gte":"2020-03-01T00:00:00", "$lte":"2020-03-29T00:00:00"}} # right format to filter data in mongodb database

app = Flask(__name__)

api = Api(app=app, version='0.1' , title='flightstats Api' , description = '' , validate =True)

@api.route("/flights/", )
class FlightList(Resource):
#http://127.0.0.1:5000/flights/?debutdate=2020-03-01&enddate=2020-03-12
    def get(self):
        debutdate = request.args.get("debutdate") #get date passing in agrs
        enddate = request.args.get("enddate") # get date passing in args
        data = [] #initialise list of data
        """Return list of flights"""
        paxquery = {"created_at" : {"$gte":debutdate+"T00:00:00", "$lte":enddate+"T00:00:00"}} #query list flights filtered by date
        cursor = mydoc.find(paxquery) #get query in mongodb database
        for flight in cursor:
            data.append(self.get_flightdata(flight)) #append each  flights in list
        return {"response": data} # return list of flights in json format
        #return jsonify(data)

#get anonymous data
    def get_flightdata(self,flight):
        dataflight=flight

        numberchild = self.numberofchild(dataflight['passengers']) # get number of child
        #get number of pax cedeao
        number_pax_cedeao= self.cedeaoflight(dataflight['passengers'])
        numer_pax_nocedeao = int(dataflight['passenger_count']) - int(number_pax_cedeao)
        #anonymise request from apis database on items related in carrier was getted
        dictdata = dict(NumberPax=dataflight['passenger_count'],NumberFlight=dataflight['flightNumber'],DateFlight=dataflight['flight_date'],FromAirport=dataflight['FromAirport']['iata'],ToAirport=dataflight['ToAirport']['iata'],NumberChild=numberchild,NumberPaxCedeao=number_pax_cedeao,NumberPaxNocedeao=numer_pax_nocedeao)

        return dictdata
#function to compute nomber of child in each passengers line
    def numberofchild(self,paxdata):
    #iterateurs = len(data['passengers'])
        number_child =0
        passengers = paxdata
        iterateurs = len(passengers)
        for i in range(iterateurs):
            if int(passengers[i]['age']) <= 2:
                number_child +=1
        return number_child
#function to compute if flight was in cedeao area or not
    def cedeaoflight(self,paxdata):
        #Code country
        code_iata_cdeao =['DSS','ABJ','OUA','COO','BJL','ACC','CKY','FNA','BKO','NIM','LOS','MLW','LFW','RAI','OXB']
        #initialize number of paxcedeao
        cedeaopax=0
        flight = paxdata
        iterateurs = len(flight)
        for i in range(iterateurs):
            departure =flight[i]['api']['embarkation'] #get depature pax
            arrival =flight[i]['api']['debarkation'] #get arrival pax
            if departure in code_iata_cdeao and arrival in code_iata_cdeao : #appartenace test in cedeao list
                cedeaopax +=1 #countup
        return cedeaopax

if __name__ == '__main__' :
    app.run(debug=True,host= '0.0.0.0',port = 5050)
