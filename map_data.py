from map import Map

maps = []

def load_maps():
    file = open("map.txt", 'r')
    f = file.readlines()
    data = {}
    for line in f:
        list = line.strip().split(',')
        if len(list) == 1:
            if len(data) != 0:
                maps.append(Map(data['name'], data['map'], data['access'], data.get('water'), data.get('sub_access'), data.get('escape')))
            data = {}
            data['name'] = list[0]
        else:
            data[list[0]] = (int(list[1]), int(list[2]))