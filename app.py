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
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">15-20</p>
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
    st.markdown("##  Brand Overview")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Purple Crayolá** is a full-service digital transformation startup in Nigeria that delivers 
        design and digital solutions to transform customer experiences and business results.
        
        **Core Services:**
        -  Digital Strategy & Transformation
        -  Web & Mobile App Development
        -  Digital Marketing (SEO, Content, Social Media, PPC)
        -  Branding & Identity Design
        -  Project & Product Management
        -  Digital Learning Solutions
        """)
    
    with col2:
        st.markdown("""
        **Brand Values:**
        - Innovation & cutting-edge technology
        - Collaboration & partnership
        - Trust & discretion
        - User Experience by Design
        - Sustainable solutions
        """)
    
    st.divider()
    
    # Content Themes
    st.markdown("##  January 2026 Content Themes")
    
    themes_col1, themes_col2 = st.columns(2)
    
    with themes_col1:
        st.markdown("""
        <div class="content-card">
        <h3> Theme 1: New Year, Digital Transformation</h3>
        <p>Capitalize on the new year energy and businesses setting digital goals.</p>
        </div>
        
        <div class="content-card">
        <h3> Theme 2: Case Studies & Success Stories</h3>
        <p>Showcase real impact and client testimonials.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with themes_col2:
        st.markdown("""
        <div class="content-card">
        <h3> Theme 3: Digital Trends 2026</h3>
        <p>Position as thought leaders on emerging tech and digital strategies.</p>
        </div>
        
        <div class="content-card">
        <h3> Theme 4: Behind the Scenes</h3>
        <p>Humanize the brand, introduce team members, show process.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Content Pillars
    st.markdown("##  Content Pillars Distribution")
    
    pillars_data = {
        'Pillar': ['Educational', 'Promotional', 'Engagement', 'Behind-the-Scenes'],
        'Percentage': [40, 30, 20, 10],
        'Description': [
            'Tips, trends, how-tos, industry insights',
            'Services, case studies, testimonials, CTAs',
            'Questions, polls, interactive content',
            'Team, culture, process'
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
    st.title(" Weekly Content Breakdown")
    
    week = st.selectbox(
        "Select Week:",
        ["Week 1: January 6-10 (New Beginnings)",
         "Week 2: January 13-17 (Solutions Spotlight)",
         "Week 3: January 20-24 (Team & Culture)",
         "Week 4: January 27-30 (Authority Building)"]
    )
    
    if "Week 1" in week:
        st.markdown("##  Week 1: New Beginnings (January 6-10)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: New Year Vision (Jan 6)
            
            **Content:**  
            "2026: The Year of Digital Excellence. As businesses reset and reimagine their strategies, 
            ask yourself: Is your digital infrastructure ready to scale? Purple Crayolá partners with 
            forward-thinking organizations to transform digital experiences. Let's make 2026 your breakthrough year."
            
            **Format:** Carousel with 3-5 slides on digital transformation pillars  
            **CTA:** Book a free digital audit consultation
            
            ---
            
            ### Post 2: Industry Trends (Jan 8)
            
            **Content:** "5 Digital Transformation Trends Shaping Nigerian Businesses in 2026"  
            **Format:** Infographic or short video (30-60 seconds)  
            **Topics:** AI integration, mobile-first experiences, data analytics, automation, personalization
            """)
        
        with tab2:
            st.markdown("""
            ### Welcome 2026 Story Series (Jan 6-7)
            
            - Quick polls: "What's your biggest digital challenge in 2026?"
            - Behind-the-scenes of team planning sessions
            - Quote graphic: "Innovation distinguishes between a leader and a follower"
            
            ---
            
            ### Feed Post (Jan 9)
            
            **Content:** "3 Signs Your Business Needs Digital Transformation in 2026"  
            **Format:** Carousel post with clean graphics, one sign per slide  
            **Include:** Actionable insights for each sign
            """)
        
        with tab3:
            st.markdown("""
            ### Daily Engagement
            
            - Daily tips thread: "Digital Transformation Tips for 2026"
            - Engagement tweets asking followers about their digital goals
            - Retweet industry news with Purple Crayolá's perspective
            """)
    
    elif "Week 2" in week:
        st.markdown("##  Week 2: Solutions Spotlight (January 13-17)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Service Showcase - Web Development (Jan 13)
            
            **Content:**  
            "Your Website is Your Digital Storefront. Is it converting visitors into customers? 
            Our custom web development solutions are built with User Experience by Design. 
            Every click, every scroll, every interaction—optimized for results."
            
            **Format:** Before/after comparison or case study snippet  
            **CTA:** Download our Web Development Guide
            
            ---
            
            ### Post 2: Thought Leadership Article (Jan 15)
            
            **Content:** "Why Nigerian Businesses Can't Afford to Ignore Mobile-First Design in 2026"  
            **Format:** LinkedIn article (800-1000 words)  
            **Include:** Stats, examples, and Purple Crayolá's approach
            """)
        
        with tab2:
            st.markdown("""
            ### Service Carousel (Jan 14)
            
            **Content:** "What We Do at Purple Crayolá"  
            **Slides:** Digital Strategy → Web/App Dev → Digital Marketing → Branding → Learning Solutions  
            **Design:** Clean, branded graphics with icons
            
            ---
            
            ### Client Testimonial Post (Jan 16)
            
            - Feature client testimonial
            - Designed quote graphic with client photo/logo if available
            - Tag client if appropriate
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Engagement
            
            - Tech tip Tuesday: Quick tips on website optimization
            - Friday feature: Spotlight on a specific service
            - Engage with tech and startup community
            """)
    
    elif "Week 3" in week:
        st.markdown("##  Week 3: Team & Culture (January 20-24)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Team Spotlight (Jan 20)
            
            **Content:** Introduce key team members  
            **Format:** Professional photo + mini Q&A about their role and vision  
            **Purpose:** Humanizes the brand
            
            ---
            
            ### Post 2: Process Post (Jan 22)
            
            **Content:** "How We Transform Ideas into Digital Reality: The Purple Crayolá Process"  
            **Format:** Infographic showing: Discovery → Strategy → Design → Development → Launch → Optimize  
            **Purpose:** Builds trust through transparency
            """)
        
        with tab2:
            st.markdown("""
            ### "Day in the Life" Stories (Jan 20-21)
            
            - Follow team members through their workday
            - Show office culture, brainstorming sessions, client calls
            - Use interactive stickers (polls, questions, quizzes)
            
            ---
            
            ### Culture Post (Jan 23)
            
            **Content:** "What makes Purple Crayolá different?"  
            **Format:** Photo carousel of team collaboration, office vibes, project work  
            **Style:** Authentic, candid shots with engaging caption
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Content
            
            - #MotivationMonday with tech/innovation quotes
            - Wednesday wisdom: Share lessons learned from projects
            - Engage with industry conversations
            """)
    
    else:  # Week 4
        st.markdown("##  Week 4: Authority Building (January 27-30)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Case Study Deep Dive (Jan 27)
            
            **Content:** Full case study of a successful project  
            **Format:** Challenge → Solution → Results → Client Impact  
            **Include:** Metrics/outcomes if possible
            
            ---
            
            ### Post 2: Industry Commentary (Jan 29)
            
            **Content:** Respond to a trending tech topic in Nigeria/Africa  
            **Purpose:** Position Purple Crayolá as thought leaders  
            **Include:** Data and insights
            """)
        
        with tab2:
            st.markdown("""
            ### Educational Carousel (Jan 28)
            
            **Content:** "5 Common Website Mistakes Killing Your Conversions"  
            **Purpose:** Demonstrate expertise with practical value  
            **Format:** Each slide = one mistake + quick fix
            
            ---
            
            ### Month-End Teaser (Jan 30)
            
            **Content:** "February is going to be exciting! Here's what's coming..."  
            **Purpose:** Build anticipation for next month's content
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Engagement
            
            - Share blog post or article
            - Tech Thursday: Industry insights
            - Weekend engagement: Light, fun tech-related content
            - Month-end wrap: "January insights from Purple Crayolá"
            """)
    
    st.divider()
    st.info(" **Note:** Content dates are flexible and may be adjusted based on approval workflow and real-time opportunities.")

elif page == "Platform Strategy":
    st.title(" Platform-Specific Strategy")
    
    platform = st.selectbox(
        "Select Platform:",
        ["LinkedIn", "Instagram", "Twitter/X"]
    )
    
    if platform == "LinkedIn":
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ##  LinkedIn Strategy
            
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
            ##  Instagram Strategy
            
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
            ##  Twitter/X Strategy
            
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
    st.title(" January 2026 Content Calendar")
    
    # Create calendar data
    calendar_data = {
        'Date': ['Jan 6', 'Jan 7', 'Jan 8', 'Jan 9', 'Jan 13', 'Jan 14', 'Jan 15', 'Jan 16',
                 'Jan 20', 'Jan 22', 'Jan 23', 'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30'],
        'Platform': ['LinkedIn', 'Instagram', 'LinkedIn', 'Instagram', 'LinkedIn', 'Instagram',
                     'LinkedIn', 'Instagram', 'LinkedIn', 'LinkedIn', 'Instagram', 'LinkedIn',
                     'Instagram', 'LinkedIn', 'Instagram'],
        'Content Type': ['Carousel', 'Stories', 'Infographic', 'Carousel', 'Post', 'Carousel',
                        'Article', 'Testimonial', 'Team Spotlight', 'Process Post', 'Culture Post',
                        'Case Study', 'Educational Carousel', 'Industry Commentary', 'February Teaser'],
        'Theme': ['New Year', 'New Year', 'Trends', 'Transformation', 'Services', 'Services',
                 'Thought Leadership', 'Success Stories', 'Team', 'Team', 'Culture',
                 'Authority', 'Authority', 'Authority', 'Preview'],
        'Status': ['Pending'] * 15
    }
    
    df = pd.DataFrame(calendar_data)
    
    # Add filters
    col1, col2 = st.columns(2)
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
    
    # Filter dataframe
    filtered_df = df[
        (df['Platform'].isin(platform_filter)) &
        (df['Theme'].isin(theme_filter))
    ]
    
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # Visual timeline
    st.markdown("### Content Distribution by Platform")
    
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
    st.title(" KPIs & Strategic Goals")
    
    st.markdown("""
    <div class="highlight">
    <h3> Month 1 Philosophy: Foundation Over Growth</h3>
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
        st.markdown("###  Strategic Objectives")
        
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
    st.markdown("###  Key Performance Indicators")
    
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
    st.markdown("###  90-Day Growth Vision")
    
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
    <h4> Strategic Approach</h4>
    <p>This strategy prioritizes building a strong foundation in January, consistent 
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