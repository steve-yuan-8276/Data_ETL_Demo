# Tableau Prep Workflow for Association Rule Mining

## **Overview**
This Tableau Prep workflow is designed to clean and preprocess order transaction data from multiple regions (**South, East, West, Central**) before applying **association rule mining**. The goal is to transform the data into a structured format suitable for **Apriori algorithm-based market basket analysis**. The workflow includes **data cleaning**, **standardization**, **merging**, and **association rule extraction**.

---

## **Workflow Breakdown**

### **1. Preprocessing Stage (Data Cleaning & Transformation)**
Before performing association rule mining, we need to ensure data consistency and integrity. This is handled in the Tableau Prep workflow as follows:

#### **Regional Data Preparation**
Each dataset undergoes different preprocessing steps:
- **`orders_south_...` → Remove Nulls**  
  - Eliminates rows with missing values to ensure data completeness.
  
- **`Orders_East` → Fix Data Type**  
  - Converts columns to the correct data types (e.g., ensuring `Order Date` is in datetime format and `Order ID` is a string).

- **`Orders (West)` → Rename States**  
  - Standardizes state names to ensure uniformity across datasets.

- **`Orders (Central)` → Fix Dates**  
  - Converts all date columns into a consistent format.

#### **Merging and Consolidation**
- The cleaned datasets are **merged** into a single dataset called **`All Orders`**, ensuring a uniform structure for downstream analysis.
- **Final Cleaning (`Clean 1`)** ensures that the consolidated dataset is ready for association rule mining.

---

## **2. Association Rule Mining**
Once the cleaned data is exported from Tableau Prep, it is processed using **association rule mining techniques** in Python (`mlxtend` library).

### **2.1 Data Preparation for Apriori Algorithm**
The dataset must be transformed into a **one-hot encoded format**, where each transaction is represented as a row, and each product category is represented as a column with binary values (`1` for purchased, `0` for not purchased).

Example format:
| Order ID | Art | Copiers | Bookcases | Fasteners | Labels | Binders | ... |
|----------|-----|---------|-----------|-----------|--------|---------|-----|
| 1001     | 1   | 0       | 0         | 0         | 1      | 0       | ... |
| 1002     | 0   | 1       | 0         | 0         | 0      | 1       | ... |
| 1003     | 1   | 0       | 1         | 0         | 0      | 1       | ... |

### **2.2 Applying the Apriori Algorithm**
The **Apriori algorithm** is used to identify frequent itemsets and generate association rules based on the dataset.

#### **Frequent Itemset Generation**
- **Minimum Support Threshold:** 0.10 (transactions containing an item at least 10% of the time)
- `apriori(DataFrame, min_support=0.10, use_colnames=True)`:  
  - Identifies frequently occurring sets of items.
  - Uses **support metric** to filter out infrequent items.

#### **Association Rule Generation**
- `association_rules(frequent_itemsets, metric="lift")`  
  - **Lift** measures how much more likely two items are purchased together compared to being purchased independently.
  - **Confidence** indicates the likelihood that an item appears given another item is in the basket.
  - **Support** represents the proportion of transactions containing a particular itemset.

Example of resulting association rules:

| Antecedents      | Consequents  | Support | Confidence | Lift  |
|-----------------|-------------|---------|------------|-------|
| Binders        | Labels      | 0.15    | 0.75       | 1.80  |
| Copiers        | Bookcases   | 0.12    | 0.65       | 2.10  |
| Accessories    | Envelopes   | 0.18    | 0.70       | 1.95  |

### **2.3 Interpretation of Association Rules**
- **Lift > 1** → The presence of `antecedent` increases the likelihood of `consequent` being purchased.
- **High Confidence (> 0.6)** → Strong probability that customers who buy `antecedent` also buy `consequent`.
- **High Support** → Common association found in transactions.

---

## **3. How to Use the Workflow**
1. **Run Tableau Prep**  
   - Load the regional datasets (`orders_south_...`, `Orders_East`, `Orders (West)`, `Orders (Central)`).
   - The workflow will clean, standardize, and merge them into **`All Orders`**.
   - Export the cleaned dataset (`Clean 1`).

2. **Run Python Script**  
   - Convert the cleaned dataset to a **one-hot encoded format**.
   - Apply the **Apriori algorithm** to extract frequent itemsets.
   - Generate **association rules** with `mlxtend`.

3. **Analyze the Rules**  
   - Use `lift`, `confidence`, and `support` to determine meaningful associations.
   - Apply insights for market basket analysis, product recommendations, or inventory planning.

---

## **Conclusion**
This workflow **prepares order data** in Tableau Prep and then applies **association rule mining** using the **Apriori algorithm** to uncover meaningful purchase patterns. By leveraging data preprocessing and machine learning techniques, this approach enhances business decision-making for product bundling, cross-selling, and customer behavior insights.
