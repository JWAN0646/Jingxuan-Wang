# Soil Salinity Risk Prediction in the Western Australian Wheatbelt

This project applies **machine learning and spatial environmental data analysis** to predict soil salinity risk across the Western Australian Wheatbelt.

The project combines my background in **Environmental Engineering** with **Data Science**, focusing on how environmental and geospatial variables can be integrated into a machine-learning workflow for soil salinity assessment.

## Project Overview

Soil salinity is an important environmental and agricultural issue in Western Australia. This project investigates whether spatial environmental variables can be used to predict soil salinity risk using machine-learning models.

The workflow integrates multiple spatial datasets, performs geospatial preprocessing and feature extraction, and compares machine-learning approaches for salinity risk classification.

## Environmental & Spatial Features

The model incorporates several environmental variables associated with soil and landscape conditions:

* **Clay content**
* **Elevation**
* **Slope**
* **Rainfall**
* **Land cover**

Spatial datasets from different sources were processed and aligned into a consistent coordinate reference system and spatial framework before modelling.

## Workflow

**Spatial Data Collection → GIS Preprocessing → Feature Engineering → Dataset Integration → Machine Learning → Model Evaluation → Risk Prediction**

Key tasks included:

* Processing raster and vector geospatial datasets
* Coordinate reference system transformation and spatial alignment
* Extracting environmental features for salinity observations
* Cleaning and integrating data from multiple environmental sources
* Training and comparing machine-learning models
* Evaluating model performance
* Developing an interactive prediction interface

## Machine Learning

The project explored machine-learning approaches including:

* **Random Forest**
* **XGBoost**

After incorporating additional soil information such as **clay content**, the best-performing model achieved an accuracy of approximately **66%**.

The results suggest that combining soil properties with climatic, terrain and land-cover information can improve salinity-risk prediction compared with models using a more limited set of environmental variables.

## Technologies

* Python
* Pandas / NumPy
* GeoPandas
* Rasterio / Rioxarray
* Scikit-learn
* XGBoost
* GIS and raster processing
* Streamlit

## Interactive Application

A Streamlit interface was developed to demonstrate the prediction workflow and communicate model results in an accessible format.

## Repository Note

This repository is a **portfolio presentation of the project**. Selected implementation components are provided to demonstrate the methodology and technical approach.

The complete modelling, geospatial preprocessing pipeline, trained models and project data are maintained in a private repository.
