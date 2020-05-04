"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.dataset import GraphReader
from littleballoffur.node_sampling import RandomWalkNodeSampler 
 
#--------------------------------
# Random Walk Node Sampler example
#--------------------------------

reader = GraphReader("twitch")

graph = reader.get_graph()

sampler = RandomWalkNodeSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))
