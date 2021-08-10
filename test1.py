import dash
import dash_html_components as html
import dash_pivottable
import dash_table
from dash.dependencies import Input, Output, State
import pandas as pd


app = dash.Dash(__name__)
server = app.server
df = pd.read_csv('athlete_events.csv')
cols = ["ID","Name","Sex","Age","Height","Weight","Team","NOC","Medal","Games","Year","Season","City","Sport","Event"]
df = df[cols]

athletes = df.to_dict('records')

app.layout = html.Div(
    [
        dash_pivottable.PivotTable(
            id="table",
            data=athletes,
            rendererName="Table",
            aggregatorName="Count",
            vals=[],
            hiddenAttributes = ["ID", "Name", "Height", "Weight", "NOC", "Events"]
        ),
        html.H3(
            id="title",
            children="Athletes Records (" + str(len(athletes)) + " Obs)",
            style={'fontFamily': 'Verdana', 'text-align': 'center'}
        ),
        dash_table.DataTable(
            id="grid",
            columns=[{"name": i, "id": i} for i in df.columns],
            data= athletes,
            page_current=0,
            page_size=10,
            style_table={'overflowX': 'scroll'},
            style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'},
            style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }]
        )
    ]
)

# @app.callback([Output('grid', 'data'), Output('title', 'children')],[Input('table', 'selectData')])
# def update_table(selectData):
#     if selectData is None:
#         raise dash.exceptions.PreventUpdate
#     else:
#         print(selectData)
#         return selectData, "Zoo Records (" + str(len(selectData)) + " Obs)"

app.clientside_callback(
    """
    function(selectData) {
        if (typeof selectData == "undefined"){
            return window.dash_clientside.no_update
        }
        return selectData
    }
    """,
    Output('grid', 'data'), [Input('table', 'selectData')]
)

app.clientside_callback(
    """
    function(selectData) {
        if (typeof selectData == "undefined"){
            return window.dash_clientside.no_update
        }
        return "Athletes Records (" + selectData.length.toString() + " Obs)"
    }
    """,
    Output('title', 'children'), [Input('table', 'selectData')]
)

if __name__ == "__main__":
    app.run_server(debug=True)