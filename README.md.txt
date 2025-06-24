# 🦠 COVID-19 Data Dashboard

A real-time interactive COVID-19 dashboard built using **Streamlit**, **MongoDB**, and **disease.sh API**, with data analytics, visualizations, and live API integration.

---

## 🚀 Live App

👉 [Click here to view the app](https://coviddashboardgit-9tuegzwr6tuqgbgfxnvipx.streamlit.app)

---

## 📌 Project Features

- 🔄 Fetches live COVID-19 statistics from the [disease.sh](https://disease.sh/docs/) API  
- 📊 Interactive visualizations using **Plotly**  
- 📚 Stores country-level data in **MongoDB** for offline use and analytics  
- 🔍 Provides summary tables, charts, and trend analysis  
- 🧹 Cleans and preprocesses data before storing and displaying  
- ☁️ Deployed on **Streamlit Cloud**

---

## 🗂 Folder Structure

covid_dashboard/
├── covid19_project/
│ └── app/
│ └── covid_dashboard.py # Main Streamlit app
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠️ Tech Stack

| Component      | Tool |
|----------------|------|
| Frontend       | Streamlit |
| API Source     | [disease.sh](https://disease.sh/docs) |
| Database       | MongoDB (via pymongo) |
| Visualization  | Plotly |
| Backend Logic  | Python |
| Deployment     | Streamlit Cloud |

---

## 💾 MongoDB Collection Structure

Example document:
```json
{
  "country": "India",
  "cases": 45000000,
  "deaths": 530000,
  "recovered": 44000000,
  "updated": "2025-06-24T10:00:00Z"
}
