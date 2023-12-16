
import helper_functions.data_helpers as help
import helper_functions.visualization_helpers as vhelp
import helper_functions.variables as var
import numpy as np
import pandas as pd

from bokeh.plotting import figure, column, row
from bokeh.models import Button, Slider, ColumnDataSource,  Div
from bokeh.io import curdoc

# Importing and formatting the data
average_over = 5
df = help.get_master_df()
names = var.to_sum
multipliers = np.array([1.0]*(len(names)+2))
df["Net import/export"][df["Net import/export"] > 0] = 0
df["Net import/export"] *= -1.0
source = ColumnDataSource(data = vhelp.get_one_average_day_from_df(df, df.index[0], 0, average_over, multipliers))

# Creating the main plot
fig = figure(x_axis_type='datetime', y_range=(0,16000), width=900, height=600)
fig.grid.minor_grid_line_color = '#eeeeee'
stacked_area = fig.varea_stack(stackers=names, x='start_time', color=var.to_sum_colors, 
                               legend_label=names, source=source) 
consumption_line = fig.line(x="start_time", y="Total Consumption", source=source, color = "black", line_width=3.0)
fig.legend.background_fill_color = "#fafafa"


# Adding widgets
slider = Slider(start=1, end=365, value=1, step=1, title="Day", sizing_mode = "stretch_width") #
btn = Button(label="Play")
inputs: [Button] = []
for i in range(len(names)):
    inputs.append(Slider(start=0, end=5, value=1, step=0.1, title=names[i], sizing_mode = "stretch_width", bar_color = var.to_sum_colors[i]))

#Define call backs
current_day = 0
def update_date():
    global current_day
    current_day = slider.value + 1
    slider.value = current_day
    if current_day == 365:
        current_day = 0

def update_multipliers(attr, old, new):
    global multipliers
    global angles_source
    multipliers = np.array([ 1.0,    1.0,    inputs[0].value, inputs[1].value, inputs[2].value, 
                            inputs[3].value, inputs[4].value, inputs[5].value, inputs[6].value])

callback = None
def execute_animation():
    global callback
    if btn.label == "Play":
        btn.label = "Pause"
        callback = curdoc().add_periodic_callback(update_date, 100)
    else:
        btn.label = "Play"
        curdoc().remove_periodic_callback(callback)

def modify_figure(attr, old, new):
    global source
    global average_over
    source.data = vhelp.get_one_average_day_from_df(df, df.index[0], slider.value, average_over, multipliers)

Title = Div(
    text="""
        <h1>How Finland's electricity production and consumption depends on the time of year.</h1>""",
width=1300,
height=30,
)

Text = Div(
    text="""
        <p>Click the start button to start the animation of Finalnds electricity production and consumption in year 2022. The black line tells the amount of electricity consumed. </p>
        <br>
        <p> By changing the values in slides, you can experiment, how Finland's energy production total could be achived with different combination of different enrgy sources. The number after names the name tells the ratio compared to the 2022 situation. For example 1.4 means, that there is 40% more production. </p>
        <br>""",
        width= 600,
        height = 120,
)

## Register Callbacks
btn.on_click(execute_animation)
slider.on_change("value", modify_figure)

inputs[0].on_change("value", update_multipliers)
inputs[1].on_change("value", update_multipliers)
inputs[2].on_change("value", update_multipliers)
inputs[3].on_change("value", update_multipliers)
inputs[4].on_change("value", update_multipliers)
inputs[5].on_change("value", update_multipliers)
inputs[6].on_change("value", update_multipliers)

## GUI
inputs_column = column(Text, inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5], inputs[6], margin = (60, 0, 0, 10), background="#F0F0F0")
curdoc().add_root(column(Title, row(column(btn, slider, fig), inputs_column, margin=(30, 0, 0, 0)), margin=(10, 20, 20, 50)))