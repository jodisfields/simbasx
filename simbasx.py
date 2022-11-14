from datetime import date

import streamlit as st
import yfinance as yf
from plotly import graph_objs as go
from prophet import Prophet
from prophet.plot import plot_plotly
from streamlit_agraph import Config, Edge, Node, agraph

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")


def home():
    st.markdown("# Home")
    st.sidebar.markdown("# Home")
    nodes = []
    edges = []
    nodes.append(
        Node(
            id="SB",
            label="John Doe`",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="FEX",
            label="FEX",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="LKE",
            label="LKE",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="AVZ",
            label="AVZ",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="MEA",
            label="MEA",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="MLS",
            label="MLS",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="CXO",
            label="CXO",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="LPM",
            label="LPM",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="A1G",
            label="A1G",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="AKE",
            label="AKE",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="FEG",
            label="FEG",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="NAE",
            label="NAE",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="CNB",
            label="CNB",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="ADV",
            label="ADV",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="PDI",
            label="PDI",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="WR1",
            label="WR1",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="SRR",
            label="SRR",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="FRB",
            label="FRB",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="PNT",
            label="PNT",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="LRV",
            label="LRV",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="AM7",
            label="AM7",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="MTC",
            label="MTC",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="1VG",
            label="1VG",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    nodes.append(
        Node(
            id="HGEN",
            label="HGEN",
            size=15,
            shape="circularImage",
            image="https://cdn.iconscout.com/icon/premium/png-256-thumb/graph-theory-1807124-1534162.png",
        )
    )  # includes **kwargs
    edges.append(
        Edge(
            source="SB",
            target="FEX",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="LKE",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="AVZ",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="MEA",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="MLS",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="CXO",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="LPM",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="A1G",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="AKE",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="FEG",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="NAE",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="CNB",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="FEX",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="ADV",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="PDI",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="WR1",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="SRR",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="FRB",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="PNT",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="LRV",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="AM7",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="MTC",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="1VG",
            # **kwargs
        )
    )
    edges.append(
        Edge(
            source="SB",
            target="HGEN",
            # **kwargs
        )
    )
    config = Config(
        width=1000,
        height=1000,
        # **kwargs
    )
    return_value = agraph(nodes=nodes, edges=edges, config=config)


def forecast():
    st.title("SimbASX Forecast")
    stocks = (
        "FEX",
        "LKE",
        "AVZ",
        "MEA",
        "MLS",
        "CXO",
        "LPM",
        "A1G",
        "AKE",
        "FEG",
        "NAE",
        "CNB",
        "ADV",
        "PDI",
        "WR1",
        "SRR",
        "FRB",
        "PNT",
        "LRV",
        "AM7",
        "MTC",
        "1VG",
        "HGEN",
    )
    selected_stock = st.selectbox("Select dataset for prediction", stocks)
    n_years = st.slider("Years of prediction:", 1, 4)
    period = n_years * 365

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data_load_state = st.text("Loading data...")
    data = load_data(selected_stock)
    data_load_state.text("Loading data... done!")

    st.subheader("Raw data")
    st.write(data.tail())

    # Plot raw data
    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="stock_open"))
        fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="stock_close"))
        fig.layout.update(
            title_text="Time Series data with Rangeslider",
            xaxis_rangeslider_visible=True,
        )
        st.plotly_chart(fig)

    plot_raw_data()

    # Predict forecast with Prophet.
    df_train = data[["Date", "Close"]]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)
    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    # Show and plot forecast
    st.subheader("Forecast data")
    st.write(forecast.tail())

    st.write(f"Forecast plot for {n_years} years")
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)


def page2():
    st.markdown("# FEX")
    st.sidebar.markdown("# FEX")
    tickerSymbol = "FEX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page3():
    st.markdown("# LKE")
    st.sidebar.markdown("# LKE")
    tickerSymbol = "LKE"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_4():
    st.markdown("# LKE")
    st.sidebar.markdown("# LKE")
    tickerSymbol = "LKE"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_5():
    st.markdown("# AVZ")
    st.sidebar.markdown("# AVZ")
    tickerSymbol = "AVZ"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_6():
    st.markdown("# MEA")
    st.sidebar.markdown("# MEA")
    tickerSymbol = "MEA"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_7():
    st.markdown("# MLS")
    st.sidebar.markdown("# MLS")
    tickerSymbol = "MLS"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_8():
    st.markdown("# CXO")
    st.sidebar.markdown("# CXO")
    tickerSymbol = "CXO"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_9():
    st.markdown("# LPM")
    st.sidebar.markdown("# LPM")
    tickerSymbol = "LPM"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_10():
    st.markdown("# A1G")
    st.sidebar.markdown("# A1G")
    tickerSymbol = "A1G"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_11():
    st.markdown("# AKE")
    st.sidebar.markdown("# AKE")
    tickerSymbol = "AKE"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_12():
    st.markdown("# FEG")
    st.sidebar.markdown("# FEG")
    tickerSymbol = "FEG"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_13():
    st.markdown("# NAE")
    st.sidebar.markdown("# NAE")
    tickerSymbol = "NAE"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_14():
    st.markdown("# CNB")
    st.sidebar.markdown("# CNB")
    tickerSymbol = "CNB"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_15():
    st.markdown("# FEX")
    st.sidebar.markdown("# FEX")
    tickerSymbol = "FEX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_16():
    st.markdown("# ADV")
    st.sidebar.markdown("# ADV")
    tickerSymbol = "ADV"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_17():
    st.markdown("# PDI")
    st.sidebar.markdown("# PDI")
    tickerSymbol = "PDI"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_18():
    st.markdown("# WR1")
    st.sidebar.markdown("# WR1")
    tickerSymbol = "WR1"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_19():
    st.markdown("# SRR")
    st.sidebar.markdown("# SRR")
    tickerSymbol = "SRR"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_20():
    st.markdown("# FRB")
    st.sidebar.markdown("# FRB")
    tickerSymbol = "FRB"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_21():
    st.markdown("# PNT")
    st.sidebar.markdown("# PNT")
    tickerSymbol = "PNT"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_22():
    st.markdown("# LRV")
    st.sidebar.markdown("# LRV")
    tickerSymbol = "LRV"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_23():
    st.markdown("# AM7")
    st.sidebar.markdown("# AM7")
    tickerSymbol = "AM7"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_24():
    st.markdown("# MTC")
    st.sidebar.markdown("# MTC")
    tickerSymbol = "MTC"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_25():
    st.markdown("# 1VG")
    st.sidebar.markdown("# 1VG")
    tickerSymbol = "1VG"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


def page_26():
    st.markdown("# HGEN")
    st.sidebar.markdown("# HGEN")
    tickerSymbol = "HGEN"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2010-5-31", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


page_names_to_funcs = {
    "Home": home,
    "Forecast": forecast,
    "FEX": page2,
    "LKE": page3,
    "LKE": page_4,
    "AVZ": page_5,
    "MEA": page_6,
    "MLS": page_7,
    "CXO": page_8,
    "LPM": page_9,
    "A1G": page_10,
    "AKE": page_11,
    "FEG": page_12,
    "NAE": page_13,
    "CNB": page_14,
    "FEX": page_15,
    "ADV": page_16,
    "PDI": page_17,
    "WR1": page_18,
    "SRR": page_19,
    "FRB": page_20,
    "PNT": page_21,
    "LRV": page_22,
    "AM7": page_23,
    "MTC": page_24,
    "1VG": page_25,
    "HGEN": page_26,
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
