
import helper_functions.data_importing as help
import helper_functions.dataframe_helper as vhelp
import helper_functions.constants as c
import helper_functions.page_texts as texts
import numpy as np
import pandas as pd

from bokeh.plotting import figure, column, row
from bokeh.models import Button, Slider, ColumnDataSource,  Div
from bokeh.io import curdoc

class App:
    def __init__(self):
        self.average_over       = 5
        self.df                 = None
        self.source             = None
        self.multipliers        = None
        self.columns            = c.INCLUDED_COLUMNS

        self.animation_callback = None
        self.current_day        = 0
        self.time_slider        = None
        self.main_fig           = None
        self.play_button        = None
        self.param_sliders      = []

    def import_data(self):
        self.multipliers = np.array([1.0]*(len(self.columns)+2))
        self.df = help.get_master_df()

        # Limiting to only imports
        self.df["Net import/export"][self.df["Net import/export"] > 0] = 0
        self.df["Net import/export"] *= -1.0

        self.source = ColumnDataSource(data = vhelp.get_one_average_day_from_df(self.df, self.df.index[0], 0, self.average_over, self.multipliers))

    def create_plots(self):

        #Figure itself
        self.main_fig = figure(x_axis_type='datetime', y_range=(0,16000), width=900, height=600)
        self.main_fig.grid.minor_grid_line_color = minor_line_color = '#eeeeee'

        #Area plot on top of the figure
        self.stacked_area = self.main_fig.varea_stack(stackers=self.columns, x='start_time', color=c.COLUMN_COLORS, 
                                    legend_label=self.columns, source=self.source) 
        
        #Consumptionline on top of the area plot
        self.consumption_line = self.main_fig.line(x="start_time", y="Total Consumption", source=self.source, color = "black", line_width=3.0)
    
    def update_date(self):
        """Widget call back"""
        self.current_day = self.time_slider.value + 1
        self.time_slider.value = self.current_day
        if self.current_day >= 365:
            self.time_slider.value = 0

    def update_multipliers(self, attr, old, new):
        """Widget call back"""
        param_values = [param.value for param in self.param_sliders]
        self.multipliers = np.array([ 1.0,    1.0] + param_values)
        self.modify_figure(None, None, None)

    def execute_animation(self):
        """Widget call back"""
        if self.play_button.label == "Play":
            self.play_button.label = "Pause"
            self.animation_callback = curdoc().add_periodic_callback(self.update_date, 100)
        else:
            self.play_button.label = "Play"
            curdoc().remove_periodic_callback(self.animation_callback)

    def modify_figure(self, attr, old, new):
        """Widget call back"""
        self.source.data = vhelp.get_one_average_day_from_df(self.df, self.df.index[0], self.time_slider.value, self.average_over, self.multipliers)

    def create_param_slider_with_callback(self, name: str, color: str, callback) -> Slider:
        slider = Slider(start=0, end=5, value=1, step=0.1, title=name, sizing_mode = "stretch_width", bar_color = color)
        slider.on_change("value", callback)
        return slider

    def create_all_widgets_and_callbacks(self):
        self.time_slider = Slider(start=1, end=365, value=1, step=1, title="Day", sizing_mode = "stretch_width")
        self.time_slider.on_change("value", self.modify_figure)

        self.play_button = Button(label="Play") 
        self.play_button.on_click(self.execute_animation)

        self.param_sliders = []
        for i in range(0, len(self.columns)):
            self.param_sliders.append(self.create_param_slider_with_callback(self.columns[i], c.COLUMN_COLORS[i], self.update_multipliers))
        

    def start(self):
        print("Loading data...")
        self.import_data()
        print("Creating plots...")
        self.create_plots()
        print("Creating widgets...")
        self.create_all_widgets_and_callbacks()
        inputs_column = column(texts.Text, *self.param_sliders, margin = (60, 0, 0, 10), background="#F0F0F0")
        body = row(column(self.play_button, self.time_slider, self.main_fig), inputs_column, margin=(30, 0, 0, 0))
        print("Starting web page...")
        curdoc().add_root(column(texts.Title, body, margin=(10, 20, 20, 50)))
        print("Web page running!")


app = App()
app.start()