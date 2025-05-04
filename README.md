# 🏡 House Price Prediction using Linear Regression

This project uses a **Linear Regression** machine learning model to predict house prices in Bangalore based on various features like location, area (sqft), number of bedrooms, and bathrooms. It includes end-to-end steps — from data preprocessing to model deployment via a simple web application using **Flask**.

---

## 🔍 Features

- Data Loading from a CSV file
- Data Cleaning (handling missing values)
- Feature Engineering
- Dimensionality Reduction
- Outlier Removal:
  - Using Business Logic
  - Using Standard Deviation
  - Using Bathroom Feature
- One-Hot Encoding for Location
- Model Building with:
  - Linear Regression
  - K-Fold Cross Validation
  - Hyperparameter Tuning using GridSearchCV
- Model Testing
- Model Export as `.pkl` file
- Web Interface using Flask for easy predictions

---

## 🗂 Folder Structure

House-Price-Prediction/
│
├── House_Price_Prediction/ # Main project folder
│ ├── artifacts/ # For storing trained model and other files
│ ├── static/ # CSS, images if any
│ ├── templates/ # HTML files (index.html, result.html, etc.)
│ ├── app.py # Flask Web App
│ ├── your_dataset.csv # Raw dataset
│ └── model.pkl # Trained model file
│
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ Installation and Usage

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/yourusername/House-Price-Prediction.git
cd House-Price-Prediction/House_Price_Prediction
🐍 2. Create and Activate a Virtual Environment (optional but recommended)
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
📦 3. Install Dependencies
pip install -r ../requirements.txt
🚀 4. Run the Web Application
python app.py
The app will start running on http://127.0.0.1:5000/ — open it in your browser.
🌐 Web App Features
The web interface allows users to:

Select location from a dropdown

Enter square footage

Choose number of BHK and bathrooms

Click "Predict Price" to get the estimated house price
🧠 ML Model Development Steps
Load the Bangalore house prices dataset into a DataFrame

Clean NA/missing values

Perform feature engineering:

Combine similar locations

Convert categorical to numerical (One-Hot Encoding)

Apply dimensionality reduction to simplify features

Remove outliers using business logic, mean-deviation filtering, and bathroom sanity check

Train the model using Linear Regression

Evaluate with K-Fold Cross Validation

Optimize with GridSearchCV for best parameters

Save the model using pickle for later use in Flask app

🧪 Testing
You can test the model directly using Python or the web interface by providing inputs like:

Location: 1st Block Jayanagar

Sqft: 2000

BHK: 3

Bathroom: 2

🧰 Tech Stack
Python

Pandas, NumPy, Scikit-learn

Matplotlib (for visualization)

Flask (for the web app)

HTML, CSS (for frontend)
