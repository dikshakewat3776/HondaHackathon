import requests
import json
from HondaHackathon.app.utils.lat_long_to_address import reverseGeocode

Tolls_URL = "https://dev.tollguru.com/v1/calc/here"
Tolls_Key = "3dHq68mqt9LL3gPnGRFnrB7dmtgQ9Qq9"


def fetch_nearest_toll_location(origin, destination):
    try:
        params = {'from': {'address': '{}'.format(origin)}, 'to': {'address': '{}'.format(destination)},
                  'vehicleType': '2AxlesAuto'}
        headers = {'Content-type': 'application/json', 'x-api-key': Tolls_Key}
        response = requests.post(Tolls_URL, json=params, headers=headers)
        response = json.loads(response.text)
        a = response.get('summary').get('route')[0].get('location')
        coordinates = tuple(a.values())
        address = reverseGeocode(coordinates)
    except Exception as e:
        address = None
        print(e)
    return address


if __name__ == "__main__":
    address = fetch_nearest_toll_location(origin="Mumbai", destination="Pune")
    print("The address is: " + str(address))