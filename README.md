# FeatureEngineering_Capstone
Hotel Booking Cancellation Prediction

Project Overview
This project applies machine learning and feature engineering to predict hotel booking cancellations. By transforming raw hotel data into actionable business features, the final model provides highly accurate predictions to help hotels optimize revenue and inventory management.

The final predictive model (Random Forest) achieved an F1 Score of 0.9665 and a ROC-AUC of 0.9944.

Repository Structure
This repository is structured to separate raw analysis, reusable pipeline code, and final reporting:

FeatureEngineering_Capstone.ipynb: The main Jupyter Notebook containing the full data science pipeline (EDA, Preprocessing, Feature Engineering, Feature Selection, and Model Training).

/src/: Contains reusable Python scripts and helper functions.

/report/: Contains the final Report.pdf with the executive summary, methodology, and final Capstone comparison tables.

requirements.txt: The required dependencies to run the project locally.

How to Run This Project Locally
This project was completed locally in VS Code. To reproduce the environment and run the notebook on your own machine, please follow these steps:

Clone the repository to your local machine: git clone [Paste your GitHub Link Here]

Set up the environment by installing the required packages: pip install -r requirements.txt

Open FeatureEngineering_Capstone.ipynb in your preferred editor.

Click "Restart & Run All" to execute the pipeline from top to bottom.

Key Features Engineered
To improve upon the baseline model, several highly predictive features were engineered, including:

Business Metrics: total_nights, total_guests, price_per_person

Interaction Features: Location-based pricing adjustments and cross-variable polynomials.

Final Model Performance
After extensive feature engineering and feature selection (using Random Forest Importance, Mutual Information, and Chi-Square tests), the final Top 20 features were modeled with the following results:

Final F1 Score: 0.9763

Final ROC-AUC: 0.9969

(THE CSV DATA SET WAS USED FROM LUMEN . THE ONE WHICH WAS PROVIDED IN THE Data Preprocessing SECTION)