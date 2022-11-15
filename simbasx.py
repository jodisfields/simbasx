from datetime import date

import streamlit as st
import yfinance as yf
from prophet import Prophet
from plotly import graph_objs as go
from prophet.plot import plot_plotly
from streamlit_agraph import Config, Edge, Node, agraph

st.set_page_config(layout="wide")

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")


def graph():
    st.markdown("# Portfolio Graph")
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


def home():
    st.title("SimbASX Forecast")
    stocks = (
        "14D.AX",
        "1AD.AX",
        "1AE.AX",
        "1AG.AX",
        "1CG.AX",
        "1MC.AX",
        "1ST.AX",
        "1VG.AX",
        "1VG.AX",
        "29M.AX",
        "2BE.AX",
        "360.AX",
        "3DA.AX",
        "3DP.AX",
        "3MF.AX",
        "3PL.AX",
        "4DS.AX",
        "4DX.AX",
        "5EA.AX",
        "5GG.AX",
        "88E.AX",
        "8CO.AX",
        "8IH.AX",
        "8VI.AX",
        "92E.AX",
        "99L.AX",
        "9SP.AX",
        "A11.AX",
        "A1G.AX",
        "A1G.AX",
        "A1M.AX",
        "A200.AX",
        "A2B.AX",
        "A2M.AX",
        "A3D.AX",
        "A4N.AX",
        "A8G.AX",
        "AAA.AX",
        "AAC.AX",
        "AAJ.AX",
        "AAP.AX",
        "AAR.AX",
        "AASF.AX",
        "AAU.AX",
        "ABA.AX",
        "ABB.AX",
        "ABC.AX",
        "ABE.AX",
        "ABP.AX",
        "ABV.AX",
        "ABX.AX",
        "ABY.AX",
        "AC8.AX",
        "ACB.AX",
        "ACDC.AX",
        "ACF.AX",
        "ACL.AX",
        "ACP.AX",
        "ACQ.AX",
        "ACR.AX",
        "ACS.AX",
        "ACU.AX",
        "ACW.AX",
        "AD1.AX",
        "AD8.AX",
        "ADA.AX",
        "ADD.AX",
        "ADEF.AX",
        "ADG.AX",
        "ADH.AX",
        "ADN.AX",
        "ADO.AX",
        "ADR.AX",
        "ADS.AX",
        "ADT.AX",
        "ADV",
        "ADX.AX",
        "ADY.AX",
        "AE1.AX",
        "AEE.AX",
        "AEF.AX",
        "AEI.AX",
        "AER.AX",
        "AESG.AX",
        "AEV.AX",
        "AFA.AX",
        "AFG.AX",
        "AFI.AX",
        "AFL.AX",
        "AFP.AX",
        "AFW.AX",
        "AGC.AX",
        "AGD.AX",
        "AGE.AX",
        "AGG.AX",
        "AGH.AX",
        "AGI.AX",
        "AGL.AX",
        "AGN.AX",
        "AGR.AX",
        "AGVT.AX",
        "AGX1.AX",
        "AGY.AX",
        "AHC.AX",
        "AHF.AX",
        "AHI.AX",
        "AHK.AX",
        "AHL.AX",
        "AHN.AX",
        "AHQ.AX",
        "AHX.AX",
        "AIA.AX",
        "AIB.AX",
        "AII.AX",
        "AIM.AX",
        "AIQ.AX",
        "AIS.AX",
        "AIV.AX",
        "AIZ.AX",
        "AJJ.AX",
        "AJL.AX",
        "AJQ.AX",
        "AJX.AX",
        "AJY.AX",
        "AKE.AX",
        "AKE.AX",
        "AKG.AX",
        "AKL.AX",
        "AKM.AX",
        "AKN.AX",
        "AKO.AX",
        "AKP.AX",
        "AL3.AX",
        "AL8.AX",
        "ALA.AX",
        "ALB.AX",
        "ALC.AX",
        "ALD.AX",
        "ALG.AX",
        "ALI.AX",
        "ALK.AX",
        "ALL",
        "ALM.AX",
        "ALO.AX",
        "ALQ.AX",
        "ALT.AX",
        "ALU.AX",
        "ALV.AX",
        "ALX.AX",
        "ALY.AX",
        "AM7.AX",
        "AM7.AX",
        "AMA.AX",
        "AMC",
        "AMD.AX",
        "AME.AX",
        "AMH.AX",
        "AMI.AX",
        "AML.AX",
        "AMM.AX",
        "AMN.AX",
        "AMO.AX",
        "AMP.AX",
        "AMPPB.AX",
        "AMS.AX",
        "AMT.AX",
        "AMX.AX",
        "AN1.AX",
        "AND.AX",
        "ANG.AX",
        "ANL.AX",
        "ANN.AX",
        "ANO.AX",
        "ANP.AX",
        "ANR.AX",
        "ANX.AX",
        "ANZ",
        "ANZPF.AX",
        "ANZPG.AX",
        "ANZPH.AX",
        "ANZPI.AX",
        "ANZPJ.AX",
        "AO1.AX",
        "AOA.AX",
        "AOF.AX",
        "AON.AX",
        "AOU.AX",
        "APA.AX",
        "APC.AX",
        "APE.AX",
        "APG.AX",
        "APM.AX",
        "APS.AX",
        "APW.AX",
        "APX.AX",
        "APZ.AX",
        "AQC.AX",
        "AQD.AX",
        "AQI.AX",
        "AQLT.AX",
        "AQN.AX",
        "AQS.AX",
        "AQX.AX",
        "AQZ.AX",
        "AR1.AX",
        "AR3.AX",
        "AR9.AX",
        "ARA.AX",
        "ARB.AX",
        "ARC.AX",
        "ARD.AX",
        "ARE.AX",
        "ARF.AX",
        "ARG.AX",
        "ARL.AX",
        "ARN.AX",
        "ARO.AX",
        "ARR.AX",
        "ART.AX",
        "ARU.AX",
        "ARV.AX",
        "ARX.AX",
        "AS2.AX",
        "ASAO.AX",
        "ASB.AX",
        "ASG.AX",
        "ASH.AX",
        "ASIA.AX",
        "ASM.AX",
        "ASN.AX",
        "ASO.AX",
        "ASP.AX",
        "ASQ.AX",
        "ASR.AX",
        "ASW.AX",
        "ASX.AX",
        "AT1.AX",
        "ATA.AX",
        "ATC.AX",
        "ATEC.AX",
        "ATH.AX",
        "ATL.AX",
        "ATM.AX",
        "ATP.AX",
        "ATR.AX",
        "ATS.AX",
        "ATU.AX",
        "ATV.AX",
        "ATX.AX",
        "AU1.AX",
        "AUA.AX",
        "AUB.AX",
        "AUC.AX",
        "AUDS.AX",
        "AUE.AX",
        "AUH.AX",
        "AUI.AX",
        "AUK.AX",
        "AUMF.AX",
        "AUN.AX",
        "AUQ.AX",
        "AUR.AX",
        "AUST.AX",
        "AUT.AX",
        "AUZ.AX",
        "AV1.AX",
        "AVA.AX",
        "AVC.AX",
        "AVD.AX",
        "AVE.AX",
        "AVG.AX",
        "AVH.AX",
        "AVJ.AX",
        "AVL.AX",
        "AVM.AX",
        "AVR.AX",
        "AVW.AX",
        "AVZ",
        "AW1.AX",
        "AWC.AX",
        "AWJ.AX",
        "AWV.AX",
        "AX1.AX",
        "AX8.AX",
        "AXE.AX",
        "AXI.AX",
        "AXP.AX",
        "AYA.AX",
        "AYI.AX",
        "AYM.AX",
        "AYT.AX",
        "AYUPA.AX",
        "AZI.AX",
        "AZJ.AX",
        "AZL.AX",
        "AZS.AX",
        "AZY.AX",
        "B4P.AX",
        "BAP.AX",
        "BAS.AX",
        "BAT.AX",
        "BBC.AX",
        "BBL.AX",
        "BBN.AX",
        "BBOZ.AX",
        "BBT.AX",
        "BBUS.AX",
        "BBX.AX",
        "BC8.AX",
        "BCA.AX",
        "BCB.AX",
        "BCC.AX",
        "BCI.AX",
        "BCK.AX",
        "BCN.AX",
        "BCT.AX",
        "BDG.AX",
        "BDM.AX",
        "BDT.AX",
        "BDX.AX",
        "BEAR.AX",
        "BEE.AX",
        "BEL.AX",
        "BEM.AX",
        "BEN.AX",
        "BENPG.AX",
        "BENPH.AX",
        "BET.AX",
        "BEX.AX",
        "BEZ.AX",
        "BFC.AX",
        "BFG.AX",
        "BFL.AX",
        "BGA.AX",
        "BGD.AX",
        "BGE.AX",
        "BGL.AX",
        "BGP.AX",
        "BGT.AX",
        "BHD.AX",
        "BHP",
        "BHYB.AX",
        "BID.AX",
        "BILL.AX",
        "BIM.AX",
        "BIO.AX",
        "BIR.AX",
        "BIS.AX",
        "BIT.AX",
        "BKG.AX",
        "BKI.AX",
        "BKL.AX",
        "BKT.AX",
        "BKW.AX",
        "BKY.AX",
        "BLD.AX",
        "BLG.AX",
        "BLU.AX",
        "BLX.AX",
        "BLY.AX",
        "BLZ.AX",
        "BME.AX",
        "BMG.AX",
        "BMH.AX",
        "BML.AX",
        "BMM.AX",
        "BMN.AX",
        "BMO.AX",
        "BMR.AX",
        "BMT.AX",
        "BNDS.AX",
        "BNKS.AX",
        "BNL.AX",
        "BNO.AX",
        "BNR.AX",
        "BNZ.AX",
        "BOA.AX",
        "BOC.AX",
        "BOD.AX",
        "BOE.AX",
        "BOL.AX",
        "BOND.AX",
        "BOQ.AX",
        "BOQPE.AX",
        "BOQPF.AX",
        "BOQPG.AX",
        "BOT.AX",
        "BPH.AX",
        "BPM.AX",
        "BPP.AX",
        "BPT.AX",
        "BRB.AX",
        "BRG.AX",
        "BRI.AX",
        "BRK.AX",
        "BRL.AX",
        "BRN.AX",
        "BRU.AX",
        "BRX.AX",
        "BSA.AX",
        "BSE.AX",
        "BSL.AX",
        "BSN.AX",
        "BST.AX",
        "BSX.AX",
        "BTC.AX",
        "BTE.AX",
        "BTH.AX",
        "BTI.AX",
        "BTN.AX",
        "BTR.AX",
        "BUB.AX",
        "BUD.AX",
        "BUR.AX",
        "BUS.AX",
        "BUX.AX",
        "BUY.AX",
        "BVR.AX",
        "BVS.AX",
        "BWF.AX",
        "BWP.AX",
        "BWX.AX",
        "BXB",
        "BXN.AX",
        "BYE.AX",
        "BYH.AX",
        "BYI.AX",
        "C1X.AX",
        "C29.AX",
        "C6C.AX",
        "C79.AX",
        "C7A.AX",
        "CAA.AX",
        "CAD.AX",
        "CAE.AX",
        "CAF.AX",
        "CAG.AX",
        "CAI.AX",
        "CAJ.AX",
        "CAM.AX",
        "CAMG.AX",
        "CAN.AX",
        "CAQ.AX",
        "CAR.AX",
        "CAT.AX",
        "CAU.AX",
        "CAV.AX",
        "CAY.AX",
        "CAZ.AX",
        "CBA",
        "CBAPD.AX",
        "CBAPG.AX",
        "CBAPH.AX",
        "CBAPI.AX",
        "CBAPJ.AX",
        "CBAPK.AX",
        "CBE.AX",
        "CBH.AX",
        "CBL.AX",
        "CBO.AX",
        "CBR.AX",
        "CBY.AX",
        "CCA.AX",
        "CCE.AX",
        "CCG.AX",
        "CCP.AX",
        "CCR.AX",
        "CCV.AX",
        "CCX.AX",
        "CCZ.AX",
        "CD1.AX",
        "CD2.AX",
        "CD3.AX",
        "CDA.AX",
        "CDD.AX",
        "CDM.AX",
        "CDO.AX",
        "CDP.AX",
        "CDR.AX",
        "CDT.AX",
        "CDX.AX",
        "CE1.AX",
        "CEL.AX",
        "CEN.AX",
        "CETF.AX",
        "CF1.AX",
        "CFO.AX",
        "CG1.AX",
        "CGA.AX",
        "CGB.AX",
        "CGC.AX",
        "CGF.AX",
        "CGFPB.AX",
        "CGFPC.AX",
        "CGN.AX",
        "CGO.AX",
        "CGS.AX",
        "CHC.AX",
        "CHK.AX",
        "CHL.AX",
        "CHM.AX",
        "CHN.AX",
        "CHR.AX",
        "CHZ.AX",
        "CI1.AX",
        "CIA.AX",
        "CII.AX",
        "CIN.AX",
        "CINPA.AX",
        "CIO.AX",
        "CIP.AX",
        "CIW.AX",
        "CKA.AX",
        "CKF.AX",
        "CL8.AX",
        "CLA.AX",
        "CLB.AX",
        "CLDD.AX",
        "CLE.AX",
        "CLG.AX",
        "CLH.AX",
        "CLNE.AX",
        "CLT.AX",
        "CLU.AX",
        "CLV.AX",
        "CLW.AX",
        "CLX.AX",
        "CLZ.AX",
        "CM8.AX",
        "CMD.AX",
        "CMG.AX",
        "CML.AX",
        "CMM.AX",
        "CMO.AX",
        "CMP.AX",
        "CMW.AX",
        "CMX.AX",
        "CNB",
        "CNEW.AX",
        "CNI.AX",
        "CNJ.AX",
        "CNQ.AX",
        "CNR.AX",
        "CNU.AX",
        "CNW.AX",
        "COB.AX",
        "COD.AX",
        "COE.AX",
        "COF.AX",
        "COG.AX",
        "COH.AX",
        "COH.AX",
        "COI.AX",
        "COL",
        "COO.AX",
        "COS.AX",
        "COY.AX",
        "CPH.AX",
        "CPM.AX",
        "CPN.AX",
        "CPO.AX",
        "CPT.AX",
        "CPU.AX",
        "CPU.AX",
        "CPV.AX",
        "CQE.AX",
        "CQR.AX",
        "CR1.AX",
        "CR9.AX",
        "CRB.AX",
        "CRD.AX",
        "CRED.AX",
        "CRM.AX",
        "CRN.AX",
        "CRR.AX",
        "CRS.AX",
        "CRYP.AX",
        "CSE.AX",
        "CSF.AX",
        "CSL",
        "CSR.AX",
        "CSS.AX",
        "CST.AX",
        "CSX.AX",
        "CT1.AX",
        "CTD.AX",
        "CTE.AX",
        "CTM.AX",
        "CTO.AX",
        "CTP.AX",
        "CTQ.AX",
        "CTT.AX",
        "CTV.AX",
        "CU6.AX",
        "CUE.AX",
        "CUF.AX",
        "CUL.AX",
        "CUP.AX",
        "CURE.AX",
        "CUS.AX",
        "CUV.AX",
        "CVC.AX",
        "CVCG.AX",
        "CVL.AX",
        "CVN.AX",
        "CVR.AX",
        "CVV.AX",
        "CVW.AX",
        "CWL.AX",
        "CWP.AX",
        "CWX.AX",
        "CWY.AX",
        "CXL.AX",
        "CXM.AX",
        "CXO.AX",
        "CXO.AX",
        "CXU.AX",
        "CXX.AX",
        "CXZ.AX",
        "CY5.AX",
        "CYC.AX",
        "CYG.AX",
        "CYL.AX",
        "CYM.AX",
        "CYP.AX",
        "CYQ.AX",
        "CZL.AX",
        "CZN.AX",
        "CZR.AX",
        "D2O.AX",
        "DAF.AX",
        "DAL.AX",
        "DBBF.AX",
        "DBF.AX",
        "DBI.AX",
        "DBO.AX",
        "DC2.AX",
        "DCC.AX",
        "DCG.AX",
        "DCL.AX",
        "DCN.AX",
        "DCX.AX",
        "DDB.AX",
        "DDH.AX",
        "DDR.AX",
        "DDT.AX",
        "DEG.AX",
        "DEL.AX",
        "DEM.AX",
        "DEV.AX",
        "DEX.AX",
        "DGGF.AX",
        "DGH.AX",
        "DGL.AX",
        "DGR.AX",
        "DHG.AX",
        "DHHF.AX",
        "DHOF.AX",
        "DJRE.AX",
        "DJW.AX",
        "DKM.AX",
        "DLM.AX",
        "DLT.AX",
        "DM1.AX",
        "DMC.AX",
        "DME.AX",
        "DMG.AX",
        "DMM.AX",
        "DMP.AX",
        "DNA.AX",
        "DNK.AX",
        "DOC.AX",
        "DOR.AX",
        "DOU.AX",
        "DOW.AX",
        "DRA.AX",
        "DRE.AX",
        "DRIV.AX",
        "DRM.AX",
        "DRO.AX",
        "DRR.AX",
        "DRUG.AX",
        "DRX.AX",
        "DSE.AX",
        "DSK.AX",
        "DTC.AX",
        "DTI.AX",
        "DTL.AX",
        "DTM.AX",
        "DTR.AX",
        "DTZ.AX",
        "DUB.AX",
        "DUG.AX",
        "DUI.AX",
        "DUN.AX",
        "DUR.AX",
        "DVDY.AX",
        "DVL.AX",
        "DVP.AX",
        "DVR.AX",
        "DW8.AX",
        "DXB.AX",
        "DXC.AX",
        "DXI.AX",
        "DXN.AX",
        "DXS.AX",
        "DYL.AX",
        "DZZF.AX",
        "E200.AX",
        "E25.AX",
        "E2M.AX",
        "E33.AX",
        "E79.AX",
        "EAI.AX",
        "EAX.AX",
        "EBG.AX",
        "EBND.AX",
        "EBO.AX",
        "EBR.AX",
        "ECF.AX",
        "ECG.AX",
        "ECL.AX",
        "ECP.AX",
        "ECPGA.AX",
        "ECS.AX",
        "ECT.AX",
        "ECX.AX",
        "EDC.AX",
        "EDE.AX",
        "EDOC.AX",
        "EDU.AX",
        "EDV.AX",
        "EEG.AX",
        "EEL.AX",
        "EEU.AX",
        "EFE.AX",
        "EGG.AX",
        "EGH.AX",
        "EGL.AX",
        "EGN.AX",
        "EGR.AX",
        "EGY.AX",
        "EHE.AX",
        "EHL.AX",
        "EIGA.AX",
        "EINC.AX",
        "EIQ.AX",
        "EL8.AX",
        "ELD.AX",
        "ELE.AX",
        "ELO.AX",
        "ELS.AX",
        "ELT.AX",
        "EM1.AX",
        "EM2.AX",
        "EMB.AX",
        "EMD.AX",
        "EME.AX",
        "EMH.AX",
        "EMKT.AX",
        "EML.AX",
        "EMMG.AX",
        "EMN.AX",
        "EMP.AX",
        "EMR.AX",
        "EMS.AX",
        "EMT.AX",
        "EMU.AX",
        "EMUCA.AX",
        "EMV.AX",
        "ENA.AX",
        "ENN.AX",
        "ENR.AX",
        "ENT.AX",
        "ENV.AX",
        "ENX.AX",
        "EOF.AX",
        "EOL.AX",
        "EOS.AX",
        "EP1.AX",
        "EPM.AX",
        "EPN.AX",
        "EPX.AX",
        "EPY.AX",
        "EQE.AX",
        "EQN.AX",
        "EQR.AX",
        "EQS.AX",
        "EQT.AX",
        "EQX.AX",
        "ERA.AX",
        "ERD.AX",
        "ERG.AX",
        "ERL.AX",
        "ERM.AX",
        "ERTH.AX",
        "ERW.AX",
        "ESGI.AX",
        "ESK.AX",
        "ESPO.AX",
        "ESR.AX",
        "ESS.AX",
        "ESTX.AX",
        "ETHI.AX",
        "ETM.AX",
        "ETPMAG.AX",
        "ETPMPD.AX",
        "ETPMPM.AX",
        "ETPMPT.AX",
        "EUR.AX",
        "EV1.AX",
        "EVE.AX",
        "EVN.AX",
        "EVO.AX",
        "EVR.AX",
        "EVS.AX",
        "EVT.AX",
        "EVZ.AX",
        "EWC.AX",
        "EX1.AX",
        "EX20.AX",
        "EXL.AX",
        "EXP.AX",
        "EXR.AX",
        "EYE.AX",
        "EZL.AX",
        "EZZ.AX",
        "F100.AX",
        "FAIR.AX",
        "FAL.AX",
        "FANG.AX",
        "FAR.AX",
        "FATP.AX",
        "FAU.AX",
        "FBR.AX",
        "FBU.AX",
        "FCL.AX",
        "FCT.AX",
        "FDEM.AX",
        "FDR.AX",
        "FDV.AX",
        "FEG",
        "FEMX.AX",
        "FEX",
        "FFF.AX",
        "FFG.AX",
        "FFI.AX",
        "FFT.AX",
        "FFX.AX",
        "FG1.AX",
        "FGG.AX",
        "FGL.AX",
        "FGR.AX",
        "FGX.AX",
        "FHE.AX",
        "FHS.AX",
        "FID.AX",
        "FIJ.AX",
        "FIN.AX",
        "FLC.AX",
        "FLN.AX",
        "FLOT.AX",
        "FLT.AX",
        "FLX.AX",
        "FME.AX",
        "FMG",
        "FML.AX",
        "FMS.AX",
        "FND.AX",
        "FNX.AX",
        "FOD.AX",
        "FOOD.AX",
        "FOR.AX",
        "FOS.AX",
        "FPC.AX",
        "FPH.AX",
        "FPP.AX",
        "FRB",
        "FRE.AX",
        "FRI.AX",
        "FRM.AX",
        "FRS.AX",
        "FRX.AX",
        "FSA.AX",
        "FSF.AX",
        "FSG.AX",
        "FSI.AX",
        "FSIGA.AX",
        "FTC.AX",
        "FTL.AX",
        "FTZ.AX",
        "FUEL.AX",
        "FUTR.AX",
        "FWD.AX",
        "FXG.AX",
        "FYI.AX",
        "FZO.AX",
        "FZR.AX",
        "G1A.AX",
        "G50.AX",
        "G6M.AX",
        "G88.AX",
        "GAL.AX",
        "GAME.AX",
        "GAP.AX",
        "GAS.AX",
        "GBE.AX",
        "GBND.AX",
        "GBR.AX",
        "GBZ.AX",
        "GC1.AX",
        "GC1PA.AX",
        "GCAP.AX",
        "GCI.AX",
        "GCR.AX",
        "GCX.AX",
        "GCY.AX",
        "GDA.AX",
        "GDC.AX",
        "GDF.AX",
        "GDG.AX",
        "GDI.AX",
        "GDX.AX",
        "GEAR.AX",
        "GED.AX",
        "GEM.AX",
        "GEN.AX",
        "GES.AX",
        "GFL.AX",
        "GFLGA.AX",
        "GFN.AX",
        "GGE.AX",
        "GGOV.AX",
        "GGUS.AX",
        "GGX.AX",
        "GIB.AX",
        "GIVE.AX",
        "GL1.AX",
        "GLA.AX",
        "GLB.AX",
        "GLE.AX",
        "GLH.AX",
        "GLL.AX",
        "GLN.AX",
        "GLOB.AX",
        "GLV.AX",
        "GMA.AX",
        "GMD.AX",
        "GME.AX",
        "GMG",
        "GML.AX",
        "GMN.AX",
        "GMR.AX",
        "GMTL.AX",
        "GNC.AX",
        "GNE.AX",
        "GNG.AX",
        "GNM.AX",
        "GNP.AX",
        "GNX.AX",
        "GO2.AX",
        "GOAT.AX",
        "GOLD.AX",
        "GOR.AX",
        "GOVT.AX",
        "GOW.AX",
        "GOZ.AX",
        "GPEQ.AX",
        "GPR.AX",
        "GPS.AX",
        "GPT.AX",
        "GQG.AX",
        "GRE.AX",
        "GRL.AX",
        "GRNV.AX",
        "GROW.AX",
        "GRR.AX",
        "GRV.AX",
        "GRX.AX",
        "GSM.AX",
        "GSN.AX",
        "GSR.AX",
        "GSS.AX",
        "GT1.AX",
        "GTE.AX",
        "GTG.AX",
        "GTI.AX",
        "GTK.AX",
        "GTN.AX",
        "GTR.AX",
        "GUD.AX",
        "GUL.AX",
        "GVF.AX",
        "GW1.AX",
        "GWA.AX",
        "GWR.AX",
        "H2G.AX",
        "HACK.AX",
        "HAL.AX",
        "HAR.AX",
        "HAS.AX",
        "HAV.AX",
        "HAW.AX",
        "HBRD.AX",
        "HCD.AX",
        "HCF.AX",
        "HCH.AX",
        "HCT.AX",
        "HCW.AX",
        "HDN.AX",
        "HE8.AX",
        "HETH.AX",
        "HEUR.AX",
        "HFR.AX",
        "HFY.AX",
        "HGEN",
        "HGH.AX",
        "HGL.AX",
        "HGO.AX",
        "HGV.AX",
        "HHI.AX",
        "HHR.AX",
        "HIL.AX",
        "HIO.AX",
        "HIQ.AX",
        "HIQR.AX",
        "HIT.AX",
        "HJPN.AX",
        "HJZP.AX",
        "HLA.AX",
        "HLF.AX",
        "HLO.AX",
        "HLS.AX",
        "HLTH.AX",
        "HLX.AX",
        "HM1.AX",
        "HMC.AX",
        "HMD.AX",
        "HMG.AX",
        "HMI.AX",
        "HMX.AX",
        "HMY.AX",
        "HNDQ.AX",
        "HNG.AX",
        "HNR.AX",
        "HOR.AX",
        "HPC.AX",
        "HPG.AX",
        "HPI.AX",
        "HPP.AX",
        "HPR.AX",
        "HQLT.AX",
        "HRE.AX",
        "HRN.AX",
        "HRZ.AX",
        "HSC.AX",
        "HSN.AX",
        "HT1.AX",
        "HT8.AX",
        "HTA.AX",
        "HTG.AX",
        "HUB.AX",
        "HUM.AX",
        "HVM.AX",
        "HVN.AX",
        "HVST.AX",
        "HVY.AX",
        "HXG.AX",
        "HXL.AX",
        "HYD.AX",
        "HYGG.AX",
        "HZN.AX",
        "HZR.AX",
        "IAA.AX",
        "IAF.AX",
        "IAG.AX",
        "IAGPD.AX",
        "IAM.AX",
        "IBAL.AX",
        "IBC.AX",
        "IBG.AX",
        "IBUY.AX",
        "IBX.AX",
        "ICE.AX",
        "ICG.AX",
        "ICI.AX",
        "ICL.AX",
        "ICN.AX",
        "ICOR.AX",
        "ICR.AX",
        "ICS.AX",
        "ICT.AX",
        "ID8.AX",
        "IDA.AX",
        "IDEA.AX",
        "IDT.AX",
        "IDX.AX",
        "IEAT.AX",
        "IEC.AX",
        "IEL.AX",
        "IEM.AX",
        "IEQ.AX",
        "IESG.AX",
        "IEU.AX",
        "IFL.AX",
        "IFM.AX",
        "IFRA.AX",
        "IFT.AX",
        "IG6.AX",
        "IGB.AX",
        "IGL.AX",
        "IGN.AX",
        "IGO.AX",
        "IGRO.AX",
        "IHCB.AX",
        "IHD.AX",
        "IHEB.AX",
        "IHHY.AX",
        "IHL.AX",
        "IHOO.AX",
        "IHR.AX",
        "IHVV.AX",
        "IHWL.AX",
        "IIGF.AX",
        "IIND.AX",
        "IIQ.AX",
        "IJH.AX",
        "IJP.AX",
        "IJR.AX",
        "IKE.AX",
        "IKO.AX",
        "IKW.AX",
        "ILA.AX",
        "ILB.AX",
        "ILC.AX",
        "ILU.AX",
        "IMA.AX",
        "IMB.AX",
        "IMC.AX",
        "IMD.AX",
        "IME.AX",
        "IMI.AX",
        "IMM.AX",
        "IMPQ.AX",
        "IMR.AX",
        "IMU.AX",
        "INA.AX",
        "INCM.AX",
        "IND.AX",
        "INES.AX",
        "INF.AX",
        "ING.AX",
        "INIF.AX",
        "INL.AX",
        "INP.AX",
        "INR.AX",
        "INV.AX",
        "IOD.AX",
        "IOO.AX",
        "IOU.AX",
        "IOZ.AX",
        "IPAY.AX",
        "IPB.AX",
        "IPC.AX",
        "IPD.AX",
        "IPG.AX",
        "IPH.AX",
        "IPL.AX",
        "IPT.AX",
        "IPX.AX",
        "IR1.AX",
        "IRD.AX",
        "IRE.AX",
        "IRI.AX",
        "IRX.AX",
        "IS3.AX",
        "ISEC.AX",
        "ISLM.AX",
        "ISO.AX",
        "ISU.AX",
        "ITEK.AX",
        "ITM.AX",
        "IVC.AX",
        "IVE.AX",
        "IVO.AX",
        "IVR.AX",
        "IVT.AX",
        "IVV.AX",
        "IVX.AX",
        "IVZ.AX",
        "IWLD.AX",
        "IXC.AX",
        "IXI.AX",
        "IXJ.AX",
        "IXR.AX",
        "IXU.AX",
        "IYLD.AX",
        "IZZ.AX",
        "JAL.AX",
        "JAN.AX",
        "JAT.AX",
        "JAV.AX",
        "JAY.AX",
        "JBH.AX",
        "JCS.AX",
        "JDO.AX",
        "JEPI.AX",
        "JGH.AX",
        "JHG.AX",
        "JHX.AX",
        "JIN.AX",
        "JLG.AX",
        "JMS.AX",
        "JNO.AX",
        "JPR.AX",
        "JREG.AX",
        "JRL.AX",
        "JRV.AX",
        "JTL.AX",
        "JXT.AX",
        "JYC.AX",
        "JZRO.AX",
        "K2F.AX",
        "KAI.AX",
        "KAL.AX",
        "KAM.AX",
        "KAR.AX",
        "KAT.AX",
        "KAU.AX",
        "KBC.AX",
        "KCC.AX",
        "KCN.AX",
        "KED.AX",
        "KEY.AX",
        "KFE.AX",
        "KFM.AX",
        "KGD.AX",
        "KGL.AX",
        "KGN.AX",
        "KIL.AX",
        "KIN.AX",
        "KKC.AX",
        "KKO.AX",
        "KLI.AX",
        "KLL.AX",
        "KLO.AX",
        "KLR.AX",
        "KLS.AX",
        "KMD.AX",
        "KME.AX",
        "KNB.AX",
        "KNG.AX",
        "KNI.AX",
        "KNM.AX",
        "KNO.AX",
        "KOB.AX",
        "KOR.AX",
        "KOV.AX",
        "KP2.AX",
        "KPG.AX",
        "KPO.AX",
        "KRM.AX",
        "KRR.AX",
        "KSC.AX",
        "KSL.AX",
        "KSM.AX",
        "KSN.AX",
        "KSS.AX",
        "KTA.AX",
        "KTG.AX",
        "KWR.AX",
        "KYP.AX",
        "KZA.AX",
        "KZR.AX",
        "LAM.AX",
        "LAU.AX",
        "LAW.AX",
        "LBL.AX",
        "LBT.AX",
        "LBY.AX",
        "LCE.AX",
        "LCL.AX",
        "LCT.AX",
        "LCY.AX",
        "LDR.AX",
        "LDX.AX",
        "LEG.AX",
        "LEL.AX",
        "LER.AX",
        "LEX.AX",
        "LFG.AX",
        "LFS.AX",
        "LFSPA.AX",
        "LGI.AX",
        "LGL.AX",
        "LGM.AX",
        "LGP.AX",
        "LHM.AX",
        "LIC.AX",
        "LIN.AX",
        "LIO.AX",
        "LIS.AX",
        "LIT.AX",
        "LKE.AX",
        "LKE.AX",
        "LKO.AX",
        "LKY.AX",
        "LLC.AX",
        "LLI.AX",
        "LLL.AX",
        "LLO.AX",
        "LM8.AX",
        "LME.AX",
        "LMG.AX",
        "LML.AX",
        "LNAS.AX",
        "LNK.AX",
        "LNR.AX",
        "LNU.AX",
        "LOM.AX",
        "LOT.AX",
        "LOV.AX",
        "LPD.AX",
        "LPE.AX",
        "LPGD.AX",
        "LPI.AX",
        "LPM.AX",
        "LPM.AX",
        "LRD.AX",
        "LRK.AX",
        "LRL.AX",
        "LRS.AX",
        "LRT.AX",
        "LRV.AX",
        "LRV.AX",
        "LSA.AX",
        "LSF.AX",
        "LSGE.AX",
        "LSR.AX",
        "LSX.AX",
        "LTR.AX",
        "LV1.AX",
        "LVE.AX",
        "LVH.AX",
        "LVT.AX",
        "LYC.AX",
        "LYK.AX",
        "LYL.AX",
        "LYN.AX",
        "M24.AX",
        "M2M.AX",
        "M2R.AX",
        "M3M.AX",
        "M7T.AX",
        "M8S.AX",
        "MAAT.AX",
        "MAD.AX",
        "MAET.AX",
        "MAF.AX",
        "MAG.AX",
        "MAH.AX",
        "MAM.AX",
        "MAN.AX",
        "MAP.AX",
        "MAQ.AX",
        "MAT.AX",
        "MAU.AX",
        "MAUCA.AX",
        "MAY.AX",
        "MBH.AX",
        "MBK.AX",
        "MBLPC.AX",
        "MBLPD.AX",
        "MBX.AX",
        "MCA.AX",
        "MCCL.AX",
        "MCE.AX",
        "MCGG.AX",
        "MCL.AX",
        "MCM.AX",
        "MCP.AX",
        "MCR.AX",
        "MCT.AX",
        "MCX.AX",
        "MCY.AX",
        "MDC.AX",
        "MDI.AX",
        "MDR.AX",
        "MDX.AX",
        "MEA.AX",
        "MEA.AX",
        "MEB.AX",
        "MEC.AX",
        "MEG.AX",
        "MEI.AX",
        "MEK.AX",
        "MEL.AX",
        "MEM.AX",
        "MEU.AX",
        "MEZ.AX",
        "MFB.AX",
        "MFD.AX",
        "MFF.AX",
        "MFG.AX",
        "MGA.AX",
        "MGF.AX",
        "MGG.AX",
        "MGH.AX",
        "MGL.AX",
        "MGOC.AX",
        "MGR.AX",
        "MGT.AX",
        "MGU.AX",
        "MGV.AX",
        "MGX.AX",
        "MHC.AX",
        "MHG.AX",
        "MHHT.AX",
        "MHI.AX",
        "MHJ.AX",
        "MHK.AX",
        "MI6.AX",
        "MICH.AX",
        "MIH.AX",
        "MIL.AX",
        "MIN.AX",
        "MIO.AX",
        "MIR.AX",
        "MKAX.AX",
        "MKG.AX",
        "MKL.AX",
        "MKR.AX",
        "MLG.AX",
        "MLM.AX",
        "MLS",
        "MLX.AX",
        "MM1.AX",
        "MM8.AX",
        "MMA.AX",
        "MMC.AX",
        "MME.AX",
        "MMI.AX",
        "MMM.AX",
        "MMR.AX",
        "MMS.AX",
        "MNB.AX",
        "MND.AX",
        "MNRS.AX",
        "MNS.AX",
        "MNY.AX",
        "MOAT.AX",
        "MOB.AX",
        "MOGL.AX",
        "MOH.AX",
        "MOM.AX",
        "MOQ.AX",
        "MOT.AX",
        "MOV.AX",
        "MOZ.AX",
        "MOZG.AX",
        "MP1.AX",
        "MPA.AX",
        "MPG.AX",
        "MPL.AX",
        "MPP.AX",
        "MPR.AX",
        "MPX.AX",
        "MQG",
        "MQGPC.AX",
        "MQGPD.AX",
        "MQGPE.AX",
        "MQGPF.AX",
        "MQR.AX",
        "MR1.AX",
        "MRC.AX",
        "MRD.AX",
        "MRG.AX",
        "MRI.AX",
        "MRL.AX",
        "MRM.AX",
        "MRQ.AX",
        "MRR.AX",
        "MRZ.AX",
        "MSB.AX",
        "MSG.AX",
        "MSI.AX",
        "MSL.AX",
        "MSTR.AX",
        "MSV.AX",
        "MTAV.AX",
        "MTB.AX",
        "MTC",
        "MTH.AX",
        "MTM.AX",
        "MTO.AX",
        "MTR.AX",
        "MTS.AX",
        "MVA.AX",
        "MVB.AX",
        "MVE.AX",
        "MVF.AX",
        "MVL.AX",
        "MVOL.AX",
        "MVP.AX",
        "MVR.AX",
        "MVS.AX",
        "MVW.AX",
        "MWY.AX",
        "MX1.AX",
        "MXC.AX",
        "MXI.AX",
        "MXO.AX",
        "MXR.AX",
        "MXT.AX",
        "MYE.AX",
        "MYG.AX",
        "MYR.AX",
        "MYS.AX",
        "MYX.AX",
        "MZZ.AX",
        "N1H.AX",
        "NAB.AX",
        "NABPD.AX",
        "NABPE.AX",
        "NABPF.AX",
        "NABPH.AX",
        "NABPI.AX",
        "NAC.AX",
        "NACGA.AX",
        "NAE.AX",
        "NAE.AX",
        "NAG.AX",
        "NAM.AX",
        "NAN.AX",
        "NBI.AX",
        "NC1.AX",
        "NC6.AX",
        "NCC.AX",
        "NCCGA.AX",
        "NCK.AX",
        "NCL.AX",
        "NCM",
        "NCR.AX",
        "NCZ.AX",
        "NDIA.AX",
        "NDQ.AX",
        "NEA.AX",
        "NEC.AX",
        "NES.AX",
        "NET.AX",
        "NEU.AX",
        "NEW.AX",
        "NFL.AX",
        "NFNG.AX",
        "NGE.AX",
        "NGI.AX",
        "NGS.AX",
        "NGY.AX",
        "NHC.AX",
        "NHE.AX",
        "NHF.AX",
        "NIC.AX",
        "NIM.AX",
        "NIS.AX",
        "NKL.AX",
        "NME.AX",
        "NML.AX",
        "NMR.AX",
        "NMT.AX",
        "NNG.AX",
        "NNL.AX",
        "NNUK.AX",
        "NOL.AX",
        "NOR.AX",
        "Not.AX",
        "NOU.AX",
        "NOV.AX",
        "NOX.AX",
        "NPM.AX",
        "NPR.AX",
        "NRX.AX",
        "NRZ.AX",
        "NSB.AX",
        "NSC.AX",
        "NSM.AX",
        "NSR.AX",
        "NST.AX",
        "NSX.AX",
        "NTD.AX",
        "NTI.AX",
        "NTL.AX",
        "NTM.AX",
        "NTO.AX",
        "NTU.AX",
        "NUC.AX",
        "NUF.AX",
        "NUH.AX",
        "NVA.AX",
        "NVU.AX",
        "NVX.AX",
        "NWC.AX",
        "NWE.AX",
        "NWF.AX",
        "NWH.AX",
        "NWL.AX",
        "NWM.AX",
        "NWS.AX",
        "NWSLV.AX",
        "NXG.AX",
        "NXL.AX",
        "NXM.AX",
        "NXS.AX",
        "NXT.AX",
        "NYM.AX",
        "NYR.AX",
        "NZK.AX",
        "NZM.AX",
        "NZO.AX",
        "NZS.AX",
        "OAK.AX",
        "OAR.AX",
        "OAU.AX",
        "OBL.AX",
        "OBM.AX",
        "OCA.AX",
        "OCC.AX",
        "OCL.AX",
        "OCN.AX",
        "OCT.AX",
        "OD6.AX",
        "ODA.AX",
        "ODE.AX",
        "ODM.AX",
        "ODY.AX",
        "OEC.AX",
        "OEL.AX",
        "OEQ.AX",
        "OFX.AX",
        "OIL.AX",
        "OKJ.AX",
        "OKR.AX",
        "OLH.AX",
        "OLI.AX",
        "OLL.AX",
        "OLY.AX",
        "OM1.AX",
        "OMA.AX",
        "OMH.AX",
        "OML.AX",
        "OMX.AX",
        "ONE.AX",
        "OOK.AX",
        "OOO.AX",
        "OPH.AX",
        "OPL.AX",
        "OPN.AX",
        "OPT.AX",
        "OPY.AX",
        "ORA.AX",
        "ORG.AX",
        "ORI.AX",
        "ORM.AX",
        "ORN.AX",
        "ORR.AX",
        "OSL.AX",
        "OSM.AX",
        "OSX.AX",
        "OVN.AX",
        "OXT.AX",
        "OXX.AX",
        "OZBD.AX",
        "OZF.AX",
        "OZL.AX",
        "OZM.AX",
        "OZR.AX",
        "OZZ.AX",
        "PAA.AX",
        "PAB.AX",
        "PAC.AX",
        "PAI.AX",
        "PAM.AX",
        "PAN.AX",
        "PAR.AX",
        "PAXX.AX",
        "PBH.AX",
        "PBL.AX",
        "PBP.AX",
        "PCG.AX",
        "PCI.AX",
        "PCK.AX",
        "PCL.AX",
        "PDI",
        "PDL.AX",
        "PDN.AX",
        "PE1.AX",
        "PEB.AX",
        "PEC.AX",
        "PEK.AX",
        "PEN.AX",
        "PET.AX",
        "PEX.AX",
        "PF1.AX",
        "PFE.AX",
        "PFG.AX",
        "PFP.AX",
        "PFT.AX",
        "PG1.AX",
        "PGC.AX",
        "PGD.AX",
        "PGF.AX",
        "PGG.AX",
        "PGH.AX",
        "PGL.AX",
        "PGM.AX",
        "PGO.AX",
        "PGY.AX",
        "PH2.AX",
        "PHL.AX",
        "PHO.AX",
        "PIA.AX",
        "PIC.AX",
        "PIL.AX",
        "PIM.AX",
        "PIQ.AX",
        "PIXX.AX",
        "PKD.AX",
        "PKO.AX",
        "PL8.AX",
        "PLG.AX",
        "PLL.AX",
        "PLS",
        "PLT.AX",
        "PLUS.AX",
        "PLY.AX",
        "PMC.AX",
        "PME.AX",
        "PMGOLD.AX",
        "PMV.AX",
        "PNC.AX",
        "PNI.AX",
        "PNM.AX",
        "PNN.AX",
        "PNR.AX",
        "PNT",
        "PNV.AX",
        "PNX.AX",
        "PO3.AX",
        "POD.AX",
        "POL.AX",
        "POS.AX",
        "POU.AX",
        "POW.AX",
        "PPC.AX",
        "PPE.AX",
        "PPG.AX",
        "PPH.AX",
        "PPK.AX",
        "PPL.AX",
        "PPM.AX",
        "PPS.AX",
        "PPT.AX",
        "PPY.AX",
        "PR1.AX",
        "PRL.AX",
        "PRM.AX",
        "PRN.AX",
        "PRO.AX",
        "PRS.AX",
        "PRT.AX",
        "PRU.AX",
        "PRX.AX",
        "PSC.AX",
        "PSI.AX",
        "PSL.AX",
        "PSQ.AX",
        "PTB.AX",
        "PTG.AX",
        "PTL.AX",
        "PTM.AX",
        "PTR.AX",
        "PTX.AX",
        "PUA.AX",
        "PUR.AX",
        "PV1.AX",
        "PVE.AX",
        "PVL.AX",
        "PVS.AX",
        "PVW.AX",
        "PWH.AX",
        "PWN.AX",
        "PWR.AX",
        "PXA.AX",
        "PXS.AX",
        "PXX.AX",
        "PYC.AX",
        "PYG.AX",
        "PYR.AX",
        "QAL.AX",
        "QAN.AX",
        "QAU.AX",
        "QBE",
        "QEM.AX",
        "QFE.AX",
        "QFN.AX",
        "QGL.AX",
        "QHAL.AX",
        "QHL.AX",
        "QIP.AX",
        "QLTY.AX",
        "QMAX.AX",
        "QMIX.AX",
        "QML.AX",
        "QOZ.AX",
        "QPM.AX",
        "QPON.AX",
        "QRE.AX",
        "QRI.AX",
        "QSML.AX",
        "QUAL.AX",
        "QUB.AX",
        "QUE.AX",
        "QUS.AX",
        "QVE.AX",
        "QXR.AX",
        "R3D.AX",
        "R8R.AX",
        "RAC.AX",
        "RAD.AX",
        "RAG.AX",
        "RAN.AX",
        "RARI.AX",
        "RAS.AX",
        "RB6.AX",
        "RBD.AX",
        "RBL.AX",
        "RBR.AX",
        "RBTZ.AX",
        "RBX.AX",
        "RC1.AX",
        "RCAP.AX",
        "RCB.AX",
        "RCE.AX",
        "RCL.AX",
        "RCR.AX",
        "RCT.AX",
        "RCW.AX",
        "RDG.AX",
        "RDM.AX",
        "RDN.AX",
        "RDS.AX",
        "RDT.AX",
        "RDV.AX",
        "RDY.AX",
        "REA",
        "REC.AX",
        "RED.AX",
        "REE.AX",
        "REG.AX",
        "REH.AX",
        "REIT.AX",
        "REM.AX",
        "REP.AX",
        "REX.AX",
        "REY.AX",
        "REZ.AX",
        "RF1.AX",
        "RFA.AX",
        "RFF.AX",
        "RFG.AX",
        "RFR.AX",
        "RFT.AX",
        "RFX.AX",
        "RGB.AX",
        "RGL.AX",
        "RGS.AX",
        "RHC.AX",
        "RHCPA.AX",
        "RHI.AX",
        "RHT.AX",
        "RHY.AX",
        "RIC.AX",
        "RIE.AX",
        "RIM.AX",
        "RINC.AX",
        "RIO",
        "RKN.AX",
        "RLC.AX",
        "RLF.AX",
        "RLG.AX",
        "RLT.AX",
        "RMC.AX",
        "RMD",
        "RMI.AX",
        "RML.AX",
        "RMS.AX",
        "RMX.AX",
        "RMY.AX",
        "RND.AX",
        "RNE.AX",
        "RNO.AX",
        "RNT.AX",
        "RNU.AX",
        "RNX.AX",
        "ROBO.AX",
        "ROC.AX",
        "ROG.AX",
        "RON.AX",
        "ROO.AX",
        "ROYL.AX",
        "RPG.AX",
        "RPL.AX",
        "RPM.AX",
        "RR1.AX",
        "RRL.AX",
        "RRR.AX",
        "RSG.AX",
        "RSH.AX",
        "RSM.AX",
        "RTE.AX",
        "RTG.AX",
        "RTH.AX",
        "RTR.AX",
        "RUL.AX",
        "RVR.AX",
        "RVS.AX",
        "RWC.AX",
        "RWD.AX",
        "RWL.AX",
        "RXH.AX",
        "RXL.AX",
        "RXM.AX",
        "RYD.AX",
        "RZI.AX",
        "S2R.AX",
        "S32.AX",
        "S3GO.AX",
        "S3N.AX",
        "S66.AX",
        "SAN.AX",
        "SAU.AX",
        "SB2.AX",
        "SBM.AX",
        "SBR.AX",
        "SBW.AX",
        "SCG.AX",
        "SCL.AX",
        "SCN.AX",
        "SCP.AX",
        "SCT.AX",
        "SCU.AX",
        "SDF.AX",
        "SDG.AX",
        "SDI.AX",
        "SDR.AX",
        "SDV.AX",
        "SE1.AX",
        "SEC.AX",
        "SEG.AX",
        "SEK.AX",
        "SEMI.AX",
        "SEN.AX",
        "SEQ.AX",
        "SER.AX",
        "SES.AX",
        "SFC.AX",
        "SFG.AX",
        "SFM.AX",
        "SFR.AX",
        "SFX.AX",
        "SFY.AX",
        "SGA.AX",
        "SGC.AX",
        "SGF.AX",
        "SGH.AX",
        "SGI.AX",
        "SGLLV.AX",
        "SGM.AX",
        "SGP.AX",
        "SGQ.AX",
        "SGR.AX",
        "SHA.AX",
        "SHE.AX",
        "SHG.AX",
        "SHH.AX",
        "SHJ.AX",
        "SHL",
        "SHM.AX",
        "SHN.AX",
        "SHO.AX",
        "SHP.AX",
        "SHV.AX",
        "SI6.AX",
        "SIG.AX",
        "SIH.AX",
        "SIO.AX",
        "SIQ.AX",
        "SIS.AX",
        "SIT.AX",
        "SIV.AX",
        "SIX.AX",
        "SKC.AX",
        "SKF.AX",
        "SKN.AX",
        "SKO.AX",
        "SKS.AX",
        "SKT.AX",
        "SKY.AX",
        "SLA.AX",
        "SLB.AX",
        "SLC.AX",
        "SLF.AX",
        "SLH.AX",
        "SLM.AX",
        "SLR.AX",
        "SLS.AX",
        "SLX.AX",
        "SLZ.AX",
        "SM1.AX",
        "SMI.AX",
        "SMLL.AX",
        "SMN.AX",
        "SMP.AX",
        "SMR.AX",
        "SMS.AX",
        "SMX.AX",
        "SNAS.AX",
        "SNC.AX",
        "SND.AX",
        "SNG.AX",
        "SNL.AX",
        "SNS.AX",
        "SNX.AX",
        "SNZ.AX",
        "SO4.AX",
        "SOL.AX",
        "SOM.AX",
        "SOP.AX",
        "SOR.AX",
        "SOV.AX",
        "SP3.AX",
        "SPA.AX",
        "SPD.AX",
        "SPK.AX",
        "SPL.AX",
        "SPN.AX",
        "SPQ.AX",
        "SPT.AX",
        "SPX.AX",
        "SPY.AX",
        "SPZ.AX",
        "SQ2.AX",
        "SRG.AX",
        "SRH.AX",
        "SRI.AX",
        "SRJ.AX",
        "SRK.AX",
        "SRL.AX",
        "SRN.AX",
        "SRR",
        "SRV.AX",
        "SRX.AX",
        "SRY.AX",
        "SRZ.AX",
        "SSG.AX",
        "SSH.AX",
        "SSL.AX",
        "SSLPA.AX",
        "SSM.AX",
        "SSO.AX",
        "SSR.AX",
        "SST.AX",
        "ST1.AX",
        "STA.AX",
        "STG.AX",
        "STK.AX",
        "STM.AX",
        "STN.AX",
        "STO",
        "STP.AX",
        "STW.AX",
        "STX.AX",
        "SUBD.AX",
        "SUH.AX",
        "SUL.AX",
        "SUM.AX",
        "SUN.AX",
        "SUNPG.AX",
        "SUNPH.AX",
        "SUNPI.AX",
        "SUV.AX",
        "SVG.AX",
        "SVL.AX",
        "SVM.AX",
        "SVW.AX",
        "SVY.AX",
        "SW1.AX",
        "SWF.AX",
        "SWM.AX",
        "SWP.AX",
        "SWTZ.AX",
        "SXE.AX",
        "SXG.AX",
        "SXL.AX",
        "SYA.AX",
        "SYA.AX",
        "SYI.AX",
        "SYM.AX",
        "SYN.AX",
        "SYR.AX",
        "SYT.AX",
        "SZL.AX",
        "T3D.AX",
        "T3K.AX",
        "T92.AX",
        "TAH.AX",
        "TAM.AX",
        "TANN.AX",
        "TAR.AX",
        "TAS.AX",
        "TBA.AX",
        "TBN.AX",
        "TBR.AX",
        "TCF.AX",
        "TCG.AX",
        "TCL",
        "TCO.AX",
        "TD1.AX",
        "TDO.AX",
        "TECH.AX",
        "TEE.AX",
        "TEG.AX",
        "TEK.AX",
        "TEM.AX",
        "TER.AX",
        "TFL.AX",
        "TG1.AX",
        "TG6.AX",
        "TGA.AX",
        "TGF.AX",
        "TGH.AX",
        "TGM.AX",
        "TGN.AX",
        "TGP.AX",
        "TGR.AX",
        "THR.AX",
        "TI1.AX",
        "TIA.AX",
        "TIE.AX",
        "TIG.AX",
        "TIP.AX",
        "TKL.AX",
        "TKM.AX",
        "TLC.AX",
        "TLG.AX",
        "TLM.AX",
        "TLS",
        "TLX.AX",
        "TMB.AX",
        "TMG.AX",
        "TMH.AX",
        "TMK.AX",
        "TML.AX",
        "TMR.AX",
        "TMS.AX",
        "TMT.AX",
        "TMX.AX",
        "TMZ.AX",
        "TNE.AX",
        "TNG.AX",
        "TNT.AX",
        "TNY.AX",
        "TOE.AX",
        "TON.AX",
        "TOP.AX",
        "TOR.AX",
        "TOT.AX",
        "TOU.AX",
        "TOY.AX",
        "TPC.AX",
        "TPD.AX",
        "TPG.AX",
        "TPO.AX",
        "TPW.AX",
        "TRA.AX",
        "TRJ.AX",
        "TRM.AX",
        "TRP.AX",
        "TRS.AX",
        "TRT.AX",
        "TRU.AX",
        "TRY.AX",
        "TSC.AX",
        "TSI.AX",
        "TSK.AX",
        "TSL.AX",
        "TSN.AX",
        "TSO.AX",
        "TTA.AX",
        "TTB.AX",
        "TTI.AX",
        "TTM.AX",
        "TTT.AX",
        "TUA.AX",
        "TUL.AX",
        "TVL.AX",
        "TWD.AX",
        "TWE.AX",
        "TWR.AX",
        "TYM.AX",
        "TYR.AX",
        "TYX.AX",
        "TZL.AX",
        "TZN.AX",
        "UBI.AX",
        "UBN.AX",
        "UCM.AX",
        "UMAX.AX",
        "UMG.AX",
        "UNI.AX",
        "UOS.AX",
        "URF.AX",
        "URFPA.AX",
        "URNM.AX",
        "URW.AX",
        "URW.AX",
        "USD.AX",
        "USHY.AX",
        "USQ.AX",
        "USTB.AX",
        "UUL.AX",
        "UVA.AX",
        "VACF.AX",
        "VAE.AX",
        "VAF.AX",
        "VAL.AX",
        "VAN.AX",
        "VAP.AX",
        "VAR.AX",
        "VAS.AX",
        "VBC.AX",
        "VBLD.AX",
        "VBND.AX",
        "VBS.AX",
        "VCF.AX",
        "VCX.AX",
        "VDBA.AX",
        "VDCO.AX",
        "VDGR.AX",
        "VDHG.AX",
        "VEA.AX",
        "VEE.AX",
        "VEFI.AX",
        "VEN.AX",
        "VEQ.AX",
        "VESG.AX",
        "VETH.AX",
        "VEU.AX",
        "VG1.AX",
        "VG8.AX",
        "VGAD.AX",
        "VGB.AX",
        "VGE.AX",
        "VGL.AX",
        "VGS.AX",
        "VHT.AX",
        "VHY.AX",
        "VIA.AX",
        "VIF.AX",
        "VIG.AX",
        "VIP.AX",
        "VISM.AX",
        "VKA.AX",
        "VLC.AX",
        "VLS.AX",
        "VLUE.AX",
        "VMC.AX",
        "VMG.AX",
        "VMIN.AX",
        "VML.AX",
        "VMM.AX",
        "VMS.AX",
        "VMT.AX",
        "VN8.AX",
        "VNGS.AX",
        "VNT.AX",
        "VOL.AX",
        "VPR.AX",
        "VR1.AX",
        "VR8.AX",
        "VRC.AX",
        "VRS.AX",
        "VRX.AX",
        "VSL.AX",
        "VSO.AX",
        "VSR.AX",
        "VTG.AX",
        "VTI.AX",
        "VTS.AX",
        "VTX.AX",
        "VUK.AX",
        "VUL.AX",
        "VVA.AX",
        "VVLU.AX",
        "VYS.AX",
        "W2V.AX",
        "WA1.AX",
        "WAA.AX",
        "WAF.AX",
        "WAK.AX",
        "WAM.AX",
        "WAR.AX",
        "WAT.AX",
        "WAX.AX",
        "WBC",
        "WBCPH.AX",
        "WBCPI.AX",
        "WBCPJ.AX",
        "WBCPK.AX",
        "WBCPL.AX",
        "WBE.AX",
        "WBT.AX",
        "WC1.AX",
        "WC8.AX",
        "WCG.AX",
        "WCMQ.AX",
        "WCN.AX",
        "WDIV.AX",
        "WDMF.AX",
        "WDS",
        "WEB.AX",
        "WEC.AX",
        "WEL.AX",
        "WEMG.AX",
        "WES",
        "WFL.AX",
        "WGB.AX",
        "WGN.AX",
        "WGO.AX",
        "WGR.AX",
        "WGX.AX",
        "WHC.AX",
        "WHF.AX",
        "WHFPA.AX",
        "WHFPB.AX",
        "WHK.AX",
        "WIA.AX",
        "WIN.AX",
        "WKT.AX",
        "WLD.AX",
        "WLE.AX",
        "WLS.AX",
        "WMA.AX",
        "WMC.AX",
        "WMG.AX",
        "WMI.AX",
        "WML.AX",
        "WNR.AX",
        "WNX.AX",
        "WOA.AX",
        "WOO.AX",
        "WOR.AX",
        "WOT.AX",
        "WOW",
        "WPR.AX",
        "WQG.AX",
        "WR1.AX",
        "WR1.AX",
        "WRK.AX",
        "WRLD.AX",
        "WRM.AX",
        "WSI.AX",
        "WSP.AX",
        "WSR.AX",
        "WTC",
        "WTL.AX",
        "WTN.AX",
        "WVOL.AX",
        "WWG.AX",
        "WWI.AX",
        "WXHG.AX",
        "WXOZ.AX",
        "WYX.AX",
        "WZR.AX",
        "X2M.AX",
        "X64.AX",
        "XAM.AX",
        "XARO.AX",
        "XCO2.AX",
        "XF1.AX",
        "XMET.AX",
        "XPN.AX",
        "XRF.AX",
        "XRG.AX",
        "XRO.AX",
        "XST.AX",
        "XTC.AX",
        "XTE.AX",
        "YAL.AX",
        "YANK.AX",
        "YBR.AX",
        "YMAX.AX",
        "YOJ.AX",
        "YOW.AX",
        "YPB.AX",
        "YRL.AX",
        "Z2U.AX",
        "ZAG.AX",
        "ZEO.AX",
        "ZER.AX",
        "ZEU.AX",
        "ZGL.AX",
        "ZIM.AX",
        "ZIP.AX",
        "ZLD.AX",
        "ZMI.AX",
        "ZMM.AX",
        "ZNC.AX",
        "ZNO.AX",
        "ZYAU.AX",
        "ZYUS.AX",
    )
    selected_stock = st.selectbox("Select dataset for prediction", stocks)
    n_years = st.slider("Years of prediction:", 1, 5)
    period = n_years * 365

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, "2015-01-01", TODAY)
        data.reset_index(inplace=True)
        return data

    data = load_data(selected_stock)

    # st.subheader("Raw data")
    # st.write(data.tail())

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



    st.write(f"Forecast plot for {n_years} years")
    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    START = st.date_input("Select start date for model")
    END = st.date_input("Select end date for model")
    tickerSymbol = selected_stock
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start=START, end=END)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
    """
    )
    st.line_chart(tickerDf.Open)
    st.write(
        """
    ## Volume Price
    """
    )
    st.line_chart(tickerDf.Volume)


    st.write("Forecast components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)


def page_2():
    st.markdown("# FEX")
    tickerSymbol = "FEX"
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    tickerDf = tickerData.history(period="1d", start="2015-01-01", end=TODAY)
    st.write(
        """
    ## Closing Price
    """
    )
    st.line_chart(tickerDf.Close)
    st.write(
        """
    ## Opening Price
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
    "Graph": graph,
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
selected_page = st.sidebar.selectbox("Select a page", list(page_names_to_funcs.keys()))
page_names_to_funcs[selected_page]()
