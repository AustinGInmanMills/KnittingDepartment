import streamlit as st
from math import trunc

machine_1 = 1600
machine_1_rpms = 15
machine_1_yarn_type = "N/A"

machine_2 = 1600
machine_2_rpms = 15
machine_2_yarn_type = "N/A"

machine_3 = 1800
machine_3_rpms = 10
machine_3_yarn_type = "Black&White Cone"

machine_4 = 1600
machine_4_rpms = 10
machine_4_yarn_type = "Horse Head Cone"

machine_5 = 1800
machine_5_rpms = 11
machine_5_yarn_type = "Black&White Cone"

machine_6 = 1600
machine_6_rpms = 15
machine_6_yarn_type = "Black&White Cone"

machine_7 = 1600
machine_7_rpms = 15
machine_7_yarn_type = "Black&White Cone"

machine_8 = 1400
machine_8_rpms = 8
machine_8_yarn_type = "Horse Head Cone"

machine_9 = 1400
machine_9_rpms = 10
machine_9_yarn_type = "Horse Head Cone"

machine_10 = 1600
machine_10_rpms = 15
machine_10_yarn_type = "N/A"

machine_11 = 1600
machine_11_rpms = 15
machine_11_yarn_type = "Black&White Cone"

machine_12 = 2800
machine_12_rpms = 8
machine_12_yarn_type = "Horse Head Cone"

machine_13 = 2800
machine_13_rpms = 12
machine_13_yarn_type = "Horse Head Cone"

machine_14 = 1600
machine_14_rpms = 15
machine_14_yarn_type = "N/A"

machine_15 = 1600
machine_15_rpms = 15
machine_15_yarn_type = "Black&White Cone"

machine_16 = 1600
machine_16_rpms = 15
machine_16_yarn_type = "Black&White Cone"

machine_17 = 1600
machine_17_rpms = 10
machine_17_yarn_type = "Pink&Black Cone"

machine_18 = 1600
machine_18_rpms = 8
machine_18_yarn_type = "Pink&Black Cone"

machine_19 = 1600
machine_19_rpms = 15
machine_19_yarn_type = "Black&White Cone"

machine_20 = 1600
machine_20_rpms = 8
machine_20_yarn_type = "Pink&Black Cone"

machine_21 = 1600
machine_21_rpms = 8
machine_21_yarn_type = "Pink&Black Cone"

machine_22 = 1600
machine_22_rpms = 15
machine_22_yarn_type = "Pink&Black Cone"

st.markdown(
    body="""
        <style>
            .block-container{
                    padding-top: 25px;
                }
        </style>
    """,
    unsafe_allow_html=True
)

st.header("Knitting Department", divider=("red"))

option = st.selectbox(
    "",
    ("Doff Time Calculator", "Machine's that are King's", "Machine's that are Queen's", "Machine's that are Black&White Cone", "Machine's that are Pink&Black Cone", "Machine's that are Horse Head Cone", "Chat"),
    index=None,
    placeholder="Select an option...",
)

