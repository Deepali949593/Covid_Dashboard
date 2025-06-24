
# 🦠 COVID-19 Data Dashboard

This is a live **COVID-19 data dashboard** built using:

- 📊 **Frontend/UI**: Streamlit (runs locally)
- ⚙️ **Backend**: Python (requests + data cleaning)
- 🗄️ **Database**: MongoDB (local or Atlas)
- 📈 **Visualization**: Plotly

The app fetches real-time COVID-19 data from a public API, stores it in MongoDB, and displays it through dynamic interactive visualizations.

---

## 🚀 Features

- Fetch & store data using [disease.sh API](https://disease.sh/)
- Save and update documents in MongoDB
- View country-level statistics
- Plot total cases, recoveries, and deaths
- Trend analysis with interactive graphs
- Dashboard runs fully offline after data storage

---

## 📸 Screenshots

### 🔹 Dashboard View

![Dashboard Screenshot](img/ss2.png)


### 🔹 Country Statistics Section

![Country Stats](img/ss1.png)



## 📁 Folder Structure

```

Covid\_Dashboard/
├── covid19\_project/
│   └── app/
│       └── covid\_dashboard.py      # Streamlit dashboard app
│
├── requirements.txt                # All Python dependencies
├── images/
│   ├── dashboard\_view\.png          # Dashboard screenshot
│   └── stats\_section.png           # Country stats screenshot
│
└── README.md                       # Project documentation

````

---

## ⚙️ How to Run Locally

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/Deepali949593/Covid_Dashboard.git
cd Covid_Dashboard
````

### 🔹 Step 2: Set Up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or source venv/bin/activate  # macOS/Linux
```

### 🔹 Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### 🔹 Step 4: Start the App

```bash
streamlit run covid19_project/app/covid_dashboard.py
```

> MongoDB must be running locally or configured with a valid Atlas URI.

---


## 📦 requirements.txt (sample)

```
streamlit
pandas
requests
pymongo
plotly
```

