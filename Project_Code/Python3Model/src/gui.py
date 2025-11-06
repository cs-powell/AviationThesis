import streamlit as st
import testPlatform as tp
from threading import Thread
import threading

def ex():
    st.title("Aviation Experiment Platform")
    # st.write("Welcome to the Aviation Experiment Platform GUI.")
    # st.write("This platform allows experimenters to configure and run aviation-related experiments with ease.")
    # st.write("Please use the sidebar to navigate through different sections of the platform.")
    stop_event = threading.Event()
    t1 = Thread(target=tp.ex, args=(stop_event,))

    st.button("Start Experiment",on_click=t1.start)
    st.button("Interrupt Experiment",on_click=stop_event.set())



if __name__ == "__main__":
    ex()