# Visualizing Frequencies of words with plotly
import pandas as pd
import plotly.express as px
df = pd.read_csv("Frequency.csv")
word = df["Word"]
freq = df["Frequency"]
page = df["Number of Pages"]

fig = px.scatter(df, x="Number of Pages", y="Frequency", hover_data=['Word'])
fig.update_traces(marker = dict(size=15,
                                color=freq,
                                showscale=True,
                                colorscale='icefire'))
fig.update_layout(
    hoverlabel=dict(
        bgcolor='black',
        font_size=60,
        font_family="Courier New, monospace"
    )
)
fig.update_yaxes(type='log', title_font={"size": 60}, tickfont_size=40)
fig.update_xaxes(type='log', title_font={"size": 60}, tickfont_size=40)
fig.write_html("3-)InteractiveVisualizeFreq.html")