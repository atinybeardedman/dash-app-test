import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

external_stylesheets = [
    'https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.min.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

pages = ['Home', 'Page-1', 'Page-2']


def mainPage():
    return html.Div(children=[
        html.Div(children=[
            html.H1(children='Home', className="title"),
        ],
                 className="box"),
        html.Div(children=[
            html.Div(children=[
                html.P("Column 1",
                       className=
                       "notification is-info has-text-centered has-text-light")
            ],
                     className="column"),
            html.Div(children=[
                html.P("Column 2",
                       className=
                       "notification is-info has-text-centered has-text-light")
            ],
                     className="column"),
            html.Div(children=[
                html.P("Column 3",
                       className=
                       "notification is-info has-text-centered has-text-light")
            ],
                     className="column"),
        ],
                 className="columns")
    ],
                    className="container")


def page1():
    return html.Div(children=[
        html.Div(children=[html.H1('Page 1', className="title")],
                 className="box"),
        html.Div(children=[
            html.Div(children=[
                html.Figure(
                    children=[html.Img(src="http://placekitten.com/400/300")],
                    className="image is-4by3")
            ],
                     className="column is-half is-offset-one-quarter")
        ],
                 className="columns"),
    ],
                    className="container")


header = ['Number', 'Name', 'Symbol', 'Weight']
elements = [{
    'Number': 1,
    'Name': 'Hydrogen',
    'Weight': 1.0079,
    'Symbol': 'H'
}, {
    'Number': 2,
    'Name': 'Helium',
    'Weight': 4.0026,
    'Symbol': 'He'
}, {
    'Number': 3,
    'Name': 'Lithium',
    'Weight': 6.941,
    'Symbol': 'Li'
}, {
    'Number': 4,
    'Name': 'Beryllium',
    'Weight': 9.0122,
    'Symbol': 'Be'
}, {
    'Number': 5,
    'Name': 'Boron',
    'Weight': 10.811,
    'Symbol': 'B'
}, {
    'Number': 6,
    'Name': 'Carbon',
    'Weight': 12.0107,
    'Symbol': 'C'
}, {
    'Number': 7,
    'Name': 'Nitrogen',
    'Weight': 14.0067,
    'Symbol': 'N'
}, {
    'Number': 8,
    'Name': 'Oxygen',
    'Weight': 15.9994,
    'Symbol': 'O'
}, {
    'Number': 9,
    'Name': 'Fluorine',
    'Weight': 18.9984,
    'Symbol': 'F'
}, {
    'Number': 10,
    'Name': 'Neon',
    'Weight': 20.1797,
    'Symbol': 'Ne'
}]


def page2():
    return html.Div(children=[
        html.Div(children=[html.H1('Page 2', className="title")],
                 className="box"),
        html.Div(children=[
            html.Div(children=[
                html.Table(children=[
                    html.Thead(children=[
                        html.Tr(children=[html.Th(x) for x in header])
                    ]),
                    html.Tbody(children=[
                        html.Tr(children=[html.Td(el[i]) for i in header])
                        for el in elements
                    ])
                ],
                           className="table is-fullwidth")
            ],
                     className="column is-8 is-offset-2"),
        ],
                 className="columns"),
    ],
                    className="container")


app.layout = html.Div(children=[
    dcc.Location(id='url', refresh=False),
    dcc.Dropdown(id='chooser',
                 options=[{
                     'label': i,
                     'value': i
                 } for i in pages],
                 value='Home'),
    html.Div(id='page-content', className="section"),
],
                      className="full-height has-background-grey-lighter")


@app.callback(dash.dependencies.Output('url', 'pathname'),
              [dash.dependencies.Input('chooser', 'value')])
def updateUrl(choice):
    return choice


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def updateContent(path):
    if path == 'Home':
        return mainPage()
    elif path == 'Page-1':
        return page1()
    else:
        return page2()


if __name__ == '__main__':
    app.run_server()
