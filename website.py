import streamlit as st
import time

def main():
    st.title("Will You Marry Me? 💍")

    # Displaying proposal message
    st.write("My Dearest life Mpaleng,")
    st.write("As I sit down to write this, I find myself at a loss for words. But there is something I want to ask you, something that has been on my mind for a long time...")

    # Buttons for proposal response
    if st.button("Yes"):
        st.success("💖💍🎉 Congratulations! You said yes! 🎉💍💖")
        # Display floating hearts
        show_hearts()
    if st.button("No"):
        st.warning("Ooops! We are still getting married 😉")

def show_hearts():
    st.write("💖" * 100)  # Displaying lots of hearts
    time.sleep(5)  # Pause for 5 seconds

if __name__ == "__main__":
    main()