Visualizing origin - destination data (commuting matrices) as an interactive plot on a map with python.


I downloaded one of the Origin Destination files from [here](https://mobilitylab.ut.ee/OD/) and made it ready to use with 4326 CRS. 


<br>It is not a Sakey plot yet, but to see the connection plot with plotly, I made a [HTML version](https://github.com/MINIMALaq/Sankey_plot_on_the_map/blob/main/Tallinn.html) of Tallinn notebook so you can see the results before running the code. <br>

You can run the code like this:<br>
`pip install -r requirements.txt` <br>
`python geo_plotly.py`

<br>
<br>



Note: I added `cartopy==0.19.0.post1` to the requirements.txt to avoid errors in installing `geoplot`. You can use other mehods which introduced [here](https://pythonissues.com/issues/2179634).
