import streamlit as st
import pickle
import pandas as pd
from joblib import load


modelo = open('modelo_preço','rb')
lm_new = pickle.load(modelo)
modelo.close()


st.title("Quanto vale a sua casa?")

st.markdown("Aqui vamos calcular o valor da sua casa, com base nos dados pedidos a seguir. ")


col1, col2 = st.columns(2)

area = col1.number_input("Quantos m2 ela tem?", format="%.3f") 

garagem = col1.number_input("Quantas vagas de garagem:", format="%d", step=1)

banheiro = col1.number_input("Quantidade de banheiros:", format="%d", step=1)

lareira = col2.number_input("Quantidade de lareiras:", format="%d", step=1)

marmore = col2.number_input("Possui revestimento em marmore:", format="%d", step=1, min_value=0, max_value=1)

andares = col2.number_input("Quantos andares tem:", format="%d", step=1)

entrada = [area, garagem, banheiro, lareira, marmore, andares]


if st.button('Avaliar casa'):
    
	preco_previsto = lm_new.predict([entrada])
	st.subheader("O valor estimado da casa é em $: ")
	st.code(float("%.3f" % preco_previsto))
else:
	print("0")