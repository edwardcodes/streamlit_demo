import pandas as pd
import plost
import streamlit as st

st.set_page_config(layout='wide',initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



st.sidebar.header('Sample Dashboard')

st.sidebar.subheader('Heat map parameter')
time_hist_color = st.sidebar.selectbox('Color by',('temp_min','temp_max'))

st.sidebar.subheader('Donut Chart Parameter')
donut_color = st.sidebar.selectbox('Select data',('q2','q3'))

st.sidebar.subheader('Line Chart Parameter')
plot_data = st.sidebar.multiselect('Select Data',['temp_min', 'temp_max', 'pressure'],['temp_min', 'temp_max', 'pressure'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)


st.sidebar.markdown(
    """
    ---
    Created with ❤️ by [RuahAI](https://ruahtech.com.au/)
    """)

st.title('🎈 Sample Dashboard')
st.write('Checking how streamlit works!!')

# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric('Temperature (°C)', '35.2 °C', '0.8 °C')
col2.metric('Pressure (hPa)', '29.92 hPa', '0.02 hPa')
col3.metric('Wind speed', '9 mph', '-8 mph')

# Row B
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv')
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns(2)
with c1:
    st.markdown('### Heat Map')
    plost.time_hist(data=seattle_weather,
                    date='date',
                    x_unit='week',
                    y_unit='day',
                    color=time_hist_color,
                    aggregate='median',
                    height=350,
                    width=500,
                    use_container_width=True)
with c2:
    st.markdown('### Donut Chart')
    plost.donut_chart(data=stocks,
                      theta=donut_color,
                      color='company',
                      legend='bottom',
                      use_container_width=True)

# Row C
st.markdown('### Bar Chart')
plost.bar_chart(data=stocks,bar='company',value=['q2','q3'],group='value',legend='bottom',color='company',use_container_width=True)