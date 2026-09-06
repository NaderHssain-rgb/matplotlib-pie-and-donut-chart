import matplotlib.pyplot as plt


# Data
fruits = ["Apple", "Banana", "Orange", "Grapes"]
sales = [25, 29.55, 15, 30.45]

# Highlight the Orange slice
explode = [0, 0, 0.1, 0]

# Custom colors for each fruit
colors = ["red", "yellow", "orange", "purple"]


# Create a Donut Chart
plt.figure(figsize=(8, 6))

plt.pie(
    sales,
    labels=fruits,
    autopct="%1.2f%%",
    explode=explode,
    wedgeprops={"width": 0.5},
    shadow=True,
    startangle=90,
    colors=colors
)

plt.title("Fruit Sales")
plt.tight_layout()
plt.show()