Sure! Below is a **complete `README.md`** file written as **one continuous document**, ideal for GitHub, and includes everything from project summary to deployment and Streamlit usage instructions.

---

```markdown
# 🦠 COVID-19 Data Dashboard with Streamlit + MongoDB + API

This project is an interactive, real-time **COVID-19 data dashboard** built using **Streamlit**, **MongoDB**, and the free public API from [disease.sh](https://disease.sh/). It demonstrates full-stack integration of live API data, data storage, analytics, and data visualization, and is fully deployable on [Streamlit Cloud](https://streamlit.io/cloud).

---

## 🔗 Live App

▶️ **[Click to open the dashboard](https://coviddashboardgit-9tuegzwr6tuqgbgfxnvipx.streamlit.app)**

---

## 📌 Features

- 🔄 Live COVID-19 data from [disease.sh API](https://disease.sh/docs/)
- 💾 Stores data in **MongoDB** for offline analysis
- 📈 Data visualizations using **Plotly**
- 📊 Tables, graphs, trend charts, and summaries
- 🧹 Preprocesses, filters, and cleans data before storing
- ☁️ **Deployable on Streamlit Cloud**

---

## 🛠️ Technologies Used

- **Frontend/UI**: Streamlit  
- **Data Source**: [disease.sh API](https://disease.sh)  
- **Database**: MongoDB using `pymongo`  
- **Data Analysis**: pandas  
- **Visualization**: Plotly  
- **Deployment**: Streamlit Cloud

---

## 📁 Folder Structure

```

Grocery-Application/
├── covid19\_project/
│   └── app/
│       └── covid\_dashboard.py     # Main Streamlit app
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation

````

---

## 💾 MongoDB Sample Document

```json
{
  "country": "India",
  "cases": 45000000,
  "deaths": 530000,
  "recovered": 44000000,
  "updated": "2025-06-24T10:00:00Z"
}
````

---

## ⚙️ Getting Started Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Deepali949593/Grocery-Application.git
cd Grocery-Application
```

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# or source venv/bin/activate (for macOS/Linux)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run covid19_project/app/covid_dashboard.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## ☁️ Deploy on Streamlit Cloud

To deploy this app publicly:

1. Push your project to GitHub: `https://github.com/Deepali949593/Grocery-Application`
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Fill out the form:

   * **Repository**: `Deepali949593/Grocery-Application`
   * **Branch**: `main`
   * **Main file path**: `covid19_project/app/covid_dashboard.py`
4. (Optional) Set any MongoDB secrets using Streamlit Cloud’s **Secrets Manager**
5. Click **Deploy**

---

## 📦 requirements.txt

Make sure this file exists in the root folder of your project:

```txt
streamlit
pandas
requests
pymongo
plotly
```

> Add any other libraries your app uses.

---

## 📸 Screenshots

> *(Upload your app screenshots to GitHub or another image host and link them here)*

![Dashboard](https://user-images.githubusercontent.com/yourusername/dashboard.png)
![Country Stats](https://user-images.githubusercontent.com/yourusername/chart.png)

---

## 👤 Author

**Deepali S.**
GitHub: [@Deepali949593](https://github.com/Deepali949593)

---

## 🪪 License

This project is licensed under the **MIT License**.

---

## ❤️ Acknowledgements

* COVID-19 data: [disease.sh API](https://disease.sh/)
* UI & deployment: [Streamlit](https://streamlit.io)
* Charting: [Plotly](https://plotly.com/python/)

---

```
