import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.5

st.title("CMOS Power Optimization Analyzer")

st.write("Analyze CMOS dynamic power consumption")

voltage = st.number_input("Supply Voltage (V)", value=1.2)
capacitance = st.number_input("Load Capacitance (F)", value=5e-12, format="%e")
frequency = st.number_input("Frequency (Hz)", value=100000000)

if st.button("Calculate Power"):

    power = alpha * capacitance * (voltage**2) * frequency
    optimized_voltage = voltage * 0.9
    optimized_power = alpha * capacitance * (optimized_voltage**2) * frequency

    st.subheader("Results")

    st.write(f"Power Consumption: {power:.6e} Watts")
    st.write(f"Optimized Voltage: {optimized_voltage:.2f} V")
    st.write(f"Optimized Power: {optimized_power:.6e} Watts")

    voltages = np.linspace(0.5, 1.5, 50)
    powers = alpha * capacitance * (voltages**2) * frequency

    fig, ax = plt.subplots()
    ax.plot(voltages, powers)
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Power Consumption (W)")
    ax.set_title("Voltage vs Power Consumption")

    st.pyplot(fig)