import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# อ่านข้อมูลจากไฟล์ Excel
df = pd.read_excel('C:/Users/Veerachai.Sawatvanic/Desktop/export.XLSX')

# สร้างแอป Dash
app = dash.Dash(__name__)

# ตัวเลือกกราฟ
graph_types = ['Bar', 'Line', 'Pie', 'Waterfall']

# สร้าง Layout ของแอป
app.layout = html.Div([
    html.H1('Data Visualization Dashboard'),
    
    # Dropdown สำหรับเลือกประเภทกราฟ
    dcc.Dropdown(
        id='graph-type',
        options=[{'label': gtype, 'value': gtype} for gtype in graph_types],
        value='Bar'
    ),

    # Dropdown สำหรับเลือกคอลัมน์ของข้อมูล (แกน x)
    dcc.Dropdown(
        id='x-axis',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[0]
    ),

    # Dropdown สำหรับเลือกคอลัมน์ของข้อมูล (แกน y)
    dcc.Dropdown(
        id='y-axis',
        options=[{'label': col, 'value': col} for col in df.columns],
        value=df.columns[1]
    ),

    # แสดงกราฟ
    dcc.Graph(id='graph')
])

# Callback สำหรับการเปลี่ยนประเภทกราฟและข้อมูลในแกน x, y
@app.callback(
    Output('graph', 'figure'),
    [Input('graph-type', 'value'),
     Input('x-axis', 'value'),
     Input('y-axis', 'value')]
)
def update_graph(graph_type, x_axis, y_axis):
    if graph_type == 'Bar':
        fig = px.bar(df, x=x_axis, y=y_axis)
    elif graph_type == 'Line':
        fig = px.line(df, x=x_axis, y=y_axis)
    elif graph_type == 'Pie':
        fig = px.pie(df, names=x_axis, values=y_axis)
    elif graph_type == 'Waterfall':
        fig = px.waterfall(df, x=x_axis, y=y_axis)
    else:
        fig = px.bar(df, x=x_axis, y=y_axis)  # Default to Bar
    return fig

# รันแอป
if __name__ == '__main__':
    app.run_server(debug=False)
