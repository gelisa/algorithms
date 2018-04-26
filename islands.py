def get_squares(rn,cn,map_size):
    """
    
    """
    return [x for x in [(rn-1,cn),(rn,cn+1),(rn+1,cn),(rn,cn-1)] if if_legit_square(x,map_size)]

def if_legit_square(coord_pair,map_size):
    rn = coord_pair[0]
    cn = coord_pair[1]
    if rn >= 0 and cn >= 0 and rn < map_size[0] and cn < map_size[1]:
        return True
    else:
        return False

def explore_nearby(rn,cn,set_of_visited,isl_map,visited):
    squares_to_check = get_squares(rn,cn,map_size)
    #print(set_of_visited)
    for sq in squares_to_check:
        if not sq in set_of_visited:
            visited[sq[0],sq[1]] = 1
            if isl_map[sq[0],sq[1]] == 0:
                pass
            else:
                set_of_visited.add(sq)
                explore_nearby(sq[0],sq[1],set_of_visited,isl_map,visited)
        else:
            pass
    
def explore_island(rn,cn,isl_map,visited):
    set_of_visited = set([(rn,cn)])
    explore_nearby(rn,cn,set_of_visited,isl_map,visited)
            
    #print(squares_to_check)

    
def count_islands(isl_map):
    """
    isl_map np.matrix
    """
    islands_count = 0
    map_size = isl_map.shape
    #initialize visited matrix with 0
    visited = np.zeros(map_size)
    #print('{}\t{}\t{}\t{}'.format('rn','cn','map','vis'))
    #for every row
    for rn in range(map_size[0]):
        #for every column
        for cn in range(map_size[1]):
            #print('{}\t{}\t{}\t{}'.format(rn,cn,isl_map[rn,cn],visited[rn,cn]))
            # if we have visited the square: ignoe
            if visited[rn,cn] == 1:
                pass
            # otherwise
            else:
                # mark as visited
                visited[rn,cn] = 1
                # if it happens to be an island
                if isl_map[rn,cn] == 1:
                    # switch new island to True
                    print('new island at {},{}'.format(rn,cn))
                    explore_island(rn,cn,isl_map,visited)
                    islands_count += 1
                else:
                    pass
    return islands_count
