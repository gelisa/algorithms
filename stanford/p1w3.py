#karger mimal cut of graphs

def readFile(filename):
    """
    makes a dictionary representation of the graph
    {node: list of nodes []}
    example:
    {1: [2,3,4], 2:[1,4], 3:[1], 4:[1,2]}
    also makes a set of all the vertices in the graph
    :param filename:
    :return: dict. links, set vertices
    """
    links = {}
    vertices = set([])
    f = open(filename,'r')
    for line in f:
        lLine = line.split('\t')
        lLine = [int(item) for item in lLine[:len(lLine)-1]]
        links[lLine[0]] = lLine[1:]
        vertices = vertices.union(set(lLine))

    return links, vertices





links, vertices = readFile('p1w3.txt')


