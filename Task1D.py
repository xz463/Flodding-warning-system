# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Test for 1D1, 1D2"""

    # testing function rivers_with_station
    stations = build_station_list()

    print(len(rivers_with_station(stations)))
    print(rivers_with_station(stations)[:10])

    # testing function stations_by_river
    list = ['River Aire', 'River Cam', 'River Thames']
    for item in stations_by_river(list):
        print(stations_by_river(list)[item])

    """
    river_station = stations_by_river(list)
    
    
    for key in river_station:
        # s = river_station[key].sort()
        river_station[key].sort()
        print(river_station[key])
    """


if __name__ == "__main__":
    run()

