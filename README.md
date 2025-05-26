# TMDB Movie Revenue Prediction

This project leverages metadata from The Movie Database (TMDB) to build a machine learning model that predicts movie revenue. The workflow includes data preprocessing, feature engineering, regression modeling, and explainability analysis using SHAP.

## Features

- Merged and cleaned TMDB metadata and credits datasets
- Feature engineering including log transformations, genre encoding, and date parsing
- Revenue prediction using XGBoost and Random Forest regressors
- SHAP-based model interpretability to understand feature impact
- Evaluation using R², RMSE, and MAE metrics

## Technologies

- Python (pandas, numpy, scikit-learn, xgboost)
- SHAP for explainability
- Matplotlib and Seaborn for visualization

## Project Structure
├── data/ # Raw and processed data files

├── models/ # Saved models

├── notebooks/ # Jupyter notebooks for EDA and modeling

├── outputs/ # Saved plots, and results

├── utils/ # Helper functions and scripts (if any)

└── README.md

## Getting Started

1. Clone the repository: https://github.com/yourusername/tmdb-revenue-prediction.git
2. Install dependencies:
3. Run the notebooks in order:
- `01_data_preprocessing.ipynb`
- `02_modeling.ipynb`
- `03_explainability.ipynb`

## Results

The best-performing model achieved an R² score of 0.7249 and an Adjusted R² score of 0.7124. Key predictors of revenue included budget, popularity, and release year.

## Future Work
- Clean up notebooks and include SHAP analysis diagrams in outputs
- Apply natural language processing to movie overviews
- Include actor and crew influence using network-based features
- Deploy a Streamlit web app for real-time revenue prediction
