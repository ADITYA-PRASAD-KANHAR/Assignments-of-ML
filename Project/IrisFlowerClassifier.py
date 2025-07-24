import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.title("IRIS Flower Classifier")

iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

if st.checkbox("Show Iris Dataset"):
    st.subheader("Iris Dataset")
    st.write(x.head(10))
    st.write("Target Labels:", iris.target_names)

st.sidebar.header("Input Features")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length (cm)', float(x['sepal length (cm)'].min()), float(x['sepal length (cm)'].max()), 5.4)
    sepal_width = st.sidebar.slider('Sepal width (cm)', float(x['sepal width (cm)'].min()), float(x['sepal width (cm)'].max()), 3.4)
    petal_length = st.sidebar.slider('Petal length (cm)', float(x['petal length (cm)'].min()), float(x['petal length (cm)'].max()), 1.3)
    petal_width = st.sidebar.slider('Petal width (cm)', float(x['petal width (cm)'].min()), float(x['petal width (cm)'].max()), 0.2)

    data = {
        'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
        'petal width (cm)': petal_width
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

model = RandomForestClassifier()
model.fit(x, y)

prediction = model.predict(input_df)
prediction_proba = model.predict_proba(input_df)

st.write("Accuracy Score :- " , model.score(x,y))

st.subheader("User Input Parameters")
st.write(input_df)

st.subheader("Prediction")
st.write(f"**Predicted Species:** {iris.target_names[prediction][0]}")

st.subheader("Prediction Probability")
proba_df = pd.DataFrame(prediction_proba, columns=iris.target_names)
st.write(proba_df)


st.subheader("Feature Importance (Random Forest)")
fig1, ax1 = plt.subplots()
feature_importances = model.feature_importances_
sns.barplot(x=feature_importances, y=iris.feature_names, palette="viridis", ax=ax1)
ax1.set_xlabel("Importance")
ax1.set_ylabel("Feature")
ax1.set_title("Feature Importance in Iris Classification")
st.pyplot(fig1)
