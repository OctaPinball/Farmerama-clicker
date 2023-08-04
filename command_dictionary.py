from map import Map
import map_data as md

def create_sub_tree(tree, subtree):
        newtree = []
        for t in tree:
                newtree.append((t, subtree))
        return newtree

md.load_maps()

tree = [('1: Run predefined commands'),
        ('2: Run quick command',
                [('1: Harvest', md.map_names),
                 ('2: Harvest and feed', md.map_names),
                 ('3: Watering', md.map_names),
                 ('4: Sowing', create_sub_tree(md.map_names, ['0','1','2','3','4','5','6','7']))]),
        '3: Create new predefined commands']

command_dictionary = {
                        0: Map.harvest,
                        1: Map.harvest_and_feed,
                        2: Map.watering,
                        3: Map.sowing
                      }

