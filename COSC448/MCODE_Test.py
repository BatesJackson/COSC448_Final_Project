import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import defaultdict

#The code for MCODE Was found at https://github.com/trueprice/python-graph-clustering/tree/master/src

WEIGHT_THRESHOLD = 0.2

WEIGHT_THRESHOLD = 1 - WEIGHT_THRESHOLD

def remove_percent_edges(G, percent):
    iterations = int((percent / 100) * len(list(G.edges)))    
    for x in range(iterations):
        upper_bound = len(list(G.edges)) - 1
        randIndex = random.randint(0, upper_bound)
        edges = list(G.edges)
        G.remove_edge(*edges[randIndex])
        
def add_percent_edges(G, percent):
    print('Totale edge count start: ', len(list(G.edges)))
    iterations = int((percent / 100) * len(list(G.edges)))
    for x in range(iterations):
        edges = sorted(list(G.edges))
        non_edges = list(nx.non_edges(G))
        chosen_non_edge = random.choice(non_edges)
        print('Chosen edge to add: ', chosen_non_edge)
        print('List of current edges: ', edges)
        G.add_edge(*chosen_non_edge)
   
    print('Totale edge count end: ', len(list(G.edges)))
    



def mcode(g):
  edges = defaultdict(set) # node id => neighboring node ids
  for edge in g:
      a,b = edge.split()[:2]
      edges[a].add(b)
      edges[b].add(a)
  print('graph loaded; %i nodes' % (len(edges),))
  
  # Stage 1: Vertex Weighting
  print('vertex weighting...')
  weights = dict((v,1.) for v in edges)
  for i,v in enumerate(edges):
    if i % 1000 == 0: print(i)
    neighborhood = set((v,)) | edges[v]
    # if node has only one neighbor, we know everything we need to know
    if len(neighborhood) <= 2: continue

    # see if larger k-cores exist
    k = 1 # highest valid k-core
    while neighborhood:
      k_core = neighborhood.copy()
      invalid_nodes = True
      while invalid_nodes and neighborhood:
        invalid_nodes = set(
          n for n in neighborhood if len(edges[n] & neighborhood) <= k)
        neighborhood -= invalid_nodes
      k += 1 # on exit, k will be one greater than we want
    # vertex weight = k-core number * density of k-core
    weights[v] = (k-1) * (sum(len(edges[n] & k_core) for n in k_core) / 
      (2. * len(k_core)**2))

  # Stage 2: Molecular Complex Prediction
  print('molecular complex prediction')
  unvisited = set(edges)
  num_clusters = 0
  cluster_list = []
  for seed in sorted(weights, key=weights.get, reverse=True):
    if seed not in unvisited: continue

    cluster, frontier = set((seed,)), set((seed,))
    w = weights[seed] * WEIGHT_THRESHOLD
    while frontier:
      cluster.update(frontier)
      unvisited -= frontier
      frontier = set(
        n for n in set.union(*(edges[n] for n in frontier)) & unvisited
        if weights[n] > w)

    # haircut: only keep 2-core complexes
    invalid_nodes = True
    while invalid_nodes and cluster:
      invalid_nodes = set(n for n in cluster if len(edges[n] & cluster) < 2)
      cluster -= invalid_nodes

    if cluster:
      # fluff never really seems to improve anything...
      #cluster.update(
      # n for n in set.union(*(edges[c] for c in cluster)) & unvisited
      # if densities[n] > FLUFF_THRESHOLD)
      #print(cluster)
      #print (' '.join(cluster))
      cluster_list.append(cluster)
      num_clusters += 1
      #print(num_clusters, len(cluster), seed)
  return cluster_list

def find_longest(list):
    length = [len(i) for i in list]
    return(max(length))
    
def getSimilarityScore(graph_list):
    simScore = 0
    for x in graph_list:
        graph = nx.read_graphml(x + '.graphml')
        graph_edgelist = list(nx.generate_edgelist(graph, data = False ))
        mcode_graph = mcode(graph_edgelist)
        largest_cluster_graph = max(mcode_graph, key=len)  
        intersections = len(set(largest_cluster_graph).intersection(set(largest_cluster_G)))
        simScore = simScore + ((intersections * 2) / (len(largest_cluster_graph) + len(largest_cluster_G)))
        print(simScore)
    avgSimScore = simScore/10
    return avgSimScore
    
