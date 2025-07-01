import streamlit as st
import requests

API_URL = "https://docker-ai-agent-python-production-0067.up.railway.app/api/chat/"
# API_URL = "http://localhost:8000/api/chat/"

st.set_page_config(page_title="AI Email & Research Assistant", page_icon=":robot_face:")

st.title("AI Email & Research Assistant")

st.markdown("""
Interactúa con el asistente de IA para investigar temas y recibir los resultados por correo electrónico.
""")

# --- Formulario principal ---
with st.form("research_form"):
    user_message = st.text_area(
        "¿Sobre qué tema quieres investigar o qué acción deseas realizar?",
        placeholder="Ejemplo: Research what is the best type of food in different parts of the world and email me the results"
    )
    send_email = st.checkbox("¿Quieres recibir la respuesta por correo electrónico?", value=True)
    recipient_email = ""
    if send_email:
        recipient_email = st.text_input("Correo electrónico destinatario", value="")
    submit = st.form_submit_button("Enviar")

if submit and user_message.strip():
    final_message = user_message
    if send_email and recipient_email:
        final_message += f" and email me the results to {recipient_email}"
    with st.spinner("Procesando..."):
        try:
            response = requests.post(
                API_URL,
                json={"message": final_message},
                headers={"Content-Type": "application/json"},
                timeout=60
            )
            if response.status_code == 200:
                data = response.json()
                st.success("¡Consulta enviada! Revisa tu correo para los resultados.")
                st.write("Respuesta del agente:")
                st.write(data.get("content", "Sin respuesta textual."))
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error de conexión: {e}")

st.markdown("---")
st.info("Puedes modificar el mensaje para pedir diferentes acciones, como enviar un correo personalizado o consultar tu bandeja de entrada.")

# --- Opcional: ver historial de mensajes ---
if st.checkbox("Ver historial de mensajes recientes"):
    try:
        history_response = requests.get(API_URL + "recent/")
        if history_response.status_code == 200:
            history = history_response.json()
            for msg in history:
                st.write(f"**{msg['created_at']}**: {msg['message']}")
        else:
            st.warning("No se pudo obtener el historial.")
    except Exception as e:
        st.warning(f"Error al obtener historial: {e}")
