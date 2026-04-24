import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="torchOS", page_icon="🔥", layout="wide")
st.title("🔥 torchOS")
st.caption("Justin's Life Synthesizer • One screen to rule it all")

# Top-level Tabs (instead of sidebar dropdown)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Dashboard", 
    "💼 Work", 
    "🏠 Personal", 
    "🧠 Ideas Lab", 
    "🧭 Life Coach", 
    "🔌 Integrations"
])

# ====================== DASHBOARD ======================
with tab1:
    st.header(f"Good afternoon, Justin — {datetime.now().strftime('%A, %B %d')}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Active Support Cases", "47", "↓12")
    with col2:
        st.metric("Team PTO Remaining", "184 days", "↑8")
    with col3:
        st.metric("Bills Due This Week", "$2,847", "3 due")
    with col4:
        st.metric("Tesla Range", "287 mi", "Charge soon")

    st.divider()
    st.subheader("This Week Snapshot")
    st.write("📅 **Mon** — IT sync • Salesforce review • AI team")
    st.write("📅 **Tue** — Capital One payment • Tesla reminder")
    st.write("📅 **Wed** — Economic Ninja new video?")

# ====================== WORK ======================
with tab2:
    st.header("💼 Work Pulse")
    
    # Sub-tabs inside Work
    wtab1, wtab2, wtab3, wtab4 = st.tabs([
        "📊 Core Metrics", 
        "👥 Staff & People", 
        "📅 Schedule", 
        "🔗 Systems"
    ])
    
    with wtab1:
        st.subheader("Support Case Metrics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("IT Support", "18 active", "↓5")
        with col2:
            st.metric("Salesforce", "21 active", "↑3")
        with col3:
            st.metric("AI Team", "8 active", "↓4")
        
        st.success("All teams under control — nice work")

    with wtab2:
        st.subheader("👥 Staff / People — Time Bank (Paylocity)")
        st.write("Vacation / PTO balances")
        
        pto_data = pd.DataFrame({
            "Employee": ["Sarah Chen", "Mike Torres", "Priya Patel", "Alex Rivera"],
            "Role": ["IT Support Lead", "Salesforce Admin", "AI Engineer", "Junior Analyst"],
            "PTO Remaining": [22, 15, 28, 19],
            "Sick Hours": [48, 62, 35, 55],
            "Last Used": ["Apr 18", "Apr 22", "Mar 30", "Apr 15"]
        })
        
        st.dataframe(pto_data, use_container_width=True, hide_index=True)
        
        st.metric("Total Team PTO Bank", "184 days", "↑8 this month")

    with wtab3:
        st.subheader("This Week's Schedule")
        st.write("📍 Key meetings and blockers")
        schedule = pd.DataFrame({
            "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "Events": [
                "9am IT Sync • 11am Salesforce • 2pm AI Standup",
                "Capital One Expense Review • 1:1 with Boss",
                "Team Offsite Planning",
                "Quarterly Review Prep",
                "Light day — focus block"
            ]
        })
        st.dataframe(schedule, use_container_width=True, hide_index=True)

    with wtab4:
        st.subheader("Connected Systems")
        st.write("Salesforce • Auvik • O365 • Slack • 8x8 • SAP Concur • Qualcomm Insight")
        st.info("We'll wire these in one by one")

# ====================== PERSONAL ======================
with tab3:
    st.header("🏠 Personal Pulse")
    st.write("Gmail • Calendar • Bills • Capital One • Chase • Tesla • Subscriptions • Plaud notes")
    st.success("Ready for manual + CSV for now")

# ====================== IDEAS LAB ======================
with tab4:
    st.header("🧠 Ideas Lab — First Principles Mode")
    idea = st.text_area("Brain dump raw thoughts here", height=400, placeholder="What if we...")
    if st.button("🔥 Break it down to First Principles"):
        st.markdown("**First Principles Refactor:**")
        st.write("• Strip away all assumptions")
        st.write("• What is the fundamental truth?")
        st.write("• Rebuild the best possible version")
        st.success("Thinking leveled up.")

# ====================== LIFE COACH ======================
with tab5:
    st.header("🧭 Life Coach — Blunt & First-Principles")
    question = st.text_area("What's on your mind right now?", "How am I doing overall?")
    if st.button("Give me the real talk"):
        st.markdown("**Coach says:**")
        st.write("You're carrying a lot across work and personal. First principle: **Energy is finite and compounds**. Biggest leak right now looks like context switching between too many tools. Recommendation: Kill or delegate one recurring low-value meeting this week and clear two personal renewals. Protect your focus blocks.")
        st.caption("— torchOS Coach")

# ====================== INTEGRATIONS ======================
with tab6:
    st.header("🔌 Integrations")
    st.write("O365, Salesforce, Paylocity, Gmail, YouTube, Plaud, Banks, etc.")
    st.success("O365 Email/Calendar page coming in next update")

st.caption("torchOS v0.3 • UI upgraded with your feedback")
