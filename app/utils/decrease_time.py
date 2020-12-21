from datetime import datetime, timedelta


def decrease_time(minutes):
    try:
        decreased_time = datetime.now() - timedelta(hours=0, minutes=minutes)
        decreased_local_time = str(decreased_time.isoformat(timespec='microseconds')) + str("+5:30")
        return decreased_local_time
    except Exception as e:
        print(e)
        return None