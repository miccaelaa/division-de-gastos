# -*- coding: utf-8 -*-
"""

"""
import streamlit as st

st.title('División de gastos 	:money_with_wings:')
st.text('''Los precios se escriben como en EEUU
con punto en vez de coma. 
Ej: 3.10 (tres pesos con diez centavos)''')



col1, col2, col3 = st.columns(3)

with col1:
    cant_personas = int(st.number_input('**Cantidad de personas:**', min_value=2, max_value=30, step=1))
    personas = {}
    key = 1
    prueba = 1
    for i in range(cant_personas):
        with st.form(key= f'forma{key}'):       
            nombre = st.text_input('**Nombre:**', key= f'name{key}')
            precio = 0.0
            cant_compras = int(st.number_input('**Cantidad de compras:**', key=f'pru{key}', min_value=1, max_value=30, step=1))
            for j in range(cant_compras):
                p = st.number_input('**Precio:** ', key= f'price{prueba}', step=0.10)
                prueba += 1
                precio += p
             
            st.form_submit_button('Listo')
            personas.update({nombre.capitalize():precio}) 
        key += 1

    if precio:  
        total = round(sum(personas.values()), 2)
        total_persona = round(total / cant_personas, 2)

        st.subheader('Compras', divider='grey')  
        for n, p in personas.items():
            st.write(f':large_purple_circle: **{n}:** $ {p}') 
        st.write(f':black_circle: Total: ${total}')
        st.write(f':black_circle: Total por persona: ${total_persona}')
        
if precio:

    st.subheader('Paga la plata', divider='grey')
    for k, v in personas.items():
        diferencia = round(v - total_persona, 2)
        if len(personas) > 1:
            if diferencia == 0:
                st.write(f':grin: {k}: cuenta saldada')
            elif diferencia > 0:
                st.write(f':sunglasses: {k} no debe plata. Le deben: $ {diferencia}')
            else:
                st.write(f':disappointed: {k} debe: $ {abs(diferencia)}')    
    st.image('https://media1.tenor.com/m/5zm4Lv18Ov0AAAAC/pagaste-dami%C3%A1n-betular.gif', width=230)





    


 

