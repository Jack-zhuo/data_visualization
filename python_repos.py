import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# make an API call and then store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()

# explore information about repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)


# set visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'most-starred python projects on github'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')













#
# # examine first repositories
# repo_dict = repo_dicts[0]
# print('\nselected information about the first repository:')
# print('name:', repo_dict['name'])
# print('owner:', repo_dict['owner']['node_id'])
