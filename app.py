import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go

# Page configuration
st.set_page_config(
    page_title='Customer Churn Predictor',
    page_icon='📊',
    layout='wide'
)

# Title
st.title('Customer Churn Prediction System')

# Load model
@st.cache_resource
def load_model():
    with open('best_churn_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()
st.success('Model loaded successfully!')

# Layout columns
col1, col2 = st.columns(2)

# Column 1: Demographics
with col1:
    st.subheader('Customer Demographics')
    gender = st.selectbox('Gender', ['Male', 'Female'])
    senior_citizen = st.selectbox('Senior Citizen', ['No', 'Yes'])
    partner = st.selectbox('Partner', ['No', 'Yes'])
    dependents = st.selectbox('Dependents', ['No', 'Yes'])

# Column 2: Account Info
with col2:
    st.subheader('Account Information')
    tenure = st.slider('Tenure (months)', 0, 72, 12)
    monthly_charges = st.number_input(
        'Monthly Charges ($)',
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

# Prediction button
if st.button('Predict Churn', type='primary'):
    
    # Create input dataframe
    input_data = {
        'gender': gender,
        'SeniorCitizen': 1 if senior_citizen == 'Yes' else 0,
        'Partner': 1 if partner == 'Yes' else 0,
        'Dependents': 1 if dependents == 'Yes' else 0,
        'tenure': tenure,
        'MonthlyCharges': monthly_charges
    }

    input_df = pd.DataFrame([input_data])

    # Encode categorical variables
    input_encoded = pd.get_dummies(input_df)

    # Align columns with model (IMPORTANT FIX)
    try:
        model_columns = model.feature_names_in_
        input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)
    except:
        pass

    # Prediction
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0]
    churn_prob = probability[1] * 100

    # Output
    if prediction == 1:
        st.error('HIGH RISK: Customer likely to churn')
        st.metric('Churn Probability', f'{churn_prob:.1f}%')
    else:
        st.success('LOW RISK: Customer likely to stay')
        st.metric('Retention Probability', f'{100 - churn_prob:.1f}%')
        import plotly.express as px

# Maan lijiye aapke pass 'Churn' column hai dataframe mein
def plot_churn_distribution(df):
    churn_counts = df['Churn'].value_counts().reset_index()
    churn_counts.columns = ['Status', 'Count']
    
    fig = px.pie(churn_counts, values='Count', names='Status', 
                 title='Customer Churn Distribution',
                 color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig) 
    def plot_feature_importance(model, feature_names):
    # XGBoost se importance nikalna
    importances = model.feature_importances_
    feature_imp_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    feature_imp_df = feature_imp_df.sort_values(by='Importance', ascending=False).head(10)

    fig = px.bar(feature_imp_df, x='Importance', y='Feature', orientation='h',
                 title='Top 10 Factors Influencing Churn',
                 color='Importance',
                 color_continuous_scale='Viridis')
    
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig)
    # Model load hone ke baad
if st.checkbox('Show Visualizations'):
    st.subheader("Project Analytics")
    
    # Do columns banayein visuals ke liye
    col1, col2 = st.columns(2)
    
    with col1:
        plot_churn_distribution(df) # 'df' aapka original dataset hai
        
    with col2:
        # 'model' aapka loaded XGBoost model hai
        # 'X.columns' aapke features ke naam hain
        plot_feature_importance(model, X.columns)
