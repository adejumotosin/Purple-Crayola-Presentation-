import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Purple Crayolá - January 2026 Content Strategy",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    .stMetric {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        border-left: 4px solid #6B46C1;
    }
    
    .stMetric label {
        font-size: 14px !important;
        font-weight: 500 !important;
        color: #64748b !important;
    }
    
    .stMetric [data-testid="stMetricValue"] {
        font-size: 32px !important;
        font-weight: 700 !important;
        color: #1e293b !important;
    }
    
    .stMetric [data-testid="stMetricDelta"] {
        font-size: 13px !important;
    }
    
    .content-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        margin-bottom: 20px;
        border-top: 3px solid #6B46C1;
    }
    
    .presence-card {
        background: linear-gradient(135deg, #6B46C1 0%, #553C9A 100%);
        color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        margin-bottom: 20px;
    }
    
    h1 {
        color: #1e293b;
        font-weight: 700;
        letter-spacing: -0.5px;
    }
    
    h2 {
        color: #334155;
        font-weight: 600;
        margin-top: 2rem;
    }
    
    h3 {
        color: #6B46C1;
        font-weight: 600;
    }
    
    .highlight {
        background: linear-gradient(135deg, #EDE9FE 0%, #DBEAFE 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #6B46C1;
        margin: 15px 0;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #6B46C1 0%, #553C9A 100%);
    }
    
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #6B46C1 0%, #553C9A 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    .author-badge {
        background: rgba(255,255,255,0.1);
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin-top: 20px;
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    # Display the Purple Crayolá logo (smaller)
    try:
        st.image("logo.png", width=120)
    except:
        st.markdown("""
            <div style="text-align: center; padding: 10px 0;">
                <h3 style="color: white; margin: 5px 0;">Purple Crayolá</h3>
                <p style="color: rgba(255,255,255,0.8); font-size: 12px; margin: 0;">Digital Transformation</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    st.title("📊 Navigation")
    
    page = st.radio(
        "Select Section:",
        ["Overview", "Campaign Focus: Presence", "Weekly Breakdown", "Platform Strategy", "Content Calendar", "KPIs & Goals"]
    )
    
    st.divider()
    
    # Author section
    st.markdown("""
        <div class="author-badge">
            <p style="font-size: 11px; margin: 0; opacity: 0.8;">DEVELOPED BY</p>
            <p style="font-size: 15px; font-weight: 600; margin: 5px 0;">Oluwatosin Adejumo</p>
            <p style="font-size: 11px; margin: 0; opacity: 0.8;">Content & Social Media Manager</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.caption("**Strategy Period:** January 6-30, 2026")
    st.caption("**Document Version:** 2.0")
    st.caption("**Primary Campaign:** Presence")

# Main content
if page == "Overview":
    st.title("🎨 Purple Crayolá - January 2026 Content Strategy")
    st.markdown("### Personal Branding Meets Digital Transformation")
    st.markdown("**Strategy Period:** January 6 - January 30, 2026")
    st.markdown("**Primary Campaign:** Presence - Own Your Story. Command Your Space. Lead with Presence.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Target Posts</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">15-18</p>
                <p style="font-size: 13px; color: #10b981; margin-top: 8px;">↑ Monthly</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Campaign Split</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">40/60</p>
                <p style="font-size: 13px; color: #10b981; margin-top: 8px;">↑ Presence / Digital Transformation</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Platforms</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">3</p>
                <p style="font-size: 13px; color: #10b981; margin-top: 8px;">↑ LinkedIn, Instagram, Twitter/X</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Expected Growth</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">1-3%</p>
                <p style="font-size: 13px; color: #10b981; margin-top: 8px;">↑ Conservative Target</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Campaign Overview
    st.markdown("## 🎯 January 2026 Campaign Overview")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
        <div class="presence-card">
            <h3 style="color: white; margin-bottom: 15px;">🟣 Primary Campaign: Presence</h3>
            <p style="font-size: 18px; font-weight: 600; margin-bottom: 10px;">40% of Content</p>
            <p style="opacity: 0.9; line-height: 1.6;">
            Purple Crayolá's signature personal branding experience for leaders ready to evolve how they show up—online and offline.
            </p>
            <p style="margin-top: 15px; font-weight: 500;">Campaign Tagline:</p>
            <p style="font-size: 16px; font-style: italic; opacity: 0.95;">"Own your story. Command your space. Lead with Presence."</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
            <h3 style="margin-bottom: 15px;">💼 Supporting Content: Digital Transformation</h3>
            <p style="font-size: 18px; font-weight: 600; color: #6B46C1; margin-bottom: 10px;">60% of Content</p>
            <p style="color: #64748b; line-height: 1.6;">
            Core services including web development, digital strategy, mobile apps, and business transformation solutions.
            </p>
            <p style="margin-top: 15px; font-weight: 500; color: #1e293b;">Focus Areas:</p>
            <p style="color: #64748b;">Web & App Development, Digital Marketing, Business Strategy, Technology Solutions</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Target Audience
    st.markdown("## 👥 Target Audience")
    
    audience_col1, audience_col2 = st.columns(2)
    
    with audience_col1:
        st.markdown("""
        <div class="content-card">
        <h4>Primary Audience (Presence Campaign)</h4>
        <ul style="line-height: 1.8; color: #64748b;">
            <li><strong>Executives & Founders:</strong> Building platform authority</li>
            <li><strong>Creatives & Educators:</strong> Ready to scale their message</li>
            <li><strong>Career Pivoters:</strong> Seeking thought leadership opportunities</li>
            <li><strong>Diaspora Professionals:</strong> Anchoring voice in new markets</li>
            <li><strong>Mission-Driven Leaders:</strong> Integrating values into public presence</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with audience_col2:
        st.markdown("""
        <div class="content-card">
        <h4>Secondary Audience (Digital Transformation)</h4>
        <ul style="line-height: 1.8; color: #64748b;">
            <li><strong>Business Owners:</strong> Seeking digital solutions</li>
            <li><strong>Startups & Scale-ups:</strong> Building tech infrastructure</li>
            <li><strong>Organizations:</strong> Needing digital strategy</li>
            <li><strong>Nigerian Businesses:</strong> Modernizing operations</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Content Themes
    st.markdown("## 🎯 January 2026 Content Themes")
    
    themes_col1, themes_col2 = st.columns(2)
    
    with themes_col1:
        st.markdown("""
        <div class="content-card">
        <h3>🟣 Presence Themes (40%)</h3>
        <p><strong>Theme 1: The PRISM Framework™</strong><br>
        Introduce the signature methodology for personal brand building</p>
        
        <p><strong>Theme 2: Transformation Stories</strong><br>
        Showcase client journeys and positioning success</p>
        
        <p><strong>Theme 3: Thought Leadership</strong><br>
        Educate on personal branding, visibility, and professional positioning</p>
        </div>
        """, unsafe_allow_html=True)
    
    with themes_col2:
        st.markdown("""
        <div class="content-card">
        <h3>💼 Digital Transformation Themes (60%)</h3>
        <p><strong>Theme 1: New Year Digital Excellence</strong><br>
        2026 as the year of transformation for businesses</p>
        
        <p><strong>Theme 2: Service Showcase</strong><br>
        Highlight web development, apps, and digital solutions</p>
        
        <p><strong>Theme 3: Innovation & Trends</strong><br>
        Position as tech thought leaders</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Content Distribution
    st.markdown("## 📊 Content Distribution")
    
    distribution_data = {
        'Category': ['Presence Campaign', 'Presence Campaign', 'Digital Transformation', 'Digital Transformation', 'Digital Transformation'],
        'Type': ['Personal Branding Education', 'PRISM Framework™ Content', 'Service Showcase', 'Thought Leadership', 'Client Success Stories'],
        'Percentage': [25, 15, 30, 20, 10]
    }
    
    fig = go.Figure(data=[go.Pie(
        labels=[f"{d['Type']}<br>({d['Percentage']}%)" for d in [dict(zip(distribution_data.keys(), values)) for values in zip(*distribution_data.values())]],
        values=distribution_data['Percentage'],
        hole=.4,
        marker_colors=['#6B46C1', '#9F7AEA', '#3B82F6', '#60A5FA', '#93C5FD'],
        textinfo='label',
        textfont_size=12
    )])
    
    fig.update_layout(
        title="Content Mix Strategy - January 2026",
        height=450,
        showlegend=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif page == "Campaign Focus: Presence":
    st.title("🟣 Campaign Focus: Presence")
    st.markdown("### Purple Crayolá's Signature Personal Branding Experience")
    
    st.markdown("""
    <div class="presence-card">
        <h2 style="color: white; margin-bottom: 15px;">What is Presence?</h2>
        <p style="font-size: 18px; line-height: 1.8; opacity: 0.95;">
        Presence is Purple Crayolá's signature personal branding experience for individuals ready to evolve 
        how they show up in the world—online and offline. We help you define what you stand for, 
        communicate it with clarity, and activate it across the spaces that matter most.
        </p>
        <p style="font-size: 20px; font-weight: 600; margin-top: 20px; font-style: italic;">
        "Own your story. Command your space. Lead with Presence."
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # The PRISM Framework
    st.markdown("## ✨ The PRISM Framework™")
    st.markdown("Our proprietary methodology that transforms your experience, values, and voice into an identity that resonates and leads.")
    
    prism_col1, prism_col2 = st.columns([1, 2])
    
    with prism_col1:
        st.markdown("""
        <div class="content-card" style="background: linear-gradient(135deg, #EDE9FE 0%, #DBEAFE 100%);">
            <h3 style="text-align: center; font-size: 48px; margin: 20px 0;">🔷</h3>
            <p style="text-align: center; font-weight: 600; font-size: 18px; color: #6B46C1;">
            Just like a prism transforms light into colour, the PRISM Framework™ transforms your experience into an identity that leads.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with prism_col2:
        st.markdown("""
        <div class="content-card">
            <p><strong style="color: #6B46C1; font-size: 18px;">P — POSITION</strong><br>
            Clarify your foundation: purpose, audience, message, and identity</p>
            
            <p><strong style="color: #6B46C1; font-size: 18px;">R — REFINE</strong><br>
            Shape your identity with language, visuals, and structure</p>
            
            <p><strong style="color: #6B46C1; font-size: 18px;">I — IGNITE</strong><br>
            Launch with intention through content calendars and storytelling</p>
            
            <p><strong style="color: #6B46C1; font-size: 18px;">S — SIGNAL</strong><br>
            Sustain visibility with media kits and platform tools</p>
            
            <p><strong style="color: #6B46C1; font-size: 18px;">M — MULTIPLY</strong><br>
            Expand impact through thought leadership and community leverage</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Packages
    st.markdown("## 📦 Presence Packages")
    
    package_col1, package_col2, package_col3, package_col4 = st.columns(4)
    
    with package_col1:
        st.markdown("""
        <div class="content-card" style="min-height: 300px;">
            <h4 style="color: #6B46C1;">🟣 Presence Core</h4>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 15px;">Strategic foundation</p>
            <ul style="font-size: 13px; line-height: 1.8; color: #64748b;">
                <li>Brand audit + discovery</li>
                <li>Personal brand strategy</li>
                <li>Audience mapping</li>
                <li>Platform bio set</li>
            </ul>
            <p style="margin-top: 15px; font-weight: 600; color: #1e293b;">2-3 weeks delivery</p>
        </div>
        """, unsafe_allow_html=True)
    
    with package_col2:
        st.markdown("""
        <div class="content-card" style="min-height: 300px;">
            <h4 style="color: #6B46C1;">🟣 Presence Pro</h4>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 15px;">Align & activate</p>
            <ul style="font-size: 13px; line-height: 1.8; color: #64748b;">
                <li>Everything in Core</li>
                <li>Full platform identity</li>
                <li>Signature narrative</li>
                <li>12-week content calendar</li>
                <li>Launch plan</li>
            </ul>
            <p style="margin-top: 15px; font-weight: 600; color: #1e293b;">4-5 weeks delivery</p>
        </div>
        """, unsafe_allow_html=True)
    
    with package_col3:
        st.markdown("""
        <div class="content-card" style="min-height: 300px;">
            <h4 style="color: #6B46C1;">🟣 Presence Elite</h4>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 15px;">Scale with influence</p>
            <ul style="font-size: 13px; line-height: 1.8; color: #64748b;">
                <li>Everything in Pro</li>
                <li>12-month strategy</li>
                <li>Media kit + speaker bios</li>
                <li>Thought leadership dev</li>
                <li>1:1 coaching</li>
            </ul>
            <p style="margin-top: 15px; font-weight: 600; color: #1e293b;">6-8 weeks delivery</p>
        </div>
        """, unsafe_allow_html=True)
    
    with package_col4:
        st.markdown("""
        <div class="content-card" style="min-height: 300px;">
            <h4 style="color: #6B46C1;">🟣 Presence Launchpad</h4>
            <p style="font-size: 13px; color: #64748b; margin-bottom: 15px;">Light-touch consistency</p>
            <ul style="font-size: 13px; line-height: 1.8; color: #64748b;">
                <li>Monthly content templates</li>
                <li>4-6 posts per month</li>
                <li>Profile review</li>
                <li>Caption prompts</li>
            </ul>
            <p style="margin-top: 15px; font-weight: 600; color: #1e293b;">Monthly retainer</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Campaign Content Strategy
    st.markdown("## 📝 January Content Strategy for Presence")
    
    st.markdown("""
    <div class="highlight">
        <h4>Content Pillars for Presence Campaign (40% of total content)</h4>
        <p><strong>Educational Content (15%):</strong> "What is personal branding?", "Why executives need Presence", "The PRISM Framework™ explained"</p>
        <p><strong>Framework Introduction (10%):</strong> Deep dives into each PRISM element, case studies, methodology showcase</p>
        <p><strong>Social Proof (8%):</strong> Client testimonials, transformation stories, before/after positioning</p>
        <p><strong>Call-to-Action (7%):</strong> Discovery call invites, package highlights, limited spots messaging</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Key Messages for January")
    
    message_col1, message_col2 = st.columns(2)
    
    with message_col1:
        st.markdown("""
        **Week 1-2: Awareness & Problem Identification**
        - "Is your expertise visible?"
        - "Great work deserves great visibility"
        - "Your personal brand is strategic, not optional"
        - Introduce Presence as the solution
        """)
    
    with message_col2:
        st.markdown("""
        **Week 3-4: Solution & Social Proof**
        - The PRISM Framework™ deep dive
        - Client success stories
        - "From invisible to influential"
        - Direct CTA for discovery calls
        """)

elif page == "Weekly Breakdown":
    st.title("📅 Weekly Content Breakdown")
    st.markdown("**Campaign Mix:** 40% Presence | 60% Digital Transformation")
    
    week = st.selectbox(
        "Select Week:",
        ["Week 1: January 6-10 (New Beginnings)",
         "Week 2: January 13-17 (Presence Introduction)",
         "Week 3: January 20-24 (Framework Deep Dive)",
         "Week 4: January 27-30 (Conversion & CTA)"]
    )
    
    if "Week 1" in week:
        st.markdown("## 🎉 Week 1: New Beginnings (January 6-10)")
        st.markdown("**Theme:** Set the tone - Digital excellence + Visibility matters")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: New Year Vision - Digital Transformation (Jan 6)
            **Category:** Digital Transformation (60%)
            
            **Content:**  
            "2026: The Year of Digital Excellence. As businesses reset and reimagine their strategies, 
            ask yourself: Is your digital infrastructure ready to scale? Purple Crayolá partners with 
            forward-thinking organizations to transform digital experiences. Let's make 2026 your **year of transformation**."
            
            **Format:** Carousel with 3-5 slides on digital transformation pillars  
            **CTA:** Book a free digital audit consultation
            
            ---
            
            ### Post 2: Presence Teaser (Jan 8)
            **Category:** Presence Campaign (40%)
            
            **Content:** "Your expertise is undeniable. But is your visibility? In 2026, great work needs great presence. 
            Introducing Presence by Purple Crayolá—a personal branding experience for leaders ready to own their story 
            and command their space."
            
            **Format:** Single image post with bold typography  
            **CTA:** "Learn more about Presence" with link
            **Hashtags:** #PersonalBranding #ThoughtLeadership #Presence #ExecutivePresence
            """)
        
        with tab2:
            st.markdown("""
            ### Welcome 2026 Story Series (Jan 6-7)
            **Category:** Digital Transformation
            
            - Quick polls: "What's your biggest digital challenge in 2026?"
            - Behind-the-scenes of team planning sessions
            - Quote graphic: "Innovation distinguishes between a leader and a follower"
            
            ---
            
            ### Presence Announcement (Jan 9)
            **Category:** Presence Campaign
            
            **Content:** Carousel introducing Presence  
            **Slides:**
            1. "Own your story. Command your space. Lead with Presence."
            2. "What is Presence? Personal branding for leaders who are ready to be seen."
            3. "The PRISM Framework™ - Coming soon"
            4. "Are you ready?" + CTA
            """)
        
        with tab3:
            st.markdown("""
            ### Daily Engagement Mix
            
            **Monday (Jan 6):** Digital transformation tip
            **Tuesday (Jan 7):** "Your expertise vs your visibility - which is stronger?" (Presence theme)
            **Wednesday (Jan 8):** Retweet industry news with Purple Crayolá perspective
            **Thursday (Jan 9):** Tech tip
            **Friday (Jan 10):** Weekend engagement post
            """)
    
    elif "Week 2" in week:
        st.markdown("## 💡 Week 2: Presence Introduction (January 13-17)")
        st.markdown("**Theme:** Introduce the problem + The PRISM Framework™")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: The Visibility Gap (Jan 13)
            **Category:** Presence Campaign (40%)
            
            **Content:**  
            "You're brilliant at what you do. You've built expertise, led projects, and delivered results. 
            But when someone searches your name, do they find a leader—or a LinkedIn ghost?  
            
            Most high-performers struggle with visibility, not capability. That's where Presence comes in.  
            
            Presence by Purple Crayolá is a personal branding experience designed for executives, founders, 
            and mission-driven leaders who are ready to own their narrative and scale their influence.  
            
            Comment 'PRESENCE' to learn more."
            
            **Format:** Text post with professional headshot or brand visual  
            **CTA:** Comment to engage + Link in comments
            
            ---
            
            ### Post 2: Digital Service Showcase (Jan 15)
            **Category:** Digital Transformation (60%)
            
            **Content:** "Your Website is Your Digital Storefront. Is it converting visitors into customers? 
            Our custom web development solutions are built with User Experience by Design."
            
            **Format:** Before/after web design comparison  
            **CTA:** Download our Web Development Guide
            """)
        
        with tab2:
            st.markdown("""
            ### PRISM Framework™ Introduction (Jan 14)
            **Category:** Presence Campaign
            
            **Content:** Carousel explaining the PRISM Framework™  
            **Slides:**
            1. "Introducing: The PRISM Framework™"
            2. P - Position your foundation
            3. R - Refine your identity
            4. I - Ignite your launch
            5. S - Signal your visibility
            6. M - Multiply your impact
            7. "Ready to build your Presence?" + CTA
            
            ---
            
            ### Service Showcase (Jan 16)
            **Category:** Digital Transformation
            
            **Content:** "What We Do at Purple Crayolá"  
            **Format:** Clean, branded carousel highlighting all services
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Engagement
            
            - Monday: Motivational quote about leadership visibility (Presence)
            - Tuesday: Tech tip Tuesday
            - Wednesday: "Personal brand = professional currency" thread (Presence)
            - Thursday: Web development insight
            - Friday: Weekend reflection on visibility
            """)
    
    elif "Week 3" in week:
        st.markdown("## 👥 Week 3: Framework Deep Dive (January 20-24)")
        st.markdown("**Theme:** PRISM Framework™ showcase + Client stories")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: PRISM Deep Dive - Position (Jan 20)
            **Category:** Presence Campaign (40%)
            
            **Content:**  
            "The first step in building your Presence: POSITION.  
            
            Before you can show up powerfully, you need clarity. Who are you speaking to? What do you stand for? 
            What's your unique positioning?  
            
            In the PRISM Framework™, Position is where we audit your current brand, define your message pillars, 
            and map your ideal audience. It's the foundation everything else is built on.  
            
            Great brands don't happen by accident. They start with strategy.  
            
            Ready to position yourself for impact? Link in bio."
            
            **Format:** Professional carousel with framework visual  
            **CTA:** "Learn about Presence packages"
            
            ---
            
            ### Post 2: Client Success Story (Jan 22)
            **Category:** Presence Campaign (40%)
            
            **Content:** "From invisible to influential: How one CEO transformed their executive presence.  
            
            'This process brought clarity, language, and strategy to things I hadn't been able to articulate for years. 
            Now I feel equipped, consistent, and positioned for the rooms I've prayed for.'  
            
            — CEO, Global Private Healthcare Institution  
            
            This is what Presence delivers. Not just a brand refresh—a complete repositioning."
            
            **Format:** Testimonial graphic with client quote  
            **CTA:** "Ready to build your Presence?"
            """)
        
        with tab2:
            st.markdown("""
            ### PRISM Elements Series (Jan 21-23)
            **Category:** Presence Campaign
            
            **Day 1 (Jan 21):** P - Position (What you stand for)  
            **Day 2 (Jan 22):** R - Refine (How you show up)  
            **Day 3 (Jan 23):** I - Ignite (Your launch moment)  
            
            Each as a story + feed post carousel
            
            ---
            
            ### Digital Transformation Post (Jan 24)
            **Category:** Digital Transformation (60%)
            
            **Content:** "5 Digital Trends Nigerian Businesses Can't Ignore in 2026"  
            **Format:** Educational carousel with actionable insights
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Engagement
            
            - Monday: #MotivationMonday - Leadership visibility quote
            - Tuesday: Thread on personal branding mistakes
            - Wednesday: Tech insight for businesses
            - Thursday: "Expertise without visibility = missed opportunities"
            - Friday: Weekend poll about professional goals
            """)
    
    else:  # Week 4
        st.markdown("## 🏆 Week 4: Conversion & CTA (January 27-30)")
        st.markdown("**Theme:** Direct CTAs + Close the month strong")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Final PRISM Elements (Jan 27)
            **Category:** Presence Campaign (40%)
            
            **Content:**  
            "SIGNAL and MULTIPLY: The final stages of the PRISM Framework™.  
            
            Signal = Building awareness systems that keep you visible (media kits, speaker bios, outreach templates)  
            Multiply = Scaling your impact (thought leadership, speaking circuits, community leverage)  
            
            This is how executives and founders become household names in their industries.  
            
            Presence isn't a one-time project. It's a system for sustainable visibility.  
            
            📅 Limited spots available for February. Book your discovery call today."
            
            **Format:** Professional visual with CTA  
            **CTA:** Direct link to booking page
            
            ---
            
            ### Post 2: Month-End Digital Transformation (Jan 29)
            **Category:** Digital Transformation (60%)
            
            **Content:** "January Review: 2026 Digital Transformation Trends We're Watching"  
            
            **Format:** Industry insights carousel  
            **CTA:** "Ready to transform your business? Let's talk."
            """)
        
        with tab2:
            st.markdown("""
            ### Limited Spots Campaign (Jan 28)
            **Category:** Presence Campaign
            
            **Content:** "LAST CALL: February Presence spots closing soon.  
            
            If you're an executive, founder, or mission-driven leader ready to own your story and command your space, 
            now is your moment.  
            
            ✅ Brand strategy  
            ✅ PRISM Framework™  
            ✅ 12-month visibility plan  
            
            DM 'PRESENCE' to secure your spot."
            
            **Format:** Urgency-driven graphic  
            **CTA:** DM for booking
            
            ---
            
            ### February Teaser (Jan 30)
            **Category:** Mixed
            
            **Content:** "What's coming in February? More transformation. More visibility. More impact."  
            **Format:** Teaser graphic
            """)
        
        with tab3:
            st.markdown("""
            ### Week 4 Engagement
            
            - Monday (Jan 27): Thread on the ROI of personal branding
            - Tuesday (Jan 28): Last chance messaging for Presence
            - Wednesday (Jan 29): Digital transformation insight
            - Thursday (Jan 30): Month wrap-up + February preview
            """)
    
    st.divider()
    st.info("💡 **Note:** Content mix maintains 40% Presence / 60% Digital Transformation throughout the month. Dates are flexible based on approval workflow.")

elif page == "Platform Strategy":
    st.title("📱 Platform-Specific Strategy")
    st.markdown("**Campaign Focus:** Presence (40%) + Digital Transformation (60%)")
    
    platform = st.selectbox(
        "Select Platform:",
        ["LinkedIn", "Instagram", "Twitter/X"]
    )
    
    if platform == "LinkedIn":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ## 💼 LinkedIn Strategy
            
            ### Primary B2B Platform for Presence Campaign
            
            **Posting Frequency:** 4-5 times/week (increased for campaign)
            
            **Best Times:**
            - Tuesday-Thursday
            - 8-10 AM WAT
            - 12-2 PM WAT
            
            **Tone:** Professional, authoritative, thought leadership
            
            **Presence Content Focus (40%):**
            - Executive positioning stories
            - PRISM Framework™ education
            - Client testimonials
            - Personal branding thought leadership
            - CTA posts for discovery calls
            
            **Digital Transformation Content (60%):**
            - Business case studies
            - Technology trends
            - Service showcases
            - Industry insights
            
            **Content Types:**
            - Carousel posts (3-10 slides) - Primary for Presence
            - Long-form text posts with storytelling
            - Client testimonial graphics
            - Video posts (30-90 seconds)
            - Engagement polls
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Key Hashtags</h4>
            <p><strong>Presence Campaign:</strong><br>
            #PersonalBranding<br>
            #ExecutivePresence<br>
            #ThoughtLeadership<br>
            #ProfessionalVisibility<br>
            #LeadershipBranding</p>
            
            <p><strong>Digital Transformation:</strong><br>
            #DigitalTransformation<br>
            #WebDevelopment<br>
            #TechInNigeria<br>
            #BusinessGrowth<br>
            #Innovation</p>
            </div>
            """, unsafe_allow_html=True)
    
    elif platform == "Instagram":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ## 📸 Instagram Strategy
            
            ### Visual Storytelling for Presence
            
            **Posting Frequency:** 3-4 posts/week + daily stories
            
            **Best Times:**
            - Monday-Friday
            - 12-1 PM WAT
            - 7-9 PM WAT
            
            **Tone:** Aspirational, empowering, visually striking
            
            **Presence Content Focus (40%):**
            - Brand transformation before/afters
            - Quote graphics about visibility
            - PRISM Framework™ visuals
            - "Day in the life" of positioning work
            - Client success celebrations
            
            **Digital Transformation Content (60%):**
            - Project showcases
            - Tech tips and trends
            - Team culture content
            - Service highlights
            
            **Content Types:**
            - Feed carousels (storytelling in slides)
            - Bold quote graphics
            - Stories with polls and engagement stickers
            - Professional photography
            - Short video clips (not Reels for now)
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Story Strategy</h4>
            <ul>
            <li>Daily Presence tips</li>
            <li>Framework breakdowns</li>
            <li>Quick polls on branding</li>
            <li>Client transformation snippets</li>
            <li>Behind-the-scenes</li>
            <li>"Ask me anything" sessions</li>
            <li>Countdown to booking deadlines</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    else:  # Twitter/X
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ## 🐦 Twitter/X Strategy
            
            ### Real-Time Engagement & Thought Leadership
            
            **Posting Frequency:** 2-3 times/day
            
            **Best Times:**
            - Throughout the day
            - 9 AM WAT
            - 12 PM WAT
            - 6 PM WAT
            
            **Tone:** Conversational, insightful, quotable
            
            **Presence Content Focus (40%):**
            - Punchy personal branding insights
            - "Expertise vs Visibility" threads
            - Quick PRISM tips
            - Engaging questions about positioning
            - Retweeting client wins
            
            **Digital Transformation Content (60%):**
            - Tech industry commentary
            - Quick business tips
            - Service highlights
            - Trending topic participation
            
            **Content Types:**
            - Single impactful tweets
            - Thread series on Presence
            - Quote tweets with insights
            - Engagement questions
            - Client spotlight retweets
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Engagement Tactics</h4>
            <ul>
            <li>Weekly Presence threads</li>
            <li>"Your expertise vs your visibility" hooks</li>
            <li>Personal branding tips</li>
            <li>Tech Tuesday insights</li>
            <li>Friday thought leadership</li>
            <li>Reply to industry conversations</li>
            <li>Share Presence success stories</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

elif page == "Content Calendar":
    st.title("📆 January 2026 Content Calendar")
    st.markdown("**Campaign Mix:** 40% Presence | 60% Digital Transformation")
    
    # Create calendar data
    calendar_data = {
        'Date': ['Jan 6', 'Jan 7', 'Jan 8', 'Jan 9', 'Jan 10',
                 'Jan 13', 'Jan 14', 'Jan 15', 'Jan 16', 'Jan 17',
                 'Jan 20', 'Jan 21', 'Jan 22', 'Jan 23', 'Jan 24',
                 'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30'],
        'Platform': ['LinkedIn', 'Instagram', 'LinkedIn', 'Instagram', 'Twitter/X',
                     'LinkedIn', 'Instagram', 'LinkedIn', 'Instagram', 'Twitter/X',
                     'LinkedIn', 'Instagram', 'LinkedIn', 'Instagram', 'Twitter/X',
                     'LinkedIn', 'Instagram', 'LinkedIn', 'Instagram'],
        'Content Type': ['Carousel', 'Stories', 'Image Post', 'Carousel', 'Thread',
                        'Text Post', 'Carousel', 'Before/After', 'Carousel', 'Thread',
                        'Carousel', 'Stories', 'Testimonial', 'PRISM Series', 'Thread',
                        'CTA Post', 'Urgency Post', 'Insights', 'Teaser'],
        'Campaign': ['Digital Transform', 'Digital Transform', 'Presence', 'Presence', 'Mixed',
                     'Presence', 'Presence', 'Digital Transform', 'Digital Transform', 'Presence',
                     'Presence', 'Presence', 'Presence', 'Digital Transform', 'Presence',
                     'Presence', 'Presence', 'Digital Transform', 'Mixed'],
        'Status': ['Pending'] * 19
    }
    
    df = pd.DataFrame(calendar_data)
    
    # Add filters
    col1, col2, col3 = st.columns(3)
    with col1:
        platform_filter = st.multiselect(
            "Filter by Platform:",
            options=df['Platform'].unique(),
            default=df['Platform'].unique()
        )
    
    with col2:
        campaign_filter = st.multiselect(
            "Filter by Campaign:",
            options=df['Campaign'].unique(),
            default=df['Campaign'].unique()
        )
    
    with col3:
        status_filter = st.multiselect(
            "Filter by Status:",
            options=df['Status'].unique(),
            default=df['Status'].unique()
        )
    
    # Filter dataframe
    filtered_df = df[
        (df['Platform'].isin(platform_filter)) &
        (df['Campaign'].isin(campaign_filter)) &
        (df['Status'].isin(status_filter))
    ]
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # Visual timeline
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📊 Content Distribution by Platform")
        
        platform_counts = df['Platform'].value_counts()
        
        fig = px.bar(
            x=platform_counts.index,
            y=platform_counts.values,
            labels={'x': 'Platform', 'y': 'Number of Posts'},
            title='Posts per Platform',
            color=platform_counts.index,
            color_discrete_map={
                'LinkedIn': '#0A66C2',
                'Instagram': '#E4405F',
                'Twitter/X': '#1DA1F2'
            }
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Content by Campaign")
        
        campaign_counts = df['Campaign'].value_counts()
        
        fig2 = px.pie(
            values=campaign_counts.values,
            names=campaign_counts.index,
            title='Campaign Distribution',
            color_discrete_sequence=['#6B46C1', '#3B82F6', '#9F7AEA']
        )
        
        st.plotly_chart(fig2, use_container_width=True)

elif page == "KPIs & Goals":
    st.title("🎯 KPIs & Strategic Goals")
    st.markdown("**Primary Campaign:** Presence Launch")
    
    st.markdown("""
    <div class="highlight">
    <h3>⚠️ Month 1 Philosophy: Foundation + Campaign Launch</h3>
    <p>January serves dual purposes: building sustainable content systems while launching the Presence campaign. 
    Success is measured both by content consistency and campaign engagement metrics.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Goals columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Growth Targets")
        st.metric("Follower Growth", "1-3%", "Conservative", help="Focus on quality audience building")
        st.metric("Engagement Rate", "2-4%", "Improvement", help="Campaign content expected to drive engagement")
        st.metric("Post Consistency", "85-90%", "Completion Rate", help="15-18 posts across platforms")
        
        st.markdown("""
        #### Why These Targets?
        - **Campaign launch** typically drives higher engagement
        - Focus on **Presence-aligned audience** (executives, founders)
        - Building **qualified leads** over vanity metrics
        - **January momentum** sets Q1 trajectory
        """)
    
    with col2:
        st.markdown("### ✅ Strategic Objectives")
        
        st.markdown("""
        **Campaign-Specific Goals:**
        - Successfully introduce Presence to market
        - Generate 10-15 qualified discovery call inquiries
        - Achieve 50+ PRISM Framework™ content engagements
        - Secure 3-5 Presence package commitments
        
        **Brand Building:**
        - Establish Purple Crayolá as personal branding authority
        - Build awareness of PRISM Framework™
        - Position team as thought leaders in executive branding
        
        **Infrastructure:**
        - Maintain 40/60 Presence/Digital Transformation split
        - Build Presence content library
        - Establish conversion tracking for campaign
        """)
    
    st.divider()
    
    # Metrics to track
    st.markdown("### 📊 Key Performance Indicators")
    
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    
    with metrics_col1:
        st.markdown("""
        **Engagement Metrics**
        - Likes per post (by campaign)
        - Comments per post
        - Shares/Saves (especially PRISM content)
        - Story interactions
        - "PRESENCE" comment responses
        """)
    
    with metrics_col2:
        st.markdown("""
        **Campaign Metrics**
        - Presence content reach
        - Discovery call requests
        - Link clicks to Presence page
        - Package inquiry DMs
        - PRISM Framework™ saves
        """)
    
    with metrics_col3:
        st.markdown("""
        **Business Impact**
        - Qualified leads generated
        - Discovery calls booked
        - Presence packages sold
        - Website traffic from campaign
        - Email list growth
        """)
    
    st.divider()
    
    # 90-day vision
    st.markdown("### 🚀 90-Day Campaign Vision")
    
    months_data = {
        'Month': ['January', 'February', 'March'],
        'Focus': ['Campaign Launch & Awareness', 'Lead Nurturing & Conversion', 'Scale & Case Studies'],
        'Expected Growth': ['1-3%', '3-5%', '5-8%'],
        'Campaign Goals': [
            'Introduce Presence, generate initial inquiries',
            'Convert inquiries to clients, deepen engagement',
            'Share client success stories, expand reach'
        ]
    }
    
    months_df = pd.DataFrame(months_data)
    st.table(months_df)
    
    st.markdown("""
    <div class="highlight">
    <h4>💡 Success Definition for January</h4>
    <p><strong>Primary Success Metric:</strong> 10-15 qualified discovery call inquiries for Presence packages</p>
    <p><strong>Secondary Metrics:</strong> Content consistency (85%+), Engagement growth (2-4%), Brand awareness (reach expansion)</p>
    <p><strong>Long-term Indicator:</strong> Building a qualified pipeline of executives and founders interested in personal branding services</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; padding: 30px 20px; background: white; border-radius: 12px; margin-top: 40px;">
    <h4 style="color: #6B46C1; margin-bottom: 10px;">🎨 Purple Crayolá Content Strategy</h4>
    <p style="color: #64748b; margin: 5px 0;">January 2026 - Presence Campaign Launch</p>
    <p style="font-size: 16px; font-style: italic; color: #6B46C1; margin: 10px 0;">"Own your story. Command your space. Lead with Presence."</p>
    <p style="font-size: 12px; color: #94a3b8; margin-top: 15px;">Developed by Oluwatosin Adejumo • Version 2.0 • Campaign Focus: 40% Presence / 60% Digital Transformation</p>
</div>
""", unsafe_allow_html=True)