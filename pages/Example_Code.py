"""
This is a page to show examples of Streamlit features using code.
"""

import streamlit as st


st.set_page_config(page_title="Page 1", page_icon="📈")

code = '''

def main():
    """
    Page 1
    """

    st.title("Page 1")
    st.sidebar.header("Page 1")

    st.write("This is the content of page 1")

    # displaying and writing data
    st.title("Hello, World!")
    st.write("Hello, World!")
    st.table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
    st.json({
        "name": "John",
        "age": 30,
        "city": "New York"
    })

    # charts
    st.line_chart([1, 2, 3, 4, 5])
    st.area_chart([1, 2, 3, 4, 5])
    st.bar_chart([1, 2, 3, 4, 5])
    st.map(
        {
            "latitude": [37.7749, 34.0522, 40.7128],
            "longitude": [-122.4194, -118.2437, -74.0060]
        }
    )

    # Input widgets
    st.button("Click me")
    st.download_button("Download", data="Hello, World!")
    st.checkbox("Check me")
    st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.multiselect("Choose an option", ["Option 1", "Option 2", "Option 3"])
    st.slider("Choose a value", 0, 100, 50)
    st.select_slider("Choose a value", [1,2,3,4,5,6,7,8,9,10])
    st.text_input("Enter some text")
    st.number_input("Choose a value", 0, 100, 50)
    st.text_area("Enter some text")
    st.date_input("Choose a date")
    st.time_input("Choose a time")
    st.file_uploader("Upload a file")
    st.color_picker("Choose a color")
    # st.camera_input("Take a photo")

    # Media elements
    st.image("https://picsum.photos/200/300")
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    st.video("https://www.youtube.com/watch?v=YQHsXMglC9A")

    # Layout and containers
    with st.sidebar:
        st.write("CHAPTER 1")
        st.write("CHAPTER 2")
        st.button("Next")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("This is column 1")
        st.button("Button 1")
    with col2:
        st.write("This is column 2")
        st.button("Button 2")

    with st.expander("Expand me"):
        st.write("This is an expander")
        st.button("Button 3")

    with st.container(): # grouping elements
        st.write("This is a container")
        st.button("Button 4")

    with st.empty(): # placeholder for future content
        for i in range(5):
            st.write(i)
            time.sleep(.2)

    # status elements

    st.progress(0.7)

    with st.spinner("Loading..."):
        time.sleep(.4)
        st.write("Spinner Done loading!")

    with st.status(
        "This is a status element", 
        state="running", # "running", "complete", "error"
        expanded=True
        ) as status:
        time.sleep(1)
        status.update(label="Status Done loading!", state="complete")
    
    st.toast("This is a toast element", icon="🍞")
    st.balloons()
    st.snow()
    st.error("This is an error")
    st.warning("This is a warning")
    st.info("This is an info")
    st.success("This is a success")
    st.exception(Exception("This is an exception"))

    # control flow
    # st.stop()
    with st.form("my_form"):
        st.write("This is a form")
        text = st.text_input("Enter some text")
        slider_val = st.slider("Choose a value", 0, 100, 50)
        checkbox_val = st.checkbox("Check me")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write(f"Text: {text}", f"Slider: {slider_val}", f"Checkbox: {checkbox_val}")
        
    # more utilities
    with st.echo():
        # the code below will be displayed and executed
        import json
        mapp = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        st.write(json.dumps(mapp, indent=4))

    # st.help("This is a cool libraly") # displays the documentation of the given object type

    # state management: persist data across re-runs
    st.session_state["name"] = "John Doe"
    if "name" in st.session_state:
        st.write(st.session_state["name"])
        st.write(st.session_state.name)
    
    # caching, resuls cached in memory, re-run only if the
    @st.cache_data
    def get_data(url):
        response = requests.get(url)
        return response.json()
    data = get_data("https://jsonplaceholder.typicode.com/todos/1")

    # cache global resources, stored in memory, shared across app all users,
    # function will be called only once, ideal for caching shared large objects
    @st.cache_resource
    def load_large_model():
        # ...
        return "large model"
    model = load_large_model()


main()
'''

st.echo()
st.code(code, language='python', line_numbers=True)
