import requests
import json

Tolls_URL = "https://dev.tollguru.com/v1/calc/here"
Tolls_Key = "3dHq68mqt9LL3gPnGRFnrB7dmtgQ9Qq9"


def AutoTollPayment(origin, destination):
    try:
        ROUTEDETAILS = "From {origin} location to {destination} location we have {toll} Number of tolls and it will " \
                       "take {duration} time to reach"
        params = {'from': {'address': '{}'.format(origin)}, 'to':{'address':'{}'.format(destination)},
                  'vehicleType': '2AxlesAuto'}
        print(params)
        headers = {'Content-type': 'application/json','x-api-key': Tolls_Key}
        response = requests.post(Tolls_URL, json=params, headers=headers)
        response = json.loads(response.text)
        print(response)
        print(type(response))
        ROUTEDETAILS = ROUTEDETAILS.format(origin=origin,destination=destination,
                                           toll=len(response["routes"][0]["tolls"]), duration=response["routes"][0][
                "summary"]["duration"]["text"].replace("h", "hours"))
        print(ROUTEDETAILS)
        # prepare_voice_output(ROUTEDETAILS)
    except Exception as e:
        print(e)
        # prepare_voice_output(WRONGLOCATIONEXCEPTION)


import requests


def fetch_hospitals():
    URL = "https://discover.search.hereapi.com/v1/discover"
    latitude = 12.96643
    longitude = 77.5871
    api_key = 'Fg3ACCJE0FKnjuw81OMMr-Rn4gzlMywcphoEbLPKnwo' # Acquire from developer.here.com
    query = 'hospitals'
    limit = 5

    PARAMS = {
                'apikey':api_key,
                'q':query,
                'limit': limit,
                'at':'{},{}'.format(latitude,longitude)
             }

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)
    data = r.json()
    print(data)


    hospitalOne = data['items'][0]['title']
    hospitalOne_address =  data['items'][0]['address']['label']
    hospitalOne_latitude = data['items'][0]['position']['lat']
    hospitalOne_longitude = data['items'][0]['position']['lng']


    hospitalTwo = data['items'][1]['title']
    hospitalTwo_address =  data['items'][1]['address']['label']
    hospitalTwo_latitude = data['items'][1]['position']['lat']
    hospitalTwo_longitude = data['items'][1]['position']['lng']

    hospitalThree = data['items'][2]['title']
    hospitalThree_address =  data['items'][2]['address']['label']
    hospitalThree_latitude = data['items'][2]['position']['lat']
    hospitalThree_longitude = data['items'][2]['position']['lng']


    hospitalFour = data['items'][3]['title']
    hospitalFour_address =  data['items'][3]['address']['label']
    hospitalFour_latitude = data['items'][3]['position']['lat']
    hospitalFour_longitude = data['items'][3]['position']['lng']

    hospitalFive = data['items'][4]['title']
    hospitalFive_address =  data['items'][4]['address']['label']
    hospitalFive_latitude = data['items'][4]['position']['lat']
    hospitalFive_longitude = data['items'][4]['position']['lng']


def here_sample():
    import requests

    URL = "https://geocode.search.hereapi.com/v1/geocode"
    location = input("Enter the location here: ")  # taking user input
    api_key = 'sUuQDiOpUUKFmd0p8zN0aGEz-542MN9300h45tOdgTs'  # Acquire from developer.here.com
    PARAMS = {'apikey': api_key, 'q': location}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    print(data)

    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']



if __name__ == '__main__':
    AutoTollPayment(origin="Mumbai", destination="Pune")
    # fetch_hospitals()
    # here_sample()