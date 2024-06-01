import streamlit as st
from streamlit_multipage import MultiPage
from frontpages import pages
import frontpages


def sidebar(st):
    pass



app = MultiPage()
app.st = st
app.start_button = "进入网站"
app.navbar_name = "导航栏"
app.next_page_button = "Next Chapter"
app.previous_page_button = "Previous Chapter"
app.reset_button = "Delete Cache"
app.navbar_style = "VerticalButton"

app.navbar_extra = sidebar

app.hide_menu = True
app.hide_navigation = True

app.add_app("landing",frontpages.landing,initial_page=True)

for app_name,app_function in pages.items():
    app.add_app(app_name,app_function)

app.run()
