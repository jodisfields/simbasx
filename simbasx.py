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
    st.sidebar("## FEX")
    st.sidebar("## LKE.AX")
    st.sidebar("## AVZ")
    st.sidebar("## MEA.AX")
    st.sidebar("## MLS")
    st.sidebar("## CXO.AX")
    st.sidebar("## LPM.AX")
    st.sidebar("## A1G.AX")
    st.sidebar("## AKE.AX")
    st.sidebar("## FEG")
    st.sidebar("## NAE.AX")
    st.sidebar("## CNB")
    st.sidebar("## ADV")
    st.sidebar("## PDI")
    st.sidebar("## WR1.AX")
    st.sidebar("## SRR")
    st.sidebar("## FRB")
    st.sidebar("## PNT")
    st.sidebar("## LRV.AX")
    st.sidebar("## AM7.AX")
    st.sidebar("## MTC")
    st.sidebar("## 1VG.AX")
    st.sidebar("## HGEN")
    st.sidebar("## SYA.AX")
    st.sidebar("## BHP")
    st.sidebar("## CBA")
    st.sidebar("## CSL")
    st.sidebar("## WBC")
    st.sidebar("## ANZ")
    st.sidebar("## WDS")
    st.sidebar("## MQG")
    st.sidebar("## FMG")
    st.sidebar("## WES")
    st.sidebar("## RMD")
    st.sidebar("## TLS")
    st.sidebar("## TCL")
    st.sidebar("## WOW")
    st.sidebar("## RIO")
    st.sidebar("## GMG")
    st.sidebar("## AMC")
    st.sidebar("## STO")
    st.sidebar("## ALL")
    st.sidebar("## COL")
    st.sidebar("## WTC")
    st.sidebar("## QBE")
    st.sidebar("## NCM")
    st.sidebar("## SHL")
    st.sidebar("## PLS")
    st.sidebar("## REA")
    st.sidebar("## BXB")
    st.sidebar("## CPU.AX")
    st.sidebar("## MIN")
    st.sidebar("## SUN")
    st.sidebar("## SCG")
    st.sidebar("## NWS")
    st.sidebar("## RHC")
    st.sidebar("## COH.AX")
    st.sidebar("## ASX")
    st.sidebar("## JHX")
    st.sidebar("## ORG")
    st.sidebar("## APA")
    st.sidebar("## EDV")
    st.sidebar("## IGO")
    st.sidebar("## IAG")
    st.sidebar("## VAS")
    st.sidebar("## Not")
    st.sidebar("## NST")
    st.sidebar("## QAN")
    st.sidebar("## URW.AX")
    st.sidebar("## MEZ")
    st.sidebar("## XRO")
    st.sidebar("## FPH")
    st.sidebar("## AIA")
    st.markdown("# Home")
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
        "LKE.AX",
        "AVZ",
        "MEA.AX",
        "MLS",
        "CXO.AX",
        "LPM.AX",
        "A1G.AX",
        "AKE.AX",
        "FEG",
        "NAE.AX",
        "CNB",
        "ADV",
        "PDI",
        "WR1.AX",
        "SRR",
        "FRB",
        "PNT",
        "LRV.AX",
        "AM7.AX",
        "MTC",
        "1VG.AX",
        "HGEN",
        "SYA.AX",
        "BHP",
        "CBA",
        "CSL",
        "WBC",
        "ANZ",
        "WDS",
        "MQG",
        "FMG",
        "WES",
        "RMD",
        "TLS",
        "TCL",
        "WOW",
        "RIO",
        "GMG",
        "AMC",
        "STO",
        "ALL",
        "COL",
        "WTC",
        "QBE",
        "NCM",
        "SHL",
        "PLS",
        "REA",
        "BXB",
        "CPU.AX",
        "MIN",
        "SUN",
        "SCG",
        "NWS",
        "RHC",
        "COH.AX",
        "ASX",
        "JHX",
        "ORG",
        "APA",
        "EDV",
        "IGO",
        "IAG",
        "VAS",
        "Not",
        "NST",
        "QAN",
        "URW.AX",
        "MEZ",
        "XRO",
        "FPH",
        "AIA",
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


def page_2():
    st.markdown("# FEX")
    tickerSymbol = "FEX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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


def page_3():
    st.markdown("# LKE.AX")
    tickerSymbol = "LKE.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# AVZ")
    tickerSymbol = "AVZ"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# MEA.AX")
    tickerSymbol = "MEA.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# MLS")
    tickerSymbol = "MLS"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# CXO.AX")
    tickerSymbol = "CXO.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# LPM.AX")
    tickerSymbol = "LPM.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# A1G.AX")
    tickerSymbol = "A1G.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# AKE.AX")
    tickerSymbol = "AKE.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# FEG")
    tickerSymbol = "FEG"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# NAE.AX")
    tickerSymbol = "NAE.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# CNB")
    tickerSymbol = "CNB"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# ADV")
    tickerSymbol = "ADV"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# PDI")
    tickerSymbol = "PDI"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# WR1.AX")
    tickerSymbol = "WR1.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# SRR")
    tickerSymbol = "SRR"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# FRB")
    tickerSymbol = "FRB"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# PNT")
    tickerSymbol = "PNT"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# LRV.AX")
    tickerSymbol = "LRV.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# AM7.AX")
    tickerSymbol = "AM7.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# MTC")
    tickerSymbol = "MTC"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# 1VG.AX")
    tickerSymbol = "1VG.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# HGEN")
    tickerSymbol = "HGEN"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    st.markdown("# SYA")
    tickerSymbol = "SYA.AX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=TODAY)
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
    "FEX": page_2,
    "LKE.AX": page_3,
    "AVZ": page_4,
    "MEA.AX": page_5,
    "MLS": page_6,
    "CXO.AX": page_7,
    "LPM.AX": page_8,
    "A1G.AX": page_9,
    "AKE.AX": page_10,
    "FEG": page_11,
    "NAE.AX": page_12,
    "CNB": page_13,
    "ADV": page_14,
    "PDI": page_15,
    "WR1.AX": page_16,
    "SRR": page_17,
    "FRB": page_18,
    "PNT": page_19,
    "LRV.AX": page_20,
    "AM7.AX": page_21,
    "MTC": page_22,
    "1VG.AX": page_23,
    "HGEN": page_24,
    "SYA.AX": page_25,
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
