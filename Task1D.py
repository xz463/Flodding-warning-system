# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from unittest import result
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

    r = stations_by_river(stations)
    for key,value in r.items():
        if key in list:
            print (value)

if __name__ == "__main__":
    run()

