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
        return jsonify({'message': 'price should be an integer'}), 400
    return jsonify({'message': 'post successful'}), 201   




    
if __name__ == '__main__':
    app.run(debug=True)        

