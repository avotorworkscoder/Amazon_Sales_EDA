# Amazon_Sales_EDA
Exploratory Data Analysis of Amazon product sales data with cleaning, visualization, pricing strategy insights, and market behavior analysis using Python.

# 🛒 Amazon Sales Data Analysis & Visualization

A complete Exploratory Data Analysis (EDA) project on Amazon product listings to understand:

• Customer satisfaction  
• Pricing strategy  
• Discounts & competition  
• Category dominance  
• Market opportunities  

This project transforms raw messy marketplace data into business insights using Python and modern visualization techniques.

---

## 🎯 Project Objectives

The goal is to answer real business questions:

✔ Are customers generally satisfied with products?  
✔ Which categories drive most engagement?  
✔ Do discounts improve ratings or hide poor quality?  
✔ What price ranges dominate the market?  
✔ Which niches show opportunity for sellers?

---

## 🧰 Tech Stack

| Tool | Purpose |
|-------|---------|
Python | Core programming |
Pandas | Data cleaning & wrangling |
NumPy | Numerical computing |
Matplotlib / Seaborn | Statistical visualization |
Plotly | Interactive treemaps |
Scikit-learn | Label encoding |
WordCloud | Text analysis |

---

## 📂 Project Structure

Amazon-Sales-EDA/
│
├── data/
│ └── amazon.csv
│
├── notebooks/
│ └── eda.ipynb
│
├── src/
│ └── utils.py
│
├── outputs/
│ └── plots/
│
├── requirements.txt
├── README.md
└── LICENSE


---

## 🧹 Data Cleaning Steps

The dataset contained messy real-world marketplace problems:

• ₹ symbols & commas in prices  
• % symbols in discount columns  
• mixed datatypes  
• missing ratings  
• duplicate rows  
• inconsistent categories  

Cleaning performed:

• Converted prices → float  
• Converted discount → decimal  
• fixed rating errors  
• removed null values  
• simplified categories  
• label encoding for ML readiness  

---

## 📊 Visual Analysis Performed

### Customer Behaviour
• Rating distribution histogram  
• Popular categories (rating count proxy for sales)  
• Word clouds from reviews  

### Pricing Strategy
• Actual vs Discounted scatter plots  
• Discount aggression by category  
• Price vs rating trends  

### Advanced Analytics
• Correlation heatmaps (Pearson & Spearman)  
• Violin plots (rating consistency)  
• Treemaps (hierarchical market share)  
• Joint plots (density analysis)  
• Pareto chart (80/20 business rule)  

---

## 📈 Example Visualizations

![Pricing_vs_customer_rating](outputs/plots/Pricing_vs_customer_rating.png)

## 📊 Key Visualizations

| Rating Distribution | Pricing Strategy |
|--------------------|----------------|
| ![](outputs/plots/Amazon_products_rating_distribution.png) | ![](outputs/plots/Pricing_strategy.png) |

| Heatmap | Wordcloud |
|---------|-----------|
| ![](outputs/plots/Correlation_matrix.png) | ![](outputs/plots/Word_cloud.png) |



---

## 🔍 Key Insights

• Most products cluster between ⭐ 4.0–4.5  
• Electronics & accessories dominate engagement  
• Heavy discounts often correlate with lower ratings  
• A few categories drive 80% of total activity  
• Mid-range pricing has highest rating density  

---

## ▶️ How to Run

### 1. Clone repo

git clone https://github.com/avotorworkscoder/Amazon_Sales_EDA
cd Amazon_Sales_EDA

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run notebook

jupyter notebook notebooks/Amazon_Sales_EDA.ipynb


---

## 📦 requirements.txt

pandas
numpy
matplotlib
seaborn
plotly
scikit-learn
wordcloud


---

## 💡 Future Improvements

• Streamlit dashboard  
• Sales prediction model  
• Sentiment analysis on reviews  
• Category recommendation system  
• Deployment as web app  

---

## 👨‍💻 Author

Amit Parihar
Mechatronics | Robotics | AI/ML | Data Science  
Passionate about building intelligent systems & extracting insights from Phsical Machines.

---

## 📜 License

This project is licensed under the MIT License.  
Free to use, modify, and distribute with attribution.

---
