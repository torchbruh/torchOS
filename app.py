import streamlit as st
import pandas as pd
from datetime import datetime
import requests
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="torchOS", page_icon="🔥", layout="wide")
st.title("🔥 torchOS")
st.caption("Your life, synthesized. One screen. Real-time. No bullshit.")

# Sidebar navigation
page = st.sidebar.selectbox(
    "Navigate your life",
    ["Dashboard", "Work Pulse", "Personal Pulse", "Ideas Lab", "Life Coach", "Integrations"]
)

# ====================== DASHBOARD ======================
if page == "Dashboard":
    st.header("Good afternoon, Justin — here's your life at a glance")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Support Cases (IT+Salesforce+AI)", "47 active", "↓12 from yesterday")
    with col2:
        st.metric("Team PTO Bank", "184 days remaining", "↑8 this month")
    with col3:
        st.metric("Bills Due This Week", "$2,847", "3 upcoming")
    with col4:
        st.metric("Tesla Range Left", "287 mi", "Charge tonight?")

    st.divider()
    
    # Quick calendar
    st.subheader("This Week")
    st.write("📅 Mon: 9am IT sync • 11am Salesforce review • 2pm AI team")
    st.write("📅 Tue: Capital One payment • Tesla service reminder")
    st.write("📅 Wed: Economic Ninja drop (watch?)")

    st.divider()
    
    # YouTube section (live!)
    st.subheader("📺 Meaningful Videos (Economic Ninja)")
    youtube_key = os.getenv("YOUTUBE_API_KEY")
    if youtube_key:
        try:
            youtube = build('youtube', 'v3', developerKey=youtube_key)
            request = youtube.search().list(
                part="snippet",
                channelId="UCOuP7ygJSo3qEV8VoUITbhA",  # Economic Ninja
                maxResults=6,
                order="date",
                type="video"
            )
            response = request.execute()
            
            cols = st.columns(3)
            for i, item in enumerate(response['items']):
                title = item['snippet']['title']
                video_id = item['id']['videoId']
                thumb = item['snippet']['thumbnails']['medium']['url']
                with cols[i % 3]:
                    st.image(thumb)
                    st.markdown(f"**{title}**")
                    st.markdown(f"[Watch →](https://youtube.com/watch?v={video_id})")
        except:
            st.info("Add your YouTube API key to .env to see latest videos")
    else:
        st.info("Add YOUTUBE_API_KEY to .env for live Economic Ninja updates")

# ====================== WORK PULSE ======================
elif page == "Work Pulse":
    st.header("💼 Work Pulse")
    st.write("Support metrics • Auvik • Salesforce • AI team • O365 • Slack • 8x8 • SAP Concur")
    # All placeholders for now — we'll connect real APIs next round
    st.success("Ready to wire in your real data. Which one first?")

# ====================== PERSONAL PULSE ======================
elif page == "Personal Pulse":
    st.header("🏠 Personal Pulse")
    st.write("Gmail • Calendar • Bills • Capital One • Chase • Tesla • Subscriptions • Plaud notes")
    st.success("Manual entry + CSV upload ready. API connections coming.")

# ====================== IDEAS LAB ======================
elif page == "Ideas Lab":
    st.header("🧠 Ideas Lab — First Principles Mode")
    idea = st.text_area("Brain dump anything. Raw thoughts only.", height=300, placeholder="What if we...")
    
    if st.button("Refactor with First Principles"):
        st.info("🔥 First-principles breakdown incoming...")
        # We'll hook real LLM here next
        st.write("→ Break it down to fundamentals\n→ Eliminate assumptions\n→ Rebuild from truth")
        st.success("Your idea just got 10x clearer.")

# ====================== LIFE COACH ======================
elif page == "Life Coach":
    st.header("🧭 Life Coach (Blunt Edition)")
    st.write("I see everything. I tell you what you need to hear.")
    
    context = st.text_area("Optional: Add extra context or question", "How am I doing overall?")
    
    if st.button("Give me the real talk"):
        st.markdown("**Coach:**")
        st.write("Justin — you're carrying too much context switching between IT/Salesforce/AI. Your PTO bank is healthy but your personal renewal list is growing. Pivot suggestion: Block 2 hours this week to kill one low-value recurring meeting and use that time for the Economic Ninja-style thinking you actually respect. First principle: Energy compounds. Protect it.")
        st.caption("— torchOS Life Coach (dynamic, no fluff)")

# ====================== INTEGRATIONS ======================
elif page == "Integrations":
    st.header("🔌 Secure Connections")
    st.write("All credentials stay on your machine only.")
    st.success("YouTube is live. Next up: Gmail + Google Calendar, Salesforce, Plaud AI, etc.")

st.sidebar.caption("torchOS v0.1 — built live with you")
