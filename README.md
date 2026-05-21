---
title: "Creating Maps in Python with GeoPandas"
author: "Juan Carlos Rubio Polania, PhD"
date: "2024-03-04"
---

# Creating Maps in Python with GeoPandas 🗺️🐍🌍

## Overview

This workflow demonstrates how to create basic geographic maps in Python using `GeoPandas` and `Matplotlib`.

The script includes:
- Installation of mapping libraries
- Loading geographic datasets
- Creating thematic maps
- Adjusting geographic extents
- Adding labels and titles
- Including scale bars
- Adding north arrows

Although this example uses the Hawaiian Archipelago, the workflow can be adapted to many applications involving:
- GIS visualization
- Ecological studies
- Environmental sciences
- Spatial analysis
- Remote sensing
- Biodiversity mapping
- Scientific visualization

The workflow provides an introduction to cartographic visualization using Python.

---

# Required Libraries

```python
!pip install matplotlib geopandas
!pip install matplotlib-scalebar
```

---

# Workflow

## 1. Import Required Libraries

```python
import matplotlib.pyplot as plt
import geopandas as gpd
```

The script imports libraries used for:
- Scientific plotting
- Geographic visualization
- Spatial data analysis

---

## 2. Enable Inline Visualization

```python
%matplotlib inline
```

Figures are displayed directly inside the notebook environment.

---

## 3. Load Geographic Data

```python
NL = gpd.read_file(
    gpd.datasets.get_path(
        'naturalearth_lowres'
    )
)
```

Natural Earth geographic boundaries are loaded using GeoPandas.

The dataset contains:
- Country polygons
- Global geographic boundaries

---

## 4. Create a Basic Map

```python
fig, ax = plt.subplots(figsize=(4, 3))
```

A map is created using:
- GeoPandas
- Matplotlib

The workflow includes:
- Polygon visualization
- Geographic limits
- Axis labels
- Map titles

---

## 5. Adjust Geographic Extent

```python
ax.set_xlim([-160.7, -154])
ax.set_ylim([18.6, 23])
```

The map extent is adjusted to focus on the Hawaiian Archipelago.

---

## 6. Add Axis Labels and Title

```python
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
```

Longitude and latitude labels are added to the figure.

---

## 7. Add a Scale Bar

```python
from matplotlib_scalebar.scalebar import ScaleBar
```

The `matplotlib-scalebar` package is used to add a cartographic scale.

```python
scalebar = ScaleBar(
    50,
    units="km",
    location='upper right'
)
```

The scale bar displays map distance in kilometers.

---

## 8. Add a North Arrow

```python
ax.annotate('N', ...)
```

A north arrow is added using Matplotlib annotations.

The arrow improves:
- Orientation
- Cartographic interpretation
- Scientific presentation

---

# Applications

This workflow can be useful for:
- GIS projects
- Ecology
- Marine sciences
- Environmental studies
- Biodiversity analyses
- Spatial visualization
- Scientific publications
- Educational purposes

---

# Requirements

- Python 3.x
- matplotlib
- geopandas
- matplotlib-scalebar

Install packages with:

```bash
pip install matplotlib geopandas matplotlib-scalebar
```

---

# Notes

This workflow uses the `naturalearth_lowres` dataset included with GeoPandas.

The same workflow can be adapted to:
- Shapefiles
- GeoJSON files
- Spatial databases
- Remote sensing products

---

# License

This project is licensed under the MIT License.

---

# Author

Juan Carlos Rubio Polania, PhD
