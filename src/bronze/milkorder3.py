import glob
import copy
from heapq import heapify, heappop, heappush

def topological_order(graph): 
    # Copy of graph with all edges reversed.
    reversed_graph = {v:set() for v in graph}
    for v, outgoing in graph.items():
        for w in outgoing:
            reversed_graph[w].add(v)

    # Topological order.
    order = []

    # Heap of sources (vertices with no incoming edges).
    sources = [v for v, incoming in reversed_graph.items() if not incoming]
    heapify(sources)

    while sources:
        v = heappop(sources)
        order.append(v)
        for w in graph[v]:
            incoming = reversed_graph[w]
            incoming.remove(v)
            if not incoming:
                heappush(sources, w)

    if any(reversed_graph.values()):
        # Some edges remain, hence there's a cycle in the graph.
        return False, None
    else:
        return True, order

def mooSort(currentSort, fullGraphOUT, fullGraphIN, numCows): 
    noIncoming = [] #keep a list of vertices with no incoming edges
    newSort = [] #the topologically sorted vertices
    newGraphIN = copy.deepcopy(fullGraphIN)
    newGraphOUT = copy.deepcopy(fullGraphOUT)

    for k in range(1,numCows+1):
        if not newGraphIN[k]:
            noIncoming.append(k) 
            del newGraphIN[k] #use this to keep track of if the graph has edges at the end

    while noIncoming: #take each element with no incoming edges and add it to our sort, remove it from the graph
        noIncoming.sort() #sorting so we can make it lexicographic as well
        m = noIncoming[0] 
        noIncoming.pop(0)
        newSort.append(m)
        for k in newGraphOUT[m]:
            newGraphIN[k].remove(m)
            if not newGraphIN[k]: #if there are no more incoming edges, we put it into noincoming
                noIncoming.append(k)
                del newGraphIN[k]
    if newGraphIN: #there's a cycle in the graph
        return False 
    else: #no cycles
        currentSort[:] = newSort #set the current sort to this one
        return True

#now do this in a binary search


with open("milkorder.in", "r") as data:
    lines = data.readlines()
   #turn the lines into a list of list ints
    inputData=[list(map(int,line.split())) for line in lines]
    numCows = inputData[0][0]
    numConditions = inputData[0][1]
#     inputData.pop(0)
    fullGraphOUT = {} #describe graph by outgoing neighbors
    fullGraphIN = {} #describe graph by incoming neighbors
    currentSort = [] #keep track of our current sorting
    for i in range(1,numCows+1): #initialize the graph to empty
       fullGraphOUT[i] = set()
       fullGraphIN[i] = set()
    for list in inputData:
        list.pop(0)
        for k in list: 
            for j in list[list.index(k)+1:]: 
                fullGraphOUT[k].add(j)
                fullGraphIN[j].add(k)
        if topological_order(graph): #once this gives false, we can no longer sort using all the conditions
          print(currentSort)
          break
    print(currentSort)
