import dash
from dash import dcc
from dash import html
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import requests
import pandas as pd

# Initialize the app
app = dash.Dash()

# Define the layout
app.layout = html.Div([
    html.H1('My dashboard'),
    dcc.Input(id="hour", type="text", placeholder="hour", style={'marginRight':'10px'}),
    dcc.Input(id="generated_power", type="text", placeholder="generated_power", style={'marginRight':'10px'}),
    dcc.Input(id="temperatureC", type="text", placeholder="temperatureC", style={'marginRight':'10px'}),
    dcc.Input(id="dewpointC", type="text", placeholder="dewpointC", style={'marginRight':'10px'}),
    dcc.Input(id="pressurehPa", type="text", placeholder="pressurehPa", style={'marginRight':'10px'}),
    dcc.Input(id="wind_direction_degrees", type="text", placeholder="wind_direction_degrees", style={'marginRight':'10px'}),
    dcc.Input(id="wind_speed_KMH", type="text", placeholder="wind_speed_KMH", style={'marginRight':'10px'}),
    dcc.Input(id="wind_speed_gustKMH", type="text", placeholder="wind_speed_gustKMH", style={'marginRight':'10px'}),
    dcc.Input(id="Humidity", type="text", placeholder="Humidity", style={'marginRight':'10px'}),
    dcc.Input(id="hourly_precipMM", type="text", placeholder="hourly_precipMM", style={'marginRight':'10px'}),
    dcc.Input(id="daily_rainMM", type="text", placeholder="daily_rainMM", style={'marginRight':'10px'}),
    dcc.Input(id="solar_radiation_Watts_m2", type="text", placeholder="solar_radiation_Watts_m2", style={'marginRight':'10px'}),
    
    html.Button('Submit', id='button'),
    # Graph to display the data
    dcc.Graph(id='api-data-graph')
])

@app.callback(
    dash.dependencies.Output('api-data-graph', 'figure'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('hour', 'value'),
    dash.dependencies.State('generated_power', 'value'),
    dash.dependencies.State('temperatureC', 'value'),
    dash.dependencies.State('dewpointC', 'value'),
    dash.dependencies.State('input-2', 'value'),
    dash.dependencies.State('input-2', 'value')
    ,dash.dependencies.State('input-2', 'value')]
)

# Function to fetch the data from the API
def fetch_data(data):
    # Make the request to the API
    data = {"array":data}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'http://127.0.0.1:5002/predict', json=data, headers=headers)
    # Process the data
    data = response.json()
    print(data)
    df = pd.DataFrame(data)
    return df

def update_graph(data):
    # Fetch the data
    df = pd.read_csv('./datasetFinal.csv')
    scaler = StandardScaler()
    names = df.columns
    d = scaler.fit_transform(df)
    df = pd.DataFrame(d, columns = names)

    y = df['generated_power']
    X = df.drop(columns='generated_power')

    x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    
    df = fetch_data(x_test)
    # Create the figure
    figure = px.bar(df, x='column1', y='column2')
    return figure

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
