import streamlit as st
from math import trunc


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


total_operable = 16
total_inoperable = 6

total_kings = 0
total_queens = 0
total_twins = 3

total_white = 8
total_pink = 5
total_horse = 5

machine_1 = "N/A"
machine_1_rpms = "N/A"
machine_1_yarn_type = "N/A"
machine_1_status = ":red[Status: Inoperable]"
machine_1_size = "N/A"

machine_2 = "N/A"
machine_2_rpms = "N/A"
machine_2_yarn_type = "N/A"
machine_2_status = ":red[Status: Inoperable]"
machine_2_size = "N/A"

machine_3 = 1800
machine_3_rpms = 10
machine_3_yarn_type = "Black&White Cone"
machine_3_status = ":green[Status: Operable]"
machine_3_size = "N/A"

machine_4 = 1600
machine_4_rpms = 10
machine_4_yarn_type = "Horse Head Cone"
machine_4_status = ":green[Status: Operable]"
machine_4_size = "N/A"

machine_5 = 1800
machine_5_rpms = 11
machine_5_yarn_type = "Black&White Cone"
machine_5_status = ":green[Status: Operable]"
machine_5_size = "N/A"

machine_6 = 1600
machine_6_rpms = 15
machine_6_yarn_type = "Black&White Cone"
machine_6_status = ":green[Status: Operable]"
machine_6_size = "N/A"

machine_7 = "N/A"
machine_7_rpms = "N/A"
machine_7_yarn_type = "Black&White Cone"
machine_7_status = ":red[Status: Inoperable]"
machine_7_size = "N/A"

machine_8 = 1400
machine_8_rpms = 8
machine_8_yarn_type = "Horse Head Cone"
machine_8_status = ":green[Status: Operable]"
machine_8_size = "N/A"

machine_9 = 1400
machine_9_rpms = 10
machine_9_yarn_type = "Horse Head Cone"
machine_9_status = ":green[Status: Operable]"
machine_9_size = "N/A"

machine_10 = "N/A"
machine_10_rpms = "N/A"
machine_10_yarn_type = "N/A"
machine_10_status = ":red[Status: Inoperable]"
machine_10_size = "N/A"

machine_11 = "N/A"
machine_11_rpms = "N/A"
machine_11_yarn_type = "Black&White Cone"
machine_11_status = ":red[Status: Inoperable]"
machine_11_size = "Twin"

machine_12 = 2800
machine_12_rpms = 8
machine_12_yarn_type = "Horse Head Cone"
machine_12_status = ":green[Status: Operable]"
machine_12_size = "Twin"

machine_13 = 2800
machine_13_rpms = 12
machine_13_yarn_type = "Horse Head Cone"
machine_13_status = ":green[Status: Operable]"
machine_13_size = "Twin"

machine_14 = "N/A"
machine_14_rpms = "N/A"
machine_14_yarn_type = "N/A"
machine_14_status = ":red[Status: Inoperable]"
machine_14_size = "N/A"

machine_15 = 1600
machine_15_rpms = 15
machine_15_yarn_type = "Black&White Cone"
machine_15_status = ":green[Status: Operable]"
machine_15_size = "N/A"

machine_16 = 1600
machine_16_rpms = 15
machine_16_yarn_type = "Black&White Cone"
machine_16_status = ":green[Status: Operable]"
machine_16_size = "N/A"

machine_17 = 1600
machine_17_rpms = 10
machine_17_yarn_type = "Pink&Black Cone"
machine_17_status = ":green[Status: Operable]"
machine_17_size = "N/A"

machine_18 = 1600
machine_18_rpms = 8
machine_18_yarn_type = "Pink&Black Cone"
machine_18_status = ":green[Status: Operable]"
machine_18_size = "N/A"

machine_19 = 1600
machine_19_rpms = 15
machine_19_yarn_type = "Black&White Cone"
machine_19_status = ":green[Status: Operable]"
machine_19_size = "N/A"

