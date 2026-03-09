# Supply Chain Network Optimization using Geospatial Analytics

![Project Map](maps/supply_chain_network_optimization_map.png)

## Project Overview

Efficient supply chain network design is critical for companies distributing goods across large geographic regions. Poor warehouse placement can significantly increase transportation costs, delivery times, and operational inefficiencies.

This project demonstrates how **Geographic Information Systems (GIS) and Python optimization models** can be combined to determine the **optimal locations for distribution centers** that minimize delivery distance while serving population demand.

The analysis integrates **ArcGIS Pro spatial analysis with Python-based facility location optimization** to simulate real-world logistics decision making.

---

## Skills Demonstrated

- Geospatial Data Analysis
- Supply Chain Network Optimization
- Facility Location Modeling
- GIS Spatial Analysis
- Python Optimization Modeling
- Scenario Analysis
- Logistics Network Design

---

## Business Problem

Organizations must determine where to locate warehouses to efficiently serve customers across a geographic region.

The objective of this project is to:

- Minimize delivery distance between warehouses and demand locations
- Serve population demand efficiently
- Identify optimal warehouse locations for logistics networks

This problem is modeled as a **facility location optimization problem**.

---

## Technologies Used

- ArcGIS Pro
- Python
- PuLP (Optimization Modeling)
- Pandas
- NumPy
- Excel
- GIS Spatial Analysis

---

## Data Sources

### County Boundaries
US Census Bureau – TIGER/Line Shapefiles

Used to define geographic service regions across California.

### Population Data
US Census Bureau County Population Estimates

Used as a proxy for demand distribution.

### Candidate Warehouse Locations
Major California cities were selected as potential distribution centers.

Examples include:

- Los Angeles
- San Diego
- Stockton
- Sacramento
- Riverside
- Fresno
- San Jose

---

## Project Workflow

The project follows a geospatial analytics pipeline:

1. Data collection from US Census Bureau
2. GIS preprocessing in ArcGIS Pro
3. County centroid generation
4. Distance matrix creation
5. Optimization modeling using Python (PuLP)
6. Scenario comparison
7. GIS visualization of optimal logistics network

---

## Methodology

### 1. GIS Data Preparation

Using ArcGIS Pro:

- Imported California county boundaries
- Generated **county centroids**
- Joined population data to counties
- Created candidate warehouse point locations

---

### 2. Distance Matrix Generation

Distances were calculated between:


County Centroids → Candidate Warehouse Cities


This created a **distance matrix** representing the distance between each county and potential warehouse.

This matrix was used as input for the optimization model.

---

### 3. Optimization Model

A **facility location optimization model** was implemented in Python using PuLP.

**Objective**

Minimize population-weighted delivery distance.

**Decision Variables**

- Which warehouses should be opened
- Which warehouse serves each county

**Constraints**

- Each county must be assigned to exactly one warehouse
- Only a limited number of warehouses can be opened
- Counties can only be served by opened warehouses

---

### 4. Scenario Analysis

Multiple scenarios were evaluated to compare network efficiency.

| Scenario | Warehouses |
|--------|-------------|
| Scenario 1 | 2 Warehouses |
| Scenario 2 | 3 Warehouses |
| Scenario 3 | 4 Warehouses |

This allows comparison of logistics trade-offs between infrastructure investment and delivery efficiency.

---

## Results

The **3-warehouse scenario** provided the best balance between logistics efficiency and infrastructure expansion.

Optimal warehouse locations:

- Los Angeles
- Stockton
- Riverside

These locations minimize the population-weighted delivery distance across California counties.

---

## Final Logistics Network Map

The optimized logistics network was visualized using ArcGIS Pro.

The map includes:

- California counties
- Population demand distribution
- Optimal warehouse locations
- Service regions assigned to each warehouse

![Supply Chain Network Map](maps/supply_chain_network__optimization_map.png)

---

## Repository Structure


supply-chain-network-optimization

data/
Raw datasets used in the project

scripts/
Python optimization model

outputs/
Optimization results and scenario analysis

maps/
Final GIS visualization

docs/
Project documentation

README.md


---

## Project Documentation

Detailed methodology and analysis can be found in the project summary.

[Download Project Summary](docs/project_summary.pdf)

---

## Future Improvements

Possible enhancements include:

- Using road network travel times instead of straight-line distances
- Adding warehouse capacity constraints
- Incorporating transportation costs
- Integrating demand forecasting models
- Expanding to multi-state logistics networks

---

## Author

**Saurabh Malik**

Geospatial Analytics | Data Science | GIS | Supply Chain Analytics

**Saurabh Malik**

Geospatial Analytics | Data Science | GIS | Supply Chain Analytics
