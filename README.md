# **📊 *Social Media Ad Predictor: End-to-End Production API***

This repository contains a full-stack Machine Learning pipeline designed to predict customer purchasing behavior from social media advertisements. The project covers the entire ML lifecycle: managing data within a SQL database, building a predictive model in Python, and deploying it as a production-ready REST API using Flask.

---

# 🎯*Project Overview*

This project serves as a comprehensive blueprint for bridging the gap between raw data science and production-grade software engineering. In modern enterprise environments, machine learning models cannot exist in isolation; they must interact seamlessly with relational databases and external client applications. 

To address this, the project establishes a robust, automated workflow divided into three core organizational phases:

* ## Data Layer & ETL:
Establishing a secure handshake with a local `MySQL` instance to query historical user advertisement data. This phase highlights how raw corporate data registries are structured, maintained, and safely ingested into memory space using optimized connection protocols.
  
* ## Modeling & Optimization Layer:
Transitioning data into analytical environments to execute feature engineering, isolate target variables, and run matrix computations. Using Scikit-Learn's Logistic Regression, the pipeline learns optimal decision boundaries to classify whether an ad viewer will convert into a buyer based on demographic factors, followed by high-efficiency serialization to freeze the model state.
 
* ## Serving Layer & Microservice Deployment:
Transforming the static model binary into a live, interactive web entity. By wrapping the predictor inside a Flask REST API framework, the system exposes scalable endpoints capable of handling real-time, stateless HTTP `POST` requests, parsing incoming JSON payloads, and generating instantaneous inference responses.

---

## 🛠️ *Technology Stack*

| Component | Technology Used | Implementation Role |
| :--- | :--- | :--- |
| **Language** | Python | Main programming environment |
| **Database** | MySQL | Relational data warehousing |
| **Data Engineering** | Pandas & NumPy | ETL processes and matrix operations |
| **Machine Learning** | Scikit-learn | Model training, evaluation, and tuning |
| **Storage** | Joblib | High-efficiency model serialization |
| **Deployment** | Flask | Microframework for API development |
| **Validation** | Postman | End-point testing and request simulation |

---

## 📂*Directory Layout*

```text
ML_Project/
│
├── app.py                   # Production Flask application & API routes
├── model training.ipynb     # Interactive Jupyter notebook for model development
├── lr_model.pkl             # Saved weights of the trained Logistic Regression model
├── requirements.txt         # Managed project dependencies
├── README.md                # Project documentation
└── venv/                    # Local isolated Python environment
```

# **🔄 *Step-by-Step Architecture***
### 1. Database Setup
The raw advertisement dataset is housed within a MySQL instance for relational tracking.

```sql
CREATE DATABASE app;
The 'Social_Network_Ads' table is populated within this schema
```

## 2. Data Retrieval (ETL)
Data is pulled directly from the SQL server into an active memory Pandas DataFrame for processing.

``` Python
import mysql.connector
import pandas as pd

# Establishing the database handshake
db_client = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="app"
)
# Extracting target dataset
df = pd.read_sql("SELECT * FROM Social_Network_Ads", db_client)
```

## 3. Preprocessing & Modeling
--> Feature Engineering:** Handling missing data fields, isolating core predictive variables, and splitting data into training and validation subsets.

--> Training Execution:** Fitting a classification algorithm to establish optimal decision boundaries.

``` Python
`from sklearn.linear_model import LogisticRegression

# Initializing and optimizing the classifier
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
```

## 4. Model Persistence
The finalized model state is frozen to disk to ensure repeatable results during web serving.

```Python
import joblib

# Saving the model state
joblib.dump(classifier, "lr_model.pkl")
```

## 5. Flask API Integration
The system imports the frozen binary model dynamically into production runtime memory.

```Python
import joblib

# Loading the model inside app.py
predictor = joblib.load("lr_model.pkl")
```

# 🔌 *API Documentation*

Inference Endpoint
Route:``` /predict```

Method: ```POST```

Content-Type:``` application/json```

## Request Body
```JSON 
{
  "input": [42, 50000]
}
```

## Successful Result
```JSON
{
  "prediction": 1
}
```

# ⚙️ *Request Execution Lifecycle*
```text
  [ Client Request ]
          │
          ▼
    Flask Server
   (POST /predict)
          │
          ▼
   Parse JSON Input
          │
          ▼
 Evaluate with Predictor
          │
          ▼
  Generate Response
          │
          ▼
  [ JSON Outbound ]
```
# 🚀 *Getting Started*

## 1. Clone & Navigate
```Bash
git clone <your-repository-url>
cd ML_Project
```
## 2. Environment Setup

Create and engage a clean virtual environment to prevent dependency conflicts:

**macOS / Linux:**

```Bash
python -m venv venv
source venv/bin/activate
```
**Windows:**

```Bash
python -m venv venv
venv\Scripts\activate
```
## 3. Install Dependencies
```Bash
pip install -r requirements.txt
```
Example Dependencies:
```
Flask
numpy
pandas
scikit-learn
mysql-connector-python
joblib
```
**4. Boot the Microservice**
```Bash
python app.py
```
The server will initialize locally. You can now use Postman or curl to fire POST requests directly at your local port.
