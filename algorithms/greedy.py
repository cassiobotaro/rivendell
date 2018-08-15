'''Greedy algorithms module'''


def _best_coverage(stations, states_to_cover):
    '''Return station and coverage states for best coverage.'''
    best_station = None
    coverage_states = {}
    for station, states in stations.items():
        coverage = states_to_cover & states
        if len(coverage) > len(coverage_states):
            best_station = station
            coverage_states = coverage
    return best_station, coverage_states


def optimize_stations(stations, states_to_cover):
    '''List stations to cover all states.'''
    final_stations = set()
    while states_to_cover:
        best_station, coverage_states = _best_coverage(stations)
        states_to_cover -= coverage_states
        final_stations.add(best_station)
    return final_stations


def main():
    '''Given states to cover and stations, pick less stations that cover
    all states.'''
    states_to_cover = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

    stations = {}
    stations['kone'] = {'id', 'nv', 'ut'}
    stations['ktwo'] = {'wa', 'id', 'mt'}
    stations['kthree'] = {'or', 'nv', 'ca'}
    stations['kfour'] = {'nv', 'ut'}
    stations['kfive'] = {'ca', 'az'}
    print("Stations: ", optimize_stations(stations, states_to_cover))


if __name__ == "__main__":
    main()
