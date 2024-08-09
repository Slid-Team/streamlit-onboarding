## Installing Streamlit

```bash
pip install streamlit
```

## Running Streamlit

```bash
streamlit run your_script.py [-- script args]

// example
streamlit run app.py --server.port 8000

// Or run a remotely hosted script, example github gist:
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

## Viewing Streamlit

After running the script you will see a message like this:

```bash
 You can now view your Streamlit app in your browser.

  Local URL: http://localhost:4000
  Network URL: http://27.1.212.23:4000
```

Anyone on the network, even with mobile phone, can view the app by accessing the network URL!
The app is your canvas, where you'll draw charts, text, widgets, tables, and more.

On the web page launched, click 'always rerun' to get hot reloads.

## Supported Streamlit methods

### Display and write data

- `st.write()`
- `st.dataframe()`
- `st.table()`
- `st.metric()`
- `st.json()`

### Charts

- `st.line_chart()`
- `st.area_chart()`
- `st.bar_chart()`
- `st.pyplot()`
- `st.altair_chart()`
- `st.vega_lite_chart()`
- `st.plotly_chart()`
- `st.bokeh_chart()`
- `st.pydeck_chart()`
- `st.graphviz_chart()`
- `st.map()`

### Input widgets

- `st.button()`
- `st.download_button()`
- `st.checkbox()`
- `st.radio()`
- `st.selectbox()`
- `st.multiselect()`
- `st.slider()`
- `st.select_slider()`
- `st.text_input()`
- `st.number_input()`
- `st.text_area()`
- `st.date_input()`
- `st.time_input()`
- `st.file_uploader()`
- `st.color_picker()`
- `st.camera_input()`

### Media elements

- `st.image()`
- `st.audio()`
- `st.video()`

### Layouts and containers

- `st.sidebar()`
- `st.columns()`
- `st.expander()`
- `st.container()`
- `st.empty()`

### Status elements

- `st.progress()`
- `st.spinner()`
- `st.status()`
- `st.toast()`
- `st.balloons()`
- `st.snow()`
- `st.error()`
- `st.warning()`
- `st.info()`
- `st.success()`
- `st.exception()`

### Control flow

- `st.stop()`
- `st.form()`
- `st.form_submit_button()`

### Utilities

- `st.set_page_config()`
- `st.echo()`
- `st.help()`

### State management

- `st.session_state`

### Caching

- `st.cache_data()`
- `st.cache_resource()`

### Mutate charts

- `st.add_rows()`

### Experimental features

- `st.experimental_rerun()`
- `st.experimental_get_query_params()`
- `st.experimental_set_query_params()`
