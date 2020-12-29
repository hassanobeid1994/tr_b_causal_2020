# -*- coding: utf-8 -*-
"""
Code for the Shared Ride 3+ Interacting Causal Graph in the
selection on observables section of the manuscript.
"""
import graphviz

# Shared Ride 3 Interacting Graph
SHARED_3P_INTERACTING_GRAPH = graphviz.Digraph(
    "Shared Ride 3+ Interacting Graph"
)
SHARED_3P_INTERACTING_GRAPH.attr(rankdir="TB")

# Edges
SHARED_3P_INTERACTING_GRAPH.edge("Number of Kids", "Utility (Shared Ride 3+)")
SHARED_3P_INTERACTING_GRAPH.edge(
    "Proposed Intervention",
    "Total Travel Distance",
    style="filled",
    color="red",
)
SHARED_3P_INTERACTING_GRAPH.edge(
    "Total Travel Distance",
    "Utility (Shared Ride 3+)",
    style="filled",
    color="red",
)
SHARED_3P_INTERACTING_GRAPH.edge(
    "Total Travel Distance", "Total Travel Time", style="filled", color="red"
)
SHARED_3P_INTERACTING_GRAPH.edge(
    "Total Travel Distance", "Total Travel Cost", style="filled", color="red"
)
SHARED_3P_INTERACTING_GRAPH.edge(
    "Total Travel Time",
    "Utility (Shared Ride 3+)",
    style="filled",
    color="red",
)
SHARED_3P_INTERACTING_GRAPH.edge("Number of Autos", "Utility (Shared Ride 3+)")
SHARED_3P_INTERACTING_GRAPH.edge("Household Size", "Utility (Shared Ride 3+)")
SHARED_3P_INTERACTING_GRAPH.edge(
    "Number of Licensed Drivers", "Utility (Shared Ride 3+)"
)
SHARED_3P_INTERACTING_GRAPH.edge("Cross Bay Trip", "Utility (Shared Ride 3+)")
SHARED_3P_INTERACTING_GRAPH.edge(
    "Total Travel Cost",
    "Utility (Shared Ride 3+)",
    style="filled",
    color="red",
)

# Nodes
SHARED_3P_INTERACTING_GRAPH.node(
    "Proposed Intervention", style="filled", color="white"
)
SHARED_3P_INTERACTING_GRAPH.node(
    "Total Travel Distance", style="outlined", color="red"
)
SHARED_3P_INTERACTING_GRAPH.node(
    "Total Travel Time", style="outlined", color="red"
)
SHARED_3P_INTERACTING_GRAPH.node(
    "Total Travel Cost", style="outlined", color="red"
)
SHARED_3P_INTERACTING_GRAPH.node(
    "Utility (Shared Ride 3+)", style="outlined", color="red"
)
