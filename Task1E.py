from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Test function rivers_by_station_number"""
    
    print(rivers_by_station_number(build_station_list(),9))

if __name__ == "__main__":
    run()
