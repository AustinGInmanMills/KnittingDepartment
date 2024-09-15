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

machine_1 = 1600
machine_1_rpms = 15
machine_1_yarn_type = "N/A"
machine_1_status = ":red[Status: Inoperable]"

machine_2 = 1600
machine_2_rpms = 15
machine_2_yarn_type = "N/A"
machine_2_status = ":red[Status: Inoperable]"

machine_3 = 1800
machine_3_rpms = 10
machine_3_yarn_type = "Black&White Cone"
machine_3_status = ":green[Status: Operable]"

machine_4 = 1600
machine_4_rpms = 10
machine_4_yarn_type = "Horse Head Cone"
machine_4_status = ":green[Status: Operable]"

machine_5 = 1800
machine_5_rpms = 11
machine_5_yarn_type = "Black&White Cone"
machine_5_status = ":green[Status: Operable]"

machine_6 = 1600
machine_6_rpms = 15
machine_6_yarn_type = "Black&White Cone"
machine_6_status = ":green[Status: Operable]"

machine_7 = 1600
machine_7_rpms = 15
machine_7_yarn_type = "Black&White Cone"
machine_7_status = ":red[Status: Inoperable]"

machine_8 = 1400
machine_8_rpms = 8
machine_8_yarn_type = "Horse Head Cone"
machine_8_status = ":green[Status: Operable]"

machine_9 = 1400
machine_9_rpms = 10
machine_9_yarn_type = "Horse Head Cone"
machine_9_status = ":green[Status: Operable]"

machine_10 = 1600
machine_10_rpms = 15
machine_10_yarn_type = "N/A"
machine_10_status = ":red[Status: Inoperable]"

machine_11 = 1600
machine_11_rpms = 15
machine_11_yarn_type = "Black&White Cone"
machine_11_status = ":red[Status: Inoperable]"

machine_12 = 2800
machine_12_rpms = 8
machine_12_yarn_type = "Horse Head Cone"
machine_12_status = ":green[Status: Operable]"

machine_13 = 2800
machine_13_rpms = 12
machine_13_yarn_type = "Horse Head Cone"
machine_13_status = ":green[Status: Operable]"

machine_14 = 1600
machine_14_rpms = 15
machine_14_yarn_type = "N/A"
machine_14_status = ":red[Status: Inoperable]"

machine_15 = 1600
machine_15_rpms = 15
machine_15_yarn_type = "Black&White Cone"
machine_15_status = ":green[Status: Operable]"

machine_16 = 1600
machine_16_rpms = 15
machine_16_yarn_type = "Black&White Cone"
machine_16_status = ":green[Status: Operable]"

machine_17 = 1600
machine_17_rpms = 10
machine_17_yarn_type = "Pink&Black Cone"
machine_17_status = ":green[Status: Operable]"

machine_18 = 1600
machine_18_rpms = 8
machine_18_yarn_type = "Pink&Black Cone"
machine_18_status = ":green[Status: Operable]"

machine_19 = 1600
machine_19_rpms = 15
machine_19_yarn_type = "Black&White Cone"
machine_19_status = ":green[Status: Operable]"

machine_20 = 1600
machine_20_rpms = 8
machine_20_yarn_type = "Pink&Black Cone"
machine_20_status = ":green[Status: Operable]"

machine_21 = 1600
machine_21_rpms = 8
machine_21_yarn_type = "Pink&Black Cone"
machine_21_status = ":green[Status: Operable]"

machine_22 = 1600
machine_22_rpms = 15
machine_22_yarn_type = "Pink&Black Cone"
machine_22_status = ":green[Status: Operable]"















st.header("Knitting Department Multi Tool", divider="red")







tab1, tab2, = st.tabs(["Doff Time Calculator", "Machines Information"])











