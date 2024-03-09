import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins  # This package provides the Palmer Penguins dataset

# added sidebar with select input for choosing either male or female. Not interactive yet.
with ui.sidebar(position="right", bg="#f8f8f8"):
    "Module 2 Sidebar"
    ui.input_select("sex", "Choose the penguin's sex", ["MALE", "FEMALE"])

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

# Using dataframe methods to gather the first and last 3 of the dataframe
penguins_df.head(3)
penguins_df.tail(3)

# added title to main page
ui.page_opts(title="Adrian's Penguin Data", fillable=True)
with ui.layout_columns():

    # made a scatterplot from information from dataframe
    @render_plotly
    def scatterplot():
        return px.scatter(
            penguins_df, x="bill_length_mm", y="body_mass_g", color="species")
        
    # modified original histogram to include penguins_dataframe data
    @render_plotly
    def plot1():
        return px.histogram(penguins_df, y="flipper_length_mm")
