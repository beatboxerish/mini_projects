import re
import pandas as pd
from plotly.graph_objs import *

# Define cleaning function for the raw POS data

def sales_report_clean(filename):
    obj = open( filename,'r')
    obj = obj.read()
    # separating the data from unnecessary starting information
    # as this data is presented in the form of a report and thus
    # has some extra information

    id_list = re.split('[\n,]ID',obj)[1:]
    for index, text in enumerate(id_list):
        sample = re.sub(',{1,10}',',',text)
        sample = re.split(',Generated',sample)[0]
        sample = 'ID' + sample

        if 'Grand Total' in sample:
            sample = re.split('Grand Total',sample)[0]

        with open('../data/sample_' + str(index), 'w') as f:  
            f.write(sample)

def generate_plots(clean_data_index = 0):
    # generate clean data
    sales_report_clean('../data/sample.csv')
    # load the ith clean dataset and generate plots for it
    df = pd.read_csv('../data/sample_' + str(clean_data_index))
    
    # we will be generating 4 different plots for it

    # 1) Top selling items graph
    top_10_items = df.sort_values(by = 'QTY', ascending = False)[:10]

    trace1 = Bar(
        x = top_10_items.loc[:,'Name'],
        y = top_10_items.loc[:,'QTY'],
        name = 'Quantity Sold',
	width = 0.4
    )

    trace2 = Bar(
        x = top_10_items.loc[:,'Name'],
        y = top_10_items.loc[:,'Price'],
        name = 'Price',
	width = 0.4
    )

    data = [trace1, trace2]

    layout = Layout(
        barmode = 'group',
        title = 'Top Selling Items',
        showlegend = True,
        yaxis = dict(
            title = 'Quantity/Price'),
        xaxis = dict(
	    automargin = True,
	    tickangle = 45),
	autosize = False,
	width = 600,
	height = 600
	)

    fig_1 = Figure(data =data, layout = layout)

    # 2) Least selling items graph
    least_10_items = df.sort_values(by = 'QTY', ascending = True)[:10]

    trace1 = Bar(
        x = least_10_items.loc[:,'Name'],
        y = least_10_items.loc[:,'QTY'],
        name = 'Quantity Sold',
	width = 0.4
    )

    trace2 = Bar(
        x = least_10_items.loc[:,'Name'],
        y = least_10_items.loc[:,'Price'],
        name = 'Price',
	width = 0.4
    )

    data = [trace1, trace2]

    layout = Layout(
        barmode = 'group',
        title = 'Least Selling Items',
        showlegend = True,
        yaxis = dict(
            title = 'Quantitiy/Price'),
	xaxis = dict(
	    automargin = True,
	    tickangle  = 45),
	autosize = False,
	height = 600,
	width = 600
    )

    fig_2 = Figure(data =data, layout = layout)

    # 3) Most Expensive items vs their quantity sold 
    most_expensive_item = df.sort_values(by = 'Price',ascending = False)[:10]
    list_A = [top_10_items.loc[:,'Name'].iloc[0]]
    list_A.extend(most_expensive_item.loc[:,'Name'].tolist())
    list_B = [top_10_items.loc[:,'Price'].iloc[0]]
    list_B.extend(most_expensive_item.loc[:,'Price'].tolist())
    list_C = [top_10_items.loc[:,'QTY'].iloc[0]]
    list_C.extend(most_expensive_item.loc[:,'QTY'].tolist())

    trace1 = Bar(
        x = list_A,
        y = list_B,
        name = 'Price',
	marker = dict(color = 'red'),
	width = 0.4
    )

    trace2 = Bar(
        x = list_A,
        y = list_C,
        name = 'Quantity Sold',
	marker = dict(color ='green'),
        width = 0.4
    )

    # NOTE: look into the below commented portion later
    '''
    trace3 = Bar(
        x = [top_10_items.loc[:, 'Name'].iloc[0]],
        y = [top_10_items.loc[:,'QTY'].iloc[0]],
        name = top_10_items.loc[:,'Name'].iloc[0],
	showlegend = False,
	marker = dict(color = 'red'),
	width = 0.4
    ) 
    trace4 = Bar(
        x = [top_10_items.loc[:,'Name'].iloc[0]],
        y = [top_10_items.loc[:,'Price'].iloc[0]],
        name = 'Price',
	showlegend = False,
	marker = dict(color = 'green'),
	width = 0.4
    )
    '''

    trace5 = Scatter(
	x = [top_10_items.loc[:, 'Name'].iloc[0]],
        y = [top_10_items.loc[:,'QTY'].iloc[0]],
        mode='markers+text',
        text=['Top Selling Item'],
        textposition='top right',
        showlegend = False,
	marker = dict(color = 'black')
    )

    data = [ trace5, trace1, trace2]

    layout = Layout(
        barmode = 'group',
        title = 'Most Expensive Items vs Quantity Sold',
        showlegend = True,
        yaxis = dict(
            title = 'Quantity/Price'),
	xaxis = dict(
	    automargin = True,
	    tickangle = 45
	),
	autosize = False,
	height = 600,
	width = 600
    )

    fig_3 = Figure(data = data, layout = layout)

    # 4) Pie chart for 5 most contributing items to total
    top_contributing_items = df.loc[:,['Name','Total']].sort_values(by = 'Total', ascending = False).head(5)

    labels = top_contributing_items.loc[:,'Name']
    values = top_contributing_items.loc[:,'Total']

    trace = [Pie(labels = labels, values = values)]

    layout = Layout(
        title = 'Top Most Contributing Items to Total Revenue($)',
    	autosize = True
	)

    fig_4 = Figure(data = trace, layout = layout)

    figures = [fig_1, fig_2, fig_3, fig_4]

    return figures
