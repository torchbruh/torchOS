import streamlit as st
from datetime import datetime

st.set_page_config(page_title="torchOS", page_icon="🔥", layout="wide")
st.title("🔥 torchOS")
st.caption("Your life, synthesized • Justin's personal OS")

# Sidebar
page = st.sidebar.selectbox(
    "Navigate your life",
    ["Dashboard", "Work Pulse", "Personal Pulse", "Ideas Lab", "Life Coach", "Integrations"]
)

if page == "Dashboard":
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

    st.divider()
    st.subheader("📺 Economic Ninja Latest")
    st.info("🔌 YouTube connection coming in the next version (once we move to local or add requirements properly)")

elif page == "Work Pulse":
    st.header("💼 Work Pulse")
    st.success("Salesforce • Auvik • O365 • Slack • 8x8 • SAP Concur • Qualcomm Insight")
    st.write("All your work dashboards will live here.")

elif page == "Personal Pulse":
    st.header("🏠 Personal Pulse")
    st.write("Gmail • Calendar • Capital One • Chase • Tesla • Subscriptions • Plaud notes")
    st.success("Ready for manual entry or CSV uploads for now.")

elif page == "Ideas Lab":
    st.header("🧠 Ideas Lab — First Principles Mode")
    idea = st.text_area("Brain dump raw thoughts here (no filter)", height=400, placeholder="What if we...")
    if st.button("🔥 Break it down to First Principles"):
        st.markdown("**First Principles Refactor:**")
        st.write("• Strip away all assumptions and analogies")
        st.write("• What is the fundamental truth?")
        st.write("• Rebuild the best possible version from there.")
        st.success("Thinking leveled up.")

elif page == "Life Coach":
    st.header("🧭 Life Coach — Blunt & First-Principles")
    question = st.text_area("What's on your mind?", "How am I doing overall right now?")
    if st.button("Give me the real talk"):
        st.markdown("**Coach says:**")
        st.write("You're carrying a lot of context switching right now. First principle: **Energy compounds**. Your biggest leak is probably too many tools and meetings. Suggestion: This week, pick one recurring low-value meeting and kill/delegate it. Also clear 2 personal renewals so they stop living in your head rent-free.")
        st.caption("— torchOS Coach (dynamic, no fluff)")

elif page == "Integrations":
    st.header("🔌 Integrations")
    st.write("All your systems (Salesforce, Gmail, YouTube, Plaud, Banks, etc.) will feed into here.")
    st.success("We'll connect them one by one after the feel is right.")

st.sidebar.caption("torchOS v0.1 Online • Built live with you")
