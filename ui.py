import streamlit as st
from finance import build_agent


st.set_page_config(
    page_title="AI Finance Agent",
    page_icon="📈",
    layout="centered"
)


st.title("📈 AI Finance Agent")

st.write(
    "Ask about stock prices, analyst recommendations, "
    "and company fundamentals."
)


@st.cache_resource
def get_agent():
    return build_agent()


agent = get_agent()


query = st.text_input(
    "Enter your finance query",
    placeholder="Example: Share the MSFT stock price and analyst recommendations"
)


if st.button("Analyze"):
    if query:
        with st.spinner("Researching..."):
            response = agent.run(query)

        st.markdown("### 📊 Analysis")
        st.markdown(response.content)

    else:
        st.warning("Please enter a query.")