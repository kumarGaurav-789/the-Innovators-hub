# 🇮🇳 SwasthyaNet — A Federated AI Nervous System for PHCs

**Track 03: Resilience** | **HackQuest: Code for Communities 2.0 (GDG Pantheon '26)**  
**Institution**: Amity University Jharkhand  
**Team: The Innovators Hub**  
- **Kumar Gaurav**  
- **Shanti Priya**  

---

## 🌟 The Vision: From One PHC to a National Digital Public Good

Across India's **1.6 Lakh+ Primary Health Centres (PHCs)**, the public health supply chain is flying blind. Essential medicines run out with zero early warning, solar refrigerators experience unmonitored cold-chain breaches, and neighboring districts cannot coordinate transfers without violating data sovereignty.

**SwasthyaNet** solves this with a privacy-preserving, federated AI architecture:
- 🏥 **1.6L+ PHCs Addressable Nationwide**: Resilient mesh architecture with no single point of failure.
- ⏱️ **2–3 Weeks Early Warning**: Time-series demand forecasting catches seasonal surges (monsoon snakebites, dengue, heatwaves).
- 🔒 **Zero Patient Data Leakage**: Federated Learning (FedAvg) + Differential Privacy ($\epsilon=1.15$) compliant with India's **DPDP Act 2023**.
- 🌐 **Model Context Protocol (MCP 2.x) Native**: Full MCP server wrapper allowing any AI agent (Claude Desktop, Cursor, Antigravity, or District Health Officer bots) to inspect telemetry, run forecasts, and execute rebalancing orders.
- 📦 **100% Digital Public Good (DPG) Ready**: Built on **ABDM** (Ayushman Bharat Digital Mission) Health Facility Registry and **HL7 FHIR R4** `SupplyDelivery` standards.

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.10+ (Python 3.12 recommended)
- Node.js (optional, only if using npm tooling)

### 2. Setup & Installation
```bash
# Clone or navigate to the repository
cd HQPantheon

# Create virtual environment (if not already created)
python -m venv .venv

# Activate virtual environment
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Launch the Mission Control Web Application
```bash
python -m uvicorn backend.server:app --host 0.0.0.0 --port 8000 --reload
```
Open your browser and navigate to:  
👉 **`http://localhost:8000`**

---

## 🤖 Connecting the MCP Server to Claude Desktop or Cursor

SwasthyaNet includes a full **Model Context Protocol (MCP)** server (`swasthyanet_mcp_server.py`) that can be used directly with Claude Desktop, Cursor, or any MCP client!

### Claude Desktop Configuration:
Add this entry to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "swasthyanet": {
      "command": "python",
      "args": [
        "c:/Users/SHANTI PRIYA/OneDrive/Desktop/HQPantheon/swasthyanet_mcp_server.py"
      ]
    }
  }
}
```

### Run MCP Server Directly in Terminal (stdio mode):
```bash
python swasthyanet_mcp_server.py
```

### Available MCP Tools:
| MCP Tool | Description |
|---|---|
| `swasthyanet_list_phcs` | Lists all monitored PHCs, coordinates, bed occupancy, and alert levels. |
| `swasthyanet_get_phc_details` | In-depth diagnostic telemetry for a facility (cold chain, stock, duty staff). |
| `swasthyanet_forecast_demand` | 21-day predictive stock-out risk forecast with seasonal surge multipliers. |
| `swasthyanet_optimize_redistribution` | Urgency-weighted graph solver calculating optimal inter-PHC supply transfers. |
| `swasthyanet_execute_transfer` | Approves and dispatches an inter-PHC transfer, updating live stock. |
| `swasthyanet_trigger_federated_round` | Simulates an edge Federated Learning aggregation round with DP noise ($\epsilon$). |
| `swasthyanet_export_abdm_fhir_bundle` | Exports ABDM / HL7 FHIR R4 `SupplyDelivery` transaction bundle. |
| `swasthyanet_generate_cmo_briefing` | Generates situational awareness report for the Chief Medical Officer. |
| `swasthyanet_simulate_crisis` | Injects sudden flood / snakebite crisis into Bundu PHC for live demos. |

---

## 🖥️ Live Demo Features in Web UI

1. **Interactive GIS Map**: Click on any PHC pin (Namkum, Kanke, Bundu, Torpa, Sisai, etc.) across Jharkhand to inspect live stock, bed occupancy, and solar vaccine fridge temperatures.
2. **"Simulate Monsoon Crisis" Button**: Injects a real-time resilience test (flash flood in Bundu + fridge alarm in Torpa). Watch the pins change color and the system automatically propose rebalancing routes!
3. **AI Supply Redistribution Hub**: Visualizes dynamic transfer corridors with Haversine distance, ETA, lives protected, and CO₂ savings. Click **Approve & Dispatch** to execute.
4. **Federated AI & Privacy Visualizer**: Watch real-time model convergence (accuracy climbing from 78% to 94%) and inspect the mathematical $(\epsilon=1.15, \delta=10^{-5})$ differential privacy bounds.
5. **Offline PWA Edge Logger**: Switch to "Offline Mode (No Internet)", log drug counts, and watch them automatically sync to SwasthyaNet Central Hub when network is restored.
6. **MCP Console & AI CMO Assistant**: Run any MCP tool interactively from the browser or chat with the autonomous Chief Medical Officer agent!
7. **ABDM & FHIR R4 Explorer**: Inspect raw, standard-compliant FHIR R4 JSON bundles.

---

## 📁 Repository Structure

```
HQPantheon/
├── backend/
│   ├── data_store.py              # Realistic Jharkhand PHC network & telemetry data store
│   ├── forecasting_engine.py      # 2-3 week predictive demand & stockout forecasting
│   ├── redistribution_optimizer.py# Haversine distance-weighted supply rebalancing solver
│   ├── federated_engine.py        # FedAvg simulation with DP-SGD differential privacy
│   ├── fhir_abdm.py               # ABDM & HL7 FHIR R4 transaction bundle generator
│   └── server.py                  # FastAPI REST, WebSockets, MCP bridge & static server
├── mcp_server/
│   ├── swasthyanet_mcp.py         # Official MCP Server (Tools, Resources, Prompts)
│   └── __init__.py
├── frontend/
│   ├── index.html                 # Modern glassmorphic mission control UI
│   └── js/
│       └── app.js                 # Leaflet mapping, Chart.js, and MCP agent logic
├── docs/
│   ├── HACKATHON_PITCH_SCRIPT.md  # 3-minute winning demo script for judges
│   └── ARCHITECTURE.md            # Deep technical architecture specification
├── swasthyanet_mcp_server.py      # Root executable MCP runner
├── requirements.txt               # Frozen dependencies
└── README.md                      # Project documentation
```

---

## 👥 Authors
**The Innovators Hub**  
- **Kumar Gaurav**  
- **Shanti Priya**  
Amity University Jharkhand • GDG Code for Communities 2.0
