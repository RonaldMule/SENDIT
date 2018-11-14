from flask import Flask, request, jsonify  
from models.model import Parcel, parcel_order_list               
app = Flask(__name__)


@app.route("/api/v1/parcels", methods =['POST'])
def makeNewParcelOrder():
    '''
    creating a parcel order
    '''
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


@app.route("/api/v1/parcels/<int:id>", methods = ['GET']) 
def singleParcelOrder(id):
    '''
    another app.route() decorator here takes in an integer id
    '''
    
    for parcel in parcel_order_list:
        if parcel['id'] == id: 
            parcel_order =parcel  
            return jsonify(parcel_order), 200
        
    return jsonify({'message': 'parce_id does not exist'})    

@app.route("/api/v1/parcels/<int:id>", methods = ['PUT']) 
def updateParcelOrder(id):
    '''
    updating status route
    '''
    data = request.get_json(force=True)
    for parcel in parcel_order_list:
        if parcel['id'] == id:
            parcel['status']= data['status']
               
            return jsonify(pa), 201
    return jsonify({'message': 'status update failed'})



if __name__ == '__main__':
    app.run(debug=True, port=5090)        

