# %% [markdown]
# # Dashboard Básico

# %%
# Instalando biblioteca
#%pip install dash

# %%
# Importando bibliotecas
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

# %% [markdown]
# ### Carregamento e preparação dos dados

# %%
# Carregar os dados
df = pd.read_csv('datasets/weather_data.csv')

# %%
# Preparar os dados
df['Date'] = pd.to_datetime(df['Date'])

# %%
# Calcula os KPIs
average_temperature = df['Temperature_C'].mean()
average_humidity = df['Humidity_percent'].mean()
max_wind_speed = df['Wind_speed_kmh'].max()

# %% [markdown]
# ### Criação do Dash

# %%
# Inicializa o Aplicativo Dash
app = dash.Dash(__name__)

# %%
# Layout do Dashboard
app.layout = html.Div([
  # Título principal
  html.H1("Dashboard de Dados Meteorológicos", style={'textAlign':'center'}),

  # Container para os KPIs
  html.Div([
    # KPI de Temperatura Média
    html.Div([
      html.H3("Temperatura Média (°C)", style={'textAlign': 'center'}),
      html.P(f"{average_temperature:.1f}", style={'textAlign': 'center', 'fontSize':'24px'})
    ], className="four columns"),
    # KPI de Umidade Média
    html.Div([
      html.H3("Umidade Média (%)", style={'textAlign':'center'}),
      html.P(f'{average_humidity:.1f}', style={'textAlign': 'center', 'fontSize':'24px'})
    ], className="four columns"),
    # KPI de Velocidade Máxima do Vento
    html.Div([
      html.H3("Velocidade Máxima do vento (km/h)", style={'textAlign':'center'}),
      html.P(f"{max_wind_speed}", style={'textAlign':'center', 'fontSize': '24px'})
    ], className='four columns')
  ], className="row"),

  # Container para os gráficos de tendência
  html.Div([
    # Gráfico de Tendência da Temperatura
    html.Div([
      dcc.Graph(
      id='temperature-trend-chart',
      figure = px.line(df, x='Date', y='Temperature_C',
                       title='Tendência da Temperatura ao Longo do Tempo',
                       labels={'Temperature_C': 'Temperatura (°C)', 'Date': 'Data'}
                       )
      )
    ], className='six columns'),
    # Gráfico de Tendência de Umidade
    html.Div([
      dcc.Graph(
        id="humidity-trend-chart",
        figure=px.line(df, x='Date', y='Humidity_percent',
                       title='Tendência da Umidade ao Longo do Tempo',
                       labels={'Humidity_percent':'Umidade (%)', 'Date': 'Data'}
                       )
      )
    ], className='six columns')
    
  ], className='row')

])

# %%
app.run_server(debug=True)


