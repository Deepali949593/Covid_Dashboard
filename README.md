Certainly! Here's the **updated README** with markdown image embed **code included**, so you can easily insert your screenshots using either local images or hosted URLs:

---

```markdown
# COVID-19 Data Dashboard

An interactive COVID-19 dashboard built with Python using live API data and MongoDB for data storage and analytics.

---

## Features

- Fetches live COVID-19 data from disease.sh API
- Stores and processes data using MongoDB
- Visualizes data with Plotly
- Built with Streamlit for easy UI (runs locally)

---

## Technologies & Packages Used

- Python 3.x  
- Streamlit  
- pandas  
- requests  
- pymongo  
- plotly  

---

## Folder Structure

```

Grocery-Application/
├── covid19\_project/
│   └── app/
│       └── covid\_dashboard.py       # Main Streamlit app
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation

````

---

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/Deepali949593/Grocery-Application.git
   cd Grocery-Application
````

2. Create and activate virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   # or source venv/bin/activate  # macOS/Linux
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:

   ```bash
   streamlit run covid19_project/app/covid_dashboard.py
   ```

---

## Screenshots

### 🖼️ Dashboard View

```markdown
![Dashboard Screenshot](images/dashboard1.png)
```

### 📊 Country Statistics

```markdown
![Country Stats Screenshot](img/ss1.png)
```

> 📝 Place your images in the `images/` folder inside the project and make sure to commit them to GitHub.

---

## Author

**Deepali S.**
GitHub: [@Deepali949593](https://github.com/Deepali949593)

---

## License

MIT License

```

---

You can now just place your screenshots at:

```

Grocery-Application/
├── images/
│   ├── dashboard1.png
│   └── dashboard2.png

```