G = nx.read_graphml('graphs/hiv.graphml')
G_edgelist = list(nx.generate_edgelist(G, data = False ))
mcode_G = mcode(G_edgelist)
largest_cluster_G = max(mcode_G, key=len)

G_add_1_list = ['graphs/hiv-add-1-1', 'graphs/hiv-add-1-2', 'graphs/hiv-add-1-3','graphs/hiv-add-1-4','graphs/hiv-add-1-5'
                ,'graphs/hiv-add-1-6','graphs/hiv-add-1-7','graphs/hiv-add-1-8','graphs/hiv-add-1-9','graphs/hiv-add-1-10']

G_add_5_list = ['graphs/hiv-add-5-1', 'graphs/hiv-add-5-2', 'graphs/hiv-add-5-3','graphs/hiv-add-5-4','graphs/hiv-add-5-5'
                ,'graphs/hiv-add-5-6','graphs/hiv-add-5-7','graphs/hiv-add-5-8','graphs/hiv-add-5-9','graphs/hiv-add-5-10']

G_add_10_list = ['graphs/hiv-add-10-1', 'graphs/hiv-add-10-2', 'graphs/hiv-add-10-3','graphs/hiv-add-10-4','graphs/hiv-add-10-5'
                ,'graphs/hiv-add-10-6','graphs/hiv-add-10-7','graphs/hiv-add-10-8','graphs/hiv-add-10-9','graphs/hiv-add-10-10']

G_remove_1_list = ['graphs/hiv-remove-1-1', 'graphs/hiv-remove-1-2', 'graphs/hiv-remove-1-3', 'graphs/hiv-remove-1-4','graphs/hiv-remove-1-5',
                   'graphs/hiv-remove-1-6','graphs/hiv-remove-1-7','graphs/hiv-remove-1-8','graphs/hiv-remove-1-9','graphs/hiv-remove-1-10',]

G_remove_5_list = ['graphs/hiv-remove-5-1', 'graphs/hiv-remove-5-2', 'graphs/hiv-remove-5-3', 'graphs/hiv-remove-5-4','graphs/hiv-remove-5-5',
                   'graphs/hiv-remove-5-6','graphs/hiv-remove-5-7','graphs/hiv-remove-5-8','graphs/hiv-remove-5-9','graphs/hiv-remove-5-10',]

G_remove_10_list = ['graphs/hiv-remove-10-1', 'graphs/hiv-remove-10-2', 'graphs/hiv-remove-10-3', 'graphs/hiv-remove-10-4','graphs/hiv-remove-10-5',
                   'graphs/hiv-remove-10-6','graphs/hiv-remove-10-7','graphs/hiv-remove-10-8','graphs/hiv-remove-10-9','graphs/hiv-remove-10-10',]

remove_sim_list = [0,0,0]
add_sim_list = [0,0,0]

add_names = ['add_1%', 'add_5%', 'add_10%']
remove_names =['remove_1%','remove_5%', 'remove_10%']

add_sim_list[0] = getSimilarityScore(G_add_1_list)
add_sim_list[1] = getSimilarityScore(G_add_5_list)
add_sim_list[2] = getSimilarityScore(G_add_10_list)

remove_sim_list[0] = getSimilarityScore(G_remove_1_list)
remove_sim_list[1] = getSimilarityScore(G_remove_5_list)
remove_sim_list[2] = getSimilarityScore(G_remove_10_list)

yaxis = [0,0.2,0.4,0.6,0.8,1.0]

print(add_sim_list)
print(remove_sim_list)

plt.figure(1)
plt.ylim(0, 1)
plt.bar(add_names, add_sim_list)

plt.figure(2)
plt.ylim(0, 1)
plt.bar(remove_names, remove_sim_list)

plt.show()

