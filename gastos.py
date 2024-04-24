# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:10:47 2024

@author: Usuario
"""
import streamlit as st

st.title('División de gastos 	:money_with_wings:')
st.text('''Los precios se escriben como en EEUU con punto en vez de coma. 
Ej: 25.20 (veinticinco pesos con veinte centavos)''')



col1, col2, col3 = st.columns(3)

with col1:
    x = int(st.number_input('**Cantidad de personas**', min_value=2, max_value=30, step=1))
    personas = {}
    key = 1
    for i in range(x):
        with st.form(key= f'forma{key}'):       
            nombre = st.text_input('Nombre:', key= f'name{key}')
            precio = st.number_input('Precio', key= f'price{key}')
            personas.update({nombre.capitalize():precio})       
            st.form_submit_button('Listo')
        key += 1
        
    total = round(sum(personas.values()), 2)
    total_persona = round(total / x, 2)
        
    st.write(f':small_blue_diamond: Total: ${total}')
    st.write(f':small_blue_diamond: Total por persona: ${total_persona}')
    st.write(personas)

for k, v in personas.items():
    diferencia = round(v - total_persona, 2)
    if len(personas) > 1:
        if diferencia == 0:
            st.write(f':grin: {k}: cuenta saldada')
        elif diferencia > 0:
            st.write(f''':sunglasses: {k} no debe plata.
                       Le deben: $ {diferencia}''')
        else:
            st.write(f':disappointed: {k} debe: $ {abs(diferencia)}')    
st.image('https://media1.tenor.com/m/5zm4Lv18Ov0AAAAC/pagaste-dami%C3%A1n-betular.gif', width=230)





    


 

