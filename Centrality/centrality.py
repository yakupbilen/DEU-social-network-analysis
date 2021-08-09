# Find and visualize Centrality values

import networkx as nx
import pandas as pd
from pyvis.network import Network
from bokeh.models import Range1d, Circle, MultiLine, HoverTool, BoxSelectTool, TapTool
from bokeh.plotting import figure, show, from_networkx
from bokeh.io import output_file
from bokeh.models.graphs import NodesAndLinkedEdges
from bokeh.palettes import Magma6


df = pd.read_csv("../DataPreparing/GrahpEdges.csv")
sources = df["Source"].tolist()
targets = df["Target"].tolist()
graph = nx.Graph()
for i in range(len(sources)):
    graph.add_edge(sources[i], targets[i])

degree = nx.degree_centrality(graph)
betweenness = nx.betweenness_centrality(graph)
closeness = nx.closeness_centrality(graph)

# These lines write centrality values to excel file
"""
degree_df = pd.DataFrame({"Web Page": degree.keys(), "Degree Centrality": degree.values()})
betweenness_df = pd.DataFrame({"Web Page 2": betweenness.keys(), "Betweenness Centrality": betweenness.values()})
closeness_df = pd.DataFrame({"Web Page 3": closeness.keys(), "Closeness Centrality": closeness.values()})

degree_df = degree_df.sort_values(by="Degree Centrality", ascending=False)
betweenness_df = betweenness_df.sort_values(by="Betweenness Centrality", ascending=False)
closeness_df = closeness_df.sort_values(by="Closeness Centrality", ascending=False)

centrality_df = degree_df
centrality_df = centrality_df.merge(closeness_df, left_on="Web Page", right_on="Web Page 3")
centrality_df = centrality_df.merge(betweenness_df, left_on='Web Page', right_on="Web Page 2")

centrality_df.to_excel("Centrality.xlsx", encoding="utf-8-sig", index=False)
"""

# bokeh interactive graph
output_file("InteractiveGraph.html", title="DEU Plot")

nx.set_node_attributes(graph, name="degree", values=degree)
nx.set_node_attributes(graph, name="betweenness", values=betweenness)
nx.set_node_attributes(graph, name="closeness", values=closeness)

hover_tool = HoverTool(tooltips=[("Web Sayfası", "@index"), ("Degree Centrality", "@degree"),
                                 ("Betweenness Centrality", "@betweenness"),
                                 ("Closeness Centrality", "@closeness")])


p = figure(title="DEU Network", tools="pan,wheel_zoom,reset", active_scroll='wheel_zoom',
           x_range=Range1d(-5, 5), y_range=Range1d(-5, 5), plot_width=1600, plot_height=800)

p.add_tools(hover_tool, BoxSelectTool(), TapTool())

g = from_networkx(graph, nx.spring_layout, scale=2, center=(0, 0))
g.node_renderer.glyph = Circle(size=10, fill_color='navy')
g.node_renderer.hover_glyph = Circle(size=20, fill_color="orange")
g.node_renderer.selection_glyph = Circle(size=30, fill_color=Magma6[2])


g.edge_renderer.glyph = MultiLine(line_color='gray', line_alpha=0.9, line_width=0.9)
g.edge_renderer.hover_glyph = MultiLine(line_color="firebrick", line_alpha=1, line_width=2)
g.edge_renderer.selection_glyph = MultiLine(line_color=Magma6[5], line_alpha=1, line_width=3)

g.inspection_policy = NodesAndLinkedEdges()
g.selection_policy = NodesAndLinkedEdges()

p.renderers.append(g)

# pyvis interactive graf
g = Network(height='100%', width='70%', bgcolor='#222222', font_color='white')
g.toggle_hide_edges_on_drag(True)
g.barnes_hut()
g.show_buttons(filter_=True)
g.from_nx(graph)
g.save_graph("InteractiveGraph2.html")

show(p)
