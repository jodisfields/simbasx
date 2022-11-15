from datetime import date

import streamlit as st
import yfinance as yf
from plotly import graph_objs as go
from prophet import Prophet
from prophet.plot import plot_plotly
from streamlit_agraph import Config, Edge, Node, agraph


START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")
st.set_page_config(layout="wide")


def home():
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
        "NAB",
        "S32",
        "CPU",
        "COH",
        "SOL",
        "TLC",
        "REH",
        "TWE",
        "ALX",
        "AKE",
        "AFI",
        "TPG",
        "OZL",
        "VCX",
        "SGP",
        "SPK",
        "PMGOLD",
        "MGOC",
        "MGR",
        "GPT",
        "IEL",
        "DXS",
        "BSL",
        "LYC",
        "WOR",
        "IPL",
        "WHC",
        "MPL",
        "SEK",
        "CAR",
        "ORI",
        "SVW",
        "EBO",
        "ARG",
        "MCY",
        "AZJ",
        "ALD",
        "YAL",
        "CHC",
        "PME",
        "ALQ",
        "CWY",
        "IFT",
        "DMP",
        "LLC",
        "SDF",
        "AGL",
        "HVN",
        "VGS",
        "IVV",
        "BEN",
        "EVN",
        "CGF",
        "BOQ",
        "JBH",
        "STW",
        "ALU",
        "QUB",
        "AWC",
        "NHC",
        "LTR",
        "A2M",
        "GQG",
        "ILU",
        "NXT",
        "VEA",
        "PMV",
        "BPT",
        "TNE",
        "AMP",
        "SQ2",
        "MTS",
        "NEC",
        "FBU",
        "ANN",
        "IOZ",
        "DOW",
        "CRN",
        "NWL",
        "NHF",
        "FLT",
        "CNU",
        "BLD",
        "BKW",
        "APE",
        "CXO",
        "CLW",
        "CIA",
        "VTS",
        "BRG",
        "PRU",
        "CBAPD",
        "SCP",
        "NSR",
        "QUAL",
        "APM",
        "SGR",
        "ZIM",
        "GOLD",
        "LOV",
        "A200",
        "HDN",
        "GNE",
        "VHY",
        "CTD",
        "PXA",
        "IOO",
        "BWP",
        "SGM",
        "PDN",
        "ORA",
        "NIC",
        "GOZ",
        "AIZ",
        "NABPH",
        "AAA",
        "NDQ",
        "ABP",
        "RWC",
        "ARB",
        "SUL",
        "DRR",
        "BAP",
        "CQR",
        "TAH",
        "EVT",
        "BFL",
        "AUB",
        "IFL",
        "SMR",
        "CSR",
        "ETHI",
        "VEU",
        "VAP",
        "VNT",
        "TLX",
        "HUB",
        "SYA",
        "WEB",
        "NUF",
        "VUK",
        "IPH",
        "MGF",
        "DEG",
        "NABPI",
        "SNZ",
        "VGAD",
        "HLS",
        "SKC",
        "NABPF",
        "CIP",
        "LIC",
        "WPR",
        "DHG",
        "CMW",
        "HBRD",
        "WAM",
        "PPT",
        "PNI",
        "SFR",
        "MFG",
        "VDHG",
        "DDR",
        "CHN",
        "JLG",
        "IRE",
        "GNC",
        "GOR",
        "LNK",
        "WBCPJ",
        "HYGG",
        "WBCPK",
        "CBAPK",
        "WBCPH",
        "PSI",
        "IAF",
        "MVW",
        "ANZPG",
        "MXT",
        "WLE",
        "CEN",
        "INA",
        "CBAPI",
        "SYR",
        "ELD",
        "CBAPH",
        "LSF",
        "IVC",
        "PDL",
        "CMM",
        "LKE",
        "WBCPL",
        "ANZPI",
        "NABPD",
        "VAF",
        "HMC",
        "OCL",
        "WBCPI",
        "CNI",
        "CBAPG",
        "JDO",
        "RRL",
        "MND",
        "PNV",
        "LFS",
        "MFF",
        "ARF",
        "CCP",
        "NAN",
        "BKL",
        "PPH",
        "ANZPJ",
        "BKI",
        "KAR",
        "NVX",
        "INR",
        "FAIR",
        "CGC",
        "IMU",
        "CQE",
        "DBI",
        "RCAP",
        "MAQ",
        "AUI",
        "IXJ",
        "CKF",
        "WAF",
        "OBL",
        "29M",
        "CBAPJ",
        "SLR",
        "360",
        "GUD",
        "NWH",
        "LFG",
        "HGH",
        "ABC",
        "PWH",
        "BGP",
        "KLS",
        "TGR",
        "BRN",
        "PTM",
        "VUL",
        "DUI",
        "MQGPC",
        "VSL",
        "NEU",
        "AAC",
        "DTL",
        "HSN",
        "GMA",
        "BGA",
        "ING",
        "ANZPF",
        "ANZPH",
        "NEA",
        "CUV",
        "RFF",
        "MQGPD",
        "UMG",
        "MP1",
        "COF",
        "NABPE",
        "AGY",
        "MMS",
        "BGL",
        "AX1",
        "DXI",
        "GRR",
        "BOE",
        "IMD",
        "ASB",
        "JIN",
        "HTA",
        "IEU",
        "RPL",
        "CXL",
        "CIN",
        "SFY",
        "SDR",
        "MICH",
        "MCR",
        "IEM",
        "XARO",
        "GEM",
        "TYR",
        "TIE",
        "RBD",
        "MAF",
        "NCK",
        "VGB",
        "WTN",
        "MQGPF",
        "DJW",
        "MAD",
        "ERA",
        "OML",
        "URW",
        "IFRA",
        "PRN",
        "RMS",
        "MGH",
        "VSO",
        "CDA",
        "MQGPE",
        "SWM",
        "ACL",
        "VVLU",
        "QAL",
        "KMD",
        "PL8",
        "PPM",
        "MSB",
        "MBLPC",
        "QPON",
        "CBO",
        "EMR",
        "EQT",
        "SHV",
        "RIC",
        "CTT",
        "WGB",
        "VIF",
        "SIQ",
        "MBLPD",
        "BLY",
        "PGF",
        "NNUK",
        "OFX",
        "ADT",
        "MVA",
        "SIG",
        "VDGR",
        "SGF",
        "IAA",
        "HACK",
        "VESG",
        "VDBA",
        "AD8",
        "JRV",
        "IDX",
        "VGE",
        "ARU",
        "TUA",
        "HPI",
        "JHG",
        "REG",
        "DYL",
        "RNU",
        "IHVV",
        "NMT",
        "SM1",
        "ABB",
        "SLX",
        "KKC",
        "TER",
        "STX",
        "NBI",
        "WHF",
        "PBH",
        "ACDC",
        "LLL",
        "MGX",
        "ECX",
        "RF1",
        "STA",
        "OCA",
        "EHE",
        "OPH",
        "HM1",
        "VACF",
        "AEF",
        "SLF",
        "GWA",
        "WBT",
        "TPW",
        "MOT",
        "ILB",
        "OMH",
        "MIR",
        "PFP",
        "QRI",
        "GMD",
        "COE",
        "VBND",
        "VG1",
        "IWLD",
        "A11",
        "MYR",
        "BENPH",
        "FCL",
        "PLL",
        "NTO",
        "MYX",
        "PPC",
        "QHAL",
        "AFG",
        "ZIP",
        "SBM",
        "IFM",
        "RED",
        "PWR",
        "AQZ",
        "CTM",
        "GLN",
        "5EA",
        "MHHT",
        "ILC",
        "BCB",
        "GL1",
        "A4N",
        "HCW",
        "IJP",
        "DGL",
        "AGG",
        "FGX",
        "GCI",
        "CGFPB",
        "MHJ",
        "HAS",
        "ELO",
        "MYS",
        "PPS",
        "PGH",
        "TLG",
        "SNL",
        "RDY",
        "MOAT",
        "SSM",
        "OPT",
        "PIC",
        "MNY",
        "PAR",
        "BLX",
        "FGG",
        "QOZ",
        "CRED",
        "GDX",
        "VG8",
        "RUL",
        "F100",
        "PE1",
        "GEAR",
        "IJR",
        "FLOT",
        "ALI",
        "VETH",
        "ASIA",
        "RMC",
        "KCN",
        "PAC",
        "IAGPD",
        "DVP",
        "WGX",
        "PGG",
        "DJRE",
        "SGLLV",
        "GDI",
        "MNS",
        "BOQPG",
        "DXC",
        "SUNPI",
        "CGFPC",
        "SSR",
        "ASG",
        "ALK",
        "SUNPH",
        "EHL",
        "ADH",
        "REP",
        "SUNPG",
        "IGL",
        "AASF",
        "UNI",
        "IVE",
        "PCI",
        "SLC",
        "SUBD",
        "DDH",
        "BTH",
        "IGB",
        "PAN",
        "GNG",
        "QAU",
        "AGVT",
        "PMC",
        "MVF",
        "JMS",
        "HT1",
        "AFP",
        "YMAX",
        "IHL",
        "BOQPE",
        "KGN",
        "SKT",
        "3PL",
        "WDIV",
        "BILL",
        "CAJ",
        "RAC",
        "CWP",
        "BBN",
        "AIS",
        "SDG",
        "QLTY",
        "APX",
        "AMH",
        "PEB",
        "BENPG",
        "SYI",
        "SRV",
        "AKP",
        "CGS",
        "AGI",
        "CDP",
        "CVW",
        "AVR",
        "SST",
        "VGL",
        "VBLD",
        "AGX1",
        "PPE",
        "NWE",
        "ARX",
        "WMI",
        "PIXX",
        "LOT",
        "GDF",
        "NWF",
        "SRG",
        "PAI",
        "BST",
        "VAE",
        "QPM",
        "BMN",
        "HFR",
        "DRE",
        "BFG",
        "NEW",
        "ECF",
        "CCX",
        "CAU",
        "IHCB",
        "MAH",
        "WVOL",
        "ASN",
        "ASM",
        "WXOZ",
        "AYUPA",
        "AMA",
        "MVR",
        "TECH",
        "FSF",
        "TRA",
        "IVZ",
        "BSE",
        "IHD",
        "AMPPB",
        "WCMQ",
        "FZO",
        "APZ",
        "SYM",
        "CDM",
        "TBN",
        "IOD",
        "TRJ",
        "MLX",
        "NGI",
        "EGG",
        "SKO",
        "FDV",
        "IMM",
        "COG",
        "HUM",
        "BCI",
        "BUB",
        "ALG",
        "UOS",
        "CVN",
        "LYL",
        "RHCPA",
        "KSC",
        "LGL",
        "WGO",
        "MRM",
        "ISEC",
        "WAX",
        "BOQPF",
        "PSQ",
        "RCB",
        "HLO",
        "RHI",
        "RARI",
        "SXL",
        "RHY",
        "SO4",
        "FUEL",
        "SVL",
        "ABA",
        "BBOZ",
        "KSL",
        "NPR",
        "BBUS",
        "PYC",
        "RDV",
        "PIA",
        "BET",
        "GDG",
        "SFC",
        "EX20",
        "BNDS",
        "VEQ",
        "IZZ",
        "PGC",
        "FFX",
        "ICT",
        "GNX",
        "CVC",
        "SPL",
        "GAL",
        "BCK",
        "VDCO",
        "PNR",
        "PLUS",
        "LPI",
        "AOF",
        "EZL",
        "IPG",
        "WQG",
        "NFNG",
        "VISM",
        "LRS",
        "ACW",
        "E25",
        "TWR",
        "ROBO",
        "FID",
        "HZN",
        "QUS",
        "WOT",
        "IJH",
        "CLV",
        "KED",
        "QVE",
        "KPG",
        "WMA",
        "ALC",
        "BHYB",
        "HE8",
        "ENN",
        "MVB",
        "IHWL",
        "CAT",
        "DHHF",
        "PTB",
        "IXI",
        "RDT",
        "FANG",
        "VLUE",
        "NTU",
        "NZM",
        "RSG",
        "SMP",
        "ANG",
        "GT1",
        "COB",
        "TGP",
        "CEL",
        "SVM",
        "GVF",
        "AZL",
        "HETH",
        "BVS",
        "D2O",
        "EML",
        "SFX",
        "FEMX",
        "SHJ",
        "ATL",
        "CKA",
        "TRS",
        "C79",
        "MAY",
        "GBND",
        "NXL",
        "MAET",
        "BTI",
        "PCG",
        "CAI",
        "SRL",
        "MVE",
        "WXHG",
        "DCN",
        "MTO",
        "WAR",
        "LAU",
        "PBP",
        "ATA",
        "SXE",
        "GNP",
        "BRI",
        "HLA",
        "RBL",
        "LGI",
        "LIN",
        "EXP",
        "HVST",
        "VLC",
        "PEN",
        "OZBD",
        "ERTH",
        "MAU",
        "SLH",
        "CU6",
        "COI",
        "IPD",
        "AVG",
        "PRT",
        "TIG",
        "LPGD",
        "OOO",
        "FRI",
        "BRL",
        "VCF",
        "AXE",
        "VIA",
        "VHT",
        "88E",
        "EGR",
        "DRUG",
        "ZER",
        "TBR",
        "EVS",
        "LRK",
        "AGE",
        "NVA",
        "HNDQ",
        "ABY",
        "IXR",
        "BKT",
        "VML",
        "RWL",
        "CCR",
        "NXS",
        "ARL",
        "RDG",
        "AVJ",
        "IMA",
        "RCT",
        "QRE",
        "ART",
        "IHOO",
        "GGUS",
        "CVL",
        "4DX",
        "AVH",
        "WGN",
        "ADN",
        "WDMF",
        "ATC",
        "REX",
        "RTR",
        "RBTZ",
        "FOOD",
        "ATEC",
        "A1M",
        "MFB",
        "CCV",
        "MVP",
        "FBR",
        "EEG",
        "GTK",
        "SSG",
        "BYE",
        "AEE",
        "ORR",
        "TGF",
        "LPD",
        "DSE",
        "MHG",
        "GOW",
        "TNT",
        "LFSPA",
        "FOR",
        "FWD",
        "NCZ",
        "ACF",
        "ERD",
        "EOL",
        "JAN",
        "DNK",
        "EMV",
        "OZR",
        "EXR",
        "WAT",
        "MIH",
        "NOL",
        "FHE",
        "CII",
        "USD",
        "CYL",
        "EUR",
        "PPK",
        "JRL",
        "LMG",
        "ESGI",
        "WR1",
        "CLG",
        "ANO",
        "POS",
        "CLNE",
        "TMH",
        "KGL",
        "3DP",
        "BKY",
        "AMI",
        "CRD",
        "IKE",
        "X64",
        "MGV",
        "OBM",
        "CAA",
        "SPY",
        "DUR",
        "M7T",
        "CAE",
        "TTM",
        "FLN",
        "MSTR",
        "FSA",
        "EL8",
        "EGN",
        "QGL",
        "DSK",
        "IPX",
        "REIT",
        "MOV",
        "ARA",
        "AHX",
        "BWX",
        "EP1",
        "HPG",
        "QIP",
        "UMAX",
        "SHA",
        "A2B",
        "DTZ",
        "EGH",
        "EPY",
        "OZF",
        "G6M",
        "AVL",
        "TNG",
        "ETPMAG",
        "AND",
        "VVA",
        "BOC",
        "GLB",
        "RCE",
        "ISO",
        "SND",
        "RXM",
        "EBND",
        "CYC",
        "ESS",
        "NRZ",
        "EBR",
        "PYG",
        "IR1",
        "SEC",
        "RFG",
        "TOT",
        "G1A",
        "NZK",
        "SLA",
        "MDX",
        "IIGF",
        "CAM",
        "MCA",
        "NET",
        "FLC",
        "MME",
        "KIL",
        "AUT",
        "PTX",
        "BBL",
        "CYG",
        "HCH",
        "VMT",
        "XRF",
        "SZL",
        "HZR",
        "LCY",
        "CNEW",
        "DRA",
        "DRX",
        "SOM",
        "IRD",
        "MSL",
        "EWC",
        "PIQ",
        "EMH",
        "DUB",
        "AHL",
        "TSK",
        "1MC",
        "URFPA",
        "MDR",
        "PGL",
        "LEG",
        "BLU",
        "BCN",
        "CLX",
        "ACB",
        "TOP",
        "GRNV",
        "MCP",
        "DEV",
        "AMN",
        "GSS",
        "URF",
        "EMMG",
        "SDI",
        "PAXX",
        "HAV",
        "NSC",
        "ASH",
        "BIS",
        "FDEM",
        "MXI",
        "PEX",
        "NXG",
        "CSS",
        "NAM",
        "ZNC",
        "RYD",
        "WIN",
        "AUC",
        "WKT",
        "CD3",
        "GLL",
        "LBL",
        "WZR",
        "MAM",
        "BRB",
        "OCC",
        "ACQ",
        "ADO",
        "DRO",
        "EAI",
        "ORN",
        "SNC",
        "EOF",
        "SPQ",
        "TEK",
        "JYC",
        "PRL",
        "SRX",
        "GDA",
        "SNAS",
        "GRX",
        "BNO",
        "KOV",
        "GDC",
        "COS",
        "SPZ",
        "ARR",
        "EOS",
        "TWD",
        "IHHY",
        "CVV",
        "HHR",
        "SMI",
        "NOV",
        "FCT",
        "INIF",
        "NTD",
        "LM8",
        "MSV",
        "FSG",
        "EVO",
        "NZO",
        "PEK",
        "CY5",
        "CRR",
        "VRX",
        "INF",
        "STG",
        "DME",
        "CXM",
        "GTN",
        "HIO",
        "BBT",
        "RND",
        "ZYUS",
        "BC8",
        "EMN",
        "SEMI",
        "TYX",
        "RGB",
        "IKO",
        "PH2",
        "PLY",
        "GCY",
        "HIT",
        "KIN",
        "BSX",
        "AZY",
        "HJPN",
        "CAN",
        "TPD",
        "CE1",
        "AZS",
        "FAR",
        "TUL",
        "CUP",
        "ICI",
        "DVDY",
        "MCM",
        "VLS",
        "MBH",
        "TSI",
        "TRY",
        "GAP",
        "VEE",
        "CBR",
        "MWY",
        "MMI",
        "TVL",
        "GAS",
        "AIM",
        "ASO",
        "LOM",
        "SPT",
        "SGH",
        "HLTH",
        "SEQ",
        "FMS",
        "PLT",
        "AQC",
        "STM",
        "ATR",
        "MEK",
        "PVE",
        "SES",
        "IIND",
        "FGR",
        "MI6",
        "ONE",
        "SHM",
        "TMT",
        "MLG",
        "WMC",
        "MKR",
        "PTG",
        "ANP",
        "IESG",
        "CYM",
        "ISLM",
        "MCL",
        "BDM",
        "IVR",
        "OEL",
        "BOT",
        "DNA",
        "ESTX",
        "INES",
        "KLL",
        "VEN",
        "ESPO",
        "GEN",
        "TGN",
        "IVX",
        "NML",
        "EIQ",
        "SMLL",
        "KKO",
        "LSX",
        "LVH",
        "SB2",
        "ZYAU",
        "OIL",
        "NTI",
        "SOP",
        "RKN",
        "AVC",
        "STK",
        "SWTZ",
        "PTL",
        "TMK",
        "HNG",
        "ETM",
        "LIS",
        "EQR",
        "CHL",
        "ISU",
        "BNKS",
        "MX1",
        "SEG",
        "VEFI",
        "XF1",
        "MFD",
        "RMY",
        "MGT",
        "DBF",
        "GROW",
        "AVA",
        "WCG",
        "IRI",
        "NWC",
        "DGR",
        "TIP",
        "LEL",
        "RFX",
        "TOE",
        "AVD",
        "CTP",
        "NXM",
        "ENR",
        "BBC",
        "XTC",
        "VRC",
        "KAI",
        "LVT",
        "HMY",
        "CD2",
        "MNB",
        "VR1",
        "BOL",
        "LIT",
        "MEA",
        "BEAR",
        "ZEO",
        "SMN",
        "ECL",
        "WAA",
        "RINC",
        "RLT",
        "CLU",
        "MNRS",
        "FML",
        "PAM",
        "EGL",
        "WSP",
        "SWP",
        "BRK",
        "QFN",
        "BRU",
        "OPY",
        "MMM",
        "NCC",
        "FYI",
        "SOR",
        "YOJ",
        "MOGL",
        "AKG",
        "SSL",
        "IMR",
        "5GG",
        "ASP",
        "ADA",
        "USQ",
        "BNL",
        "BML",
        "TZN",
        "AUMF",
        "SVY",
        "HNR",
        "QXR",
        "PPG",
        "PRO",
        "WA1",
        "RMI",
        "AR1",
        "S2R",
        "APW",
        "IBC",
        "HMX",
        "SGQ",
        "AKL",
        "ESK",
        "XTE",
        "HGO",
        "DUG",
        "IIQ",
        "EMD",
        "SEN",
        "LGP",
        "SDV",
        "UBI",
        "ELT",
        "WRLD",
        "MRR",
        "SWF",
        "PFG",
        "BMT",
        "AE1",
        "GME",
        "IXU",
        "SPN",
        "MAP",
        "EM2",
        "CZR",
        "OSL",
        "CLDD",
        "CVCG",
        "NC1",
        "TI1",
        "MEC",
        "EFE",
        "CPN",
        "RFT",
        "DZZF",
        "CURE",
        "CYP",
        "GW1",
        "ERM",
        "ATS",
        "CPH",
        "MOZ",
        "MEU",
        "PSC",
        "ELS",
        "CRYP",
        "CAF",
        "TAM",
        "KME",
        "AHQ",
        "AJL",
        "CUE",
        "TGA",
        "BYI",
        "LKO",
        "FSI",
        "DXB",
        "RSM",
        "IAM",
        "MVS",
        "FME",
        "TGM",
        "EBG",
        "VBS",
        "VAN",
        "IXC",
        "92E",
        "HRZ",
        "CHZ",
        "GBE",
        "WOA",
        "MRL",
        "STP",
        "SFG",
        "HEUR",
        "FAL",
        "AYA",
        "PNN",
        "RZI",
        "ARN",
        "KRM",
        "KSS",
        "BWF",
        "HTG",
        "FTZ",
        "CDX",
        "SNS",
        "LME",
        "PPL",
        "VMS",
        "INV",
        "PXS",
        "GBR",
        "ARV",
        "AKM",
        "NOU",
        "JGH",
        "CSX",
        "TTT",
        "AMX",
        "DTR",
        "BNR",
        "NOX",
        "MRC",
        "SPD",
        "EPM",
        "CPV",
        "KYP",
        "HRN",
        "AME",
        "EV1",
        "BLG",
        "CMP",
        "MPX",
        "DKM",
        "XAM",
        "LEX",
        "COD",
        "AAR",
        "JAL",
        "NAG",
        "PAB",
        "CIW",
        "DDB",
        "KSN",
        "BOND",
        "POD",
        "EYE",
        "PNC",
        "MPA",
        "LRT",
        "SRJ",
        "WRK",
        "EDC",
        "IHEB",
        "ST1",
        "KPO",
        "FFI",
        "RVR",
        "PCL",
        "WLD",
        "ASW",
        "E200",
        "PCK",
        "DTC",
        "TKM",
        "AGN",
        "MXC",
        "DGH",
        "VRS",
        "AV1",
        "IMPQ",
        "BBX",
        "EMKT",
        "WAK",
        "WWI",
        "NAC",
        "KAT",
        "DVR",
        "AIQ",
        "QSML",
        "SVG",
        "CDO",
        "MZZ",
        "TON",
        "AR3",
        "HQLT",
        "KZR",
        "LNR",
        "SPX",
        "ANL",
        "4DS",
        "PHO",
        "CAMG",
        "AZI",
        "HMD",
        "AML",
        "TSO",
        "CBE",
        "SXG",
        "CNR",
        "LSGE",
        "AR9",
        "RTG",
        "SUV",
        "UBN",
        "ALY",
        "CCZ",
        "AUST",
        "BNZ",
        "PV1",
        "RGL",
        "CAY",
        "LNAS",
        "QMIX",
        "MRD",
        "NUH",
        "CTE",
        "C6C",
        "EIGA",
        "JAY",
        "MYG",
        "RTE",
        "GGE",
        "ABX",
        "AUZ",
        "GTG",
        "GC1",
        "AMS",
        "RHT",
        "RSH",
        "AXI",
        "VYS",
        "AT1",
        "TOY",
        "REE",
        "TBA",
        "ROG",
        "DEM",
        "QHL",
        "AHF",
        "MPP",
        "WIA",
        "CD1",
        "RNO",
        "VR8",
        "CCE",
        "DRM",
        "CF1",
        "DCG",
        "KNM",
        "RPM",
        "GBZ",
        "TPC",
        "ASR",
        "AEV",
        "BDT",
        "CNW",
        "EDU",
        "K2F",
        "AHC",
        "EME",
        "NDIA",
        "IBX",
        "KNI",
        "8VI",
        "JAT",
        "ICOR",
        "TOU",
        "LLI",
        "GSN",
        "RXL",
        "OKR",
        "AFA",
        "AMO",
        "MAG",
        "AQN",
        "ECT",
        "IG6",
        "CST",
        "ATH",
        "PF1",
        "BKG",
        "VBC",
        "CHR",
        "FRE",
        "HAW",
        "ADS",
        "TCG",
        "RRR",
        "SMX",
        "MCE",
        "DCL",
        "GOVT",
        "IDA",
        "GCAP",
        "FPC",
        "RTH",
        "PET",
        "STN",
        "E2M",
        "LPM",
        "CCG",
        "BEM",
        "BSA",
        "FOD",
        "VN8",
        "PBL",
        "HAL",
        "AWV",
        "WTL",
        "IOU",
        "RAS",
        "DGGF",
        "GLE",
        "SRK",
        "BFC",
        "GSR",
        "NGE",
        "SSO",
        "AXP",
        "MYE",
        "YBR",
        "VAL",
        "MVOL",
        "GFL",
        "AGD",
        "GPR",
        "FRX",
        "1AE",
        "CCA",
        "MGL",
        "REY",
        "TLM",
        "SHP",
        "WNX",
        "MKAX",
        "MM8",
        "NGY",
        "AUQ",
        "TAR",
        "PNM",
        "AON",
        "VMC",
        "APC",
        "NWSLV",
        "SKF",
        "CHM",
        "PGO",
        "KAU",
        "BIT",
        "ADX",
        "WHFPB",
        "ITM",
        "QEM",
        "PIL",
        "CG1",
        "ALO",
        "MLM",
        "PAA",
        "AGR",
        "GRV",
        "GOAT",
        "PPY",
        "KFM",
        "EINC",
        "INCM",
        "SCN",
        "AGH",
        "SOV",
        "MOQ",
        "MOZG",
        "ECS",
        "MIL",
        "MIO",
        "AQI",
        "ICS",
        "COY",
        "CDT",
        "SKS",
        "RNE",
        "IDT",
        "SIO",
        "OEC",
        "MAAT",
        "MAN",
        "TFL",
        "MEL",
        "EVZ",
        "TMS",
        "OD6",
        "AS2",
        "LCT",
        "NYR",
        "GTR",
        "OMA",
        "XPN",
        "8CO",
        "TYM",
        "MMA",
        "KRR",
        "KTG",
        "WLS",
        "DCC",
        "EMB",
        "BCT",
        "ANX",
        "AOU",
        "TEG",
        "HCF",
        "RWD",
        "8IH",
        "MEI",
        "OLI",
        "BGT",
        "MCCL",
        "CGA",
        "QML",
        "KNO",
        "OSX",
        "BUD",
        "ELE",
        "CGN",
        "PRX",
        "OCN",
        "TCF",
        "TIA",
        "XRG",
        "FFG",
        "BPH",
        "KTA",
        "CSE",
        "ENA",
        "IHR",
        "FFT",
        "ATX",
        "LBT",
        "S66",
        "GWR",
        "VTG",
        "WHK",
        "URNM",
        "MKG",
        "EQX",
        "CM8",
        "FND",
        "HSC",
        "PG1",
        "JCS",
        "IYLD",
        "PNX",
        "NCCGA",
        "SNG",
        "CTO",
        "BID",
        "ACR",
        "RAD",
        "LCL",
        "ZEU",
        "BUX",
        "EVR",
        "BCC",
        "WSI",
        "PFT",
        "HMG",
        "TGH",
        "MGU",
        "ADR",
        "HGL",
        "SRN",
        "CNQ",
        "FSIGA",
        "IMB",
        "IMI",
        "ODY",
        "SKY",
        "WEMG",
        "IME",
        "CDD",
        "MDC",
        "VPR",
        "DOU",
        "14D",
        "FPP",
        "99L",
        "ECP",
        "LSA",
        "ARD",
        "AVE",
        "ZNO",
        "FHS",
        "CUF",
        "TSL",
        "TZL",
        "ASQ",
        "WC8",
        "RDM",
        "MAT",
        "DEL",
        "E33",
        "GTI",
        "MQR",
        "CETF",
        "CLA",
        "PGD",
        "PWN",
        "OPN",
        "AC8",
        "MVL",
        "N1H",
        "FLX",
        "IMC",
        "IKW",
        "VMIN",
        "IBG",
        "TPO",
        "IPT",
        "BMH",
        "SBW",
        "COO",
        "AW1",
        "WRM",
        "HPC",
        "ATV",
        "YRL",
        "VIG",
        "NHE",
        "3DA",
        "ODM",
        "CLB",
        "TSN",
        "SYN",
        "HGV",
        "QFE",
        "ALA",
        "RNT",
        "SGA",
        "ACU",
        "NIM",
        "DBBF",
        "BTN",
        "HLF",
        "AYI",
        "ORM",
        "EGY",
        "NACGA",
        "EDE",
        "ESR",
        "GLH",
        "AAU",
        "KZA",
        "AHI",
        "TMZ",
        "WC1",
        "CAD",
        "SCU",
        "BMR",
        "ABV",
        "DM1",
        "ATP",
        "AJQ",
        "EEL",
        "DOC",
        "LCE",
        "NCL",
        "KGD",
        "DUN",
        "BGD",
        "RFA",
        "AU1",
        "TCO",
        "TDO",
        "MEM",
        "LIO",
        "TNY",
        "SIH",
        "2BE",
        "SHN",
        "NSX",
        "SLS",
        "H2G",
        "1VG",
        "HYD",
        "SCL",
        "HPR",
        "GMN",
        "1AD",
        "BPP",
        "RDN",
        "ARO",
        "RIE",
        "RCL",
        "SNX",
        "AJJ",
        "TRU",
        "HVM",
        "EMT",
        "RIM",
        "NWM",
        "RCW",
        "LBY",
        "BOD",
        "HOR",
        "ODA",
        "ADD",
        "KBC",
        "RLF",
        "AUH",
        "SHO",
        "GML",
        "C7A",
        "TMR",
        "WCN",
        "ADEF",
        "ZGL",
        "LYN",
        "AL3",
        "AQLT",
        "AQD",
        "CGO",
        "ICG",
        "LRL",
        "MCT",
        "BXN",
        "AII",
        "AUDS",
        "PEC",
        "HLX",
        "HFY",
        "MXR",
        "EX1",
        "CAV",
        "ERW",
        "TEM",
        "EM1",
        "Z2U",
        "X2M",
        "RFR",
        "LLO",
        "KOB",
        "AM7",
        "JNO",
        "CAG",
        "OAR",
        "RVS",
        "MTH",
        "HIL",
        "POU",
        "INL",
        "SBR",
        "TRP",
        "CNJ",
        "EQE",
        "B4P",
        "PVW",
        "FTC",
        "BTR",
        "NAE",
        "MR1",
        "KOR",
        "WEC",
        "ETPMPM",
        "MRZ",
        "ARE",
        "LER",
        "OLH",
        "BMM",
        "INP",
        "NSM",
        "S3N",
        "SRZ",
        "AMT",
        "WML",
        "BIO",
        "C29",
        "GPEQ",
        "SGI",
        "FZR",
        "BTC",
        "PTR",
        "MHK",
        "RGS",
        "AFL",
        "CLE",
        "T92",
        "NMR",
        "KWR",
        "AAJ",
        "AKO",
        "GGOV",
        "ABE",
        "MOB",
        "PUR",
        "DRIV",
        "IND",
        "CWX",
        "PGM",
        "WNR",
        "FIN",
        "BAT",
        "CI1",
        "ACS",
        "JXT",
        "GUL",
        "PVS",
        "1ST",
        "DHOF",
        "TTI",
        "GED",
        "CAQ",
        "BCA",
        "GIB",
        "DLM",
        "NNL",
        "G50",
        "FTL",
        "AKN",
        "BRX",
        "GMR",
        "MAUCA",
        "AD1",
        "SHH",
        "CAZ",
        "GTE",
        "ECPGA",
        "ALM",
        "IS3",
        "DMC",
        "WWG",
        "MRG",
        "TRT",
        "CPM",
        "MHC",
        "ARC",
        "GRL",
        "NSB",
        "CHK",
        "NC6",
        "LV1",
        "CUS",
        "UCM",
        "NGS",
        "CMD",
        "ZLD",
        "ZAG",
        "ADY",
        "TOR",
        "HRE",
        "PGY",
        "CZN",
        "AJX",
        "IRX",
        "LDX",
        "YANK",
        "PO3",
        "ICE",
        "TEE",
        "EXL",
        "WEL",
        "DTM",
        "BEZ",
        "BIR",
        "AUN",
        "BEX",
        "GFLGA",
        "THR",
        "BAS",
        "DCX",
        "A8G",
        "KSM",
        "OXT",
        "FRS",
        "RLG",
        "AEI",
        "CR9",
        "SHG",
        "A1G",
        "CZL",
        "KLO",
        "MM1",
        "HJZP",
        "LPE",
        "VNGS",
        "CLH",
        "LNU",
        "KAM",
        "ODE",
        "EEU",
        "SHE",
        "NUC",
        "FXG",
        "LSR",
        "RML",
        "AUR",
        "BDX",
        "PSL",
        "REZ",
        "JAV",
        "NME",
        "AER",
        "MXO",
        "SIV",
        "LRV",
        "HXG",
        "ECG",
        "SRI",
        "KP2",
        "YTMORG",
        "SGC",
        "AMD",
        "MRI",
        "GLA",
        "TMG",
        "POL",
        "CBL",
        "NPM",
        "SRY",
        "FDR",
        "SI6",
        "YOW",
        "BVR",
        "FNX",
        "CXZ",
        "OAU",
        "DW8",
        "CLZ",
        "HCD",
        "AHK",
        "GCR",
        "MRQ",
        "RR1",
        "BEE",
        "ICN",
        "NIS",
        "CMX",
        "VMM",
        "OLL",
        "1CG",
        "ALV",
        "LRD",
        "ATU",
        "R3D",
        "LAW",
        "BUR",
        "BUY",
        "NKL",
        "ILA",
        "VKA",
        "KAL",
        "TSC",
        "BSN",
        "MSG",
        "E79",
        "SLZ",
        "BTE",
        "MBK",
        "AX8",
        "SPA",
        "MDI",
        "EPN",
        "CUL",
        "YTMIP1",
        "RCR",
        "PFE",
        "SW1",
        "CXX",
        "1AG",
        "ID8",
        "WFL",
        "AAP",
        "TMB",
        "ACP",
        "NOR",
        "RAG",
        "MEG",
        "AIV",
        "USTB",
        "HCT",
        "IPC",
        "AVW",
        "9SP",
        "DDT",
        "GCX",
        "TAS",
        "AYM",
        "PVL",
        "ICL",
        "BOA",
        "OOK",
        "ERL",
        "BDG",
        "S3GO",
        "PXX",
        "CTQ",
        "ZMI",
        "SIX",
        "AYT",
        "OSM",
        "OCT",
        "FG1",
        "BYH",
        "M2R",
        "CR1",
        "VMG",
        "NCR",
        "DXN",
        "GNM",
        "SSH",
        "MOM",
        "NNG",
        "TML",
        "PUA",
        "HPP",
        "DTI",
        "EMP",
        "LDR",
        "CPO",
        "ETPMPT",
        "A3D",
        "VOL",
        "FRM",
        "MPG",
        "DOR",
        "SCT",
        "RAN",
        "RMX",
        "REC",
        "BMG",
        "LYK",
        "EPX",
        "AHN",
        "KFE",
        "SKN",
        "YTMGP1",
        "DAF",
        "WBE",
        "MPR",
        "XST",
        "LGM",
        "VTI",
        "SLB",
        "CML",
        "NTM",
        "SFM",
        "CLT",
        "APG",
        "LHM",
        "HAR",
        "ERG",
        "GES",
        "NTL",
        "KLI",
        "SE1",
        "SAU",
        "MKL",
        "SP3",
        "RLC",
        "VSR",
        "AUA",
        "PR1",
        "BMO",
        "AN1",
        "CMG",
        "MGA",
        "AFW",
        "YTMQF4",
        "ENT",
        "VAR",
        "UUL",
        "CRM",
        "NFL",
        "RXH",
        "KNB",
        "GC1PA",
        "YTMDO2",
        "SYT",
        "AVM",
        "T3K",
        "CIO",
        "OLY",
        "PKO",
        "FFF",
        "M2M",
        "DVL",
        "YTMALD",
        "EQN",
        "HMI",
        "DEX",
        "ZMM",
        "FIJ",
        "BHD",
        "SIS",
        "BUS",
        "AWJ",
        "PYR",
        "IGN",
        "CGB",
        "YTMDX3",
        "TG1",
        "WGR",
        "SUH",
        "GSM",
        "TRM",
        "CBY",
        "CXU",
        "RNX",
        "GPS",
        "MTR",
        "TMX",
        "SUM",
        "BIM",
        "KCC",
        "EVE",
        "M24",
        "REM",
        "TTB",
        "POW",
        "YTMDX2",
        "ETPMPD",
        "BLZ",
        "AOA",
        "NRX",
        "MHI",
        "YTMDX1",
        "EMS",
        "HT8",
        "BPM",
        "IVT",
        "VTX",
        "HIQ",
        "CPT",
        "OZM",
        "BEL",
        "DBO",
        "G88",
        "MMC",
        "OVN",
        "W2V",
        "AMM",
        "MOH",
        "FAU",
        "AGC",
        "WYX",
        "ENX",
        "CRB",
        "TANN",
        "VIP",
        "IPAY",
        "TG6",
        "GLV",
        "CWL",
        "RON",
        "KNG",
        "ALT",
        "LML",
        "SER",
        "RBR",
        "GRE",
        "SRH",
        "IEQ",
        "GO2",
        "AQS",
        "RB6",
        "RDS",
        "M8S",
        "CT1",
        "CVR",
        "AQX",
        "WOO",
        "M3M",
        "RBX",
        "DMG",
        "ENV",
        "CL8",
        "NYM",
        "UVA",
        "WMG",
        "CBH",
        "EZZ",
        "DLT",
        "PHL",
        "TKL",
        "GGX",
        "LVE",
        "AL8",
        "DAL",
        "CRS",
        "AUE",
        "ADG",
        "R8R",
        "C1X",
        "IBAL",
        "HVY",
        "AUK",
        "YTMVC1",
        "IGRO",
        "CMO",
        "YTMAS2",
        "BGE",
        "ITEK",
        "FOS",
        "AESG",
        "DMM",
        "OMX",
        "OM1",
        "RC1",
        "FATP",
        "TD1",
        "YTMMQ1",
        "MTM",
        "IPB",
        "GLOB",
        "GFN",
        "YTMTL2",
        "MTB",
        "EMU",
        "APS",
        "PIM",
        "NZS",
        "ICR",
        "GAME",
        "NVU",
        "MEB",
        "ANR",
        "SAN",
        "MGG",
        "MMR",
        "JPR",
        "SIT",
        "AO1",
        "T3D",
        "IEC",
        "SLM",
        "CDR",
        "ALB",
        "KEY",
        "WSR",
        "PRS",
        "GIVE",
        "OEQ",
        "ROC",
        "ROYL",
        "BME",
        "OKJ",
        "AJY",
        "HXL",
        "FGL",
        "CSF",
        "MSI",
        "OZZ",
        "CYQ",
        "PRM",
        "DC2",
        "OAK",
        "IEAT",
        "YTMF15",
        "ROO",
        "LKY",
        "SMS",
        "MTAV",
        "PKD",
        "CFO",
        "MBX",
        "OPL",
        "RPG",
        "OXX",
        "TTA",
        "XCO2",
        "JTL",
        "QMAX",
        "USHY",
        "KLR",
        "EAX",
        "3MF",
        "EQS",
        "HHI",
        "NES",
        "XMET",
        "IDEA",
        "EDOC",
        "GMTL",
        "YPB",
        "MCX",
        "IVO",
        "PLG",
        "ATM",
        "JREG",
        "YTMMG2",
        "JEPI",
        "CTV",
        "YTMSG3",
        "YTMAP1",
        "QUE",
        "IBUY",
        "JZRO",
        "FUTR",
        "LAM",
        "AIB",
        "YTMSCP",
        "HIQR",
        "MCGG",
        "YTMVCX",
        "CINPA",
        "ASAO",
        "SSLPA",
        "EMUCA",
        "WHFPA",
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
selected_page = st.sidebar.selectbox("Select a page", list(page_names_to_funcs.keys()))
page_names_to_funcs[selected_page]()
