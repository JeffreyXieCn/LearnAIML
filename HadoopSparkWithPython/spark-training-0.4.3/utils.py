import math

def read_data(data_file):
    '''
    Read the 2D data points in data_file, , where each line is a 
    point, and the coordinates are space-separated.
    '''
    with open(data_file) as f:
        lines = f.readlines()
    points = [ ( float(str.split(line)[0]),
                 float(str.split(line)[1]) ) for line in lines ]
    return points

def plot_data(data_points, classes=[], initial_centroids=[], new_centroids=[]):
    '''
    Plots the 2D points passed in data_points.
    '''

    import matplotlib.pyplot as plt

    # Plot data points, then centroids (otherwise centroids may be masked)
    x = [ p[0] for p in data_points ]
    y = [ p[1] for p in data_points ]
    x += [ p[0] for p in initial_centroids ]
    y += [ p[1] for p in initial_centroids ]
    x += [ p[0] for p in new_centroids ]
    y += [ p[1] for p in new_centroids]
    assert(len(x) == len(y))
    assert(classes == [] or len(classes) == len(data_points))
    
    area = [ math.pi*6**2 for x in data_points ]
    area += [ 20 for x in initial_centroids ]
    area += [ 20 for x in new_centroids ]

    if not classes:
        color = [ 'gray' for x in data_points ]
    else:
         from matplotlib import colors as mcolors
         colors = [ x for x in list(mcolors.XKCD_COLORS.keys()) if x != 'xkcd:red' and x!= 'xkcd:black' ]
#         colors = [ 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan' ]        
         color = [ colors[ classes[i] % len(colors) ] for i in range(len(data_points)) ]
    color += [ 'black' for x in initial_centroids ]
    color += [ 'red' for x in new_centroids ]

    plt.scatter(x,y,c=color, s=area)
    return plt

def plot_states(color_map):
    import matplotlib.pyplot as plt
    import geopandas


    states_usa = geopandas.read_file('data/session2/geo/usa-states-census-2014.shp')
    states_ca = geopandas.read_file('data/session2/geo/canada.shp')

    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 24))

    ax1.set_xticks([])
    ax1.set_yticks([])
    ax2.set_xticks([])
    ax2.set_yticks([])

    for name in list(states_ca['PRENAME']):
        if color_map.get(name): 
            states_ca[states_ca['PRENAME'] == name].plot(color=color_map[name], ax=ax1)
    states_ca.boundary.plot(color='black', ax=ax1)

    for name in list(states_usa['NAME']):
        if color_map.get(name):
            states_usa[states_usa['NAME'] == name].plot(color=color_map[name], ax=ax2)
    states_usa.boundary.plot(color='black', ax=ax2)
    return plt

def convert_state(state_name):
    return state_abbr[state_name] 

def encode_plant_list(state_plants):
    from numpy import array
    vector = []
    for i in plant_list:
        if i in state_plants:
            vector += [ 1 ]
        else:
            vector += [ 0 ]
    return array(vector)

state_abbr = {}
with open('data/session2/plants/stateabbr.txt', 'r') as f:
    lines = f.readlines()
for line in lines:
    splits = line.split(" ")
    state_abbr[splits[0]] = (" ".join(splits[1:])).strip()

filename = 'data/session2/plants/plants.data'
plant_list = []
with open(filename, 'r', encoding='latin1') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    name = line.split(",")[0]
    plant_list += [ name ]