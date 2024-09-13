import streamlit as st
import joblib
import pandas as pd
st.set_page_config(page_title="Prédiction Objectif Patrimonial", page_icon="💰", layout="centered")

page_bg_img = '''
<style>
    .stApp {
        background-color: #00a581;
    }
 
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.image('logo.png', width=200)


title_html = '''
<h1 style="font-family:Arial, sans-serif; color:#125b45; font-size: 42px; text-align:center;">
    Prédiction objective du patrimoine
</h1>
'''
st.markdown(title_html, unsafe_allow_html=True)

model = joblib.load('Objectif Patrimonial.pkl')

with st.form(key='prediction_form'):

    st.markdown('<p style="font-family:Arial; font-size:20px; color:#166751;">Veuillez entrer les détails ci-dessous :</p>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    data = {
        'Nombre enfants': cols[0].number_input('Nombre enfants', min_value=0, step=1, help='Indiquez le nombre d\'enfants.'),
        'GP-Impôt sur le Revenu brut': cols[1].number_input('GP-Impôt sur le Revenu brut', value=0.0, format='%f', help='Saisissez le montant total des impôts sur le revenu.'),
        'GP-Revenus professionnels foyer': cols[2].number_input('GP-Revenus professionnels foyer', value=0.0, format='%f', help='Entrez les revenus professionnels totaux du foyer.'),
        'GP-Solde Flux': cols[0].number_input('GP-Solde Flux', value=0.0, format='%f', help='Saisissez le solde des flux financiers.'),
        'GP-Patrimoine Professionnel': cols[1].number_input('GP-Patrimoine Professionnel', value=0.0, format='%f', help='Indiquez la valeur du patrimoine professionnel.'),
        'GP-Passif cumulé': cols[2].number_input('GP-Passif cumulé', value=0.0, format='%f', help='Saisissez le montant total des passifs.'),
        'GP-Patrimoine immobilier': cols[0].number_input('GP-Patrimoine immobilier', value=0.0, format='%f', help='Indiquez la valeur du patrimoine immobilier.'),
        'GP-Patrimoine financier': cols[1].number_input('GP-Patrimoine financier', value=0.0, format='%f', help='Indiquez la valeur du patrimoine financier.'),
        'GP-Solde actif&passif': cols[2].number_input('GP-Solde actif&passif', value=0.0, format='%f', help='Saisissez le solde des actifs et passifs.'),
        'GP-Total actif brut': cols[0].number_input('GP-Total actif brut', value=0.0, format='%f', help='Indiquez le montant total des actifs bruts.'),
        'Age': cols[1].number_input('Age', min_value=0, step=1, help='Entrez l\'âge de la personne.')
    }

    submit_button = st.form_submit_button(label='Predict', help='Cliquez pour prédire l\'objectif patrimonial.')
if submit_button:
    input_df = pd.DataFrame([data])
    try:
        prediction = model.predict(input_df)[0]
        st.markdown(f'<p style="font-family:Arial; font-size:24px; color:#0a9250;">Prédiction de l\'objectif patrimonial : {prediction}</p>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<p style="font-family:Arial; font-size:24px; color:#d9534f;">Erreur lors de la prédiction : {e}</p>', unsafe_allow_html=True)

        st.error(f'Error during prediction: {e}')



