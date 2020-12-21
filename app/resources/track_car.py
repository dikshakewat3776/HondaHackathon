from datetime import datetime, timedelta
from HondaHackathon.app.utils.make_db_connection import execute_sql_query, DATABASE_CONFIGS
from HondaHackathon.app.utils.lat_long_to_address import reverseGeocode


MAX_MINUTES = 15


def get_coordinates(mobId, local_time):
    try:
        local_time = local_time[0:16]
        print("Get coordinates for mobId {} and local_time {}". format(mobId, local_time))
        lat = None
        long = None
        r = execute_sql_query("SELECT * FROM {}.mytable where mo_id='{}' and local_time like'%{}%'".format(
            DATABASE_CONFIGS['DB_NAME'], mobId, local_time))
        if r['Success']:
            if isinstance(r, dict):
                row = r['Row']
                print(row)
                if row is ():
                    return None
                else:
                    lat = row.get('latitude')
                    long = row.get('longitude')
        return lat, long
    except Exception as e:
        print(e)
        return None


def decrease_time(minutes):
    try:
        decreased_time = datetime.now() - timedelta(hours=0, minutes=minutes)
        decreased_local_time = str(decreased_time.isoformat(timespec='microseconds')) + str("+5:30")
        return decreased_local_time
    except Exception as e:
        print(e)
        return None


def track_car(mobId):
    try:
        address = None
        current_local_time = str(datetime.now().isoformat(timespec='microseconds')) + str("+5:30")

        if current_local_time:
            coordinates = get_coordinates(mobId=mobId, local_time=current_local_time)
            if coordinates is None:
                minutes = 1
                while minutes < MAX_MINUTES:
                    local_time = decrease_time(minutes=minutes)
                    coordinates = get_coordinates(mobId=mobId, local_time=local_time)
                    if coordinates is not None:
                        address = reverseGeocode(coordinates)
                        break
                    else:
                        minutes += 1
                        pass
            else:
                address = reverseGeocode(coordinates)
    except Exception as e:
        address = None
        print(e)
    print("The address is: " + str(address))
    return address


# Driver function
if __name__ == "__main__":
    address = track_car(mobId="MOBL153HHT0015627")
    print("The address is: " + str(address))
    # a = get_coordinates(mobId="MOBL153HHT0015627", local_time="2020-07-15T09:24:13.000+05:30")
    # print(a)