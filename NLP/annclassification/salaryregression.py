#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pickle


# In[4]:


data=pd.read_csv('Churn_Modelling.csv')
data.head()


# In[5]:


# Preprocess the data
data = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)


# In[6]:


# Encode categorical variables
label_encoder_gender = LabelEncoder()
data['Gender'] = label_encoder_gender.fit_transform(data['Gender'])


# In[7]:


data


# In[8]:


# One-hot encode 'Geography'
onehot_encoder_geo = OneHotEncoder(handle_unknown='ignore')
geo_encoded = onehot_encoder_geo.fit_transform(data[['Geography']]).toarray()
geo_encoded_df = pd.DataFrame(geo_encoded, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))
geo_encoded_df


# In[9]:


# Combine one-hot encoded columns with original data
data = pd.concat([data.drop('Geography', axis=1), geo_encoded_df], axis=1)
data.head()


# In[10]:


# Split the data into features and target
X = data.drop('EstimatedSalary', axis=1)
y = data['EstimatedSalary']


# In[11]:


## Split the data in training and tetsing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)


# In[12]:


## Scale these features
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# In[13]:


# Save the encoders and scaler for later use
with open('label_encoder_gender.pkl', 'wb') as file:
    pickle.dump(label_encoder_gender, file)

with open('onehot_encoder_geo.pkl', 'wb') as file:
    pickle.dump(onehot_encoder_geo, file)

with open('scaler.pkl', 'wb') as file:
    pickle.dump(scaler, file)


# #### ANN Regression Problem statement

# In[14]:


import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[15]:


# Build the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(32, activation='relu'),
    Dense(1)  # Output layer for regression
])

## compile the model
model.compile(optimizer='adam',loss='mean_absolute_error',metrics=['mae'])

model.summary()


# In[16]:


from tensorflow.keras.callbacks import EarlyStopping, TensorBoard
import datetime

# Set up TensorBoard
log_dir = "regressionlogs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=log_dir, histogram_freq=1)


# In[17]:


# Set up Early Stopping
early_stopping_callback = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)


# In[18]:


# Train the model
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=100,
    callbacks=[early_stopping_callback, tensorboard_callback]
)


# In[19]:


get_ipython().run_line_magic('load_ext', 'tensorboard')


# In[20]:


get_ipython().run_line_magic('tensorboard', '--logdir regressionlogs/fit')


# In[21]:


## Evaluate model on the test data
test_loss,test_mae=model.evaluate(X_test,y_test)
print(f'Test MAE : {test_mae}')


# In[ ]:


model.save('regression_model.h5')


# In[ ]:




