import pandas as pd
import geopandas
import folium

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_meat_consumption'

tables = pd.read_html(url)
table = tables[0]

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 1000)

world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))

table = world.merge(table, how='left', left_on=['name'], right_on=['Country'])
table = table.dropna(subset=['kg/person (2002)[9][note 1]'])


m = folium.Map(
    location=[13.133932434766733, 16.103938729508073], zoom_start=2)

folium.Choropleth(
    geo_data=table,
    name="choropleth",
    data=table,
    columns=["Country", "kg/person (2002)[9][note 1]"],
    key_on="feature.properties.name",
    fill_color="OrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Meat Consumption Rate (kg/person)/year (2002)",
).add_to(m)

m.save('/home/muhammad/Desktop/Python Projects/Interactive_map_show_world_meat_consumption/interactive_map_meat_consumption.html')


print(table)
