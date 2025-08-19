# chart.py
# Contact: 23f3002034@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# Generate synthetic data
# -----------------------------
np.random.seed(42)

products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
quarters = ["Q1", "Q2", "Q3", "Q4"]

data = []
for product in products:
    base_sales = np.random.randint(80, 150)
    for quarter in quarters:
        sales = base_sales + np.random.randint(-20, 20)
        data.append({"Product": product, "Quarter": quarter, "Sales": sales})

df = pd.DataFrame(data)

# -----------------------------
# Visualization
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# Ensure 512x512 pixels:
# figsize in inches × dpi = final pixels
plt.figure(figsize=(8, 8), dpi=64)

ax = sns.barplot(
    data=df,
    x="Product",
    y="Sales",
    hue="Quarter",
    palette="muted",
    ci=None
)

ax.set_title("Quarterly Sales Performance by Product", fontsize=18, pad=15)
ax.set_xlabel("Product", fontsize=14)
ax.set_ylabel("Sales (in units)", fontsize=14)
ax.legend(title="Quarter", fontsize=12, title_fontsize=13)

# Force exact 512x512 output
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
