*SENDIT API endpoints
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories.

*End points

```

|           EndPoint            |                  Functionality   |                        

|     GET /parcels              |           Fetch all parcel delivery orders   |            
|GET /parcels/<parcelId>        |   Fetch a specific parcel delivery order    |             
|GET /users/<userId>/parcels    |Fetch all parcel delivery orders by a specific user|     

|PUT /parcels/<parcelId>/cancel |  Cancel the specific parcel delivery order|

|POST /parcels                  |  Create a parcel delivery order          |                

```
