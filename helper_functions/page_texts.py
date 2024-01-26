from bokeh.models import Div

Title = Div(
    text="""
        <h1>How Finland's electricity production and consumption depends on the time of year.</h1>""",
width=1300,
height=30,
)

Text = Div(
    text="""
        <p>Click the start button to start the animation of Finalnd's electricity production and consumption in year 2022. The black line tells the amount of electricity consumed. </p>
        <br>
        <p> By changing the values in slides, you can experiment, how Finland's energy production total could be achived with different combination of different enrgy sources. The number after names the name tells the ratio compared to the 2022 situation. For example 1.4 means, that there is 40% more production. </p>
        <br>""",
        width= 600,
        height = 120,
)