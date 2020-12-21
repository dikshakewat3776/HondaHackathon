import reverse_geocoder as rg
from geopy.geocoders import Nominatim
import json


def reverseGeocode(coordinates):
    result = rg.search(coordinates)
    r = json.loads(json.dumps(result))
    res_dict = r[0]
    del res_dict['lat']
    del res_dict['lon']
    res = []
    for key in res_dict.keys():
        res.append(res_dict[key])
    address = ' '.join([str(elem) for elem in res])
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(address)
    data = location.raw
    loc_data = data['display_name'].split()
    zip_code = loc_data[-2].strip(',')
    return address + ' ' + zip_code


# Driver function
if __name__ == "__main__":
    # Coorinates tuple.Can contain more than one pair.
    coordinates = (12.71219, 77.89142)
    address = reverseGeocode(coordinates)
    print("The address is: " + str(address))