if option == "Doff Time Calculator":
    st.header("Doff Time Calculator", divider="red")

    st.subheader("Machine #1 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_1_yarn_type}]")
    st.write("DOFF = ", int(machine_1))
    st.write("RPMS = ", int(machine_1_rpms))
    machine_current_revs = st.text_input("Current REVS", "0", key="1")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_1 - machine_current_revs
        calculation = calculation / machine_1_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #2 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_2_yarn_type}]")
    st.write("DOFF = ", int(machine_2))
    st.write("RPMS = ", int(machine_2_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="2")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_2 - machine_current_revs
        calculation = calculation / machine_2_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #3 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_3_yarn_type}]")
    st.write("DOFF = ", int(machine_3))
    st.write("RPMS = ", int(machine_3_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="3")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_3 - machine_current_revs
        calculation = calculation / machine_3_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #4 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_4_yarn_type}]")
    st.write("DOFF = ", int(machine_4))
    st.write("RPMS = ", int(machine_4_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="4")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_4 - machine_current_revs
        calculation = calculation / machine_4_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #5 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_5_yarn_type}]")
    st.write("DOFF = ", int(machine_5))
    st.write("RPMS = ", int(machine_5_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="5")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_5 - machine_current_revs
        calculation = calculation / machine_5_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #6 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_6_yarn_type}]")
    st.write("DOFF = ", int(machine_6))
    st.write("RPMS = ", int(machine_6_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="6")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_6 - machine_current_revs
        calculation = calculation / machine_6_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #7 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_7_yarn_type}]")
    st.write("DOFF = ", int(machine_7))
    st.write("RPMS = ", int(machine_7_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="7")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_7 - machine_current_revs
        calculation = calculation / machine_7_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #8 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_8_yarn_type}]")
    st.write("DOFF = ", int(machine_8))
    st.write("RPMS = ", int(machine_8_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="8")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_8 - machine_current_revs
        calculation = calculation / machine_8_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #9 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_9_yarn_type}]")
    st.write("DOFF = ", int(machine_9))
    st.write("RPMS = ", int(machine_9_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="9")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_9 - machine_current_revs
        calculation = calculation / machine_9_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #10 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_10_yarn_type}]")
    st.write("DOFF = ", int(machine_10))
    st.write("RPMS = ", int(machine_10_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="10")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_10 - machine_current_revs
        calculation = calculation / machine_10_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #11 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_11_yarn_type}]")
    st.write("DOFF = ", int(machine_11))
    st.write("RPMS = ", int(machine_11_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="11")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_11 - machine_current_revs
        calculation = calculation / machine_11_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #12 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_12_yarn_type}]")
    st.write("DOFF = ", int(machine_12))
    st.write("RPMS = ", int(machine_12_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="12")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_12 - machine_current_revs
        calculation = calculation / machine_12_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #13 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_13_yarn_type}]")
    st.write("DOFF = ", int(machine_13))
    st.write("RPMS = ", int(machine_13_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="13")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_13 - machine_current_revs
        calculation = calculation / machine_13_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #14 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_14_yarn_type}]")
    st.write("DOFF = ", int(machine_14))
    st.write("RPMS = ", int(machine_14_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="14")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_14 - machine_current_revs
        calculation = calculation / machine_14_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #15 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_15_yarn_type}]")
    st.write("DOFF = ", int(machine_15))
    st.write("RPMS = ", int(machine_15_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="15")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_15 - machine_current_revs
        calculation = calculation / machine_15_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #16 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_16_yarn_type}]")
    st.write("DOFF = ", int(machine_16))
    st.write("RPMS = ", int(machine_16_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="16")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_16 - machine_current_revs
        calculation = calculation / machine_16_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #17 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_17_yarn_type}]")
    st.write("DOFF = ", int(machine_17))
    st.write("RPMS = ", int(machine_17_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="17")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_17 - machine_current_revs
        calculation = calculation / machine_17_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #18 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_18_yarn_type}]")
    st.write("DOFF = ", int(machine_18))
    st.write("RPMS = ", int(machine_18_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="18")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_18 - machine_current_revs
        calculation = calculation / machine_18_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #19 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_19_yarn_type}]")
    st.write("DOFF = ", int(machine_19))
    st.write("RPMS = ", int(machine_19_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="19")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_19 - machine_current_revs
        calculation = calculation / machine_19_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #20 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_20_yarn_type}]")
    st.write("DOFF = ", int(machine_20))
    st.write("RPMS = ", int(machine_20_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="20")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_20 - machine_current_revs
        calculation = calculation / machine_20_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #21 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_21_yarn_type}]")
    st.write("DOFF = ", int(machine_21))
    st.write("RPMS = ", int(machine_21_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="21")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_21 - machine_current_revs
        calculation = calculation / machine_21_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass

    st.divider()

    st.subheader("Machine #22 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_22_yarn_type}]")
    st.write("DOFF = ", int(machine_22))
    st.write("RPMS = ", int(machine_22_rpms))
    machine_current_revs = st.text_input("Current Revs", "0", key="22")
    try:
        machine_current_revs = float(machine_current_revs)
        calculation = machine_22 - machine_current_revs
        calculation = calculation / machine_22_rpms
        if calculation > 60:
            calculation = calculation / 60
            number_dec1 = trunc(calculation)
            number_dec2 = str(calculation - int(calculation))[1:]
            minutes_calc = float(number_dec2) * 60
            minutes_calc = trunc(minutes_calc)
            calculation = str(calculation)
            st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes")
        else:
            calculation = round(calculation, 2)
            calculation = str(calculation)
            st.write(calculation, "minutes")
    except:
        pass
elif option == "Machine's that are Queen's":
    st.header("Queen's Total = :green[1]", divider="red")
    st.subheader("[1]Machine #1 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_1_yarn_type}]")
    st.write("DOFF = ", int(machine_1))
    st.write("RPMS = ", int(machine_1_rpms))
    st.divider()

elif option == "Machine's that are King's":
    st.header("King's Total = :green[1]", divider="red")
    st.subheader("[1]Machine #1 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_1_yarn_type}]")
    st.write("DOFF = ", int(machine_1))
    st.write("RPMS = ", int(machine_1_rpms))
    st.divider()
elif option == "Machine's that are Black&White Cone":
    st.header("Black&White Total = :green[10]", divider="red")
    st.subheader("[1]Machine #1 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_1_yarn_type}]")
    st.write("DOFF = ", int(machine_1))
    st.write("RPMS = ", int(machine_1_rpms))
    st.divider()
    st.subheader("[2]Machine #2 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_2_yarn_type}]")
    st.write("DOFF = ", int(machine_2))
    st.write("RPMS = ", int(machine_2_rpms))
    st.divider()
    st.subheader("[3]Machine #3 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_3_yarn_type}]")
    st.write("DOFF = ", int(machine_3))
    st.write("RPMS = ", int(machine_3_rpms))
    st.divider()
    st.subheader("[4]Machine #5 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_5_yarn_type}]")
    st.write("DOFF = ", int(machine_5))
    st.write("RPMS = ", int(machine_5_rpms))
    st.divider()
    st.subheader("[5]Machine #6 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_6_yarn_type}]")
    st.write("DOFF = ", int(machine_6))
    st.write("RPMS = ", int(machine_6_rpms))
    st.divider()
    st.subheader("[6]Machine #7 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_7_yarn_type}]")
    st.write("DOFF = ", int(machine_7))
    st.write("RPMS = ", int(machine_7_rpms))
    st.divider()
    st.subheader("[7]Machine #11 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_11_yarn_type}]")
    st.write("DOFF = ", int(machine_11))
    st.write("RPMS = ", int(machine_11_rpms))
    st.divider()
    st.subheader("[8]Machine #15 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_15_yarn_type}]")
    st.write("DOFF = ", int(machine_15))
    st.write("RPMS = ", int(machine_15_rpms))
    st.divider()
    st.subheader("[9]Machine #16 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_16_yarn_type}]")
    st.write("DOFF = ", int(machine_16))
    st.write("RPMS = ", int(machine_16_rpms))
    st.divider()
    st.subheader("[10]Machine #19 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_19_yarn_type}]")
    st.write("DOFF = ", int(machine_19))
    st.write("RPMS = ", int(machine_19_rpms))
    st.divider()
elif option == "Machine's that are Pink&Black Cone":
    st.header("Pink&Black Total = :green[5]", divider="red")
    st.subheader("[1]Machine #17 | :red[Status Down]")
    st.markdown(f"Yarn Type = :green[{machine_17_yarn_type}]")
    st.write("DOFF = ", int(machine_17))
    st.write("RPMS = ", int(machine_17_rpms))
    st.divider()
    st.subheader("[2]Machine #18 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_18_yarn_type}]")
    st.write("DOFF = ", int(machine_18))
    st.write("RPMS = ", int(machine_18_rpms))
    st.divider()
    st.subheader("[3]Machine #20 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_20_yarn_type}]")
    st.write("DOFF = ", int(machine_20))
    st.write("RPMS = ", int(machine_20_rpms))
    st.divider()
    st.subheader("[4]Machine #21 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_21_yarn_type}]")
    st.write("DOFF = ", int(machine_21))
    st.write("RPMS = ", int(machine_21_rpms))
    st.divider()
    st.subheader("[5]Machine #22 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_22_yarn_type}]")
    st.write("DOFF = ", int(machine_22))
    st.write("RPMS = ", int(machine_22_rpms))
    st.divider()
elif option == "Machine's that are Horse Head Cone":
    st.header("Horse Head Total = :green[5]", divider="red")
    st.subheader("[1]Machine #4 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_4_yarn_type}]")
    st.write("DOFF = ", int(machine_4))
    st.write("RPMS = ", int(machine_4_rpms))
    st.divider()
    st.subheader("[2]Machine #8 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_8_yarn_type}]")
    st.write("DOFF = ", int(machine_8))
    st.write("RPMS = ", int(machine_8_rpms))
    st.divider()
    st.subheader("[3]Machine #9 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_9_yarn_type}]")
    st.write("DOFF = ", int(machine_9))
    st.write("RPMS = ", int(machine_9_rpms))
    st.divider()
    st.subheader("[4]Machine #12 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_12_yarn_type}]")
    st.write("DOFF = ", int(machine_12))
    st.write("RPMS = ", int(machine_12_rpms))
    st.divider()
    st.subheader("[5]Machine #13 | :green[Status Running]")
    st.markdown(f"Yarn Type = :green[{machine_13_yarn_type}]")
    st.write("DOFF = ", int(machine_13))
    st.write("RPMS = ", int(machine_13_rpms))
    st.divider()
