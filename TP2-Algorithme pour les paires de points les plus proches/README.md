# TP2 - Convex Hull and Closest Pair of Points

## Overview

This project implements two fundamental algorithms in computational geometry:

1. **Convex Hull using Graham's Scan Algorithm**: Finds the smallest convex polygon (convex hull) enclosing a given set of points in a 2D plane.
   
2. **Closest Pair of Points Algorithm**: Determines the two closest points among a given set of points based on Euclidean distance.

The program also includes a visualization of the results, showing both the convex hull and the closest pair of points using **matplotlib**.

---

## Features

- **Graham's Scan Algorithm**:
  - Computes the convex hull of a set of 2D points.
  - Efficient with a time complexity of **O(n log n)** due to the sorting step.
  
- **Closest Pair of Points Algorithm**:
  - Utilizes a divide-and-conquer approach.
  - Efficient with a time complexity of **O(n log n)**.

- **Interactive Input**:
  - Users can enter custom points directly via the console.

- **Graphical Visualization**:
  - Displays all input points, highlights the convex hull, and marks the closest pair of points.

---

## Steps of Each Algorithm

### **1. Graham's Scan Algorithm**
- **Step 1**: Find the lowest point \( P_b \) (smallest y-coordinate, and in case of a tie, the smallest x-coordinate).
- **Step 2**: Sort points based on the polar angle relative to \( P_b \). If angles are equal, sort by distance from \( P_b \).
- **Step 3**: Use a stack to determine the convex hull:
  - Traverse the sorted points.
  - Add points to the stack unless they create a "right turn" with the last two points in the stack.

### **2. Closest Pair of Points Algorithm**
- **Step 1**: Sort points by x-coordinate (primary) and y-coordinate (secondary).
- **Step 2**: Divide the points into two halves and recursively find the closest pair in each half.
- **Step 3**: Merge results by checking the closest pair that spans the dividing line.

---

## Code Overview

The program consists of the following key components:

### **1. Main Functions**
- **`graham_scan(points)`**: Calculates the convex hull using Graham's scan.
- **`closest_pair(points)`**: Finds the closest pair of points using a divide-and-conquer approach.
- **`distance(p1, p2)`**: Computes the Euclidean distance between two points.
- **`plot_results(points, hull, closest_pair)`**: Visualizes the points, convex hull, and closest pair using matplotlib.

### **2. Input**
Users can input 2D points interactively. Enter "fin" to complete input.

### **3. Output**
- The convex hull as a list of points.
- The closest pair of points with their Euclidean distance.
- A graphical representation of the points, convex hull, and closest pair.

---


**Visualization**:
- All points are plotted.
- The convex hull is outlined.
- The closest pair of points is highlighted.

---

## Example of Convex Hull

Below is an example of the convex hull generated for a set of points.
![Screenshot from 2024-11-18 17-20-37](https://github.com/user-attachments/assets/cc107270-3320-4e3c-b3df-8211af3fcafb)


## Project Content

### Python Code:
- Core implementation of the algorithms.
- Interactive input handling.
- Graphical visualization with `matplotlib`.

### Modules Used:
- `math` for geometric calculations.
- `matplotlib` for plotting.

---

## How to Run the Project

1. **Install Python** (version 3.7 or higher).
2. **Install the required modules**:
```bash
pip install matplotlib
   ```
3. **Run the Python scrip**:
  ```bash
   python Algorithme.py
   ```
4. **Enter points as prompted** Visual results will display upon completion.

## Technologies Used

- **Python** for the core algorithmic implementation.
- **Matplotlib** for graphical visualization.
- **Divide-and-Conquer** strategy for the closest pair of points.
- **Sorting and Stack Manipulation** for Graham's Scan.

---

## Key Learning Outcomes

- Understanding and implementing geometric algorithms.
- Efficient sorting and recursion techniques.
- Visual representation of computational results.


