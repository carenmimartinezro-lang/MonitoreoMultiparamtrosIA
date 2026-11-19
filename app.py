import streamlit as st
import numpy as np
import plotly.graph_objects as go
import random

st.set_page_config(
    page_title="Monitoreo Multiparamétrico IA",
    page_icon="💓",
    layout="wide"
)

st.title("💓 MONITOREO MULTIPARAMÉTRICO IA")
st.caption("Simulador educativo de señales biomédicas")

st.info("Simulación con fines educativos. No utilizar para diagnóstico clínico.")

if st.button("▶ Iniciar simulación"):
    st.session_state.iniciar = True

if st.button("⏹ Detener simulación"):
    st.session_state.iniciar = False

if "iniciar" not in st.session_state:
    st.session_state.iniciar = False

if st.session_state.iniciar:

    fc = random.randint(65, 100)
    spo2 = random.randint(95, 100)
    fr = random.randint(12, 22)
    temperatura = round(random.uniform(36.0, 37.5), 1)
    pas = random.randint(105, 125)
    pad = random.randint(65, 85)

    st.subheader("Signos vitales")

    c1, c2, c3 = st.columns(3)
    c1.metric("Frecuencia cardíaca", f"{fc} lpm")
    c2.metric("Saturación SpO₂", f"{spo2} %")
    c3.metric("Frecuencia respiratoria", f"{fr} rpm")

    c4, c5, c6 = st.columns(3)
    c4.metric("Temperatura", f"{temperatura} °C")
    c5.metric("Presión sistólica", f"{pas} mmHg")
    c6.metric("Presión diastólica", f"{pad} mmHg")

    st.subheader("Señal electrocardiográfica ECG")

    t = np.linspace(0, 5, 1000)
    ecg = np.zeros_like(t)

    for latido in np.arange(0.5, 5, 60/fc):
        ecg += 0.15 * np.exp(-((t-(latido-0.2))/0.04)**2)
        ecg -= 0.15 * np.exp(-((t-(latido-0.04))/0.015)**2)
        ecg += 1.0 * np.exp(-((t-latido)/0.012)**2)
        ecg -= 0.25 * np.exp(-((t-(latido+0.04))/0.02)**2)
        ecg += 0.3 * np.exp(-((t-(latido+0.25))/0.08)**2)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=t, y=ecg,
        mode="lines",
        name="ECG"
    ))

    fig.update_layout(
        template="plotly_dark",
        height=350,
        xaxis_title="Tiempo (segundos)",
        yaxis_title="Amplitud",
        showlegend=False
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("Asistente inteligente básico")

    if fc > 100:
        st.warning("Frecuencia cardíaca elevada en esta simulación.")
    else:
        st.success("Frecuencia cardíaca dentro del rango configurado.")

    st.write(
        f"El simulador generó una frecuencia cardíaca de {fc} "
        f"lpm y una saturación de oxígeno de {spo2}%."
    )

else:
    st.warning("Presiona Iniciar simulación para visualizar el monitor.")