with tab1:
    options = st.selectbox(
        "You can calculate how long a machine has left till it doffs by selecting one of the options.",
        ("Machine #1", "Machine #2", "Machine #3", "Machine #4", "Machine #5", "Machine #6", "Machine #7", "Machine #8", "Machine #9",
         "Machine #10", "Machine #11", "Machine #12", "Machine #13", "Machine #14", "Machine #15", "Machine #16", "Machine #17", "Machine #18",
         "Machine #19", "Machine #20", "Machine #21", "Machine #22",),
        index=None,
        placeholder="Select an option...",
        key="calculator",
    )

    if options == "Machine #1":
        st.subheader(f"Machine #1 | {machine_1_status}")
        st.markdown(f"Yarn Type = :green[{machine_1_yarn_type}]")
        st.write("DOFF = ", int(machine_1))
        st.write("RPMS = ", int(machine_1_rpms))
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

    elif options == "Machine #2":
        st.subheader(f"Machine #2 | {machine_2_status}")
        st.markdown(f"Yarn Type = :green[{machine_2_yarn_type}]")
        st.write("DOFF = ", int(machine_2))
        st.write("RPMS = ", int(machine_2_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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

    elif options == "Machine #3":
        st.subheader(f"Machine #3 | {machine_3_status}")
        st.markdown(f"Yarn Type = :green[{machine_3_yarn_type}]")
        st.write("DOFF = ", int(machine_3))
        st.write("RPMS = ", int(machine_3_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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

    elif options == "Machine #4":
        st.subheader(f"Machine #4 | {machine_4_status}")
        st.markdown(f"Yarn Type = :green[{machine_4_yarn_type}]")
        st.write("DOFF = ", int(machine_4))
        st.write("RPMS = ", int(machine_4_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #5":
        st.subheader(f"Machine #5 | {machine_5_status}")
        st.markdown(f"Yarn Type = :green[{machine_5_yarn_type}]")
        st.write("DOFF = ", int(machine_5))
        st.write("RPMS = ", int(machine_5_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #6":
        st.subheader(f"Machine #6 | {machine_6_status}")
        st.markdown(f"Yarn Type = :green[{machine_6_yarn_type}]")
        st.write("DOFF = ", int(machine_6))
        st.write("RPMS = ", int(machine_6_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #7":
        st.subheader(f"Machine #7 | {machine_7_status}")
        st.markdown(f"Yarn Type = :green[{machine_7_yarn_type}]")
        st.write("DOFF = ", int(machine_7))
        st.write("RPMS = ", int(machine_7_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #8":
        st.subheader(f"Machine #8 | {machine_8_status}")
        st.markdown(f"Yarn Type = :green[{machine_8_yarn_type}]")
        st.write("DOFF = ", int(machine_8))
        st.write("RPMS = ", int(machine_8_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #9":
        st.subheader(f"Machine #9 | {machine_9_status}")
        st.markdown(f"Yarn Type = :green[{machine_9_yarn_type}]")
        st.write("DOFF = ", int(machine_9))
        st.write("RPMS = ", int(machine_9_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #10":
        st.subheader(f"Machine #10 | {machine_10_status}")
        st.markdown(f"Yarn Type = :green[{machine_10_yarn_type}]")
        st.write("DOFF = ", int(machine_10))
        st.write("RPMS = ", int(machine_10_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #11":
        st.subheader(f"Machine #11 | {machine_11_status}")
        st.markdown(f"Yarn Type = :green[{machine_11_yarn_type}]")
        st.write("DOFF = ", int(machine_11))
        st.write("RPMS = ", int(machine_11_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #12":
        st.subheader(f"Machine #12 | {machine_12_status}")
        st.markdown(f"Yarn Type = :green[{machine_12_yarn_type}]")
        st.write("DOFF = ", int(machine_12))
        st.write("RPMS = ", int(machine_12_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #13":
        st.subheader(f"Machine #13 | {machine_13_status}")
        st.markdown(f"Yarn Type = :green[{machine_13_yarn_type}]")
        st.write("DOFF = ", int(machine_13))
        st.write("RPMS = ", int(machine_13_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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



    elif options == "Machine #14":
        st.subheader(f"Machine #14 | {machine_14_status}")
        st.markdown(f"Yarn Type = :green[{machine_14_yarn_type}]")
        st.write("DOFF = ", int(machine_14))
        st.write("RPMS = ", int(machine_14_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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



    elif options == "Machine #15":
        st.subheader(f"Machine #15 | {machine_15_status}")
        st.markdown(f"Yarn Type = :green[{machine_15_yarn_type}]")
        st.write("DOFF = ", int(machine_15))
        st.write("RPMS = ", int(machine_15_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #16":
        st.subheader(f"Machine #16 | {machine_16_status}")
        st.markdown(f"Yarn Type = :green[{machine_16_yarn_type}]")
        st.write("DOFF = ", int(machine_16))
        st.write("RPMS = ", int(machine_16_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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

    elif options == "Machine #17":
        st.subheader(f"Machine #17 | {machine_17_status}")
        st.markdown(f"Yarn Type = :green[{machine_17_yarn_type}]")
        st.write("DOFF = ", int(machine_17))
        st.write("RPMS = ", int(machine_17_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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

    elif options == "Machine #18":
        st.subheader(f"Machine #18 | {machine_18_status}")
        st.markdown(f"Yarn Type = :green[{machine_18_yarn_type}]")
        st.write("DOFF = ", int(machine_18))
        st.write("RPMS = ", int(machine_18_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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

    elif options == "Machine #19":
        st.subheader(f"Machine #19 | {machine_19_status}")
        st.markdown(f"Yarn Type = :green[{machine_19_yarn_type}]")
        st.write("DOFF = ", int(machine_19))
        st.write("RPMS = ", int(machine_19_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #20":
        st.subheader(f"Machine #20 | {machine_20_status}")
        st.markdown(f"Yarn Type = :green[{machine_20_yarn_type}]")
        st.write("DOFF = ", int(machine_20))
        st.write("RPMS = ", int(machine_20_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #21":
        st.subheader(f"Machine #21 | {machine_21_status}")
        st.markdown(f"Yarn Type = :green[{machine_21_yarn_type}]")
        st.write("DOFF = ", int(machine_21))
        st.write("RPMS = ", int(machine_21_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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


    elif options == "Machine #22":
        st.subheader(f"Machine #22 | {machine_22_status}")
        st.markdown(f"Yarn Type = :green[{machine_22_yarn_type}]")
        st.write("DOFF = ", int(machine_22))
        st.write("RPMS = ", int(machine_22_rpms))
        machine_current_revs = st.text_input("Current REVS", "0", key="#1")
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
        ("Machines Status", "Machines Fabric Size", "Machines Yarn Type", "Machines Doff Revs"),
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
            st.markdown(f"Yarn Type = :green[{machine_3_yarn_type}]")
            st.write("DOFF = ", int(machine_3))
            st.write("RPMS = ", int(machine_3_rpms))
            st.divider()
            st.subheader(f"Machine #4 | {machine_4_status}")
            st.markdown(f"Yarn Type = :green[{machine_4_yarn_type}]")
            st.write("DOFF = ", int(machine_4))
            st.write("RPMS = ", int(machine_4_rpms))
            st.divider()
            st.subheader(f"Machine #5 | {machine_5_status}")
            st.markdown(f"Yarn Type = :green[{machine_5_yarn_type}]")
            st.write("DOFF = ", int(machine_5))
            st.write("RPMS = ", int(machine_5_rpms))
            st.divider()
            st.subheader(f"Machine #6 | {machine_6_status}")
            st.markdown(f"Yarn Type = :green[{machine_6_yarn_type}]")
            st.write("DOFF = ", int(machine_6))
            st.write("RPMS = ", int(machine_6_rpms))
            st.divider()
            st.subheader(f"Machine #8 | {machine_8_status}")
            st.markdown(f"Yarn Type = :green[{machine_8_yarn_type}]")
            st.write("DOFF = ", int(machine_8))
            st.write("RPMS = ", int(machine_8_rpms))
            st.divider()
            st.subheader(f"Machine #9 | {machine_9_status}")
            st.markdown(f"Yarn Type = :green[{machine_9_yarn_type}]")
            st.write("DOFF = ", int(machine_9))
            st.write("RPMS = ", int(machine_9_rpms))
            st.divider()
            st.subheader(f"Machine #12 | {machine_12_status}")
            st.markdown(f"Yarn Type = :green[{machine_12_yarn_type}]")
            st.write("DOFF = ", int(machine_12))
            st.write("RPMS = ", int(machine_12_rpms))
            st.divider()
            st.subheader(f"Machine #13 | {machine_13_status}")
            st.markdown(f"Yarn Type = :green[{machine_13_yarn_type}]")
            st.write("DOFF = ", int(machine_13))
            st.write("RPMS = ", int(machine_13_rpms))
            st.divider()
            st.subheader(f"Machine #15 | {machine_15_status}")
            st.markdown(f"Yarn Type = :green[{machine_15_yarn_type}]")
            st.write("DOFF = ", int(machine_15))
            st.write("RPMS = ", int(machine_15_rpms))
            st.divider()
            st.subheader(f"Machine #16 | {machine_16_status}")
            st.markdown(f"Yarn Type = :green[{machine_16_yarn_type}]")
            st.write("DOFF = ", int(machine_16))
            st.write("RPMS = ", int(machine_16_rpms))
            st.divider()
            st.subheader(f"Machine #17 | {machine_17_status}")
            st.markdown(f"Yarn Type = :green[{machine_17_yarn_type}]")
            st.write("DOFF = ", int(machine_17))
            st.write("RPMS = ", int(machine_17_rpms))
            st.divider()
            st.subheader(f"Machine #18 | {machine_18_status}")
            st.markdown(f"Yarn Type = :green[{machine_18_yarn_type}]")
            st.write("DOFF = ", int(machine_18))
            st.write("RPMS = ", int(machine_18_rpms))
            st.divider()
            st.subheader(f"Machine #19 | {machine_19_status}")
            st.markdown(f"Yarn Type = :green[{machine_19_yarn_type}]")
            st.write("DOFF = ", int(machine_19))
            st.write("RPMS = ", int(machine_19_rpms))
            st.divider()
            st.subheader(f"Machine #20 | {machine_20_status}")
            st.markdown(f"Yarn Type = :green[{machine_20_yarn_type}]")
            st.write("DOFF = ", int(machine_20))
            st.write("RPMS = ", int(machine_20_rpms))
            st.divider()
            st.subheader(f"Machine #21 | {machine_21_status}")
            st.markdown(f"Yarn Type = :green[{machine_21_yarn_type}]")
            st.write("DOFF = ", int(machine_21))
            st.write("RPMS = ", int(machine_21_rpms))
            st.divider()
            st.subheader(f"Machine #22 | {machine_22_status}")
            st.markdown(f"Yarn Type = :green[{machine_22_yarn_type}]")
            st.write("DOFF = ", int(machine_22))
            st.write("RPMS = ", int(machine_22_rpms))
        elif options == "Inoperable":
            st.caption(f"Total Inoperable Machines = :red[{total_inoperable}]")
            st.subheader(f"Machine #1 | {machine_1_status}")
            st.markdown(f"Yarn Type = :green[{machine_1_yarn_type}]")
            st.write("DOFF = ", int(machine_1))
            st.write("RPMS = ", int(machine_1_rpms))
            st.divider()
            st.subheader(f"Machine #2 | {machine_2_status}")
            st.markdown(f"Yarn Type = :green[{machine_2_yarn_type}]")
            st.write("DOFF = ", int(machine_2))
            st.write("RPMS = ", int(machine_2_rpms))
            st.divider()
            st.subheader(f"Machine #7 | {machine_7_status}")
            st.markdown(f"Yarn Type = :green[{machine_7_yarn_type}]")
            st.write("DOFF = ", int(machine_7))
            st.write("RPMS = ", int(machine_7_rpms))
            st.divider()
            st.subheader(f"Machine #10 | {machine_10_status}")
            st.markdown(f"Yarn Type = :green[{machine_10_yarn_type}]")
            st.write("DOFF = ", int(machine_10))
            st.write("RPMS = ", int(machine_10_rpms))
            st.divider()
            st.subheader(f"Machine #11 | {machine_11_status}")
            st.markdown(f"Yarn Type = :green[{machine_11_yarn_type}]")
            st.write("DOFF = ", int(machine_11))
            st.write("RPMS = ", int(machine_11_rpms))
            st.divider()
            st.subheader(f"Machine #14 | {machine_14_status}")
            st.markdown(f"Yarn Type = :green[{machine_14_yarn_type}]")
            st.write("DOFF = ", int(machine_14))
            st.write("RPMS = ", int(machine_14_rpms))
        elif options == "All 1-22":
            st.caption(f"Total Inoperable Machines = :red[{total_inoperable}] Total Operable Machines = :green[{total_operable}]")
            st.subheader(f"Machine #1 | {machine_1_status}")
            st.markdown(f"Yarn Type = :green[{machine_1_yarn_type}]")
            st.write("DOFF = ", int(machine_1))
            st.write("RPMS = ", int(machine_1_rpms))
            st.divider()
            st.subheader(f"Machine #2 | {machine_2_status}")
            st.markdown(f"Yarn Type = :green[{machine_2_yarn_type}]")
            st.write("DOFF = ", int(machine_2))
            st.write("RPMS = ", int(machine_2_rpms))
            st.divider()
            st.subheader(f"Machine #3 | {machine_3_status}")
            st.markdown(f"Yarn Type = :green[{machine_3_yarn_type}]")
            st.write("DOFF = ", int(machine_3))
            st.write("RPMS = ", int(machine_3_rpms))
            st.divider()
            st.subheader(f"Machine #4 | {machine_4_status}")
            st.markdown(f"Yarn Type = :green[{machine_4_yarn_type}]")
            st.write("DOFF = ", int(machine_4))
            st.write("RPMS = ", int(machine_4_rpms))
            st.divider()
            st.subheader(f"Machine #5 | {machine_5_status}")
            st.markdown(f"Yarn Type = :green[{machine_5_yarn_type}]")
            st.write("DOFF = ", int(machine_5))
            st.write("RPMS = ", int(machine_5_rpms))
            st.divider()
            st.subheader(f"Machine #6 | {machine_6_status}")
            st.markdown(f"Yarn Type = :green[{machine_6_yarn_type}]")
            st.write("DOFF = ", int(machine_6))
            st.write("RPMS = ", int(machine_6_rpms))
            st.divider()
            st.subheader(f"Machine #7 | {machine_7_status}")
            st.markdown(f"Yarn Type = :green[{machine_7_yarn_type}]")
            st.write("DOFF = ", int(machine_7))
            st.write("RPMS = ", int(machine_7_rpms))
            st.divider()
            st.subheader(f"Machine #8 | {machine_8_status}")
            st.markdown(f"Yarn Type = :green[{machine_8_yarn_type}]")
            st.write("DOFF = ", int(machine_8))
            st.write("RPMS = ", int(machine_8_rpms))
            st.divider()
            st.subheader(f"Machine #9 | {machine_9_status}")
            st.markdown(f"Yarn Type = :green[{machine_9_yarn_type}]")
            st.write("DOFF = ", int(machine_9))
            st.write("RPMS = ", int(machine_9_rpms))
            st.divider()
            st.subheader(f"Machine #10 | {machine_10_status}")
            st.markdown(f"Yarn Type = :green[{machine_10_yarn_type}]")
            st.write("DOFF = ", int(machine_10))
            st.write("RPMS = ", int(machine_10_rpms))
            st.divider()
            st.subheader(f"Machine #11 | {machine_11_status}")
            st.markdown(f"Yarn Type = :green[{machine_11_yarn_type}]")
            st.write("DOFF = ", int(machine_11))
            st.write("RPMS = ", int(machine_11_rpms))
            st.divider()
            st.subheader(f"Machine #12 | {machine_12_status}")
            st.markdown(f"Yarn Type = :green[{machine_12_yarn_type}]")
            st.write("DOFF = ", int(machine_12))
            st.write("RPMS = ", int(machine_12_rpms))
            st.divider()
            st.subheader(f"Machine #13 | {machine_13_status}")
            st.markdown(f"Yarn Type = :green[{machine_13_yarn_type}]")
            st.write("DOFF = ", int(machine_13))
            st.write("RPMS = ", int(machine_13_rpms))
            st.divider()
            st.subheader(f"Machine #14 | {machine_14_status}")
            st.markdown(f"Yarn Type = :green[{machine_14_yarn_type}]")
            st.write("DOFF = ", int(machine_14))
            st.write("RPMS = ", int(machine_14_rpms))
            st.divider()
            st.subheader(f"Machine #15 | {machine_15_status}")
            st.markdown(f"Yarn Type = :green[{machine_15_yarn_type}]")
            st.write("DOFF = ", int(machine_15))
            st.write("RPMS = ", int(machine_15_rpms))
            st.divider()
            st.subheader(f"Machine #16 | {machine_16_status}")
            st.markdown(f"Yarn Type = :green[{machine_16_yarn_type}]")
            st.write("DOFF = ", int(machine_16))
            st.write("RPMS = ", int(machine_16_rpms))
            st.divider()
            st.subheader(f"Machine #17 | {machine_17_status}")
            st.markdown(f"Yarn Type = :green[{machine_17_yarn_type}]")
            st.write("DOFF = ", int(machine_17))
            st.write("RPMS = ", int(machine_17_rpms))
            st.divider()
            st.subheader(f"Machine #18 | {machine_18_status}")
            st.markdown(f"Yarn Type = :green[{machine_18_yarn_type}]")
            st.write("DOFF = ", int(machine_18))
            st.write("RPMS = ", int(machine_18_rpms))
            st.divider()
            st.subheader(f"Machine #19 | {machine_19_status}")
            st.markdown(f"Yarn Type = :green[{machine_19_yarn_type}]")
            st.write("DOFF = ", int(machine_19))
            st.write("RPMS = ", int(machine_19_rpms))
            st.divider()
            st.subheader(f"Machine #20 | {machine_20_status}")
            st.markdown(f"Yarn Type = :green[{machine_20_yarn_type}]")
            st.write("DOFF = ", int(machine_20))
            st.write("RPMS = ", int(machine_20_rpms))
            st.divider()
            st.subheader(f"Machine #21 | {machine_21_status}")
            st.markdown(f"Yarn Type = :green[{machine_21_yarn_type}]")
            st.write("DOFF = ", int(machine_21))
            st.write("RPMS = ", int(machine_21_rpms))
            st.divider()
            st.subheader(f"Machine #22 | {machine_22_status}")
            st.markdown(f"Yarn Type = :green[{machine_22_yarn_type}]")
            st.write("DOFF = ", int(machine_22))
            st.write("RPMS = ", int(machine_22_rpms))
