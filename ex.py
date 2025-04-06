import streamlit as st
from sklearn.ensemble import RandomForestClassifier
import numpy as np

st.title("🌱 Iris Flower Classifier")

# Collect user input
sepal_len = st.slider("Sepal Length", 4.0, 8.0, 5.1)
sepal_wid = st.slider("Sepal Width", 2.0, 4.5, 3.5)
petal_len = st.slider("Petal Length", 1.0, 7.0, 1.4)
petal_wid = st.slider("Petal Width", 0.1, 2.5, 0.2)

# Train a quick model (for demo)
from sklearn.datasets import load_iris
iris = load_iris()
X, y = iris.data, iris.target
model = RandomForestClassifier()
model.fit(X, y)

# Predict
input_data = np.array([[sepal_len, sepal_wid, petal_len, petal_wid]])
pred = model.predict(input_data)
pred_label = iris.target_names[pred[0]]

st.write("🌸 Predicted Species:", pred_label)
