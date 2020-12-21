from datetime import datetime
from HondaHackathon.app.utils.make_db_connection import execute_sql_query, DATABASE_CONFIGS
from HondaHackathon.app.utils.lat_long_to_address import reverseGeocode
from HondaHackathon.app.utils.decrease_time import decrease_time

MAX_MINUTES = 15


def check_security(mobId, local_time):
    try:
        local_time = local_time[0:16]
        print("Get coordinates for mobId {} and local_time {}". format(mobId, local_time))
        r = execute_sql_query("SELECT * FROM {}.mytable where mo_id='{}' and propertiesLSecurityAlarm='{}' and "
                              "local_time like'%{}%'".format(DATABASE_CONFIGS['DB_NAME'], mobId, "ON", local_time))
        if r['Success']:
            if isinstance(r, dict):
                row = r['Row']
                print(row)
                if row is ():
                    return False
                else:
                    return True
    except Exception as e:
        print(e)
        return False


def contact_police():
    pass


def capture_stealer(mobId):
    contact_police_flag = False
    try:
        current_local_time = str(datetime.now().isoformat(timespec='microseconds')) + str("+5:30")

        if current_local_time:
            security_flag = check_security(mobId=mobId, local_time=current_local_time)
            if security_flag is False:
                minutes = 1
                while minutes < MAX_MINUTES:
                    local_time = decrease_time(minutes=minutes)
                    security_flag = check_security(mobId=mobId, local_time=local_time)
                    if security_flag is True:
                        contact_police()
                        contact_police_flag = True
                        break
                    else:
                        minutes += 1
                        pass
            else:
                contact_police()
                contact_police_flag = True
    except Exception as e:
        contact_police_flag = False
        print(e)
    finally:
        if contact_police_flag:
            state = True
        else:
            state = False
    return state


