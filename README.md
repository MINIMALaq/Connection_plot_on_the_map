# Sankey_plot_on_the_map
Visualizing Sankey plot on a map with python.

Basically used one of the D3 [connection map](https://www.d3-graph-gallery.com/graph/connectionmap_csv.html) to visulize the connections between points. <br>

The data source is https://mobilitylab.ut.ee/OD/.<br>

I downloaded one of the origin Destination files and made it ready to use for D3 example. 


Note: I added `cartopy==0.19.0.post1` to the requirements.txt to avoid errors in installing geoplot. You can use other mehods which introdced [here](https://pythonissues.com/issues/2179634).
