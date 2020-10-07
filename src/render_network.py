import plotly.graph_objects as go

import networkx as nx
import chart_studio.plotly as py
from plotly.graph_objs import *

import igraph as ig

# with open('src/data/graph.gml', 'r') as file:
#     graph_file = file.read()

G=ig.Graph.Read_GML('src/data/graph.gml')
labels=list(G.vs['label'])
N=len(labels)
E=[e.tuple for e in G.es]# list of edges
layt=G.layout('kk') #kamada-kawai layout

Xn=[layt[k][0] for k in range(N)]
Yn=[layt[k][1] for k in range(N)]
Xe=[]
Ye=[]
for e in E:
    Xe+=[layt[e[0]][0],layt[e[1]][0], None]
    Ye+=[layt[e[0]][1],layt[e[1]][1], None]

trace1=Scatter(x=Xe,
               y=Ye,
               mode='lines',
               line= dict(color='rgb(210,210,210)', width=1),
               hoverinfo='none'
               )
trace2=Scatter(x=Xn,
               y=Yn,
               mode='markers',
               name='ntw',
               marker=dict(symbol='circle-dot',
                                        size=5,
                                        color='#6959CD',
                                        line=dict(color='rgb(50,50,50)', width=0.5)
                                        ),
               text=labels,
               hoverinfo='text'
               )

axis=dict(showline=False, # hide axis line, grid, ticklabels and  title
          zeroline=False,
          showgrid=False,
          showticklabels=False,
          title=''
          )

width=800
height=800
layout=Layout(title= "Coauthorship network of scientists working on network theory and experiment"+\
              "<br> Data source: <a href='https://networkdata.ics.uci.edu/data.php?id=11'> [1]</a>",
    font= dict(size=12),
    showlegend=False,
    autosize=False,
    width=width,
    height=height,
    xaxis=layout.XAxis(axis),
    yaxis=layout.YAxis(axis),
    margin=layout.Margin(
        l=40,
        r=40,
        b=85,
        t=100,
    ),
    hovermode='closest',
    annotations=[
           dict(
           showarrow=False,
            text='This igraph.Graph has the Kamada-Kawai layout',
            xref='paper',
            yref='paper',
            x=0,
            y=-0.1,
            xanchor='left',
            yanchor='bottom',
            font=dict(
            size=14
            )
            )
        ]
    )

data=[trace1, trace2]
fig=Figure(data=data, layout=layout)
py.iplot(fig, filename='Coautorship-network-igraph')

# G = nx.parse_gml(graph_file)
#
# print(type(G))
#
# pos = nx.fruchterman_reingold_layout(G)
#
# Xv=[pos[k][0] for k in range(N)]
# Yv=[pos[k][1] for k in range(N)]
# Xed=[]
# Yed=[]
# for edge in E:
#     Xed+=[pos[edge[0]][0],pos[edge[1]][0], None]
#     Yed+=[pos[edge[0]][1],pos[edge[1]][1], None]
#
# trace3=Scatter(x=Xed,
#                y=Yed,
#                mode='lines',
#                line=dict(color='rgb(210,210,210)', width=1),
#                hoverinfo='none'
#                )
# trace4=Scatter(x=Xv,
#                y=Yv,
#                mode='markers',
#                name='net',
#                marker=dict(symbol='circle-dot',
#                              size=5,
#                              color='#6959CD',
#                              line=dict(color='rgb(50,50,50)', width=0.5)
#                              ),
#                text=labels,
#                hoverinfo='text'
#                )
#
# annot="This networkx.Graph has the Fruchterman-Reingold layout<br>Code:"+\
# "<a href='http://nbviewer.ipython.org/gist/empet/07ea33b2e4e0b84193bd'> [2]</a>"
#
# data1=[trace3, trace4]
# fig1=Figure(data=data1, layout=layout)
# fig1['layout']['annotations'][0]['text']=annot
# py.iplot(fig1, filename='Coautorship-network-nx')

# edge_x = []
# edge_y = []
# for edge in G.edges():
#     x0, y0 = G.nodes[edge[0]]['pos']
#     x1, y1 = G.nodes[edge[1]]['pos']
#     edge_x.append(x0)
#     edge_x.append(x1)
#     edge_x.append(None)
#     edge_y.append(y0)
#     edge_y.append(y1)
#     edge_y.append(None)
#
# edge_trace = go.Scatter(
#     x=edge_x, y=edge_y,
#     line=dict(width=0.5, color='#888'),
#     hoverinfo='none',
#     mode='lines')
#
# node_x = []
# node_y = []
# for node in G.nodes():
#     x, y = G.nodes[node]['pos']
#     node_x.append(x)
#     node_y.append(y)
#
# node_trace = go.Scatter(
#     x=node_x, y=node_y,
#     mode='markers',
#     hoverinfo='text',
#     marker=dict(
#         showscale=True,
#         # colorscale options
#         #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
#         #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
#         #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
#         colorscale='Blackbody',
#         reversescale=True,
#         color=[],
#         size=10,
#         colorbar=dict(
#             thickness=15,
#             title='Node Connections',
#             xanchor='left',
#             titleside='right'
#         ),
#         line_width=2))
#
# node_adjacencies = []
# node_text = []
# for node, adjacencies in enumerate(G.adjacency()):
#     node_adjacencies.append(len(adjacencies[1]))
#     node_text.append('# of connections: '+str(len(adjacencies[1])))
#
# node_trace.marker.color = node_adjacencies
# node_trace.text = node_text
#
# fig = go.Figure(data=[edge_trace, node_trace],
#              layout=go.Layout(
#                 title='<br>Players and their Teammates',
#                 titlefont_size=16,
#                 showlegend=False,
#                 hovermode='closest',
#                 margin=dict(b=20,l=5,r=5,t=40),
#                 annotations=[ dict(
#                     text="Python code: <a href='https://github.com/TScafeJR/nba-kevin-bacon'>https://github.com/TScafeJR/nba-kevin-bacon</a>",
#                     showarrow=False,
#                     xref="paper", yref="paper",
#                     x=0.005, y=-0.002 ) ],
#                 xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
#                 yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
#                 )
# fig.show()