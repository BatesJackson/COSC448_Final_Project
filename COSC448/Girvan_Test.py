import networkx as nx
import random
import matplotlib.pyplot as plt
from collections import defaultdict

# The code for Girvan Newman was sourced from https://www.youtube.com/watch?v=5P7ZCk3GM2o&t=609s

def edge_to_remove(G):
    dict1 = nx.edge_betweenness_centrality(G)
    list_of_tuples = sorted(dict1.items(), key = lambda x:x[1], reverse = True)
    print('removing edge: ', list_of_tuples[0][0])
    return(list_of_tuples[0][0])
    
def girvan(G):
    c = nx.connected_component_subgraphs(G)
    l = sum(1 for x in c)
    
    while(l <= 2):
        G.remove_edge(*edge_to_remove(G))
        c = nx.connected_component_subgraphs(G)
        l = sum(1 for x in c)       
    return c

def find_longest(list):
    length = [len(i) for i in list]
    return(max(length))
    
def getSimilarityScore(graph_list):
    simScore = 0
    for x in graph_list:
        graph = nx.read_graphml(x + '.graphml')
        #graph_edgelist = list(nx.generate_edgelist(graph, data = False ))
        girvan_graph = girvan(graph)
        clusters = list(nx.connected_component_subgraphs(graph))
        largest_cluster_graph = max(clusters, key=len)  
        intersections = len(set(largest_cluster_graph).intersection(set(largest_cluster_G)))
        simScore = simScore + ((intersections * 2) / (len(largest_cluster_graph) + len(largest_cluster_G)))
        print(simScore)
    avgSimScore = simScore/5
    return avgSimScore
    
G = nx.read_graphml("graphs/hiv-girvan.graphml")
girvan_clusters = list(nx.connected_component_subgraphs(G))
largest_cluster_G = max(girvan_clusters, key=len)
print(largest_cluster_G)

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

print('ADD: ', add_sim_list)
print('REMOVE: ', remove_sim_list)


plt.figure(1)
plt.ylim(0,1)
plt.bar(add_names, add_sim_list)

plt.figure(2)
plt.ylim(0,1)
plt.bar(remove_names, remove_sim_list)

plt.show()



