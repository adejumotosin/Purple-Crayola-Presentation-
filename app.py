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
        ["Overview", "Weekly Breakdown", "Platform Strategy", "Content Calendar", "KPIs & Goals"]
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
    st.caption("**Document Version:** 1.0")

# Main content
if page == "Overview":
    st.title("🎨 Purple Crayolá - January 2026 Content Strategy")
    st.markdown("### Digital Transformation Through Strategic Content")
    st.markdown("**Strategy Period:** January 6 - January 30, 2026")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Target Posts</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">12-15</p>
                <p style="font-size: 13px; color: #10b981; margin-top: 8px;">↑ Monthly</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Platforms</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">3</p>
                <p style="font-size: 13px; color: #10b981; margin-top: 8px;">↑ LinkedIn, Instagram, Twitter/X</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Content Themes</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">4</p>
                <p style="font-size: 13px; color: #10b981; margin-top: 8px;">↑ Strategic Pillars</p>
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
    
    # Brand Overview
    st.markdown("## 🏢 Brand Overview")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Purple Crayolá** is a full-service digital transformation startup in Nigeria that delivers 
        design and digital solutions to transform customer experiences and business results.
        
        **Core Services:**
        - 🎯 Digital Strategy & Transformation
        - 💻 Web & Mobile App Development
        - 📱 Digital Marketing (SEO, Content, Social Media, PPC)
        - 🎨 Branding & Identity Design
        - 📊 Project & Product Management
        - 📚 Digital Learning Solutions
        - ✨ **Presence**: Personal Branding for Leaders & Professionals
        """)
    
    with col2:
        st.markdown("""
        **Brand Values:**
        - Innovation & cutting-edge technology
        - Collaboration & partnership
        - Trust & discretion
        - User Experience by Design
        - Sustainable solutions
        
        **January Focus:**
        - 40% Presence (Personal Branding)
        - 60% Digital Transformation
        """)
    
    st.divider()
    
    # Content Themes
    st.markdown("## 🎯 January 2026 Content Themes")
    
    themes_col1, themes_col2 = st.columns(2)
    
    with themes_col1:
        st.markdown("""
        <div class="content-card">
        <h3>🚀 Theme 1: New Year, Digital Transformation</h3>
        <p>Capitalize on the new year energy and businesses setting digital goals.</p>
        </div>
        
        <div class="content-card">
        <h3>📊 Theme 2: Presence - Personal Brand Excellence</h3>
        <p>Introduce Presence and showcase how personal branding elevates professional visibility and authority.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with themes_col2:
        st.markdown("""
        <div class="content-card">
        <h3>📈 Theme 3: Thought Leadership & Positioning</h3>
        <p>Position Purple Crayolá and clients as industry thought leaders through the PRISM Framework™.</p>
        </div>
        
        <div class="content-card">
        <h3>👥 Theme 4: Behind the Scenes</h3>
        <p>Humanize the brand, introduce team members, show process and client transformations.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Content Pillars
    st.markdown("## 📊 Content Pillars Distribution")
    
    pillars_data = {
        'Pillar': ['Educational', 'Presence (Personal Branding)', 'Engagement', 'Behind-the-Scenes'],
        'Percentage': [35, 40, 15, 10],
        'Description': [
            'Digital transformation tips, trends, industry insights',
            'Personal branding, PRISM Framework™, thought leadership',
            'Questions, polls, interactive content',
            'Team, culture, process, testimonials'
        ]
    }
    
    fig = go.Figure(data=[go.Pie(
        labels=pillars_data['Pillar'],
        values=pillars_data['Percentage'],
        hole=.4,
        marker_colors=['#6B46C1', '#9F7AEA', '#D6BCFA', '#EDE9FE']
    )])
    
    fig.update_layout(
        title="Content Mix Strategy",
        height=400,
        showlegend=True
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif page == "Weekly Breakdown":
    st.title("📅 Weekly Content Breakdown")
    
    week = st.selectbox(
        "Select Week:",
        ["Week 1: January 6-10 (New Beginnings)",
         "Week 2: January 13-17 (Solutions Spotlight)",
         "Week 3: January 20-24 (Team & Culture)",
         "Week 4: January 27-30 (Authority Building)"]
    )
    
    if "Week 1" in week:
        st.markdown("## 🎉 Week 1: New Beginnings (January 6-10)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: New Year Vision (Jan 6)
            
            **Content:**  
            "2026: The Year of Digital Excellence. As businesses reset and reimagine their strategies, 
            ask yourself: Is your digital infrastructure ready to scale? Purple Crayolá partners with 
            forward-thinking organizations to transform digital experiences. Let's make 2026 your growth year."
            
            **Format:** Carousel with 3-5 slides on digital transformation pillars  
            **CTA:** Book a free digital audit consultation
            
            ---
            
            ### Post 2: Introducing Presence (Jan 8)
            
            **Content:** "Your expertise is undeniable. But is your visibility matching your impact? Introducing Presence by Purple Crayolá — personal branding for leaders ready to own their story, command their space, and lead with presence. Built on our signature PRISM Framework™."
            
            **Format:** Video or carousel showcasing the PRISM Framework™  
            **CTA:** Learn more at purplecrayola.com/presence
            """)
        
        with tab2:
            st.markdown("""
            ### Welcome 2026 Story Series (Jan 6-7)
            
            - Quick polls: "What's your biggest digital challenge in 2026?"
            - Poll: "Are you satisfied with your professional visibility online?"
            - Quote graphic: "Own your story. Command your space. Lead with Presence."
            
            ---
            
            ### Introducing Presence - Instagram Version (Jan 8)
            
            **Content:** "Your expertise is undeniable 🎯 But is your visibility matching your impact? 
            Introducing Presence by Purple Crayolá — personal branding for leaders ready to own their story. 
            Built on our signature PRISM Framework™ ✨"
            
            **Format:** Eye-catching carousel with bold visuals (5-7 slides)
            **Slides:** Problem → Presence Introduction → PRISM Overview → Who It's For → Results
            **Style:** Instagram-native, visual-first, punchy copy
            **CTA:** "Link in bio to learn more"
            
            ---
            
            ### Feed Post (Jan 9)
            
            **Content:** "3 Signs You Need a Personal Brand Strategy in 2026"  
            **Format:** Carousel post with clean graphics, one sign per slide  
            **Slides:** 
            1. Your work speaks louder than your name
            2. Opportunities aren't finding you
            3. Your LinkedIn feels generic
            **Final Slide:** "Ready to build your Presence? Link in bio 🔗"
            **Design:** Bold typography, brand colors, professional yet approachable
            """)
        
        with tab3:
            st.markdown("""
            ### Daily Engagement
            
            - Thread: "Personal branding isn't vanity. It's visibility with purpose. Here's why it matters in 2026..." (7-10 tweet thread)
            - Quote tweet success stories about professional visibility
            - Retweet industry conversations about thought leadership
            - Engagement question: "What's one word you want to be known for professionally?"
            - Share quick Presence tip: "Your bio is your billboard. Make every word count."
            """)
    
    elif "Week 2" in week:
        st.markdown("## 💡 Week 2: Solutions Spotlight (January 13-17)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: The PRISM Framework™ Deep Dive (Jan 13)
            
            **Content:**  
            "What if your personal brand could be as clear as light through a prism? Introducing the PRISM Framework™ — 
            our signature methodology that transforms your experience, values, and voice into an identity that resonates and leads. 
            Position. Refine. Ignite. Signal. Multiply."
            
            **Format:** Carousel explaining each element of PRISM  
            **CTA:** "Ready to discover your Presence? DM us or visit purplecrayola.com/presence"
            
            ---
            
            ### Post 2: Digital Transformation Case Study (Jan 15)
            
            **Content:** "From invisible to influential: How we helped a fintech ops leader build a personal brand that opened doors they'd prayed for."  
            **Format:** LinkedIn article or carousel (Challenge → Solution → Results)  
            **Include:** Testimonial quote, before/after visibility metrics
            """)
        
        with tab2:
            st.markdown("""
            ### PRISM Framework™ - Instagram Version (Jan 14)
            
            **Content:** "What if your personal brand could be as clear as light through a prism? 💎 
            Meet the PRISM Framework™ — Position. Refine. Ignite. Signal. Multiply. 
            The system that transforms your expertise into influence."
            
            **Format:** High-impact carousel (7-10 slides)
            **Slides:** 
            - Cover: "Introducing the PRISM Framework™"
            - P: Position (foundation & clarity)
            - R: Refine (identity & visuals)
            - I: Ignite (launch strategy)
            - S: Signal (visibility systems)
            - M: Multiply (scale & impact)
            - Results: "Your brand, amplified"
            - CTA: "DM 'PRESENCE' to start"
            **Design:** Bold colors, geometric prism visuals, modern typography
            
            ---
            
            ### Case Study Story Highlight (Jan 15-16)
            
            **Day 1 (Jan 15) - The Problem:**
            - Story series: "Meet Sarah, a fintech ops leader..."
            - "Excellent at her job. Invisible online."
            - "She had the expertise. But not the visibility."
            
            **Day 2 (Jan 16) - The Transformation:**
            - "Then she discovered Presence."
            - Carousel showing: Before/After profile | PRISM process | New visibility
            - Client quote graphic (testimonial)
            - Final slide: "From invisible to influential. That's the power of Presence."
            **CTA:** "Ready for your transformation? Link in bio"
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Engagement
            
            - #PresenceTuesday thread: "The 5 elements of the PRISM Framework™ and how each one transforms your brand..."
            - Poll: "What's holding you back from building your personal brand?" (Options: Time, Clarity, Confidence, Don't know where to start)
            - Retweet and comment on inspiring thought leadership content
            - Share client win: "This is what happens when you align expertise with visibility"
            - Engagement: "Drop a 💎 if you're ready to build your Presence in 2026"
            """)
    
    elif "Week 3" in week:
        st.markdown("## 👥 Week 3: Team & Culture (January 20-24)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Team Spotlight + Presence Behind-the-Scenes (Jan 20)
            
            **Content:** "Meet the team behind Presence. From brand strategists to cultural storytellers, 
            we're architects of personal brands that move people, open doors, and leave a mark."  
            **Format:** Professional photo carousel + mini Q&A  
            **Purpose:** Humanizes the brand while reinforcing Presence expertise
            
            ---
            
            ### Post 2: Who Presence Is For (Jan 22)
            
            **Content:** "Presence isn't for everyone. It's for the builders, the believers, the timid but audacious. 
            For executives seeking platform authority. Creatives ready to scale their message. Professionals navigating pivots. 
            Diaspora talents anchoring their voice in new markets. Mission-driven individuals leading with values."  
            **Format:** Infographic or video showcasing target audiences  
            **Purpose:** Clear positioning and audience qualification
            """)
        
        with tab2:
            st.markdown("""
            ### Team + Presence BTS Stories (Jan 20-21)
            
            **Story Series:**
            - "Meet the team behind Presence 👋"
            - Follow a Presence strategist through a client session
            - Show the PRISM Framework™ in action (whiteboard, planning)
            - Behind-the-scenes content creation process
            - Team member spotlight with quick Q&A stickers
            - Interactive: "What would your personal brand tagline be?" (Question sticker)
            
            ---
            
            ### Who Presence Is For - Instagram Version (Jan 22-23)
            
            **Jan 22 Post:**
            **Content:** "Presence isn't for everyone. It's for the builders, the believers, the timid but audacious 🚀"
            
            **Format:** Carousel (7-8 slides)
            **Slides:**
            - Cover: "Is Presence for you?"
            - Slide 1: Executives seeking platform authority
            - Slide 2: Creatives ready to scale their message
            - Slide 3: Professionals navigating career pivots
            - Slide 4: Diaspora talents anchoring their voice
            - Slide 5: Mission-driven leaders integrating values
            - Slide 6: "If you said yes to any of these..."
            - Final: "Presence is for you. Link in bio 🔗"
            **Design:** People-focused imagery, inclusive representation
            
            **Jan 23 - Values Post:**
            **Content:** "'You'nique collaboration. Cultural fluency. Data-informed impact. 
            At Purple Crayolá, your brand is as unique as your journey 💜"
            **Format:** Photo carousel of team collaboration moments
            **Style:** Warm, authentic, inspiring
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Content
            
            - #MotivationMonday: "Your visibility is not vanity. It's stewardship of your gifts."
            - Wednesday thread: "3 personal branding myths that keep talented people invisible"
            - Engage with and amplify diaspora professionals and thought leaders
            - Share and celebrate client wins with commentary
            - Quote tweet: Thought-provoking content about leadership and visibility
            """)
    
    else:  # Week 4
        st.markdown("## 🏆 Week 4: Authority Building (January 27-30)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Presence Packages Breakdown (Jan 27)
            
            **Content:** "From clarity to scale. Presence Core. Presence Pro. Presence Elite. Presence Launchpad. 
            Four pathways to building a personal brand that doesn't just look good—it moves people."  
            **Format:** Visual comparison chart or carousel  
            **Include:** Package features, ideal for, starting prices  
            **CTA:** "Book a discovery call: purplecrayola.com/presence"
            
            ---
            
            ### Post 2: January Impact Wrap + February Teaser (Jan 29)
            
            **Content:** "January was about laying the foundation. February? We're going deeper into thought leadership, 
            content strategy, and the art of showing up with intention. Plus: exclusive Presence insights you won't want to miss."  
            **Format:** Engaging visual recap  
            **Purpose:** Build anticipation and momentum
            """)
        
        with tab2:
            st.markdown("""
            ### Presence Packages - Instagram Version (Jan 27-28)
            
            **Jan 27 Post:**
            **Content:** "From clarity to scale 📈 Find your perfect pathway to building a personal brand that moves people."
            
            **Format:** Swipeable carousel (6 slides)
            **Slides:**
            - Cover: "Choose Your Presence Pathway"
            - Presence Core: "Start with clarity"
            - Presence Pro: "Align and activate"
            - Presence Elite: "Scale with influence"
            - Presence Launchpad: "Consistent content"
            - CTA: "Book your discovery call. Link in bio 🔗"
            **Design:** Clean, comparison format, package icons
            
            **Jan 28 - Success Story:**
            **Content:** "From underrepresented to unmissable 🌟 
            How Presence helped a healthcare CEO build a values-aligned platform 
            and scale her leadership voice across continents."
            
            **Format:** Story-driven carousel (5-7 slides)
            **Slides:** Challenge → Journey → PRISM in action → Results → Testimonial quote → CTA
            **Style:** Emotional, inspiring, authentic photos/graphics
            
            ---
            
            ### Month-End Content (Jan 29-30)
            
            **Jan 29 Stories:**
            - "January was about laying the foundation 🏗️"
            - Swipe-through recap of top posts
            - Poll: "What was your favorite content this month?"
            - "February preview: We're going deeper 👀"
            
            **Jan 30 Post:**
            **Content:** "Your work speaks louder than your visibility. 
            It's time to align the two 🎯 Presence is your platform. Your signal. 
            Your story—told with excellence. Let's build it together."
            
            **Format:** High-impact branded visual with strong CTA
            **Design:** Bold, eye-catching, professional
            **CTA:** "Start your Presence journey. DM us or link in bio to book 💜"
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Engagement
            
            - Thread: "The 5 stages of personal brand evolution—and where you are right now" (Educational, actionable)
            - Share Presence packages breakdown as visual thread
            - Final week engagement: "What's your biggest takeaway from January? Drop it below 👇"
            - Share thought-provoking content about visibility and authentic leadership
            - Preview February: "Next month we're talking thought leadership frameworks, content strategies, and the art of showing up with intention"
            - Engagement tweet: "Fill in the blank: In 2026, I want to be known for _____"
            """)
    
    st.divider()
    st.info("💡 **Note:** Content dates are flexible and may be adjusted based on approval workflow and real-time opportunities.")

elif page == "Platform Strategy":
    st.title("📱 Platform-Specific Strategy")
    
    platform = st.selectbox(
        "Select Platform:",
        ["LinkedIn", "Instagram", "Twitter/X"]
    )
    
    if platform == "LinkedIn":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ## 💼 LinkedIn Strategy
            
            ### Primary B2B Platform
            
            **Posting Frequency:** 3-4 times/week
            
            **Best Times:**
            - Tuesday-Thursday
            - 8-10 AM WAT
            - 12-2 PM WAT
            
            **Tone:** Professional, authoritative, thought leadership
            
            **Focus Areas:**
            - Long-form content
            - Case studies
            - Industry insights
            - Thought leadership articles
            - Team spotlights
            - Process transparency
            
            **Content Types:**
            - Carousel posts (3-10 slides)
            - Single image posts with long captions
            - LinkedIn articles (800-1000 words)
            - Video posts (30-90 seconds)
            - Polls and questions
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Key Hashtags</h4>
            <p><strong>Branded:</strong><br>
            #PurpleCrayolá<br>
            #DigitalTransformationNG<br>
            #UserExperienceByDesign</p>
            
            <p><strong>Industry:</strong><br>
            #DigitalTransformation<br>
            #WebDevelopment<br>
            #TechInNigeria<br>
            #NigerianStartups<br>
            #BusinessGrowth</p>
            </div>
            """, unsafe_allow_html=True)
    
    elif platform == "Instagram":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ## 📸 Instagram Strategy
            
            ### Visual Storytelling Platform
            
            **Posting Frequency:** 3-4 posts/week + daily stories
            
            **Best Times:**
            - Monday-Friday
            - 12-1 PM WAT
            - 7-9 PM WAT
            
            **Tone:** Creative, energetic, behind-the-scenes
            
            **Focus Areas:**
            - Visual design showcase
            - Company culture
            - Quick tips and insights
            - Carousel posts
            - Stories for daily engagement
            
            **Content Types:**
            - Feed carousels (5-10 slides)
            - Single image posts
            - Stories (polls, questions, behind-the-scenes)
            - Quote graphics
            - Client testimonials
            - Team spotlights
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Story Ideas</h4>
            <ul>
            <li>Day in the life series</li>
            <li>Quick polls and questions</li>
            <li>Behind-the-scenes office</li>
            <li>Client project previews</li>
            <li>Team introductions</li>
            <li>Tips and tricks</li>
            <li>Quote graphics</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    else:  # Twitter/X
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ## 🐦 Twitter/X Strategy
            
            ### Real-Time Engagement Platform
            
            **Posting Frequency:** 1-3 times/day
            
            **Best Times:**
            - Throughout the day
            - 9 AM WAT
            - 12 PM WAT
            - 6 PM WAT
            
            **Tone:** Conversational, timely, engaging
            
            **Focus Areas:**
            - Quick insights
            - Industry commentary
            - Community engagement
            - Trending topic participation
            - Thread creation
            
            **Content Types:**
            - Single tweets (280 characters)
            - Thread series (5-10 tweets)
            - Quote tweets with commentary
            - Polls
            - Image posts
            - Video clips
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Engagement Tactics</h4>
            <ul>
            <li>#TechTuesday tips</li>
            <li>#MotivationMonday quotes</li>
            <li>Wednesday wisdom threads</li>
            <li>Tech Thursday insights</li>
            <li>Friday discussions</li>
            <li>Weekend polls</li>
            <li>Reply to industry leaders</li>
            <li>Retweet with commentary</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

elif page == "Content Calendar":
    st.title("📆 January 2026 Content Calendar")
    
    # Create calendar data
    calendar_data = {
        'Date': ['Jan 6', 'Jan 7', 'Jan 8', 'Jan 9', 'Jan 13', 'Jan 14', 'Jan 15', 'Jan 16',
                 'Jan 20', 'Jan 22', 'Jan 23', 'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30'],
        'Platform': ['LinkedIn', 'Instagram', 'LinkedIn', 'Instagram', 'LinkedIn', 'Instagram',
                     'LinkedIn', 'Instagram', 'LinkedIn', 'LinkedIn', 'Instagram', 'LinkedIn',
                     'Instagram', 'LinkedIn', 'Instagram'],
        'Content Type': ['Carousel', 'Stories', 'Video/Carousel', 'Carousel', 'Carousel', 'Testimonial',
                        'Article/Case Study', 'Educational Carousel', 'Team Spotlight', 'Audience Positioning', 'Culture Post',
                        'Package Breakdown', 'Success Story', 'Impact Wrap', 'CTA Campaign'],
        'Theme': ['Digital Transformation', 'Presence Launch', 'Presence Introduction', 'Personal Branding', 'PRISM Framework™', 'Testimonial',
                 'Case Study', 'Personal Branding', 'Team + Presence', 'Presence Positioning', 'Culture + Values',
                 'Presence Packages', 'Success Story', 'Recap + Teaser', 'CTA'],
        'Focus': ['General (60%)', 'Presence (40%)', 'Presence (40%)', 'Presence (40%)', 'Presence (40%)', 'Presence (40%)',
                 'General (60%)', 'Presence (40%)', 'Mixed', 'Presence (40%)', 'General (60%)',
                 'Presence (40%)', 'Presence (40%)', 'General (60%)', 'Presence (40%)'],
        'Status': ['Pending'] * 15
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
        theme_filter = st.multiselect(
            "Filter by Theme:",
            options=df['Theme'].unique(),
            default=df['Theme'].unique()
        )
    
    with col3:
        focus_filter = st.multiselect(
            "Filter by Focus:",
            options=df['Focus'].unique(),
            default=df['Focus'].unique()
        )
    
    # Filter dataframe
    filtered_df = df[
        (df['Platform'].isin(platform_filter)) &
        (df['Theme'].isin(theme_filter)) &
        (df['Focus'].isin(focus_filter))
    ]
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # Visual timeline
    st.markdown("### 📊 Content Distribution by Platform")
    
    platform_counts = df['Platform'].value_counts()
    
    fig = px.bar(
        x=platform_counts.index,
        y=platform_counts.values,
        labels={'x': 'Platform', 'y': 'Number of Posts'},
        title='Planned Posts per Platform',
        color=platform_counts.index,
        color_discrete_map={
            'LinkedIn': '#0A66C2',
            'Instagram': '#E4405F',
            'Twitter/X': '#1DA1F2'
        }
    )
    
    st.plotly_chart(fig, use_container_width=True)

elif page == "KPIs & Goals":
    st.title("🎯 KPIs & Strategic Goals")
    
    st.markdown("""
    <div class="highlight">
    <h3>⚠️ Month 1 Philosophy: Foundation Over Growth</h3>
    <p>January focuses on building sustainable systems, learning the brand voice, and understanding 
    what resonates with the audience. Significant growth typically happens in months 2-4.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Goals columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Growth Targets")
        st.metric("Follower Growth", "1-3%", "Conservative", help="Focus on foundation building")
        st.metric("Engagement Rate", "0-2%", "Improvement", help="Maintain or slightly improve baseline")
        st.metric("Post Consistency", "80-90%", "Completion Rate", help="12-15 posts across platforms")
        
        st.markdown("""
        #### Why Conservative Targets?
        - Building brand presence and audience understanding
        - January typically shows slower engagement post-holidays
        - Algorithm optimization requires consistent posting patterns
        - Quality foundation enables sustainable long-term growth
        """)
    
    with col2:
        st.markdown("### ✅ Strategic Objectives")
        
        st.markdown("""
        **Infrastructure:**
        - Establish content calendar and workflow
        - Build reusable content templates
        - Set up comprehensive analytics tracking
        
        **Engagement:**
        - Respond to all engagement within 24-48 hours
        - Build relationships with 10-15 key industry accounts
        - Foster active community discussions
        
        **Business Impact:**
        - Generate 2-5 qualified inquiries
        - Increase website traffic from social channels
        - Establish Purple Crayolá as industry thought leader
        """)
    
    st.divider()
    
    # Metrics to track
    st.markdown("### 📊 Key Performance Indicators")
    
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    
    with metrics_col1:
        st.markdown("""
        **Engagement Metrics**
        - Likes per post
        - Comments per post
        - Shares/Saves
        - Story views
        - Story interactions
        """)
    
    with metrics_col2:
        st.markdown("""
        **Growth Metrics**
        - Follower count
        - Reach & impressions
        - Profile visits
        - Website clicks
        - New connections
        """)
    
    with metrics_col3:
        st.markdown("""
        **Business Impact**
        - DM inquiries
        - Consultation requests
        - Website traffic from social
        - Lead generation
        - Average response time
        """)
    
    st.divider()
    
    # 90-day vision
    st.markdown("### 🚀 90-Day Growth Vision")
    
    months_data = {
        'Month': ['January', 'February', 'March'],
        'Focus': ['Foundation & Learning', 'Optimization & Iteration', 'Consistency & Refinement'],
        'Expected Growth': ['1-3%', '3-5%', '5-8%'],
        'Key Activities': [
            'Build systems, learn audience, establish consistency',
            'Optimize based on data, refine content approach',
            'Scale proven content types, expand successful formats'
        ]
    }
    
    months_df = pd.DataFrame(months_data)
    st.table(months_df)
    
    st.markdown("""
    <div class="highlight">
    <h4>💡 Strategic Approach</h4>
    <p>This strategy prioritizes building a strong foundation in January—consistent 
    quality content, understanding audience preferences, and establishing robust systems. 
    Growth will be gradual and sustainable, with each month building on learnings from 
    the previous period. Significant momentum typically develops in months 3-6 as 
    audience relationships deepen and content strategy matures.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; padding: 30px 20px; background: white; border-radius: 12px; margin-top: 40px;">
    <h4 style="color: #6B46C1; margin-bottom: 10px;">🎨 Purple Crayolá Content Strategy</h4>
    <p style="color: #64748b; margin: 5px 0;">January 2026 - Strategic Digital Transformation</p>
    <p style="font-size: 12px; color: #94a3b8; margin-top: 15px;">Developed by Oluwatosin Adejumo • Version 1.0</p>
</div>
""", unsafe_allow_html=True)