# Retail Sales Intelligence & Performance Analytics

## 1. Problem Statement
The objective of this project is to analyze the performance of a multi-branch retail network. Management needs actionable insights regarding branch profitability, product category performance, and customer loyalty behaviors to optimize inventory and marketing strategies.

## 2. Objectives
- Analyze sales performance across different branches and cities.
- Identify the most and least profitable product categories.
- Understand the purchasing behavior of different customer types (Member vs. Normal).
- Uncover seasonal or monthly sales trends.
- Evaluate the effectiveness of different payment methods.

## 3. Dataset Description
- **Type**: Self-generated synthetic dataset created specifically for this project.
- **Records**: 1,000 realistic retail transactions.
- **Fields**: Transaction_ID, Date, Branch, City, Customer_ID, Customer_Type, Gender, Age, Product, Category, Quantity, Unit_Price, Discount, Payment_Method, Customer_Rating, Cost, Sales, Profit.

## 4. Technologies & Libraries
- **Language**: Python
- **Libraries**: `pandas`, `numpy`, `streamlit`, `plotly`
- **Dashboard Framework**: Streamlit

## 5. Project Structure
```
Project_1/
├── project_1.py              # Main Streamlit dashboard application
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── Project_1_Report.docx     # Comprehensive business report
└── data/
    └── retail_sales_1.csv    # Synthetic dataset
```

## 6. Installation & Execution
1. Ensure Python 3.8+ is installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the dashboard:
   ```bash
   streamlit run project_1.py
   ```

## 7. Dashboard Instructions
- The dashboard is divided into three main tabs: Branch & Time Analysis, Product & Category Performance, and Customer & Payment Insights.
- Use the sidebar filters to drill down into specific Branches or Categories.
- The KPIs at the top will dynamically update based on your filter selections.

## 8. KPIs & Analytical Questions
**KPIs Monitored:** Total Sales, Total Profit, Total Transactions, Profit Margin.
**Questions Answered:**
- Which branch generates the highest sales and profit?
- How do Members compare to Normal customers?
- Which product categories drive the highest margins?

## 9. Key Findings
- **Branch A (New York)** is the dominant driver of overall sales and profitability.
- **Electronics and Clothing** categories generate the majority of profit, although Electronics operates on tighter margins.
- **Member customers** spend significantly more and maintain higher customer satisfaction ratings compared to Normal customers.

## 10. Business Recommendations
1. **Inventory Allocation:** Prioritize inventory replenishment for high-margin products in Branch A.
2. **Loyalty Program:** Launch campaigns targeted at converting 'Normal' customers to 'Members', given the higher average transaction value of members.
3. **Cross-Selling:** Strategically place high-margin items near high-volume, low-margin Groceries to boost overall transaction profitability.

## 11. Limitations & Conclusion
**Limitations**: The dataset is entirely synthetic. Real-world data would exhibit more noise, outliers, and potentially complex missing value patterns.
**Conclusion**: By transitioning from raw transaction logs to an interactive dashboard, management can quickly identify high-performing segments and address underperforming branches.
