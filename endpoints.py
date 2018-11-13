from flask import Flask, request, jsonify  
from models.model import Parcel, parcel_order_list               
app = Flask(__name__)

parcels = []
@app.route("/api/v1/parcels", methods =['GET','POST'])
def parcelOrders():
   if request.method == 'GET':
       #call the method to get all parcel orders
       return getAllParcelOrders()
   elif request.method == 'POST':
        #call the method to make new parcel order
        return makeNewParcelOrder()

#another app.route() decorator here takes in an integer id 
@app.route("/api/v1/parcels/<int:id>", methods = ['GET', 'PUT', 'DELETE']) 
def singleParcelOrder(id):
    if request.method == 'GET':
        #call a method to get a specific parcel order
        return getParcelOrder(id)
    if request.method == 'PUT':
        #call a method to update parcel order
        return updateParcelOrder(id)
    elif request.method == 'DELETE':
        #call the method to cancel parcel order
        return deleteParcelOrder(id)



def getAllParcelOrders():
    
    return jsonify({'parcels':parcel_order_list}), 200 
 

def makeNewParcelOrder():
    data = request.get_json(force=True)

    try:
        
       parcels = Parcel(parcel_weight=data['parcel_weight'], pickup_location=data['pickup_location'], 
       destination=data['destination'], price=data['price'], status=data['status'])
       parcels.to_json()
    except ValueError as e:
        print(e)
        
    return jsonify({'message': 'post successful'}), 201   

def getParcelOrder(id):
    for parcel in parcels:
        if parcel.parcel_id == parcel_id:   
            return jsonify(parcel), 200

def updateParcelOrder(id):
    pass
def  deleteParcelOrder(id):
    pass   

if __name__ == '__main__':
    app.run(debug=True)        

