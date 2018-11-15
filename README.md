#"*SENDIT*" 
~~~
SENDIT API endpoints
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT
provides courier quotes based on weight categories.
~~~
#API endpoints

[![Build Status](https://travis-ci.org/RonaldMule/SENDIT.svg?branch=Developee)](https://travis-ci.org/RonaldMule/SENDIT)


~~~
##Required Features


    1. Create a parcel delivery order
    2. Get all parcel delivery orders
    3. Get a specific parcel delivery order
    4. Cancel a parcel delivery order
~~~

##Tools

~~~

    • Server-Side Framework: <Flask Python Framework>
    • Linting Library: <Pylint, a Python Linting Library>
        • Style Guide: <PEP8 Style Guide>
    • Testing Framework: <PyTest, a Python Testing Framework>
~~~

|     EndPoint 	                |                Functionality             | 
|_______________________________|__________________________________________|
|GET /parcels                   |Fetch all parcel delivery orders          |
|GET /parcels/<parcelId>        |Fetch a specific parcel delivery order    |
|GET /users/<userId>/parcels    |Fetch all parcel delivery orders by a specific user|
|PUT /parcels/<parcelId>/cancel |Cancel the specific parcel delivery order|
|POST /parcels                  |Create a parcel delivery order         |

