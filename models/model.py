parcel_order_list = []

class Parcel:
    def __init__(self, parcel_weight, pickup_location, destination, price, status):
        self.id = id
        self.parcel_weight = parcel_weight
        self.pickup_location = pickup_location
        self.destination = destination
        self.price = price
        self.status = status
    #A propety to serialize information 
    def to_json(self):
        parcel_orders = {
                
                'parcel_weight':self.parcel_weight,
                'pickup_location': self.pickup_location,
                'destination': self.destination,
                'price': self.price,
                'status': self.status 
                  } 
        parcel_order_list.append(parcel_orders)
        

        

