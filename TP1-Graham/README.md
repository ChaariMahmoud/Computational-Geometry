# TP1 - Convex Hull using Graham's Scan Algorithm

## Overview

The **Graham Scan** is a well-known algorithm for finding the **convex hull** of a set of points in a 2D plane. The convex hull is the smallest polygon that encloses all the points, and it is a fundamental problem in computational geometry.

### Steps of Graham's Scan Algorithm:

1. **Find the lowest point (Pb)**: Identify the point with the smallest y-coordinate. If multiple points share the same y-coordinate, choose the one with the smallest x-coordinate.
  
2. **Sort points by polar angle**: Sort the remaining points based on the angle they form with Pb. In case of a tie, place the point farther from Pb first.

3. **Traverse and construct the convex hull**: Begin with Pb and the point with the smallest angle. As you traverse through the sorted points:
   - If moving from the two most recently considered points to the next point makes a "right turn", remove the previous point (it cannot be part of the convex hull).
   - Continue this process until all points are processed, leaving the points that form the convex hull.

The algorithm's time complexity is **O(n log n)** due to the sorting step.

## Example of Convex Hull

Below is an example of the convex hull generated for a set of points.

![Graham](https://github.com/user-attachments/assets/fb786fd6-1021-44de-86cd-5094f76ccb57))


## Project Content

This project implements the Graham Scan algorithm to calculate and display the convex hull for a user-defined set of points. Users input the number of points and their coordinates, and the program visualizes the points along with the convex hull.

## Technologies Used

- **Python** for the core implementation.

- **`math`** module for geometric calculations.
- **`matplotlib`** for visualizing the points and convex hull.


