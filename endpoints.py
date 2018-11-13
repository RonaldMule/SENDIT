from flask import Flask, request, jsonify  
from models.model import Parcel, parcel_order_list               
app = Flask(__name__)


@app.route("/api/v1/parcels", methods =['POST'])
def makeNewParcelOrder():
    data = request.get_json(force=True)
    try:
        
       parcels = Parcel(parcel_weight=data['parcel_weight'], pickup_location=data['pickup_location'], 
       destination=data['destination'], price=data['price'], status=data['status'])
       parcels.to_json()
    except ValueError as e:
        print(e)
        
    return jsonify({'message': 'post successful'}), 201 

@app.route("/api/v1/parcels", methods =['GET'])
def getAllParcelOrders(): 
    return jsonify({'parcels':parcel_order_list}), 200 

#another app.route() decorator here takes in an integer id
@app.route("/api/v1/parcels/<int:id>", methods = ['GET']) 
def singleParcelOrder(id):
    
    for parcel in parcel_order_list:
        if parcel['id'] == id: 
            parcel_order =parcel  
            return jsonify(parcel_order), 200
        
    return jsonify({'message': 'parce_id does not exist'})    


def updateParcelOrder(id):
    pass
def  deleteParcelOrder(id):
    pass   

if __name__ == '__main__':
    app.run(debug=True, port=5010)        

