# 🧠 STIL File Analysis & Scan Architecture Dashboard

## 📌 Project Overview

This project focuses on analyzing semiconductor test data using a **STIL (Standard Test Interface Language)** file.
It automatically parses scan test information and presents it through an **interactive engineering dashboard**.

The system extracts key scan architecture details and visualizes them in a structured and user-friendly format.

---

## 🎯 Objectives

* Parse STIL file data
* Extract scan architecture metrics
* Generate structured summaries
* Visualize scan chains and architecture
* Build an interactive dashboard for engineers

---

## ⚙️ Features

### ✅ STIL Parsing

* Extracts:

  * Total Patterns
  * Test Type (EDT Scan)
  * Total Scan Chains
  * Scan Length per Chain
  * Total Scan Flip-Flops (FFs)
  * Series & Parallel Connections

---

### 📊 Dashboard Visualization

* Summary metrics (cards + table)
* Architecture overview
* Scan chain statistics
* Clean UI for engineering insights

---

### 🧩 Architecture Representation

* JTAG / TAP Controller flow
* EDT Compression Logic
* Scan Chains visualization
* Flip-Flop distribution

---

### 🔬 Advanced UI Features

* Scan chain table with signal mapping
* Fault simulation panel (UI-based)
* Heatmap visualization for fault distribution

---

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS, JavaScript
* **Parsing:** Regex-based STIL parser
* **Visualization:** Custom SVG & UI components

---

## 📂 Project Structure

```
project/
│── app.py
│── parser.py
│── templates/
│     └── index.html
│── sample.stil
│── README.md
```

---

## ▶️ How to Run Locally

1. Install dependencies:

```
pip install flask
```

2. Run the application:

```
python app.py
```

3. Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🌐 Live Demo

👉 https://claude.ai/public/artifacts/22bedd62-315c-4bf6-aacc-65e2d7306347

---

## 📊 Sample Output

* Total Patterns: **19**
* Scan Chains: **23**
* Scan Length: **234 FF per chain**
* Total Flip-Flops: **5382**

---

## 🚀 Key Highlights

* Efficient STIL parsing using lightweight logic
* Clean and modern dashboard UI
* Real-time data visualization
* Extendable for fault simulation and testing workflows

---

## 🔮 Future Enhancements

* Fault localization visualization
* ATPG pattern analysis
* Real-time tester log simulation
* Interactive scan chain graph (D3.js)

---

## 👩‍💻 Author

Jayashree H N
Computer Science & Design Student

---

## 📌 Note

This project is developed as part of a **Semiconductor AI / STIL File Analysis Assessment** to demonstrate parsing, visualization, and dashboard development skills.
