# Importing the libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import metrics

import pickle
df = pd.read_csv('/home/msjahid/Desktop/model-flask/dak_movements_clean.csv')
map_operation_type = {'Sent': 0, 'Forward': 1, 'NothiVukto' : 2, 'NothiJato' : 3}
df['operation_type'] = df['operation_type'].map(map_operation_type)
y = df['dak_actions9']
X = df.drop(['dak_actions9', 'from_officer_name'] , axis=1).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)

# Saving model to disk
pickle.dump(rfc, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
result = model.predict([[1, 65, 5121, 77858, 12643, 65, 5121, 77847, 12642, 1, 1, 0]])
prediction = model.predict(X_test)
print('The accuracy of the Random Forest classifier is',metrics.accuracy_score(prediction,y_test))
print(result)
