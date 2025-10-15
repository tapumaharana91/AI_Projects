import streamlit as st
import pandas as pd
from datetime import datetime
from src.database import log_intake, get_intake_history
from src.agent import waterIntakeAgent

if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False


# Welcome section
if not st.session_state.tracker_started:
    st.title("💧 Water Intake Tracker")
    st.markdown("""Track your daily water intake with AI assistant.
                Log your intake, get smart feedback and stay hydrated!
                """)
    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()

else:
    st.title("💧 Water Intake Tracker")

    # Sidebar for user Intake input
    st.sidebar.header("Log Water Intake")
    user_id=st.sidebar.text_input("User ID", value="user_1")
    intake_ml=st.sidebar.number_input("Water Intake (ml)",min_value=0,step=100)

    if st.sidebar.button("Submit"):
        if user_id and intake_ml:
            log_intake(user_id,intake_ml)
            st.success(f"Logged {intake_ml} ml for {user_id}")


            agent=waterIntakeAgent()
            feedback=agent.analyze_intake(intake_ml)
            st.info(f"AI Feedback: {feedback}")
    
    # Divider
    st.markdown("---")

    # History Section
    st.header("Your Water Intake History")
    
    if user_id:
        history=get_intake_history(user_id)
        if history:
            dates=[datetime.strptime(row[1], "%Y-%m-%d") for row in history]
            values=[row[0] for row in history]

            df=pd.DataFrame(
                {
                    "Date": dates,
                    "Water Intake (ml)": values
                }
            )

            st.dataframe(df)
            st.line_chart(df, x="Date", y="Water Intake (ml)", use_container_width=True)
        else:
            st.warning("No intake history found. Log some water intake!")



