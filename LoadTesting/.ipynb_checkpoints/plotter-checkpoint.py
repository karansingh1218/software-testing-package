# plotter.py
import requests
import six

from bokeh.client import push_session
from bokeh.layouts import gridplot
from bokeh.plotting import figure, curdoc


config = {'figures': [{'charts':
                           [{'color': 'black', 'legend': 'average response time', 'marker': 'diamond',
                             'key': 'avg_response_time'},
                            {'color': 'blue', 'legend': 'median response time', 'marker': 'triangle',
                             'key': 'median_response_time'},
                            {'color': 'green', 'legend': 'min response time', 'marker': 'inverted_triangle',
                             'key': 'min_response_time'},
                            {'color': 'red', 'legend': 'max response time', 'marker': 'circle',
                             'key': 'max_response_time'}],
                       'xlabel': 'Requests count',
                       'ylabel': 'Milliseconds',
                       'title': '{} response times'
                       },
                      {'charts': [{'color': 'green', 'legend': 'current rps', 'marker': 'circle',
                                   'key': 'current_rps'},
                                  {'color': 'red', 'legend': 'failures', 'marker': 'cross',
                                   'key': 'num_failures', 'skip_null': True}],
                       'xlabel': 'Requests count',
                       'ylabel': 'RPS/Failures count',
                       'title': '{} RPS/Failures'
                       }],
          'url': 'http://localhost:8089/stats/requests',  
          'states': ['hatching', 'running'],  
          'requests_key': 'num_requests'
          }

data_sources = {}  
figures = []  

for state in config['states']:
    data_sources[state] = {}  
    
    for figure_data in config['figures']:
     
    
        new_figure = figure(title=figure_data['title'].format(state.capitalize()))
        new_figure.xaxis.axis_label = figure_data['xlabel']
        new_figure.yaxis.axis_label = figure_data['ylabel']
     
    
        for chart in figure_data['charts']:

            
            marker = getattr(new_figure, chart['marker'])
            scatter = marker(x=[0], y=[0], color=chart['color'], size=10, legend=chart['legend'])
            line = new_figure.line(x=[0], y=[0], color=chart['color'], line_width=1, legend=chart['legend'])
     
    
            data_sources[state][chart['key']] = scatter.data_source = line.data_source
        figures.append(new_figure)

requests_key = config['requests_key']
url = config['url']




session = push_session(curdoc())



def update():
    try:
        resp = requests.get(url)
    except requests.RequestException:
        return
    resp_data = resp.json()
    data = resp_data['stats'][-1] 
    if resp_data['state'] in config['states']:
        for key, data_source in six.iteritems(data_sources[resp_data['state']]):

            data_source.data['x'].append(data[requests_key])
            data_source.data['y'].append(data[key])

            data_source.trigger('data', data_source.data, data_source.data)

curdoc().add_periodic_callback(update, 1000)

session.show(gridplot(figures, ncols=2)) 

session.loop_until_closed() 