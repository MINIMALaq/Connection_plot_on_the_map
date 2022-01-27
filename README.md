# Sankey_plot_on_the_map
Visualizing Sankey plot on a map with python.


I downloaded one of the Origin Destination files from [here](https://mobilitylab.ut.ee/OD/) and made it ready to use woth 4326 projection. 


<br>To see the plot with plotly you can run the code like this:<br>
`pip install -r requirements.txt`
`python geo_plotly.py`

<br>
<br>



Note: I added `cartopy==0.19.0.post1` to the requirements.txt to avoid errors in installing `geoplot`. You can use other mehods which introdced [here](https://pythonissues.com/issues/2179634).
