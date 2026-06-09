from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().with_name('Social_Network_Ads.csv')

df = pd.read_csv(DATA_PATH)

print(df.head())
df = df.drop(columns=['User ID' , 'Gender'])

x = df.drop(columns=['Purchased'])
y = df['Purchased']

# train the model 

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(x_train, y_train)

# save the model 

import joblib
joblib.dump(rf, 'rf_model.pkl')
print("Model trained and saved as 'rf_model.pkl'")