machine_20 = 1600
machine_20_rpms = 8
machine_20_yarn_type = "Pink&Black Cone"
machine_20_status = ":green[Status: Operable]"
machine_20_size = "N/A"

machine_21 = 1600
machine_21_rpms = 8
machine_21_yarn_type = "Pink&Black Cone"
machine_21_status = ":green[Status: Operable]"
machine_21_size = "N/A"

machine_22 = 1600
machine_22_rpms = 15
machine_22_yarn_type = "Pink&Black Cone"
machine_22_status = ":green[Status: Operable]"
machine_22_size = "N/A"


st.header("Knitting Department Multi Tool", divider="red")


tab1, tab2, = st.tabs(["Doff Time Calculator", "Machines Information"])


with tab1:
        st.markdown("You can calculate how long a machine has left till it doffs here.")


        st.subheader(f"Machine #1 | {machine_1_status}")
        st.markdown(f"Size = :orange[{machine_1_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_1_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_1}]")
        st.markdown(f"RPMS = :orange[{machine_1_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


        st.subheader(f"Machine #2 | {machine_2_status}")
        st.markdown(f"Size = :orange[{machine_2_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_2_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_2}]")
        st.markdown(f"RPMS = :orange[{machine_2_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#2")
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


        st.subheader(f"Machine #3 | {machine_3_status}")
        st.markdown(f"Size = :orange[{machine_3_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_3_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_3}]")
        st.markdown(f"RPMS = :orange[{machine_3_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#3")
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


        st.subheader(f"Machine #4 | {machine_4_status}")
        st.markdown(f"Size = :orange[{machine_4_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_4_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_4}]")
        st.markdown(f"RPMS = :orange[{machine_4_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#4")
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


        st.subheader(f"Machine #5 | {machine_5_status}")
        st.markdown(f"Size = :orange[{machine_5_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_5_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_5}]")
        st.markdown(f"RPMS = :orange[{machine_5_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#5")
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


        st.subheader(f"Machine #6 | {machine_6_status}")
        st.markdown(f"Size = :orange[{machine_6_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_6_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_6}]")
        st.markdown(f"RPMS = :orange[{machine_6_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#6")
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


        st.subheader(f"Machine #7 | {machine_7_status}")
        st.markdown(f"Size = :orange[{machine_7_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_7_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_7}]")
        st.markdown(f"RPMS = :orange[{machine_7_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#7")
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


        st.subheader(f"Machine #8 | {machine_8_status}")
        st.markdown(f"Size = :orange[{machine_8_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_8_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_8}]")
        st.markdown(f"RPMS = :orange[{machine_8_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#8")
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


        st.subheader(f"Machine #9 | {machine_9_status}")
        st.markdown(f"Size = :orange[{machine_9_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_9_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_9}]")
        st.markdown(f"RPMS = :orange[{machine_9_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#9")
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


        st.subheader(f"Machine #10 | {machine_10_status}")
        st.markdown(f"Size = :orange[{machine_10_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_10_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_10}]")
        st.markdown(f"RPMS = :orange[{machine_10_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#10")
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


        st.subheader(f"Machine #11 | {machine_11_status}")
        st.markdown(f"Size = :orange[{machine_11_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_11_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_11}]")
        st.markdown(f"RPMS = :orange[{machine_11_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#11")
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


        st.subheader(f"Machine #12 | {machine_12_status}")
        st.markdown(f"Size = :orange[{machine_12_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_12_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_12}]")
        st.markdown(f"RPMS = :orange[{machine_12_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#12")
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


        st.subheader(f"Machine #13 | {machine_13_status}")
        st.markdown(f"Size = :orange[{machine_13_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_13_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_13}]")
        st.markdown(f"RPMS = :orange[{machine_13_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#13")
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


        st.subheader(f"Machine #14 | {machine_14_status}")
        st.markdown(f"Size = :orange[{machine_14_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_14_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_14}]")
        st.markdown(f"RPMS = :orange[{machine_14_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#14")
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


        st.subheader(f"Machine #15 | {machine_15_status}")
        st.markdown(f"Size = :orange[{machine_15_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_15_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_15}]")
        st.markdown(f"RPMS = :orange[{machine_15_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#15")
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


        st.subheader(f"Machine #16 | {machine_16_status}")
        st.markdown(f"Size = :orange[{machine_16_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_16_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_16}]")
        st.markdown(f"RPMS = :orange[{machine_16_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#16")
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


        st.subheader(f"Machine #17 | {machine_17_status}")
        st.markdown(f"Size = :orange[{machine_17_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_17_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_17}]")
        st.markdown(f"RPMS = :orange[{machine_17_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#17")
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


        st.subheader(f"Machine #18 | {machine_18_status}")
        st.markdown(f"Size = :orange[{machine_18_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_18_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_18}]")
        st.markdown(f"RPMS = :orange[{machine_18_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#18")
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


        st.subheader(f"Machine #19 | {machine_19_status}")
        st.markdown(f"Size = :orange[{machine_19_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_19_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_19}]")
        st.markdown(f"RPMS = :orange[{machine_19_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#19")
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


        st.subheader(f"Machine #20 | {machine_20_status}")
        st.markdown(f"Size = :orange[{machine_20_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_20_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_20}]")
        st.markdown(f"RPMS = :orange[{machine_20_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#20")
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


        st.subheader(f"Machine #21 | {machine_21_status}")
        st.markdown(f"Size = :orange[{machine_21_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_21_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_21}]")
        st.markdown(f"RPMS = :orange[{machine_21_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#21")
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


        st.subheader(f"Machine #22 | {machine_22_status}")
        st.markdown(f"Size = :orange[{machine_22_size}]")
        st.markdown(f"Yarn Type = :orange[{machine_22_yarn_type}]")
        st.markdown(f"DOFF = :orange[{machine_22}]")
        st.markdown(f"RPMS = :orange[{machine_22_rpms}]")
        machine_current_revs = st.text_input("Current REVS", "0", key="#22")
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


with tab2:
    options = st.selectbox(
        "You can view all the department machines information by selecting one of the options.",
        ("Machines Status", "Machines Fabric Size", "Machines Yarn Type"),
        index=None,
        placeholder="Select an option...",
        key="machines",
    )


    if options == "Machines Status":
        options = st.selectbox(
            "You can view which machines are operable or that are inoperable by selecting one of the options.",
            ("Operable", "Inoperable", "All 1-22"),
            index=None,
            placeholder="Select an option...",
            key="status",
        )


        if options == "Operable":
            st.caption(f"Total Operable Machines = :green[{total_operable}]")
            st.subheader(f"Machine #3 | {machine_3_status}")
            st.markdown(f"Size = :orange[{machine_3_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_3_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_3}]")
            st.markdown(f"RPMS = :orange[{machine_3_rpms}]")
            st.divider()
            st.subheader(f"Machine #4 | {machine_4_status}")
            st.markdown(f"Size = :orange[{machine_4_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_4_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_4}]")
            st.markdown(f"RPMS = :orange[{machine_4_rpms}]")
            st.divider()
            st.subheader(f"Machine #5 | {machine_5_status}")
            st.markdown(f"Size = :orange[{machine_5_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_5_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_5}]")
            st.markdown(f"RPMS = :orange[{machine_5_rpms}]")
            st.divider()
            st.subheader(f"Machine #6 | {machine_6_status}")
            st.markdown(f"Size = :orange[{machine_6_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_6_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_6}]")
            st.markdown(f"RPMS = :orange[{machine_6_rpms}]")
            st.divider()
            st.subheader(f"Machine #8 | {machine_8_status}")
            st.markdown(f"Size = :orange[{machine_8_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_8_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_8}]")
            st.markdown(f"RPMS = :orange[{machine_8_rpms}]")
            st.divider()
            st.subheader(f"Machine #9 | {machine_9_status}")
            st.markdown(f"Size = :orange[{machine_9_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_9_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_9}]")
            st.markdown(f"RPMS = :orange[{machine_9_rpms}]")
            st.divider()
            st.subheader(f"Machine #12 | {machine_12_status}")
            st.markdown(f"Size = :orange[{machine_12_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_12_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_12}]")
            st.markdown(f"RPMS = :orange[{machine_12_rpms}]")
            st.divider()
            st.subheader(f"Machine #13 | {machine_13_status}")
            st.markdown(f"Size = :orange[{machine_13_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_13_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_13}]")
            st.markdown(f"RPMS = :orange[{machine_13_rpms}]")
            st.divider()
            st.subheader(f"Machine #15 | {machine_15_status}")
            st.markdown(f"Size = :orange[{machine_15_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_15_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_15}]")
            st.markdown(f"RPMS = :orange[{machine_15_rpms}]")
            st.divider()
            st.subheader(f"Machine #16 | {machine_16_status}")
            st.markdown(f"Size = :orange[{machine_16_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_16_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_16}]")
            st.markdown(f"RPMS = :orange[{machine_16_rpms}]")
            st.divider()
            st.subheader(f"Machine #17 | {machine_17_status}")
            st.markdown(f"Size = :orange[{machine_17_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_17_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_17}]")
            st.markdown(f"RPMS = :orange[{machine_17_rpms}]")
            st.divider()
            st.subheader(f"Machine #18 | {machine_18_status}")
            st.markdown(f"Size = :orange[{machine_18_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_18_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_18}]")
            st.markdown(f"RPMS = :orange[{machine_18_rpms}]")
            st.divider()
            st.subheader(f"Machine #19 | {machine_19_status}")
            st.markdown(f"Size = :orange[{machine_19_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_19_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_19}]")
            st.markdown(f"RPMS = :orange[{machine_19_rpms}]")
            st.divider()
            st.subheader(f"Machine #20 | {machine_20_status}")
            st.markdown(f"Size = :orange[{machine_20_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_20_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_20}]")
            st.markdown(f"RPMS = :orange[{machine_20_rpms}]")
            st.divider()
            st.subheader(f"Machine #21 | {machine_21_status}")
            st.markdown(f"Size = :orange[{machine_21_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_21_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_21}]")
            st.markdown(f"RPMS = :orange[{machine_21_rpms}]")
            st.divider()
            st.subheader(f"Machine #22 | {machine_22_status}")
            st.markdown(f"Size = :orange[{machine_22_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_22_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_22}]")
            st.markdown(f"RPMS = :orange[{machine_22_rpms}]")


        elif options == "Inoperable":
            st.caption(f"Total Inoperable Machines = :red[{total_inoperable}]")
            st.subheader(f"Machine #1 | {machine_1_status}")
            st.markdown(f"Size = :orange[{machine_1_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_1_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_1}]")
            st.markdown(f"RPMS = :orange[{machine_1_rpms}]")
            st.divider()
            st.subheader(f"Machine #2 | {machine_2_status}")
            st.markdown(f"Size = :orange[{machine_2_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_2_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_2}]")
            st.markdown(f"RPMS = :orange[{machine_2_rpms}]")
            st.divider()
            st.subheader(f"Machine #7 | {machine_7_status}")
            st.markdown(f"Size = :orange[{machine_7_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_7_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_7}]")
            st.markdown(f"RPMS = :orange[{machine_7_rpms}]")
            st.divider()
            st.subheader(f"Machine #10 | {machine_10_status}")
            st.markdown(f"Size = :orange[{machine_10_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_10_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_10}]")
            st.markdown(f"RPMS = :orange[{machine_10_rpms}]")
            st.divider()
            st.subheader(f"Machine #11 | {machine_11_status}")
            st.markdown(f"Size = :orange[{machine_11_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_11_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_11}]")
            st.markdown(f"RPMS = :orange[{machine_11_rpms}]")
            st.divider()
            st.subheader(f"Machine #14 | {machine_14_status}")
            st.markdown(f"Size = :orange[{machine_14_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_14_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_14}]")
            st.markdown(f"RPMS = :orange[{machine_14_rpms}]")


        elif options == "All 1-22":
            st.caption(f"Total Inoperable Machines = :red[{total_inoperable}] Total Operable Machines = :green[{total_operable}]")
            st.subheader(f"Machine #1 | {machine_1_status}")
            st.markdown(f"Size = :orange[{machine_1_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_1_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_1}]")
            st.markdown(f"RPMS = :orange[{machine_1_rpms}]")
            st.divider()
            st.subheader(f"Machine #2 | {machine_2_status}")
            st.markdown(f"Size = :orange[{machine_2_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_2_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_2}]")
            st.markdown(f"RPMS = :orange[{machine_2_rpms}]")
            st.divider()
            st.subheader(f"Machine #3 | {machine_3_status}")
            st.markdown(f"Size = :orange[{machine_3_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_3_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_3}]")
            st.markdown(f"RPMS = :orange[{machine_3_rpms}]")
            st.divider()
            st.subheader(f"Machine #4 | {machine_4_status}")
            st.markdown(f"Size = :orange[{machine_4_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_4_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_4}]")
            st.markdown(f"RPMS = :orange[{machine_4_rpms}]")
            st.divider()
            st.subheader(f"Machine #5 | {machine_5_status}")
            st.markdown(f"Size = :orange[{machine_5_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_5_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_5}]")
            st.markdown(f"RPMS = :orange[{machine_5_rpms}]")
            st.divider()
            st.subheader(f"Machine #6 | {machine_6_status}")
            st.markdown(f"Size = :orange[{machine_6_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_6_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_6}]")
            st.markdown(f"RPMS = :orange[{machine_6_rpms}]")
            st.divider()
            st.subheader(f"Machine #7 | {machine_7_status}")
            st.markdown(f"Size = :orange[{machine_7_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_7_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_7}]")
            st.markdown(f"RPMS = :orange[{machine_7_rpms}]")
            st.divider()
            st.subheader(f"Machine #8 | {machine_8_status}")
            st.markdown(f"Size = :orange[{machine_8_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_8_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_8}]")
            st.markdown(f"RPMS = :orange[{machine_8_rpms}]")
            st.divider()
            st.subheader(f"Machine #9 | {machine_9_status}")
            st.markdown(f"Size = :orange[{machine_9_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_9_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_9}]")
            st.markdown(f"RPMS = :orange[{machine_9_rpms}]")
            st.divider()
            st.subheader(f"Machine #10 | {machine_10_status}")
            st.markdown(f"Size = :orange[{machine_10_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_10_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_10}]")
            st.markdown(f"RPMS = :orange[{machine_10_rpms}]")
            st.divider()
            st.subheader(f"Machine #11 | {machine_11_status}")
            st.markdown(f"Size = :orange[{machine_11_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_11_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_11}]")
            st.markdown(f"RPMS = :orange[{machine_11_rpms}]")
            st.divider()
            st.subheader(f"Machine #12 | {machine_12_status}")
            st.markdown(f"Size = :orange[{machine_12_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_12_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_12}]")
            st.markdown(f"RPMS = :orange[{machine_12_rpms}]")
            st.divider()
            st.subheader(f"Machine #13 | {machine_13_status}")
            st.markdown(f"Size = :orange[{machine_13_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_13_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_13}]")
            st.markdown(f"RPMS = :orange[{machine_13_rpms}]")
            st.divider()
            st.subheader(f"Machine #14 | {machine_14_status}")
            st.markdown(f"Size = :orange[{machine_14_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_14_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_14}]")
            st.markdown(f"RPMS = :orange[{machine_14_rpms}]")
            st.divider()
            st.subheader(f"Machine #15 | {machine_15_status}")
            st.markdown(f"Size = :orange[{machine_15_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_15_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_15}]")
            st.markdown(f"RPMS = :orange[{machine_15_rpms}]")
            st.divider()
            st.subheader(f"Machine #16 | {machine_16_status}")
            st.markdown(f"Size = :orange[{machine_16_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_16_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_16}]")
            st.markdown(f"RPMS = :orange[{machine_16_rpms}]")
            st.divider()
            st.subheader(f"Machine #17 | {machine_17_status}")
            st.markdown(f"Size = :orange[{machine_17_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_17_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_17}]")
            st.markdown(f"RPMS = :orange[{machine_17_rpms}]")
            st.divider()
            st.subheader(f"Machine #18 | {machine_18_status}")
            st.markdown(f"Size = :orange[{machine_18_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_18_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_18}]")
            st.markdown(f"RPMS = :orange[{machine_18_rpms}]")
            st.divider()
            st.subheader(f"Machine #19 | {machine_19_status}")
            st.markdown(f"Size = :orange[{machine_19_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_19_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_19}]")
            st.markdown(f"RPMS = :orange[{machine_19_rpms}]")
            st.divider()
            st.subheader(f"Machine #20 | {machine_20_status}")
            st.markdown(f"Size = :orange[{machine_20_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_20_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_20}]")
            st.markdown(f"RPMS = :orange[{machine_20_rpms}]")
            st.divider()
            st.subheader(f"Machine #21 | {machine_21_status}")
            st.markdown(f"Size = :orange[{machine_21_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_21_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_21}]")
            st.markdown(f"RPMS = :orange[{machine_21_rpms}]")
            st.divider()
            st.subheader(f"Machine #22 | {machine_22_status}")
            st.markdown(f"Size = :orange[{machine_22_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_22_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_22}]")
            st.markdown(f"RPMS = :orange[{machine_22_rpms}]")


    elif options == "Machines Fabric Size":
        options = st.selectbox(
            "You can view which machines produce which size by selecting one of the options.",
            ("King Fabric Machines", "Queen Fabric Machines", "Twin Fabric Machines"),
            index=None,
            placeholder="Select an option...",
            key="fabric",
        )


        if options == "King Fabric Machines":
            st.header("Currently Not Added...")


        elif options == "Queen Fabric Machines":
            st.header("Currently Not Added...")


        elif options == "Twin Fabric Machines":
            st.caption(f"Total Twin Machines = :orange[{total_twins}]")

            st.subheader(f"Machine #11 | {machine_11_status}")
            st.markdown(f"Size = :orange[{machine_11_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_11_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_11}]")
            st.markdown(f"RPMS = :orange[{machine_11_rpms}]")
            st.divider()


            st.subheader(f"Machine #12 | {machine_12_status}")
            st.markdown(f"Size = :orange[{machine_12_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_12_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_12}]")
            st.markdown(f"RPMS = :orange[{machine_12_rpms}]")
            st.divider()


            st.subheader(f"Machine #13 | {machine_13_status}")
            st.markdown(f"Size = :orange[{machine_13_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_13_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_13}]")
            st.markdown(f"RPMS = :orange[{machine_13_rpms}]")


    elif options == "Machines Yarn Type":
        options = st.selectbox(
            "You can view which machines use which yarn by selecting one of the options.",
            ("Black&White Machines", "Pink&Black Machines", "Horse Head Machines"),
            index=None,
            placeholder="Select an option...",
            key="yarn",
        )


        if options == "Black&White Machines":
            st.caption(f"Total Black&White Machines = :orange[{total_white}]")
            st.subheader(f"Machine #3 | {machine_3_status}")
            st.markdown(f"Size = :orange[{machine_3_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_3_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_3}]")
            st.markdown(f"RPMS = :orange[{machine_3_rpms}]")
            st.divider()

            st.subheader(f"Machine #5 | {machine_5_status}")
            st.markdown(f"Size = :orange[{machine_5_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_5_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_5}]")
            st.markdown(f"RPMS = :orange[{machine_5_rpms}]")
            st.divider()

            st.subheader(f"Machine #6 | {machine_6_status}")
            st.markdown(f"Size = :orange[{machine_6_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_6_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_6}]")
            st.markdown(f"RPMS = :orange[{machine_6_rpms}]")
            st.divider()

            st.subheader(f"Machine #7 | {machine_7_status}")
            st.markdown(f"Size = :orange[{machine_7_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_7_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_7}]")
            st.markdown(f"RPMS = :orange[{machine_7_rpms}]")
            st.divider()

            st.subheader(f"Machine #11 | {machine_11_status}")
            st.markdown(f"Size = :orange[{machine_11_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_11_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_11}]")
            st.markdown(f"RPMS = :orange[{machine_11_rpms}]")
            st.divider()

            st.subheader(f"Machine #15 | {machine_15_status}")
            st.markdown(f"Size = :orange[{machine_15_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_15_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_15}]")
            st.markdown(f"RPMS = :orange[{machine_15_rpms}]")
            st.divider()


            st.subheader(f"Machine #16 | {machine_16_status}")
            st.markdown(f"Size = :orange[{machine_16_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_16_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_16}]")
            st.markdown(f"RPMS = :orange[{machine_16_rpms}]")
            st.divider()

            st.subheader(f"Machine #19 | {machine_19_status}")
            st.markdown(f"Size = :orange[{machine_19_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_19_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_19}]")
            st.markdown(f"RPMS = :orange[{machine_19_rpms}]")


        elif options == "Pink&Black Machines":
            st.caption(f"Total Pink&Black Machines = :orange[{total_pink}]")
            st.subheader(f"Machine #17 | {machine_17_status}")
            st.markdown(f"Size = :orange[{machine_17_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_17_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_17}]")
            st.markdown(f"RPMS = :orange[{machine_17_rpms}]")
            st.divider()


            st.subheader(f"Machine #18 | {machine_18_status}")
            st.markdown(f"Size = :orange[{machine_18_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_18_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_18}]")
            st.markdown(f"RPMS = :orange[{machine_18_rpms}]")
            st.divider()

            st.subheader(f"Machine #20 | {machine_20_status}")
            st.markdown(f"Size = :orange[{machine_20_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_20_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_20}]")
            st.markdown(f"RPMS = :orange[{machine_20_rpms}]")
            st.divider()


            st.subheader(f"Machine #21 | {machine_21_status}")
            st.markdown(f"Size = :orange[{machine_21_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_21_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_21}]")
            st.markdown(f"RPMS = :orange[{machine_21_rpms}]")
            st.divider()


            st.subheader(f"Machine #22 | {machine_22_status}")
            st.markdown(f"Size = :orange[{machine_22_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_22_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_22}]")
            st.markdown(f"RPMS = :orange[{machine_22_rpms}]")


        elif options == "Horse Head Machines":
            st.caption(f"Total Horse Head Machines = :orange[{total_horse}]")
            st.subheader(f"Machine #4 | {machine_4_status}")
            st.markdown(f"Size = :orange[{machine_4_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_4_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_4}]")
            st.markdown(f"RPMS = :orange[{machine_4_rpms}]")
            st.divider()

            st.subheader(f"Machine #8 | {machine_8_status}")
            st.markdown(f"Size = :orange[{machine_8_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_8_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_8}]")
            st.markdown(f"RPMS = :orange[{machine_8_rpms}]")
            st.divider()


            st.subheader(f"Machine #9 | {machine_9_status}")
            st.markdown(f"Size = :orange[{machine_9_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_9_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_9}]")
            st.markdown(f"RPMS = :orange[{machine_9_rpms}]")
            st.divider()

            st.subheader(f"Machine #12 | {machine_12_status}")
            st.markdown(f"Size = :orange[{machine_12_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_12_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_12}]")
            st.markdown(f"RPMS = :orange[{machine_12_rpms}]")
            st.divider()


            st.subheader(f"Machine #13 | {machine_13_status}")
            st.markdown(f"Size = :orange[{machine_13_size}]")
            st.markdown(f"Yarn Type = :orange[{machine_13_yarn_type}]")
            st.markdown(f"DOFF = :orange[{machine_13}]")
            st.markdown(f"RPMS = :orange[{machine_13_rpms}]")
