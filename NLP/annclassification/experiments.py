#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
import pickle


# In[3]:


## Load the dataset
data=pd.read_csv("Churn_Modelling.csv")
data.head()


# In[4]:


## Preprocess the data
### Drop irrelevant columns
data=data.drop(['RowNumber','CustomerId','Surname'],axis=1)
data


# In[5]:


## Encode categorical variables
label_encoder_gender=LabelEncoder()
data['Gender']=label_encoder_gender.fit_transform(data['Gender'])
data


# In[6]:


## Onehot encode 'Geography
from sklearn.preprocessing import OneHotEncoder
onehot_encoder_geo=OneHotEncoder()
geo_encoder=onehot_encoder_geo.fit_transform(data[['Geography']]).toarray()
geo_encoder


# In[7]:


onehot_encoder_geo.get_feature_names_out(['Geography'])


# In[8]:


geo_encoded_df=pd.DataFrame(geo_encoder,columns=onehot_encoder_geo.get_feature_names_out(['Geography']))
geo_encoded_df


# In[9]:


## Combine one hot encoder columns with the original data
data=pd.concat([data.drop('Geography',axis=1),geo_encoded_df],axis=1)
data.head()


# In[10]:


## Save the encoders and sscaler
with open('label_encoder_gender.pkl','wb') as file:
    pickle.dump(label_encoder_gender,file)

with open('onehot_encoder_geo.pkl','wb') as file:
    pickle.dump(onehot_encoder_geo,file)


# In[11]:


data.head()


# In[12]:


## DiVide the dataset into indepent and dependent features
X=data.drop('Exited',axis=1)
y=data['Exited']

## Split the data in training and tetsing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

## Scale these features
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)


# In[13]:


X_train


# In[14]:


with open('scaler.pkl','wb') as file:
    pickle.dump(scaler,file)


# In[15]:


data


# In[ ]:


get_ipython().system(' pip install tensorflow')


# ### ANN Implementation

# In[17]:


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping,TensorBoard
import datetime


# In[18]:


## Build Our ANN Model
model = Sequential([
    Dense(64,activation='relu',input_shape=(X_train.shape[1],)), ## first hidden layer
    Dense(32,activation='relu'), ## second hidden layer
    Dense(1,activation='sigmoid') ## output layer
])


# In[19]:


model.summary()


# In[20]:


opt = tf.keras.optimizers.Adam(learning_rate=0.01)
tf.keras.losses.BinaryCrossentropy()


# In[21]:


## compile the model
model.compile(optimizer=opt,loss='binary_crossentropy',metrics=['accuracy'])


# In[22]:


#Set up  the Tensorboard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorflow_callback = TensorBoard(log_dir=log_dir,histogram_freq=1)


# In[23]:


# Set up Early Stopping
EarlyStopping_callback = EarlyStopping(monitor='val_loss',patience=10,restore_best_weights=True)


# In[24]:


## Training the model
history = model.fit(
    X_train,y_train,validation_data = (X_test,y_test),epochs = 100,
    callbacks = [tensorflow_callback,EarlyStopping_callback]
)


# In[25]:


model.save('model.h5')


# In[26]:


get_ipython().system(' pip install tensorboard')


# In[27]:


## Load Tensorboard Extension
import tensorboard
get_ipython().run_line_magic('load_ext', 'tensorboard')


# In[28]:


get_ipython().run_line_magic('tensorboard', '--logdir logs/fit')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




