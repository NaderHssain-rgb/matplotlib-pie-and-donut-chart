# 🍩 Matplotlib Pie & Donut Chart

A beginner-friendly Python project for practicing **Pie Charts** and **Donut Charts** using **Matplotlib**.

The project visualizes fruit sales and demonstrates how to customize chart colors, percentages, shadows, slice positions, and donut-style charts.

---

## 📌 Project Overview

This project demonstrates how to create and customize a Pie Chart using Matplotlib.

The chart includes:

* 🍎 Fruit sales data
* 📊 Percentage labels
* 🎨 Custom colors
* 💥 Exploded slices
* 🌑 Shadow effect
* 🔄 Custom starting angle
* 🍩 Donut-style chart

---

## 🛠️ Technologies Used

* Python
* Matplotlib

---

## 📚 Concepts Practiced

### Pie Chart

The `plt.pie()` function is used to create a Pie Chart.

```python
plt.pie(sales, labels=fruits)
```

### Percentage Labels

The `autopct` parameter displays percentages inside the chart.

```python
autopct="%1.2f%%"
```

### Exploded Slice

The `explode` parameter separates a specific slice from the rest of the chart.

```python
explode = [0, 0, 0.1, 0]
```

In this project, the Orange slice is highlighted.

### Custom Colors

Each fruit has its own color:

```python
colors = ["red", "yellow", "orange", "purple"]
```

### Shadow

A shadow can be added using:

```python
shadow=True
```

### Starting Angle

The chart starts from 90 degrees:

```python
startangle=90
```

### Donut Chart

The chart is converted into a Donut Chart using:

```python
wedgeprops={"width": 0.5}
```

This creates an empty space in the center of the Pie Chart.

---

## 📊 Dataset

The project uses the following example data:

|  Fruit | Sales |
| :----: | ----: |
|  Apple |    25 |
| Banana | 29.55 |
| Orange |    15 |
| Grapes | 30.45 |

---

## 🖼️ Visual Preview

### Donut Chart

![Donut Chart Preview](donut_chart.png)

---

## 📂 Project Structure

```text
matplotlib-pie-and-donut-chart/
│
├── matplotlib_pie_and_donut_chart.py
├── donut_chart.png
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/matplotlib-pie-and-donut-chart.git
```

### 2. Open the project folder

```bash
cd matplotlib-pie-and-donut-chart
```

### 3. Install the required library

```bash
pip install -r requirements.txt
```

### 4. Run the Python file

```bash
python matplotlib_pie_and_donut_chart.py
```

---

## 📦 Requirements

The project requires:

```text
matplotlib
```

---

## 🎯 Learning Goals

This project helped me practice:

* Creating Pie Charts
* Creating Donut Charts
* Using `plt.pie()`
* Displaying percentages
* Using `explode`
* Customizing chart colors
* Adding shadows
* Changing the starting angle
* Using `wedgeprops`
* Improving chart presentation

---

## 👨‍💻 Author

**Nader**

This project is part of my Python and Data Visualization learning journey.

---

## ⭐ Future Improvements

Possible improvements:

* Add more fruits
* Use real-world sales data
* Add a legend
* Compare monthly sales
* Create multiple Donut Charts
* Load data from a CSV file
* Use Pandas for data analysis

---

## 📄 License

This project is created for educational and practice purposes.
