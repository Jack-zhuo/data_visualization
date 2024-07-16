import json
from contry_codes import get_country_code
import pygal
from pygal.style import RotateStyle


# load the data into a list
file_name = 'population_data.json'
with open(file_name) as f:
    pop_data = json.load(f)

cc_populations = {}
# print the 2010 population for each name.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print("error-"+country_name)

# group countries into 3 population levels
cc_pop_1, cc_pop_2, cc_pop_3 = {},{},{}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pop_1[cc] = pop
    elif pop < 1000000000:
        cc_pop_2[cc] = pop
    else:
        cc_pop_3[cc] = pop
print(len(cc_pop_1), len(cc_pop_2), len(cc_pop_3))

wm = pygal.maps.world.World()
wm_style = RotateStyle('#336699')
wm = pygal.Worldmap(style=wm_style)

wm.title = 'world population in 2010, by country'
wm.add('人口小于1千万', cc_pop_1)
wm.add('人口小于10亿', cc_pop_2)
wm.add('人口大于10亿', cc_pop_3)

wm.render_to_file('11111.svg')