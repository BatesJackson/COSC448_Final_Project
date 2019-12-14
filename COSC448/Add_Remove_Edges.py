# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:29:04 2019

@author: Jackson
"""
import sys
import networkx as nx
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def remove_percent_edges(G, percent):
    iterations = int((percent / 100) * len(list(G.edges)))
    #print('iterations: ', iterations) 
    for x in range(iterations):
        upper_bound = len(list(G.edges)) - 1
        randIndex = random.randint(0, upper_bound)
        edges = list(G.edges)
        #print('rand index: ', randIndex)
        #print('removing: ', *edges[randIndex])
        G.remove_edge(*edges[randIndex])
        
def add_percent_edges(G, percent):
    print('Total edge count start: ', len(list(G.edges)))
    iterations = int((percent / 100) * len(list(G.edges)))
    for x in range(iterations):
        edges = sorted(list(G.edges))
        non_edges = list(nx.non_edges(G))
        chosen_non_edge = random.choice(non_edges)
        print('Chosen edge to add: ', chosen_non_edge)
        print('List of current edges: ', edges)
        G.add_edge(*chosen_non_edge)
   
    print('Total edge count end: ', len(list(G.edges)))

for x in range(10):
    G = nx.read_graphml('hiv.graphml')
    remove_percent_edges(G, 1)
    nx.write_graphml_lxml(G, "graphs/hiv-remove-1-"+str(x+1)+".graphml")

for x in range(10):
    G = nx.read_graphml('hiv.graphml')
    remove_percent_edges(G, 5)
    nx.write_graphml_lxml(G, "graphs/hiv-remove-5-"+str(x+1)+".graphml")
    
for x in range(10):
    G = nx.read_graphml('hiv.graphml')
    remove_percent_edges(G, 10)
    nx.write_graphml_lxml(G, "graphs/hiv-remove-10-"+str(x+1)+".graphml")
    
for x in range(10):
    G = nx.read_graphml('hiv.graphml')
    remove_percent_edges(G, 1)
    nx.write_graphml_lxml(G, "graphs/hiv-add-1-"+str(x+1)+".graphml")

for x in range(10):
    G = nx.read_graphml('hiv.graphml')
    remove_percent_edges(G, 5)
    nx.write_graphml_lxml(G, "graphs/hiv-add-5-"+str(x+1)+".graphml")
    
for x in range(10):
    G = nx.read_graphml('hiv.graphml')
    remove_percent_edges(G, 10)
    nx.write_graphml_lxml(G, "graphs/hiv-add-10-"+str(x+1)+".graphml")