# SIT720 Housing Price Prediction

This project predicts housing sale prices in Manly, Bankstown and Parramatta using machine learning.

## Project Files

- `housing data.csv` - collected housing dataset
- `housing_project.ipynb` - data cleaning, analysis and model development
- `app.py` - Streamlit web application
- `housing_model.pkl` - trained Random Forest model
- `model_columns.pkl` - model feature columns

## Models Used

The project compares:
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

Random Forest gave the best cross-validation performance.

## Run the Streamlit App

Install the required packages:

```bash
pip install streamlit pandas scikit-learn joblib