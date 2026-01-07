import streamlit as st
import pandas as pd
from datetime import datetime
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
    
    .metric-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        border-left: 4px solid #6B46C1;
        min-height: 140px;
    }
    
    .metric-label {
        font-size: 14px;
        font-weight: 500;
        color: #64748b;
        margin-bottom: 10px;
    }
    
    .metric-value {
        font-size: 36px;
        font-weight: 700;
        color: #1e293b;
        margin: 0;
    }
    
    .metric-delta {
        font-size: 13px;
        color: #10b981;
        margin-top: 8px;
    }
    
    .content-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        margin-bottom: 20px;
        border-top: 3px solid #6B46C1;
    }
    
    .week-card {
        background: linear-gradient(135deg, #EDE9FE 0%, #DBEAFE 100%);
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #6B46C1;
        margin: 15px 0;
    }
    
    .post-card {
        background: white;
        padding: 20px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 3px solid #9F7AEA;
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
    
    .warning-box {
        background: #FEF3C7;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #F59E0B;
        margin: 15px 0;
    }
    
    .success-box {
        background: #D1FAE5;
        padding: 20px;
        border-radius: 10px;
        border-left: 4px solid #10B981;
        margin: 15px 0;
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
    
    .platform-badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        margin-right: 8px;
    }
    
    .linkedin-badge {
        background: #0A66C2;
        color: white;
    }
    
    .instagram-badge {
        background: #E4405F;
        color: white;
    }
    
    .twitter-badge {
        background: #1DA1F2;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
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
        ["Executive Summary", "Strategic Approach", "Weekly Breakdown", "Content Examples", "Platform Strategy", "Content Calendar", "KPIs & Success Metrics", "Implementation Guide"]
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
    st.caption("**Strategy Period:** January 6-31, 2026")
    st.caption("**Document Version:** 2.0 (Revised)")

# Main content
if page == "Executive Summary":
    st.title("🎨 Purple Crayolá - January 2026 Content Strategy")
    st.markdown("### Revised & Optimized for Maximum Impact")
    st.markdown("**Strategy Period:** January 6 - January 31, 2026")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Total Posts</p>
                <p class="metric-value">16</p>
                <p class="metric-delta">↑ 4 posts/week</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Platforms</p>
                <p class="metric-value">3</p>
                <p class="metric-delta">↑ LinkedIn, Instagram, X</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Content Pillars</p>
                <p class="metric-value">5</p>
                <p class="metric-delta">↑ Balanced Mix</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div class="metric-card">
                <p class="metric-label">Growth Target</p>
                <p class="metric-value">3-5%</p>
                <p class="metric-delta">↑ Realistic & Achievable</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Strategy Improvements
    st.markdown("## 🎯 Key Strategy Improvements")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>✅ What's New</h4>
        <ul>
        <li><strong>Phased Presence Launch:</strong> Build brand awareness first (Weeks 1-2), then introduce Presence (Weeks 3-4)</li>
        <li><strong>Platform-Optimized Content:</strong> Unique content for each platform's algorithm</li>
        <li><strong>Reels & Video Focus:</strong> Critical for Instagram growth in 2026</li>
        <li><strong>Daily Engagement Plan:</strong> Not just posting - active community building</li>
        <li><strong>Realistic Posting Schedule:</strong> 4 posts/week with strategic timing</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4>⚠️ Critical Changes from V1.0</h4>
        <ul>
        <li><strong>Delayed Presence Launch:</strong> Moved from Week 2 to Week 4 (build trust first)</li>
        <li><strong>Shorter Captions:</strong> Reduced by 40% for better engagement</li>
        <li><strong>More Video Content:</strong> 30% of content now video/Reels</li>
        <li><strong>Daily Twitter Activity:</strong> 1-3 posts daily vs scheduled only</li>
        <li><strong>Enhanced CTAs:</strong> Specific, action-driven calls-to-action</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Brand Context
    st.markdown("## 🏢 Brand Overview")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Purple Crayolá** is a full-service digital transformation agency delivering design 
        and digital solutions that transform customer experiences and business results.
        
        **Core Services:**
        - 🎯 Digital Strategy & Transformation
        - 💻 Web & Mobile App Development
        - 📱 Digital Marketing (SEO, Content, Social Media, PPC)
        - 🎨 Branding & Identity Design
        - 📊 Project & Product Management
        - 📚 Digital Learning Solutions
        - ✨ **Presence**: Personal Branding for Leaders (NEW)
        
        **PURPLE Values:**
        - **P**assionate - Heart and soul in every project
        - **U**nique - 'You'nique collaboration approach
        - **R**esolute - Unwavering commitment to excellence
        - **P**eople-Driven - Relationships are everything
        - **L**eadership - Empowering at every level
        - **E**nterprising - Always innovating
        """)
    
    with col2:
        st.markdown("""
        <div class="highlight">
        <h4>January Focus Areas</h4>
        <p><strong>Weeks 1-2 (60%):</strong><br>
        Brand awareness, credibility building, digital transformation expertise</p>
        
        <p><strong>Weeks 3-4 (40%):</strong><br>
        Presence introduction, personal branding education, PRISM Framework™</p>
        
        <p><strong>Target Audience:</strong><br>
        • Nigerian businesses seeking digital transformation<br>
        • Professionals needing personal branding<br>
        • Executives & founders<br>
        • Diaspora professionals</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Content Pillars
    st.markdown("## 📊 Content Pillars Distribution")
    
    pillars_data = {
        'Pillar': ['Educational', 'Promotional', 'Social Proof', 'Behind-the-Scenes', 'Engagement'],
        'Percentage': [35, 25, 20, 10, 10],
        'Description': [
            'Tips, insights, how-tos, industry trends',
            'Services showcase, Presence promotion',
            'Testimonials, case studies, results',
            'Team, culture, process transparency',
            'Polls, questions, community discussions'
        ]
    }
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        fig = go.Figure(data=[go.Pie(
            labels=pillars_data['Pillar'],
            values=pillars_data['Percentage'],
            hole=.4,
            marker_colors=['#6B46C1', '#9F7AEA', '#D6BCFA', '#EDE9FE', '#C4B5FD']
        )])
        
        fig.update_layout(
            title="Content Mix Strategy",
            height=400,
            showlegend=True
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        df_pillars = pd.DataFrame(pillars_data)
        st.dataframe(df_pillars, hide_index=True, use_container_width=True)
    
    st.divider()
    
    # Success Metrics Preview
    st.markdown("## 🎯 Success Metrics (Quick View)")
    
    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)
    
    with metrics_col1:
        st.markdown("""
        **Growth Targets**
        - Follower Growth: 3-5%
        - Engagement Rate: 2-4%
        - Profile Visits: +15%
        """)
    
    with metrics_col2:
        st.markdown("""
        **Engagement Goals**
        - Avg Comments: 5-10/post
        - Avg Shares: 3-5/post
        - Story Views: 100-200
        """)
    
    with metrics_col3:
        st.markdown("""
        **Business Impact**
        - Consultation Requests: 3-7
        - Website Traffic: +20%
        - DM Inquiries: 10-15
        """)

elif page == "Strategic Approach":
    st.title("🎯 Strategic Approach")
    
    st.markdown("""
    <div class="highlight">
    <h3>Core Philosophy: Foundation Before Flight</h3>
    <p>January is about building trust, establishing credibility, and creating sustainable systems. 
    We're not chasing viral posts - we're building a brand that lasts.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Phased Approach
    st.markdown("## 📅 4-Week Phased Approach")
    
    # Week 1
    st.markdown("""
    <div class="week-card">
    <h3>Week 1 (Jan 6-10): Brand Foundation 🏗️</h3>
    <p><strong>Goal:</strong> Introduce Purple Crayolá, establish expertise, build initial audience trust</p>
    
    <p><strong>Content Focus:</strong></p>
    <ul>
    <li>Digital transformation insights and trends</li>
    <li>Company introduction and values</li>
    <li>Industry commentary and thought leadership</li>
    <li>Team introduction (behind-the-scenes)</li>
    </ul>
    
    <p><strong>Key Message:</strong> "Purple Crayolá is your partner in digital transformation"</p>
    <p><strong>Success Metric:</strong> Establish baseline engagement, 50+ new followers</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Week 2
    st.markdown("""
    <div class="week-card">
    <h3>Week 2 (Jan 13-17): Credibility Building 📈</h3>
    <p><strong>Goal:</strong> Demonstrate expertise through value-driven content and social proof</p>
    
    <p><strong>Content Focus:</strong></p>
    <ul>
    <li>Educational content (how-tos, tips, frameworks)</li>
    <li>Client success stories (if available) or case studies</li>
    <li>Process transparency (how we work)</li>
    <li>Industry insights and analysis</li>
    </ul>
    
    <p><strong>Key Message:</strong> "We deliver real results for real businesses"</p>
    <p><strong>Success Metric:</strong> 2-3 consultation inquiries, 10%+ engagement rate</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Week 3
    st.markdown("""
    <div class="week-card">
    <h3>Week 3 (Jan 20-24): Presence Teasing 👀</h3>
    <p><strong>Goal:</strong> Introduce personal branding concept, build anticipation for Presence</p>
    
    <p><strong>Content Focus:</strong></p>
    <ul>
    <li>Personal branding education (why it matters)</li>
    <li>Professional visibility insights</li>
    <li>Subtle Presence teasers ("something is coming")</li>
    <li>Thought leadership on expertise vs visibility</li>
    </ul>
    
    <p><strong>Key Message:</strong> "Expertise without visibility is opportunity lost"</p>
    <p><strong>Success Metric:</strong> 100+ story views, 20+ DM inquiries about "what's coming"</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Week 4
    st.markdown("""
    <div class="week-card">
    <h3>Week 4 (Jan 27-31): Presence Launch 🚀</h3>
    <p><strong>Goal:</strong> Officially launch Presence, drive consultation bookings</p>
    
    <p><strong>Content Focus:</strong></p>
    <ul>
    <li>Presence official announcement</li>
    <li>PRISM Framework™ introduction and education</li>
    <li>Package breakdown and value proposition</li>
    <li>Early testimonials and case studies</li>
    <li>Limited-time launch offer (optional)</li>
    </ul>
    
    <p><strong>Key Message:</strong> "Own your story. Command your space. Lead with Presence."</p>
    <p><strong>Success Metric:</strong> 5-10 discovery call bookings, 200+ landing page visits</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Platform Strategy Overview
    st.markdown("## 📱 Platform Strategy Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="content-card">
        <h4>💼 LinkedIn</h4>
        <p><strong>Frequency:</strong> 3-4 posts/week</p>
        <p><strong>Best Times:</strong> Tues-Thurs, 9-11 AM</p>
        <p><strong>Focus:</strong> Thought leadership, long-form insights, B2B content</p>
        <p><strong>Content Types:</strong></p>
        <ul>
        <li>Carousels (5-8 slides)</li>
        <li>Text posts with insights</li>
        <li>Articles (monthly)</li>
        <li>Polls & questions</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
        <h4>📸 Instagram</h4>
        <p><strong>Frequency:</strong> 4-5 posts/week + daily stories</p>
        <p><strong>Best Times:</strong> Mon-Fri, 12-1 PM, 7-9 PM</p>
        <p><strong>Focus:</strong> Visual storytelling, culture, behind-the-scenes</p>
        <p><strong>Content Types:</strong></p>
        <ul>
        <li>Reels (2-3/week)</li>
        <li>Carousels (2/week)</li>
        <li>Stories (daily)</li>
        <li>Single posts</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="content-card">
        <h4>🐦 Twitter/X</h4>
        <p><strong>Frequency:</strong> 1-3 posts/day</p>
        <p><strong>Best Times:</strong> Throughout day, 9 AM, 12 PM, 6 PM</p>
        <p><strong>Focus:</strong> Real-time engagement, quick insights, community</p>
        <p><strong>Content Types:</strong></p>
        <ul>
        <li>Threads (2/week)</li>
        <li>Single tweets</li>
        <li>Quote tweets</li>
        <li>Polls</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Content Creation Workflow
    st.markdown("## 🔄 Content Creation Workflow")
    
    workflow_data = {
        'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        'Activity': [
            'Content Planning & Ideation',
            'Content Creation & Design',
            'Content Scheduling & Review',
            'Posting & Engagement',
            'Analytics Review & Adjustment'
        ],
        'Time Required': ['2 hours', '3-4 hours', '2 hours', '2-3 hours', '1-2 hours'],
        'Deliverables': [
            'Weekly content calendar approved',
            'All graphics, videos, captions ready',
            'Content scheduled across platforms',
            'Active engagement, DM responses',
            'Weekly report, next week adjustments'
        ]
    }
    
    df_workflow = pd.DataFrame(workflow_data)
    st.dataframe(df_workflow, hide_index=True, use_container_width=True)
    
    st.markdown("""
    <div class="highlight">
    <h4>💡 Pro Tip: Batch Content Creation</h4>
    <p>Create 1 week of content in 1-2 focused sessions. This ensures consistency, 
    reduces daily stress, and maintains quality standards.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Weekly Breakdown":
    st.title("📅 Weekly Content Breakdown")
    
    week = st.selectbox(
        "Select Week:",
        ["Week 1: January 6-10 (Brand Foundation)",
         "Week 2: January 13-17 (Credibility Building)",
         "Week 3: January 20-24 (Presence Teasing)",
         "Week 4: January 27-31 (Presence Launch)"]
    )
    
    if "Week 1" in week:
        st.markdown("## 🏗️ Week 1: Brand Foundation (January 6-10)")
        st.markdown("**Goal:** Introduce Purple Crayolá and establish initial credibility")
        
        st.markdown("---")
        
        # Monday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Monday, January 6</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        
        <h5>🎯 Post: Welcome to 2026 - Digital Transformation Focus</h5>
        
        <p><strong>LinkedIn Caption (150 words):</strong></p>
        <p><em>"2026 is the year of digital transformation. As Nigerian businesses reset and reimagine their strategies, one question matters most: Is your digital infrastructure ready to scale?
        
        At Purple Crayolá, we partner with forward-thinking organizations to transform digital experiences that drive real business results.
        
        Whether it's web development, digital marketing, or complete digital transformation—we're here to turn your vision into reality.
        
        Let's make 2026 your growth year. 📈
        
        Book a free digital audit: purplecrayola.com"</em></p>
        
        <p><strong>Instagram Caption (100 words):</strong></p>
        <p><em>"2026: Your year of digital transformation 🚀
        
        Is your digital infrastructure ready to scale?
        
        At Purple Crayolá, we transform digital experiences that drive real results.
        
        Web dev | Digital marketing | Branding | Complete transformation
        
        Let's make 2026 your growth year 📈
        
        Link in bio for free digital audit ✨"</em></p>
        
        <p><strong>Twitter/X Thread (5 tweets):</strong></p>
        <p><em>1/ 2026 is here. And for Nigerian businesses, the digital transformation opportunity has never been bigger.
        
        Here's what's changing (and why it matters): 🧵
        
        2/ Consumers expect seamless digital experiences. Your website, social media, customer service—it all needs to work together.
        
        3/ AI and automation are no longer "nice to have." They're competitive advantages that save time and increase efficiency.
        
        4/ Personal branding for leaders is becoming critical. People buy from people they trust and know.
        
        5/ At Purple Crayolá, we help businesses and leaders navigate this transformation.
        
        Ready to scale in 2026? Let's talk: purplecrayola.com</em></p>
        
        <p><strong>Content Type:</strong> Carousel (5 slides) showing digital transformation trends</p>
        <p><strong>Design:</strong> Professional, modern, Purple Crayolá branding</p>
        <p><strong>CTA:</strong> Book free digital audit consultation</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tuesday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Tuesday, January 7</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        
        <h5>👥 Post: Meet Purple Crayolá - Behind the Scenes</h5>
        
        <p><strong>LinkedIn Caption:</strong></p>
        <p><em>"Behind every successful project is a team that lives and breathes our PURPLE values:
        
        💜 Passionate - Heart and soul in every project
        💜 Unique - 'You'nique collaboration approach
        💜 Resolute - Unwavering commitment to excellence
        💜 People-Driven - Relationships matter most
        💜 Leadership - Empowering at every level
        💜 Enterprising - Always innovating
        
        These aren't just words on a wall. They're the foundation of how we work, create, and deliver for our clients.
        
        When you work with Purple Crayolá, you're not just hiring a vendor—you're partnering with people who genuinely care about your success.
        
        Want to experience the difference? Let's connect."</em></p>
        
        <p><strong>Instagram:</strong> Reel showing team collaboration, office culture, behind-the-scenes moments</p>
        <p><strong>Content Type:</strong> Team photo + values graphic OR Behind-the-scenes Reel</p>
        <p><strong>CTA:</strong> "Follow us for more behind-the-scenes content"</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Wednesday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Wednesday, January 8</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        
        <h5>📚 Educational Post: 5 Signs Your Business Needs Digital Transformation</h5>
        
        <p><strong>LinkedIn Carousel (7 slides):</strong></p>
        <ol>
        <li>Cover: "5 Signs You Need Digital Transformation"</li>
        <li>Your website looks outdated (and customers notice)</li>
        <li>You're losing customers to competitors with better digital experiences</li>
        <li>Manual processes are slowing down your team</li>
        <li>You're not tracking data or using analytics effectively</li>
        <li>Your marketing feels scattered across platforms</li>
        <li>CTA: "Ready to transform? Let's talk."</li>
        </ol>
        
        <p><strong>Instagram:</strong> Reel version (15-30 seconds) hitting these 5 points quickly</p>
        <p><strong>Design:</strong> Bold, numbered format, easy to digest</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Thursday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Thursday, January 9</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        
        <h5>💡 Thought Leadership: The State of Nigerian Tech in 2026</h5>
        
        <p><strong>LinkedIn:</strong> Short article or long-form post (200-250 words) on trends, opportunities, challenges in Nigerian tech ecosystem</p>
        
        <p><strong>Twitter/X:</strong> Engagement thread asking "What's your biggest digital challenge in 2026?" + respond to replies</p>
        
        <p><strong>Purpose:</strong> Position Purple Crayolá as industry thought leader</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Friday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Friday, January 10</h4>
        <span class="platform-badge instagram-badge">Instagram</span>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        
        <h5>🎉 Friday Wrap-Up & Weekend Engagement</h5>
        
        <p><strong>Instagram:</strong> Stories recap of the week + poll "What content did you enjoy most this week?"</p>
        
        <p><strong>Twitter/X:</strong> Weekend inspiration tweet + community question</p>
        
        <p><strong>Example Tweet:</strong></p>
        <p><em>"Happy Friday! 🎉
        
        This week we talked about digital transformation, our PURPLE values, and the signs your business needs to evolve.
        
        Question for the weekend: What's one digital goal you want to achieve in Q1 2026?
        
        Drop it below 👇"</em></p>
        
        <p><strong>Purpose:</strong> Build community engagement and end week on positive note</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif "Week 2" in week:
        st.markdown("## 📈 Week 2: Credibility Building (January 13-17)")
        st.markdown("**Goal:** Demonstrate expertise and build trust through value-driven content")
        
        st.markdown("---")
        
        # Monday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Monday, January 13</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        
        <h5>📚 Educational: Digital Marketing ROI Framework</h5>
        
        <p><strong>LinkedIn Carousel (6 slides):</strong></p>
        <ol>
        <li>Cover: "How to Calculate Your Digital Marketing ROI"</li>
        <li>Why ROI matters (not just vanity metrics)</li>
        <li>Formula: (Revenue - Investment) / Investment × 100</li>
        <li>What to track: Website traffic, leads, conversions, customer value</li>
        <li>Common mistakes to avoid</li>
        <li>CTA: "Need help tracking ROI? Let's chat."</li>
        </ol>
        
        <p><strong>Instagram:</strong> Single post graphic with simplified ROI formula + quick tips</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tuesday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Tuesday, January 14</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        
        <h5>💼 Case Study/Process Showcase</h5>
        
        <p><strong>LinkedIn:</strong> "How We Approach Digital Transformation Projects" - Behind-the-scenes look at Purple Crayolá's methodology</p>
        
        <p><strong>Content Structure:</strong></p>
        <ul>
        <li>Discovery & Audit phase</li>
        <li>Strategy Development</li>
        <li>Implementation & Testing</li>
        <li>Launch & Optimization</li>
        <li>Ongoing Support</li>
        </ul>
        
        <p><strong>Twitter/X:</strong> Thread breaking down the process in bite-sized insights</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Wednesday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Wednesday, January 15</h4>
        <span class="platform-badge instagram-badge">Instagram</span>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        
        <h5>🎥 Video/Reel: "Day in the Life" or "How We Create"</h5>
        
        <p><strong>Instagram Reel (30-45 seconds):</strong> Behind-the-scenes of creating a website, designing a brand, or running a campaign</p>
        
        <p><strong>Twitter/X:</strong> Share Reel with commentary + engagement question</p>
        
        <p><strong>Purpose:</strong> Humanize brand, show process, build connection</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Thursday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Thursday, January 16</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        
        <h5>🌟 Social Proof: Client Success Story or Testimonial</h5>
        
        <p><strong>LinkedIn Post:</strong> Share a client success story (anonymized if needed) or testimonial</p>
        
        <p><strong>Structure:</strong></p>
        <ul>
        <li>The Challenge: What problem they faced</li>
        <li>The Solution: How Purple Crayolá helped</li>
        <li>The Results: Measurable outcomes</li>
        <li>Client Quote: Testimonial</li>
        </ul>
        
        <p><strong>Alternative (if no clients yet):</strong> "What Our Clients Can Expect" - showcase your process and commitment</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Friday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Friday, January 17</h4>
        <span class="platform-badge instagram-badge">Instagram</span>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        
        <h5>💡 Quick Win Tips: Weekend Value Drop</h5>
        
        <p><strong>Instagram Carousel (5 slides):</strong> "5 Quick Wins to Improve Your Website This Weekend"</p>
        <ol>
        <li>Optimize page load speed</li>
        <li>Update your About page</li>
        <li>Add clear CTAs</li>
        <li>Check mobile responsiveness</li>
        <li>Update contact information</li>
        </ol>
        
        <p><strong>LinkedIn:</strong> Poll "Which website improvement are you tackling this weekend?"</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif "Week 3" in week:
        st.markdown("## 👀 Week 3: Presence Teasing (January 20-24)")
        st.markdown("**Goal:** Introduce personal branding concepts and build anticipation")
        
        st.markdown("---")
        
        # Monday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Monday, January 20</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        
        <h5>🎯 Thought Leadership: Why Professional Visibility Matters</h5>
        
        <p><strong>LinkedIn Post (180 words):</strong></p>
        <p><em>"Your expertise is undeniable. Your work speaks for itself.
        
        But here's the uncomfortable truth: In 2026, excellence without visibility is opportunity lost.
        
        Decision-makers don't have time to search for hidden talent. They go with who's visible:
        
        • The executive with a clear LinkedIn presence
        • The consultant whose insights they've been following
        • The professional they feel they already 'know'
        
        This isn't about becoming an influencer. It's about strategic positioning—ensuring the right people find you at the right time.
        
        Your competitors aren't just companies anymore. They're individuals building platforms, thought leadership, and trust.
        
        The question isn't whether you need visibility. It's whether you're willing to be intentional about it.
        
        What's your take? Does professional visibility matter in your industry?"</em></p>
        
        <p><strong>Instagram:</strong> Quote graphic "Excellence without visibility is opportunity lost"</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tuesday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Tuesday, January 21</h4>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        
        <h5>📊 Educational Thread: Personal Branding Fundamentals</h5>
        
        <p><strong>Twitter/X Thread (7 tweets):</strong></p>
        <p><em>1/ Personal branding isn't vanity. It's visibility with purpose.
        
        Here's why it matters in 2026: 🧵
        
        2/ The marketplace is crowded. Your competitors aren't just companies—they're individuals building platforms and thought leadership.
        
        3/ Decision-makers research people, not just companies. Before that meeting, that deal, that opportunity—people Google you.
        
        4/ Your network is your net worth. But strong networks aren't built in shadows. Visibility attracts connection.
        
        5/ Opportunities follow visibility. Speaking gigs. Board positions. Partnerships. They don't find hidden talent.
        
        6/ Trust is built through consistent presence. One post won't change your career. But showing up consistently builds credibility.
        
        7/ Your voice is your competitive advantage. Your experience is unique. Your perspective is valuable. But if no one hears it, it doesn't create impact."</em></p>
        
        <p><strong>Instagram Stories:</strong> Poll series "Do you have a personal brand strategy?" "What's holding you back?"</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Wednesday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Wednesday, January 22</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        
        <h5>💭 Thought Piece: Expertise vs Visibility</h5>
        
        <p><strong>LinkedIn Post:</strong> Long-form reflection on the gap between expertise and visibility</p>
        
        <p><strong>Key Points:</strong></p>
        <ul>
        <li>Many professionals spend years building expertise but never develop visibility</li>
        <li>The hidden cost of being invisible professionally</li>
        <li>How visibility amplifies impact</li>
        <li>Subtle hint: "We're building something to help bridge this gap"</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Thursday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Thursday, January 23</h4>
        <span class="platform-badge instagram-badge">Instagram</span>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        
        <h5>👀 Subtle Teaser: "Something is Coming"</h5>
        
        <p><strong>Instagram:</strong> Aesthetic teaser post or Reel with cryptic but intriguing message</p>
        
        <p><strong>Caption Example:</strong></p>
        <p><em>"Excellence matters. But visibility shapes opportunity.
        
        For too long, talented professionals have remained invisible—brilliant at what they do, but unknown for it.
        
        That's about to change.
        
        Something intentional. Something strategic. Something human.
        
        Coming soon. 👀"</em></p>
        
        <p><strong>LinkedIn:</strong> Similar teaser with professional tone</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Friday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Friday, January 24</h4>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        
        <h5>🎯 Engagement & Build Curiosity</h5>
        
        <p><strong>Twitter/X:</strong> "Next week, we're unveiling something we've been building for leaders, founders, and professionals ready to own their story. Stay tuned. 👀"</p>
        
        <p><strong>Instagram Stories:</strong> Countdown sticker "3 days until launch" + behind-the-scenes of "the project"</p>
        
        <p><strong>Purpose:</strong> Build anticipation for Presence launch</p>
        </div>
        """, unsafe_allow_html=True)
    
    else:  # Week 4
        st.markdown("## 🚀 Week 4: Presence Launch (January 27-31)")
        st.markdown("**Goal:** Officially launch Presence and drive discovery call bookings")
        
        st.markdown("---")
        
        # Monday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Monday, January 27</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        
        <h5>🎉 PRESENCE LAUNCH ANNOUNCEMENT</h5>
        
        <p><strong>LinkedIn Post (200 words):</strong></p>
        <p><em>"Introducing Presence by Purple Crayolá 💜
        
        Your expertise is strong. But is your visibility matching your impact?
        
        Presence is our signature personal branding experience for individuals ready to evolve how they show up—online and offline.
        
        Built on the PRISM Framework™, Presence transforms your experience, values, and voice into an identity that:
        • Opens doors before you enter the room
        • Builds trust before the first conversation
        • Positions you as the authority you are
        
        For executives, founders, creatives, diaspora professionals, and mission-driven leaders ready to own their story and command their space.
        
        This isn't just branding. It's your Presence.
        
        Learn more: purplecrayola.com/presence
        
        Ready to build your Presence? DM us 'PRESENCE' or book a discovery call."</em></p>
        
        <p><strong>Instagram:</strong> Eye-catching carousel (7-8 slides) introducing Presence</p>
        <p><strong>Twitter/X:</strong> Launch thread with key details</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tuesday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Tuesday, January 28</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        
        <h5>💎 Deep Dive: PRISM Framework™ Introduction</h5>
        
        <p><strong>LinkedIn Carousel (8 slides):</strong></p>
        <ol>
        <li>Cover: "The PRISM Framework™"</li>
        <li>What is PRISM? (Like a prism transforms light, we transform your brand)</li>
        <li>P - Position: Clarify your foundation</li>
        <li>R - Refine: Shape your identity</li>
        <li>I - Ignite: Launch with intention</li>
        <li>S - Signal: Sustain visibility</li>
        <li>M - Multiply: Expand your impact</li>
        <li>CTA: "Ready to discover your Presence?"</li>
        </ol>
        
        <p><strong>Instagram:</strong> Reel explaining PRISM in 30 seconds</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Wednesday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Wednesday, January 29</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        
        <h5>📦 Presence Packages Breakdown</h5>
        
        <p><strong>LinkedIn:</strong> Infographic or carousel showing 4 Presence packages</p>
        
        <p><strong>Packages:</strong></p>
        <ul>
        <li>🟣 Presence Core - Foundation & Clarity</li>
        <li>🟣 Presence Pro - Align & Activate</li>
        <li>🟣 Presence Elite - Scale with Influence</li>
        <li>✳️ Presence Launchpad - Consistent Content</li>
        </ul>
        
        <p><strong>Twitter/X:</strong> Thread breaking down who each package is for</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Thursday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Thursday, January 30</h4>
        <span class="platform-badge instagram-badge">Instagram</span>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        
        <h5>🌟 Testimonials & Social Proof</h5>
        
        <p><strong>Instagram:</strong> Carousel featuring client testimonials from Presence document</p>
        
        <p><strong>Testimonials to highlight:</strong></p>
        <ul>
        <li>"This process brought clarity, language, and strategy..." - Global Scheme Ops Leader, Fintech</li>
        <li>"This journey gave structure to my experience..." - CEO, Global Private Healthcare</li>
        </ul>
        
        <p><strong>LinkedIn:</strong> Case study-style post showing transformation journey</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Friday
        st.markdown("""
        <div class="post-card">
        <h4>📅 Friday, January 31</h4>
        <span class="platform-badge linkedin-badge">LinkedIn</span>
        <span class="platform-badge instagram-badge">Instagram</span>
        <span class="platform-badge twitter-badge">Twitter/X</span>
        
        <h5>🎯 Final CTA: Month-End Wrap + Strong Call-to-Action</h5>
        
        <p><strong>All Platforms:</strong> Month recap + Presence CTA</p>
        
        <p><strong>Example Post:</strong></p>
        <p><em>"January was about laying the foundation.
        
        We introduced you to Purple Crayolá, our values, our approach to digital transformation.
        
        And this week, we launched Presence—for leaders ready to align their expertise with their visibility.
        
        Your work speaks louder than your visibility. It's time to align the two.
        
        Own your story. Command your space. Lead with Presence.
        
        📅 Book your discovery call: purplecrayola.com/presence
        💬 DM us 'PRESENCE' to learn more
        
        Let's build together. 💜"</em></p>
        
        <p><strong>Instagram:</strong> High-impact visual with strong CTA</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Content Examples":
    st.title("✍️ Content Examples & Templates")
    
    content_type = st.selectbox(
        "Select Content Type:",
        ["LinkedIn Carousels", "Instagram Reels", "Twitter Threads", "Captions Templates"]
    )
    
    if content_type == "LinkedIn Carousels":
        st.markdown("## 📊 LinkedIn Carousel Templates")
        
        st.markdown("""
        <div class="highlight">
        <h4>Carousel Best Practices</h4>
        <ul>
        <li><strong>Slides:</strong> 5-10 slides optimal (attention span sweet spot)</li>
        <li><strong>First Slide:</strong> Eye-catching hook with clear value proposition</li>
        <li><strong>Middle Slides:</strong> Numbered points, one concept per slide</li>
        <li><strong>Last Slide:</strong> Strong CTA with brand logo</li>
        <li><strong>Design:</strong> Consistent colors, large fonts, minimal text</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Template 1
        st.markdown("""
        <div class="content-card">
        <h4>Template 1: "X Signs You Need [Solution]"</h4>
        
        <p><strong>Structure:</strong></p>
        <ol>
        <li><strong>Slide 1 (Cover):</strong> "5 Signs You Need Digital Transformation"</li>
        <li><strong>Slides 2-6 (Signs):</strong> One sign per slide with brief explanation</li>
        <li><strong>Slide 7 (CTA):</strong> "Ready to transform? Book a free audit."</li>
        </ol>
        
        <p><strong>Caption Template:</strong></p>
        <p><em>"Is your business ready for 2026?
        
        Here are 5 clear signs you need digital transformation 👉
        
        [Brief intro - 2-3 sentences]
        
        If any of these resonate, it's time to evolve.
        
        [CTA]"</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Template 2
        st.markdown("""
        <div class="content-card">
        <h4>Template 2: "How to [Achieve Goal]"</h4>
        
        <p><strong>Structure:</strong></p>
        <ol>
        <li><strong>Slide 1:</strong> "How to Build a Personal Brand in 2026"</li>
        <li><strong>Slides 2-7:</strong> Step-by-step process</li>
        <li><strong>Slide 8:</strong> "Need help? We've got you covered."</li>
        </ol>
        
        <p><strong>Makes content:</strong> Actionable, educational, shareable</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Template 3
        st.markdown("""
        <div class="content-card">
        <h4>Template 3: "Common Mistakes in [Topic]"</h4>
        
        <p><strong>Structure:</strong></p>
        <ol>
        <li><strong>Slide 1:</strong> "5 Digital Marketing Mistakes Costing You Money"</li>
        <li><strong>Slides 2-6:</strong> Mistake + Why it matters + Quick fix</li>
        <li><strong>Slide 7:</strong> "Avoid these mistakes. Let's work together."</li>
        </ol>
        
        <p><strong>Psychology:</strong> People love avoiding mistakes (loss aversion)</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif content_type == "Instagram Reels":
        st.markdown("## 🎥 Instagram Reels Script Templates")
        
        st.markdown("""
        <div class="highlight">
        <h4>Reels Best Practices</h4>
        <ul>
        <li><strong>Length:</strong> 15-45 seconds (shorter = better retention)</li>
        <li><strong>Hook:</strong> First 1-2 seconds must grab attention</li>
        <li><strong>Trending Audio:</strong> Use when relevant to boost reach</li>
        <li><strong>Text Overlays:</strong> Essential (80% watch without sound)</li>
        <li><strong>CTA:</strong> End with clear next step</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Reel Template 1
        st.markdown("""
        <div class="content-card">
        <h4>Reel Template 1: "3 Quick Tips"</h4>
        
        <p><strong>Script (30 seconds):</strong></p>
        
        <p><strong>Hook (0-3s):</strong> "3 ways to improve your website TODAY 👇"</p>
        
        <p><strong>Tip 1 (3-13s):</strong> "1. Check your page speed. Slow sites lose 40% of visitors."</p>
        
        <p><strong>Tip 2 (13-23s):</strong> "2. Add clear CTAs. Tell people exactly what to do next."</p>
        
        <p><strong>Tip 3 (23-28s):</strong> "3. Mobile optimization. 60% browse on phones."</p>
        
        <p><strong>CTA (28-30s):</strong> "Need help? DM us!"</p>
        
        <p><strong>Visual:</strong> Quick transitions, text overlays, on-brand colors</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Reel Template 2
        st.markdown("""
        <div class="content-card">
        <h4>Reel Template 2: "Behind-the-Scenes"</h4>
        
        <p><strong>Script (45 seconds):</strong></p>
        
        <p><strong>Hook (0-3s):</strong> "POV: You're watching us design a brand 👀"</p>
        
        <p><strong>Process (3-40s):</strong> Show creative process, team collaboration, tools used</p>
        
        <p><strong>CTA (40-45s):</strong> "This could be your brand. Let's talk."</p>
        
        <p><strong>Purpose:</strong> Humanize brand, show expertise, build connection</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Reel Template 3
        st.markdown("""
        <div class="content-card">
        <h4>Reel Template 3: "Myth vs Reality"</h4>
        
        <p><strong>Script (30 seconds):</strong></p>
        
        <p><strong>Hook (0-3s):</strong> "Digital marketing myths you need to stop believing 🚫"</p>
        
        <p><strong>Myth 1 (3-13s):</strong> "Myth: Social media is free marketing" → "Reality: It costs time or money"</p>
        
        <p><strong>Myth 2 (13-23s):</strong> "Myth: More followers = more sales" → "Reality: Engagement matters more"</p>
        
        <p><strong>CTA (23-30s):</strong> "Want real results? Link in bio"</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif content_type == "Twitter Threads":
        st.markdown("## 🐦 Twitter/X Thread Templates")
        
        st.markdown("""
        <div class="highlight">
        <h4>Thread Best Practices</h4>
        <ul>
        <li><strong>Length:</strong> 5-10 tweets ideal</li>
        <li><strong>Hook Tweet:</strong> Must be compelling enough to expand</li>
        <li><strong>Numbered:</strong> Use numbers so readers know length</li>
        <li><strong>Value:</strong> Each tweet should offer insight</li>
        <li><strong>CTA:</strong> Last tweet drives action</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Thread Template 1
        st.markdown("""
        <div class="content-card">
        <h4>Thread Template 1: "Lessons Learned"</h4>
        
        <p><strong>Tweet 1 (Hook):</strong><br>
        "5 lessons from helping 20+ businesses with digital transformation.
        
        Some were obvious. Others surprised me: 🧵"</p>
        
        <p><strong>Tweets 2-6 (Lessons):</strong><br>
        One lesson per tweet with brief explanation</p>
        
        <p><strong>Tweet 7 (CTA):</strong><br>
        "Want to avoid these mistakes in your transformation?
        
        Let's talk: [link]"</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Thread Template 2
        st.markdown("""
        <div class="content-card">
        <h4>Thread Template 2: "Step-by-Step Guide"</h4>
        
        <p><strong>Tweet 1 (Hook):</strong><br>
        "How to build a personal brand in 2026 (complete guide):
        
        8 steps that actually work 🧵"</p>
        
        <p><strong>Tweets 2-9 (Steps):</strong><br>
        1/ Step 1: Define your niche<br>
        2/ Step 2: Audit your current presence<br>
        [etc...]</p>
        
        <p><strong>Tweet 10 (CTA):</strong><br>
        "This is just the framework. The real work is execution.
        
        Need help? We built Presence for exactly this: [link]"</p>
        </div>
        """, unsafe_allow_html=True)
    
    else:  # Caption Templates
        st.markdown("## ✍️ Caption Templates by Platform")
        
        # LinkedIn
        st.markdown("""
        <div class="content-card">
        <h4>LinkedIn Caption Formula</h4>
        
        <p><strong>Structure (150-200 words):</strong></p>
        
        <p><strong>1. Hook (1-2 sentences):</strong><br>
        Attention-grabbing statement or question</p>
        
        <p><em>Example: "Your website has 3 seconds to make an impression. Most businesses waste it."</em></p>
        
        <p><strong>2. Context (2-3 sentences):</strong><br>
        Why this matters, set the scene</p>
        
        <p><em>Example: "In 2026, users expect instant gratification. Slow load times, confusing navigation, or unclear value propositions cost you customers every day."</em></p>
        
        <p><strong>3. Value (Main body):</strong><br>
        Tips, insights, story, or explanation</p>
        
        <p><strong>4. CTA (1-2 sentences):</strong><br>
        What should they do next?</p>
        
        <p><em>Example: "Ready to optimize your website? Book a free audit at [link]."</em></p>
        
        <p><strong>5. Engagement Question (optional):</strong><br>
        Encourage comments</p>
        
        <p><em>Example: "What's the first thing you notice when you visit a website?"</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Instagram
        st.markdown("""
        <div class="content-card">
        <h4>Instagram Caption Formula</h4>
        
        <p><strong>Structure (80-150 words):</strong></p>
        
        <p><strong>1. Hook (1 sentence):</strong><br>
        Start strong, use emoji strategically</p>
        
        <p><em>Example: "Your brand deserves better than generic templates 🎨"</em></p>
        
        <p><strong>2. Value (Short paragraphs with line breaks):</strong><br>
        Keep sentences short and punchy</p>
        
        <p><em>Example:<br>
        "At Purple Crayolá, we create custom digital experiences.
        
        No templates. No shortcuts. Just 'You'nique solutions.
        
        Web design | Branding | Digital marketing"</em></p>
        
        <p><strong>3. CTA:</strong><br>
        Simple and clear</p>
        
        <p><em>Example: "Link in bio to start your project ✨"</em></p>
        
        <p><strong>4. Hashtags (20-30):</strong><br>
        Mix of branded, niche, and broad hashtags</p>
        
        <p><em>#PurpleCrayolá #DigitalTransformation #BrandDesign #WebDevelopment #NigeriaTech</em></p>
        </div>
        """, unsafe_allow_html=True)
        
        # Twitter/X
        st.markdown("""
        <div class="content-card">
        <h4>Twitter/X Caption Formula</h4>
        
        <p><strong>Structure (Tweet Length):</strong></p>
        
        <p><strong>Single Tweet (280 characters):</strong></p>
        
        <p><em>"Your website is your 24/7 salesperson.
        
        Is it selling or sitting?
        
        3 things every business website needs:
        • Clear value proposition
        • Fast load speed
        • Mobile optimization
        
        Missing any? We can help: [link]"</em></p>
        
        <p><strong>Pro Tips:</strong></p>
        <ul>
        <li>Start with a hook or question</li>
        <li>Use line breaks for readability</li>
        <li>Include 1-2 hashtags max</li>
        <li>Tag relevant accounts when appropriate</li>
        <li>Always include a CTA</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

elif page == "Platform Strategy":
    st.title("📱 Platform-Specific Strategy")
    
    platform = st.selectbox(
        "Select Platform:",
        ["LinkedIn", "Instagram", "Twitter/X", "Cross-Platform"]
    )
    
    if platform == "LinkedIn":
        st.markdown("## 💼 LinkedIn Strategy")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### Primary B2B Platform for Purple Crayolá
            
            **Posting Frequency:** 3-4 posts/week
            
            **Optimal Posting Times (WAT):**
            - Tuesday: 9-11 AM
            - Wednesday: 9-11 AM, 1-2 PM
            - Thursday: 9-11 AM
            - Avoid: Weekends, Mondays before 10 AM, Fridays after 3 PM
            
            **Content Strategy:**
            - **60%** Educational (how-tos, insights, frameworks)
            - **20%** Thought leadership (industry commentary)
            - **10%** Company/team highlights
            - **10%** Promotional (services, Presence)
            
            **Engagement Strategy:**
            - Comment on 5-10 relevant posts daily
            - Respond to all comments within 2-4 hours
            - Join 3-5 relevant LinkedIn groups
            - Send personalized connection requests (10-15/week)
            - Engage with target audience posts consistently
            
            **Best Performing Content Types:**
            1. **Carousels** (highest engagement) - 5-8 slides
            2. **Text posts** with personal insights
            3. **Polls** (great for engagement)
            4. **Video posts** (native upload, not YouTube links)
            5. **LinkedIn Articles** (monthly long-form)
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Hashtag Strategy</h4>
            
            <p><strong>Branded (Always use):</strong></p>
            <ul>
            <li>#PurpleCrayolá</li>
            <li>#PRISMFramework</li>
            <li>#PresenceByPurpleCrayolá</li>
            </ul>
            
            <p><strong>Industry (Rotate):</strong></p>
            <ul>
            <li>#DigitalTransformation</li>
            <li>#WebDevelopment</li>
            <li>#DigitalMarketing</li>
            <li>#TechInNigeria</li>
            <li>#NigerianStartups</li>
            <li>#BusinessGrowth</li>
            </ul>
            
            <p><strong>Presence-Specific:</strong></p>
            <ul>
            <li>#PersonalBranding</li>
            <li>#ThoughtLeadership</li>
            <li>#ProfessionalGrowth</li>
            <li>#CareerDevelopment</li>
            <li>#ExecutivePresence</li>
            </ul>
            
            <p><strong>Usage:</strong> 3-5 hashtags per post</p>
            </div>
            """, unsafe_allow_html=True)
    
    elif platform == "Instagram":
        st.markdown("## 📸 Instagram Strategy")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### Visual Storytelling & Culture Platform
            
            **Posting Frequency:**
            - **Feed Posts:** 4-5/week
            - **Reels:** 2-3/week
            - **Stories:** Daily (5-10 per day)
            
            **Optimal Posting Times (WAT):**
            - Monday-Friday: 12-1 PM, 7-9 PM
            - Weekends: 11 AM - 1 PM
            
            **Content Mix:**
            - **30%** Reels (educational, behind-the-scenes, tips)
            - **30%** Carousels (educational, showcase)
            - **20%** Single posts (quotes, announcements)
            - **20%** Stories (daily engagement, polls, Q&A)
            
            **Reels Strategy (Critical for Growth):**
            - Post 2-3 Reels per week
            - Length: 15-45 seconds
            - Use trending audio when relevant
            - Include text overlays (80% watch without sound)
            - Hook in first 1-2 seconds
            - End with clear CTA
            
            **Stories Strategy:**
            - Daily updates (morning/evening)
            - Behind-the-scenes content
            - Polls and questions (engagement)
            - Story highlights for:
              - About Us
              - Services
              - Presence
              - Client Work
              - Team Culture
            
            **Engagement Tactics:**
            - Respond to all DMs within 4 hours
            - Comment on 10-15 target accounts daily
            - Use location tags (Lagos, Nigeria)
            - Tag relevant brands/people when appropriate
            - Save posts to collections (inspires shares)
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Hashtag Strategy</h4>
            
            <p><strong>Mix Strategy (20-30 hashtags):</strong></p>
            
            <p><strong>Large (500K+ posts):</strong></p>
            <ul>
            <li>#DigitalMarketing</li>
            <li>#WebDesign</li>
            <li>#BrandingDesign</li>
            <li>#BusinessGrowth</li>
            </ul>
            
            <p><strong>Medium (50K-500K):</strong></p>
            <ul>
            <li>#NigeriaDigital</li>
            <li>#LagosStartups</li>
            <li>#DigitalTransformation</li>
            <li>#PersonalBranding</li>
            </ul>
            
            <p><strong>Small (5K-50K):</strong></p>
            <ul>
            <li>#PurpleCrayolá</li>
            <li>#NigeriaTech</li>
            <li>#LagosCreatives</li>
            <li>#AfricanStartups</li>
            </ul>
            
            <p><strong>Niche (<5K):</strong></p>
            <ul>
            <li>#PRISMFramework</li>
            <li>#PresenceByPurpleCrayolá</li>
            </ul>
            </div>
            
            <div class="warning-box">
            <h4>⚠️ Instagram Algorithm Tips</h4>
            <ul>
            <li>Post when your audience is active</li>
            <li>Prioritize Reels (algorithm favors them)</li>
            <li>Respond to comments within 1 hour</li>
            <li>Use all 30 hashtags</li>
            <li>Add alt text to images</li>
            <li>Avoid external links in captions</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    elif platform == "Twitter/X":
        st.markdown("## 🐦 Twitter/X Strategy")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### Real-Time Engagement & Community Platform
            
            **Posting Frequency:** 1-3 posts/day (daily presence is critical)
            
            **Optimal Posting Times (WAT):**
            - Morning: 9-10 AM
            - Lunch: 12-1 PM
            - Evening: 6-8 PM
            
            **Daily Activity Schedule:**
            - **9 AM:** Morning insight/quote/question
            - **Throughout day:** Engage with 10-20 accounts
            - **12 PM:** Educational tweet or thread
            - **3-5 PM:** Reply to mentions and DMs
            - **6-7 PM:** Engagement tweet or community question
            
            **Content Mix:**
            - **40%** Single tweets (insights, tips, observations)
            - **30%** Engagement tweets (questions, polls)
            - **20%** Threads (2/week - educational)
            - **10%** Quote tweets with commentary
            
            **Thread Strategy:**
            - Post 2 threads per week
            - 5-10 tweets per thread
            - Hook tweet must compel expansion
            - Number tweets (1/, 2/, 3/)
            - End with strong CTA
            - Topics: How-tos, lessons, breakdowns
            
            **Engagement Strategy (Most Important on Twitter):**
            - Spend 30-45 minutes daily engaging
            - Reply to tweets in your niche
            - Quote tweet with added value
            - Join relevant Twitter Spaces
            - Build relationships with 10-15 key accounts
            - Retweet with commentary (not just RT)
            
            **Twitter/X Best Practices:**
            - Keep tweets conversational
            - Use line breaks for readability
            - Ask questions to drive engagement
            - Share opinions (but professionally)
            - Be timely (comment on trends when relevant)
            - Use images/GIFs to increase visibility
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight">
            <h4>Growth Tactics</h4>
            
            <p><strong>Daily Checklist:</strong></p>
            <ul>
            <li>✅ Post 1-3 times</li>
            <li>✅ Reply to 10-20 tweets</li>
            <li>✅ Quote tweet 2-3 times</li>
            <li>✅ Respond to all mentions</li>
            <li>✅ Engage with target audience</li>
            </ul>
            
            <p><strong>Hashtag Usage:</strong></p>
            <ul>
            <li>Use 1-2 hashtags max</li>
            <li>Only when adding value</li>
            <li>#TechTwitter #BuildInPublic</li>
            <li>#NigeriaTech #DigitalMarketing</li>
            </ul>
            
            <p><strong>Accounts to Engage With:</strong></p>
            <ul>
            <li>Nigerian tech founders</li>
            <li>Digital marketing experts</li>
            <li>Startup ecosystem leaders</li>
            <li>Target clients/prospects</li>
            <li>Industry publications</li>
            </ul>
            </div>
            
            <div class="success-box">
            <h4>✅ Twitter Growth Formula</h4>
            <p><strong>Consistency + Engagement > Content Quality</strong></p>
            <p>On Twitter, showing up daily and engaging authentically drives more growth than perfect content posted sporadically.</p>
            </div>
            """, unsafe_allow_html=True)
    
    else:  # Cross-Platform
        st.markdown("## 🔄 Cross-Platform Strategy")
        
        st.markdown("""
        <div class="highlight">
        <h3>Content Repurposing: One Post, Multiple Platforms</h3>
        <p>Create once, optimize for each platform. This maximizes efficiency while respecting each platform's unique audience and algorithm.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Repurposing Example
        st.markdown("### 📊 Content Repurposing Example")
        
        st.markdown("""
        <div class="content-card">
        <h4>Original Content: "5 Signs You Need Digital Transformation"</h4>
        
        <p><strong>LinkedIn (Carousel - 7 slides):</strong></p>
        <ul>
        <li>Professional design with brand colors</li>
        <li>Slide 1: Title slide with hook</li>
        <li>Slides 2-6: One sign per slide (detailed)</li>
        <li>Slide 7: CTA with link to book audit</li>
        <li>Caption: 150-180 words with context and CTA</li>
        <li>Hashtags: 3-5 professional hashtags</li>
        </ul>
        
        <p><strong>Instagram (Reel - 30 seconds):</strong></p>
        <ul>
        <li>Quick visual transitions</li>
        <li>Text overlays for each sign</li>
        <li>Trending audio in background</li>
        <li>Fast-paced, engaging format</li>
        <li>Caption: 80-100 words, punchy</li>
        <li>Hashtags: 20-30 mix of broad and niche</li>
        <li>End screen: "Link in bio"</li>
        </ul>
        
        <p><strong>Twitter/X (Thread - 7 tweets):</strong></p>
        <ul>
        <li>Tweet 1: Hook "5 signs you need digital transformation (and most businesses miss them): 🧵"</li>
        <li>Tweets 2-6: One sign per tweet (concise)</li>
        <li>Tweet 7: CTA "Ready to transform? [link]"</li>
        <li>Conversational tone</li>
        <li>No hashtags (maybe 1-2 max)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Cross-Platform Calendar
        st.markdown("### 📅 Weekly Cross-Platform Posting Schedule")
        
        schedule_data = {
            'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
            'LinkedIn': ['Post 1', 'Engage Only', 'Post 2', 'Engage Only', 'Post 3'],
            'Instagram': ['Feed Post + Stories', 'Reel + Stories', 'Feed Post + Stories', 'Reel + Stories', 'Stories Only'],
            'Twitter/X': ['2-3 tweets', '2-3 tweets + Thread', '2-3 tweets', '2-3 tweets + Thread', '2-3 tweets']
        }
        
        df_schedule = pd.DataFrame(schedule_data)
        st.dataframe(df_schedule, hide_index=True, use_container_width=True)
        
        st.markdown("---")
        
        # Platform Comparison
        st.markdown("### 📊 Platform Comparison")
        
        comparison_data = {
            'Feature': ['Best For', 'Posting Frequency', 'Content Length', 'Engagement Style', 'Growth Strategy', 'Business Value'],
            'LinkedIn': [
                'B2B, thought leadership',
                '3-4/week',
                'Long-form (150-200 words)',
                'Professional comments',
                'Quality content + networking',
                'High (direct B2B leads)'
            ],
            'Instagram': [
                'Visual storytelling, culture',
                '4-5/week + daily stories',
                'Short (80-120 words)',
                'DMs, comments, polls',
                'Reels + consistency',
                'Medium (brand awareness)'
            ],
            'Twitter/X': [
                'Real-time, community',
                '1-3/day',
                'Very short (280 chars)',
                'Replies, quote tweets',
                'Engagement > posting',
                'Medium (community building)'
            ]
        }
        
        df_comparison = pd.DataFrame(comparison_data)
        st.dataframe(df_comparison, hide_index=True, use_container_width=True)

elif page == "Content Calendar":
    st.title("📆 January 2026 Master Content Calendar")
    
    # Calendar view selector
    view = st.radio("Select View:", ["Full Calendar", "By Week", "By Platform"])
    
    if view == "Full Calendar":
        # Create comprehensive calendar data
        calendar_data = {
            'Date': ['Jan 6', 'Jan 7', 'Jan 8', 'Jan 9', 'Jan 10',
                     'Jan 13', 'Jan 14', 'Jan 15', 'Jan 16', 'Jan 17',
                     'Jan 20', 'Jan 21', 'Jan 22', 'Jan 23', 'Jan 24',
                     'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30', 'Jan 31'],
            'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri',
                    'Mon', 'Tue', 'Wed', 'Thu', 'Fri',
                    'Mon', 'Tue', 'Wed', 'Thu', 'Fri',
                    'Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
            'Week': ['Week 1', 'Week 1', 'Week 1', 'Week 1', 'Week 1',
                     'Week 2', 'Week 2', 'Week 2', 'Week 2', 'Week 2',
                     'Week 3', 'Week 3', 'Week 3', 'Week 3', 'Week 3',
                     'Week 4', 'Week 4', 'Week 4', 'Week 4', 'Week 4'],
            'LinkedIn': ['New Year Vision', '-', '5 Signs DT', 'Nigerian Tech', '-',
                        'ROI Framework', '-', '-', 'Case Study', '-',
                        'Visibility Matters', '-', 'Expertise vs Visibility', '-', '-',
                        'Presence Launch', 'PRISM Deep Dive', 'Packages', '-', 'Month Wrap'],
            'Instagram': ['Stories + Reel', 'Team BTS Reel', 'Reel: 5 Signs', '-', 'Stories Recap',
                         'ROI Graphic', '-', 'Day in Life Reel', '-', 'Weekend Tips',
                         'Quote Graphic', 'Poll Stories', '-', 'Teaser Post', 'Countdown',
                         'Launch Carousel', 'PRISM Reel', '-', 'Testimonials', 'CTA Post'],
            'Twitter/X': ['DT Thread', 'Engagement', '-', 'Poll', 'Weekend Q',
                         '-', 'Process Thread', 'Share Reel', '-', '-',
                         '-', 'Branding Thread', '-', '-', 'Launch Teaser',
                         'Launch Thread', '-', 'Packages Thread', '-', 'CTA Tweet'],
            'Content Type': ['Educational', 'Culture', 'Educational', 'Thought Leadership', 'Engagement',
                           'Educational', 'Process', 'BTS', 'Social Proof', 'Educational',
                           'Thought Leadership', 'Educational', 'Thought Leadership', 'Promotional', 'Engagement',
                           'Promotional', 'Educational', 'Promotional', 'Social Proof', 'Promotional'],
            'Focus': ['General', 'General', 'General', 'General', 'General',
                     'General', 'General', 'General', 'General', 'General',
                     'Presence Tease', 'Presence Tease', 'Presence Tease', 'Presence Tease', 'Presence Tease',
                     'Presence', 'Presence', 'Presence', 'Presence', 'Presence']
        }
        
        df_calendar = pd.DataFrame(calendar_data)
        
        # Add filters
        col1, col2, col3 = st.columns(3)
        with col1:
            week_filter = st.multiselect(
                "Filter by Week:",
                options=df_calendar['Week'].unique(),
                default=df_calendar['Week'].unique()
            )
        
        with col2:
            focus_filter = st.multiselect(
                "Filter by Focus:",
                options=df_calendar['Focus'].unique(),
                default=df_calendar['Focus'].unique()
            )
        
        with col3:
            type_filter = st.multiselect(
                "Filter by Content Type:",
                options=df_calendar['Content Type'].unique(),
                default=df_calendar['Content Type'].unique()
            )
        
        # Filter dataframe
        filtered_df = df_calendar[
            (df_calendar['Week'].isin(week_filter)) &
            (df_calendar['Focus'].isin(focus_filter)) &
            (df_calendar['Content Type'].isin(type_filter))
        ]
        
        st.dataframe(filtered_df, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Visual Distribution
        st.markdown("### 📊 Content Distribution Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Posts by platform
            platform_posts = {
                'LinkedIn': df_calendar['LinkedIn'].notna().sum() - (df_calendar['LinkedIn'] == '-').sum(),
                'Instagram': df_calendar['Instagram'].notna().sum() - (df_calendar['Instagram'] == '-').sum(),
                'Twitter/X': df_calendar['Twitter/X'].notna().sum() - (df_calendar['Twitter/X'] == '-').sum()
            }
            
            fig1 = px.bar(
                x=list(platform_posts.keys()),
                y=list(platform_posts.values()),
                labels={'x': 'Platform', 'y': 'Number of Posts'},
                title='Posts per Platform',
                color=list(platform_posts.keys()),
                color_discrete_map={
                    'LinkedIn': '#0A66C2',
                    'Instagram': '#E4405F',
                    'Twitter/X': '#1DA1F2'
                }
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # Content type distribution
            type_counts = df_calendar['Content Type'].value_counts()
            
            fig2 = px.pie(
                values=type_counts.values,
                names=type_counts.index,
                title='Content Type Distribution',
                color_discrete_sequence=['#6B46C1', '#9F7AEA', '#D6BCFA', '#EDE9FE', '#C4B5FD']
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    elif view == "By Week":
        week = st.selectbox(
            "Select Week:",
            ["Week 1 (Jan 6-10)", "Week 2 (Jan 13-17)", "Week 3 (Jan 20-24)", "Week 4 (Jan 27-31)"]
        )
        
        # Show detailed breakdown for selected week
        st.markdown(f"## {week} - Detailed Schedule")
        
        # Week-specific data would go here
        st.info("Refer to 'Weekly Breakdown' section for detailed content of each week.")
    
    else:  # By Platform
        platform = st.selectbox(
            "Select Platform:",
            ["LinkedIn", "Instagram", "Twitter/X"]
        )
        
        st.markdown(f"## {platform} - January Content Plan")
        
        # Platform-specific calendar
        if platform == "LinkedIn":
            linkedin_posts = [
                {'Date': 'Jan 6', 'Content': 'New Year Digital Transformation Vision', 'Type': 'Carousel'},
                {'Date': 'Jan 8', 'Content': '5 Signs You Need Digital Transformation', 'Type': 'Carousel'},
                {'Date': 'Jan 9', 'Content': 'State of Nigerian Tech 2026', 'Type': 'Article'},
                {'Date': 'Jan 13', 'Content': 'Digital Marketing ROI Framework', 'Type': 'Carousel'},
                {'Date': 'Jan 16', 'Content': 'Client Success Story', 'Type': 'Post'},
                {'Date': 'Jan 20', 'Content': 'Why Professional Visibility Matters', 'Type': 'Post'},
                {'Date': 'Jan 22', 'Content': 'Expertise vs Visibility', 'Type': 'Post'},
                {'Date': 'Jan 27', 'Content': 'Presence Launch Announcement', 'Type': 'Post'},
                {'Date': 'Jan 28', 'Content': 'PRISM Framework Deep Dive', 'Type': 'Carousel'},
                {'Date': 'Jan 29', 'Content': 'Presence Packages Breakdown', 'Type': 'Carousel'},
                {'Date': 'Jan 31', 'Content': 'Month-End Wrap + CTA', 'Type': 'Post'}
            ]
            
            df_platform = pd.DataFrame(linkedin_posts)
            st.dataframe(df_platform, use_container_width=True, hide_index=True)

elif page == "KPIs & Success Metrics":
    st.title("🎯 KPIs & Success Metrics")
    
    st.markdown("""
    <div class="highlight">
    <h3>January Focus: Foundation & Learning</h3>
    <p>Month 1 priorities: Build systems, understand audience, establish consistency. 
    Significant growth typically develops in months 2-4 as content strategy matures.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Primary KPIs
    st.markdown("## 📈 Primary KPIs")
    
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
    
    with kpi_col1:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-label">Follower Growth</p>
            <p class="metric-value">3-5%</p>
            <p class="metric-delta">↑ ~150-250 new followers</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Breakdown by Platform:**
        - LinkedIn: 50-100 new connections
        - Instagram: 80-120 new followers
        - Twitter/X: 20-30 new followers
        """)
    
    with kpi_col2:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-label">Engagement Rate</p>
            <p class="metric-value">2-4%</p>
            <p class="metric-delta">↑ Avg across all platforms</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Target by Platform:**
        - LinkedIn: 3-5%
        - Instagram: 2-3%
        - Twitter/X: 1-2%
        """)
    
    with kpi_col3:
        st.markdown("""
        <div class="metric-card">
            <p class="metric-label">Website Traffic</p>
            <p class="metric-value">+20%</p>
            <p class="metric-delta">↑ From social channels</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        **Goal:**
        - 500-800 visitors from social
        - 3-5% conversion to consultation
        - 10-15 form submissions
        """)
    
    st.divider()
    
    # Secondary Metrics
    st.markdown("## 📊 Secondary Metrics")
    
    metrics_data = {
        'Metric': [
            'Profile Visits',
            'Post Impressions',
            'Story Views (IG)',
            'Link Clicks',
            'DM Inquiries',
            'Consultation Requests',
            'Average Comments/Post',
            'Average Shares/Post',
            'Video Views'
        ],
        'Target': [
            '+15%',
            '10,000-15,000',
            '100-200 per story',
            '200-300',
            '10-15',
            '3-7',
            '5-10',
            '3-5',
            '2,000-3,000'
        ],
        'Platform': [
            'All',
            'All',
            'Instagram',
            'All',
            'All',
            'All',
            'All',
            'LinkedIn, Instagram',
            'Instagram, LinkedIn'
        ]
    }
    
    df_metrics = pd.DataFrame(metrics_data)
    st.dataframe(df_metrics, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # Weekly Tracking
    st.markdown("## 📅 Weekly Tracking Checklist")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="content-card">
        <h4>Every Week - Track:</h4>
        
        <p><strong>Growth Metrics:</strong></p>
        <ul>
        <li>Follower count (start vs end of week)</li>
        <li>Profile visits</li>
        <li>Post reach and impressions</li>
        </ul>
        
        <p><strong>Engagement Metrics:</strong></p>
        <ul>
        <li>Total likes, comments, shares</li>
        <li>Engagement rate per post</li>
        <li>DMs and inquiries received</li>
        <li>Story views and interactions</li>
        </ul>
        
        <p><strong>Content Performance:</strong></p>
        <ul>
        <li>Top 3 performing posts (why?)</li>
        <li>Bottom 2 performing posts (why?)</li>
        <li>Best content type/format</li>
        <li>Optimal posting times</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
        <h4>Business Impact Metrics:</h4>
        
        <p><strong>Lead Generation:</strong></p>
        <ul>
        <li>Website visits from social</li>
        <li>Contact form submissions</li>
        <li>Discovery call bookings</li>
        <li>Email newsletter signups</li>
        </ul>
        
        <p><strong>Brand Awareness:</strong></p>
        <ul>
<li>Mentions and tags</li>
        <li>Shares and saves</li>
        <li>Brand search volume</li>
        <li>Direct messages about services</li>
        </ul>
        
        <p><strong>Presence-Specific (Week 4 onwards):</strong></p>
        <ul>
        <li>Presence landing page visits</li>
        <li>Discovery call bookings for Presence</li>
        <li>Presence-related inquiries</li>
        <li>Downloads of Presence materials</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # 90-Day Vision
    st.markdown("## 🚀 90-Day Growth Vision")
    
    months_data = {
        'Month': ['January 2026', 'February 2026', 'March 2026'],
        'Focus': ['Foundation & Learning', 'Optimization & Iteration', 'Scaling & Refinement'],
        'Expected Growth': ['3-5%', '5-8%', '8-12%'],
        'Key Activities': [
            'Build systems, learn audience, establish consistency',
            'Optimize based on data, refine content approach, scale what works',
            'Scale proven content, expand successful formats, increase reach'
        ],
        'Primary Goals': [
            'Consistency, baseline engagement, 3-7 consultations',
            'Higher engagement, 8-12 consultations, testimonials',
            'Strong momentum, 15+ consultations, case studies'
        ]
    }
    
    months_df = pd.DataFrame(months_data)
    st.dataframe(months_df, use_container_width=True, hide_index=True)
    
    st.markdown("""
    <div class="success-box">
    <h4>✅ Growth Philosophy</h4>
    <p><strong>Month 1:</strong> Foundation (systems, consistency, learning)</p>
    <p><strong>Month 2:</strong> Optimization (double down on what works)</p>
    <p><strong>Month 3:</strong> Scaling (expand reach, increase frequency)</p>
    <p><strong>Months 4-6:</strong> Momentum (compounding growth, authority positioning)</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Implementation Guide":
    st.title("🛠️ Implementation Guide")
    
    st.markdown("""
    <div class="highlight">
    <h3>Your Week-by-Week Action Plan</h3>
    <p>Practical, step-by-step guide to executing this strategy successfully.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Tools & Resources
    st.markdown("## 🧰 Essential Tools & Resources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="content-card">
        <h4>Content Creation Tools</h4>
        
        <p><strong>Design:</strong></p>
        <ul>
        <li><strong>Canva Pro</strong> ($12.99/mo) - Graphics, carousels, templates</li>
        <li><strong>Figma</strong> (Free) - Advanced design work</li>
        <li><strong>Adobe Express</strong> ($9.99/mo) - Quick designs</li>
        </ul>
        
        <p><strong>Video:</strong></p>
        <ul>
        <li><strong>CapCut</strong> (Free) - Reels editing</li>
        <li><strong>InShot</strong> (Free) - Mobile video editing</li>
        <li><strong>Descript</strong> ($12/mo) - Advanced video editing</li>
        </ul>
        
        <p><strong>Stock Assets:</strong></p>
        <ul>
        <li><strong>Unsplash/Pexels</strong> (Free) - Stock photos</li>
        <li><strong>Envato Elements</strong> ($16.50/mo) - Everything</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
        <h4>Scheduling & Analytics</h4>
        
        <p><strong>Scheduling:</strong></p>
        <ul>
        <li><strong>Buffer</strong> ($15/mo) - Multi-platform scheduling</li>
        <li><strong>Later</strong> ($18/mo) - Instagram-focused</li>
        <li><strong>Meta Business Suite</strong> (Free) - FB & IG</li>
        </ul>
        
        <p><strong>Analytics:</strong></p>
        <ul>
        <li><strong>LinkedIn Analytics</strong> (Built-in)</li>
        <li><strong>Instagram Insights</strong> (Built-in)</li>
        <li><strong>Twitter Analytics</strong> (Built-in)</li>
        <li><strong>Google Analytics</strong> (Free) - Website traffic</li>
        </ul>
        
        <p><strong>Productivity:</strong></p>
        <ul>
        <li><strong>Notion</strong> (Free) - Content planning</li>
        <li><strong>Trello</strong> (Free) - Task management</li>
        <li><strong>Google Sheets</strong> (Free) - Tracking</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Weekly Workflow
    st.markdown("## 📅 Weekly Workflow Template")
    
    workflow_tabs = st.tabs(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    
    with workflow_tabs[0]:  # Monday
        st.markdown("""
        ### Monday: Planning & Strategy
        
        **Time Required:** 2-3 hours
        
        **Morning (9-11 AM):**
        1. ✅ Review last week's analytics
        2. ✅ Identify top-performing content
        3. ✅ Note what didn't work and why
        4. ✅ Check DMs and respond to inquiries
        
        **Afternoon (2-5 PM):**
        1. ✅ Plan this week's content topics
        2. ✅ Create content calendar for the week
        3. ✅ Gather resources (stats, quotes, images)
        4. ✅ Write post captions (draft form)
        5. ✅ Get approval from team/founder if needed
        
        **Deliverable:** Complete content calendar for the week
        """)
    
    with workflow_tabs[1]:  # Tuesday
        st.markdown("""
        ### Tuesday: Content Creation Day 1
        
        **Time Required:** 4-5 hours
        
        **Morning (9 AM-12 PM):**
        1. ✅ Create LinkedIn carousel designs (2-3 posts)
        2. ✅ Design Instagram carousel/posts (2-3 posts)
        3. ✅ Create graphics for Twitter threads
        
        **Afternoon (2-5 PM):**
        1. ✅ Record and edit Reels (1-2 videos)
        2. ✅ Create Stories templates
        3. ✅ Finalize all captions
        4. ✅ Add hashtags
        
        **Deliverable:** 50% of week's content ready
        """)
    
    with workflow_tabs[2]:  # Wednesday
        st.markdown("""
        ### Wednesday: Content Creation Day 2 & Scheduling
        
        **Time Required:** 3-4 hours
        
        **Morning (9 AM-12 PM):**
        1. ✅ Finish remaining content creation
        2. ✅ Final review of all posts
        3. ✅ Make adjustments based on brand voice
        
        **Afternoon (2-4 PM):**
        1. ✅ Schedule all content in Buffer/Later
        2. ✅ Double-check times and dates
        3. ✅ Prepare Stories content
        4. ✅ Set reminders for engagement
        
        **Deliverable:** All content scheduled for the week
        """)
    
    with workflow_tabs[3]:  # Thursday
        st.markdown("""
        ### Thursday: Engagement & Community Building
        
        **Time Required:** 2-3 hours
        
        **Throughout Day:**
        1. ✅ Respond to all comments (target: within 2 hours)
        2. ✅ Reply to all DMs (target: within 4 hours)
        3. ✅ Comment on 10-15 target accounts (LinkedIn)
        4. ✅ Engage with 10-15 accounts (Instagram)
        5. ✅ Reply to 15-20 tweets (Twitter)
        6. ✅ Send 5-10 connection requests (LinkedIn)
        
        **Evening (6-7 PM):**
        1. ✅ Post Instagram/Twitter evening content
        2. ✅ Engage with evening audience
        
        **Deliverable:** Strong community engagement
        """)
    
    with workflow_tabs[4]:  # Friday
        st.markdown("""
        ### Friday: Analytics & Optimization
        
        **Time Required:** 2-3 hours
        
        **Morning (9-11 AM):**
        1. ✅ Pull analytics from all platforms
        2. ✅ Update tracking spreadsheet
        3. ✅ Identify top 3 posts of the week
        4. ✅ Identify bottom 2 posts of the week
        5. ✅ Note insights and patterns
        
        **Afternoon (2-4 PM):**
        1. ✅ Create weekly report
        2. ✅ Document learnings
        3. ✅ Brainstorm next week's content ideas
        4. ✅ Update content bank
        
        **Deliverable:** Weekly analytics report + next week's ideas
        """)
    
    st.divider()
    
    # Crisis Management
    st.markdown("## 🚨 Crisis Management & Contingencies")
    
    st.markdown("""
    <div class="warning-box">
    <h4>⚠️ What If Things Go Wrong?</h4>
    
    <p><strong>Scenario 1: You're sick or unavailable</strong></p>
    <ul>
    <li>Use emergency content bank (5-10 evergreen posts)</li>
    <li>Reduce posting frequency to 2x/week</li>
    <li>Focus on Instagram Stories (quickest content)</li>
    <li>Set up auto-responder for DMs</li>
    </ul>
    
    <p><strong>Scenario 2: Content isn't performing</strong></p>
    <ul>
    <li>Don't panic - first month is learning</li>
    <li>Analyze: Is it timing? Format? Topic?</li>
    <li>Test different posting times</li>
    <li>Try different content formats</li>
    <li>Ask audience what they want to see</li>
    </ul>
    
    <p><strong>Scenario 3: Negative comments or feedback</strong></p>
    <ul>
    <li>Respond professionally and quickly</li>
    <li>Don't delete (unless spam/offensive)</li>
    <li>Take conversations to DM if heated</li>
    <li>Learn from constructive criticism</li>
    <li>Document for team awareness</li>
    </ul>
    
    <p><strong>Scenario 4: No consultation bookings by Week 3</strong></p>
    <ul>
    <li>Review CTAs - are they clear?</li>
    <li>Add more social proof</li>
    <li>Create limited-time offer</li>
    <li>Increase engagement efforts</li>
    <li>Consider paid promotion (small budget)</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Quick Start Checklist
    st.markdown("## ✅ Quick Start Checklist (Before January 6)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="content-card">
        <h4>Setup (Complete Before Jan 6)</h4>
        
        <p><strong>Accounts:</strong></p>
        <ul>
        <li>☐ Optimize all social media bios</li>
        <li>☐ Update profile pictures (consistent)</li>
        <li>☐ Add links to purplecrayola.com</li>
        <li>☐ Create Instagram highlights structure</li>
        <li>☐ Join relevant LinkedIn groups</li>
        </ul>
        
        <p><strong>Tools:</strong></p>
        <ul>
        <li>☐ Set up Canva Pro account</li>
        <li>☐ Install scheduling tool</li>
        <li>☐ Create brand templates in Canva</li>
        <li>☐ Set up analytics tracking sheet</li>
        <li>☐ Download mobile editing apps</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
        <h4>Content Preparation</h4>
        
        <p><strong>Week 1 Content:</strong></p>
        <ul>
        <li>☐ Create Week 1 carousel designs</li>
        <li>☐ Write all Week 1 captions</li>
        <li>☐ Schedule Week 1 posts</li>
        <li>☐ Prepare Stories templates</li>
        <li>☐ Create emergency content bank</li>
        </ul>
        
        <p><strong>Assets:</strong></p>
        <ul>
        <li>☐ Team photos for posts</li>
        <li>☐ Purple Crayolá logo files</li>
        <li>☐ Brand color codes saved</li>
        <li>☐ Office/workspace photos</li>
        <li>☐ Client testimonials (if available)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Success Tips
    st.markdown("## 💡 Final Success Tips")
    
    st.markdown("""
    <div class="success-box">
    <h4>The 5 Rules for Social Media Success</h4>
    
    <p><strong>1. Consistency > Perfection</strong></p>
    <p>Post consistently, even if not perfect. Algorithm rewards consistency.</p>
    
    <p><strong>2. Engagement > Posting</strong></p>
    <p>Spend as much time engaging as creating. Build real relationships.</p>
    
    <p><strong>3. Value > Promotion</strong></p>
    <p>Give 4x more value than you promote. People follow for value, not ads.</p>
    
    <p><strong>4. Patience > Panic</strong></p>
    <p>Month 1 is learning. Real growth comes in months 3-6. Trust the process.</p>
    
    <p><strong>5. Data > Assumptions</strong></p>
    <p>Let analytics guide decisions, not gut feelings. Test, measure, optimize.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight">
    <h4>🎯 Your January Mission</h4>
    <p><strong>Primary Goal:</strong> Establish Purple Crayolá as a credible, consistent voice in digital transformation</p>
    <p><strong>Secondary Goal:</strong> Build foundation for Presence launch</p>
    <p><strong>Success Metric:</strong> 3-7 consultation bookings + sustainable content system</p>
    <p><strong>Mindset:</strong> Foundation before flight. Consistency before virality.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Contact & Support
    st.markdown("## 📞 Questions or Need Support?")
    
    st.markdown("""
    <div class="content-card">
    <p>If you have questions about implementing this strategy:</p>
    <ul>
    <li><strong>Email:</strong> heros@purplecrayola.com</li>
    <li><strong>Review Meetings:</strong> Every Friday to discuss performance</li>
    <li><strong>Quick Questions:</strong> Slack/internal messaging</li>
    </ul>
    
    <p><strong>Remember:</strong> This is a living strategy. Adjust based on what works. 
    The best content strategy is the one you can execute consistently.</p>
    
    <p style="text-align: center; font-size: 18px; margin-top: 20px;">
    <strong>Let's make January 2026 the foundation for Purple Crayolá's social media success! 🚀</strong>
    </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; padding: 30px 20px; background: white; border-radius: 12px; margin-top: 40px;">
    <h4 style="color: #6B46C1; margin-bottom: 10px;">🎨 Purple Crayolá Content Strategy</h4>
    <p style="color: #64748b; margin: 5px 0;">January 2026 - Strategic Digital Transformation</p>
    <p style="font-size: 12px; color: #94a3b8; margin-top: 15px;">
        Developed by Oluwatosin Adejumo, Content & Social Media Manager<br>
        Document Version 2.0 (Revised & Optimized)
    </p>
    <p style="font-size: 11px; color: #cbd5e1; margin-top: 10px;">
        Last Updated: January 08, 2026
    </p>
</div>
""", unsafe_allow_html=True)