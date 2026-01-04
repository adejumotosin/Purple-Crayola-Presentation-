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
    .main {
        background-color: #f8f9fa;
    }
    .stMetric {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .content-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    h1 {
        color: #6B46C1;
    }
    h2 {
        color: #553C9A;
    }
    h3 {
        color: #6B46C1;
    }
    .highlight {
        background-color: #EDE9FE;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #6B46C1;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/200x80/6B46C1/FFFFFF?text=Purple+Crayola", use_container_width=True)
    st.title("📊 Navigation")
    
    page = st.radio(
        "Select Section:",
        ["Overview", "Weekly Breakdown", "Platform Strategy", "Content Calendar", "KPIs & Goals", "Resources"]
    )
    
    st.divider()
    st.caption("**Prepared by:** Oluwatosin Daniel Adejumo")
    st.caption("**Role:** Content & Social Media Experience Manager")
    st.caption("**Date:** January 2, 2026")

# Main content
if page == "Overview":
    st.title("🎨 Purple Crayolá - January 2026 Content Strategy")
    st.markdown("### Digital Transformation Through Strategic Content")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Target Posts", "12-15", "Monthly")
    with col2:
        st.metric("Platforms", "3", "LinkedIn, Instagram, Twitter/X")
    with col3:
        st.metric("Content Themes", "4", "Strategic Pillars")
    with col4:
        st.metric("Expected Growth", "1-3%", "Conservative Target")
    
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
    st.markdown("## 🎯 January 2026 Content Themes")
    
    themes_col1, themes_col2 = st.columns(2)
    
    with themes_col1:
        st.markdown("""
        <div class="content-card">
        <h3>🚀 Theme 1: New Year, Digital Transformation</h3>
        <p>Capitalize on the new year energy and businesses setting digital goals.</p>
        </div>
        
        <div class="content-card">
        <h3>📊 Theme 2: Case Studies & Success Stories</h3>
        <p>Showcase real impact (like the patient menu app testimonial).</p>
        </div>
        """, unsafe_allow_html=True)
    
    with themes_col2:
        st.markdown("""
        <div class="content-card">
        <h3>📈 Theme 3: Digital Trends 2026</h3>
        <p>Position as thought leaders on emerging tech and digital strategies.</p>
        </div>
        
        <div class="content-card">
        <h3>👥 Theme 4: Behind the Scenes</h3>
        <p>Humanize the brand, introduce team members, show process.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Content Pillars
    st.markdown("## 📊 Content Pillars Distribution")
    
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
    st.title("📅 Weekly Content Breakdown")
    
    week = st.selectbox(
        "Select Week:",
        ["Week 1: January 2-5 (New Beginnings)",
         "Week 2: January 6-12 (Solutions Spotlight)",
         "Week 3: January 13-19 (Team & Culture)",
         "Week 4: January 20-26 (Authority Building)",
         "Week 5: January 27-31 (Month-End Push)"]
    )
    
    if "Week 1" in week:
        st.markdown("## 🎉 Week 1: New Beginnings (January 2-5)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: New Year Vision (Jan 2)
            
            **Content:**  
            "2026: The Year of Digital Excellence. As businesses reset and reimagine their strategies, 
            ask yourself: Is your digital infrastructure ready to scale? Purple Crayolá partners with 
            forward-thinking organizations to transform digital experiences. Let's make 2026 your breakthrough year."
            
            **Format:** Carousel with 3-5 slides on digital transformation pillars  
            **CTA:** Book a free digital audit consultation
            
            ---
            
            ### Post 2: Industry Trends (Jan 4)
            
            **Content:** "5 Digital Transformation Trends Shaping Nigerian Businesses in 2026"  
            **Format:** Infographic or short video (30-60 seconds)  
            **Topics:** AI integration, mobile-first experiences, data analytics, automation, personalization
            """)
        
        with tab2:
            st.markdown("""
            ### Welcome 2026 Story Series (Jan 2-3)
            
            - Quick polls: "What's your biggest digital challenge in 2026?"
            - Behind-the-scenes of team planning sessions
            - Quote graphic: "Innovation distinguishes between a leader and a follower"
            
            ---
            
            ### Feed Post (Jan 5)
            
            **Content:** "3 Signs Your Business Needs Digital Transformation in 2026"  
            **Format:** Carousel post with clean graphics, one sign per slide  
            **Include:** Actionable insights for each sign
            """)
        
        with tab3:
            st.markdown("""
            ### Daily Engagement
            
            - Daily tips thread: "Digital Transformation Tips for 2026" (5 tweets throughout the week)
            - Engagement tweets asking followers about their digital goals
            - Retweet industry news with Purple Crayolá's perspective
            """)
    
    elif "Week 2" in week:
        st.markdown("## 💡 Week 2: Solutions Spotlight (January 6-12)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Service Showcase - Web Development (Jan 7)
            
            **Content:**  
            "Your Website is Your Digital Storefront. Is it converting visitors into customers? 
            Our custom web development solutions are built with User Experience by Design. 
            Every click, every scroll, every interaction—optimized for results."
            
            **Format:** Before/after comparison or case study snippet  
            **CTA:** Download our Web Development Guide
            
            ---
            
            ### Post 2: Thought Leadership Article (Jan 9)
            
            **Content:** "Why Nigerian Businesses Can't Afford to Ignore Mobile-First Design in 2026"  
            **Format:** LinkedIn article (800-1000 words)  
            **Include:** Stats, examples, and Purple Crayolá's approach
            """)
        
        with tab2:
            st.markdown("""
            ### Service Carousel (Jan 8)
            
            **Content:** "What We Do at Purple Crayolá"  
            **Slides:** Digital Strategy → Web/App Dev → Digital Marketing → Branding → Learning Solutions  
            **Design:** Clean, branded graphics with icons
            
            ---
            
            ### Client Testimonial Post (Jan 10)
            
            - Feature the patient menu app testimonial
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
        st.markdown("## 👥 Week 3: Team & Culture (January 13-19)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Team Spotlight (Jan 14)
            
            **Content:** Introduce key team members (start with Founder, COO, Joy)  
            **Format:** Professional photo + mini Q&A about their role and vision  
            **Purpose:** Humanizes the brand
            
            ---
            
            ### Post 2: Process Post (Jan 16)
            
            **Content:** "How We Transform Ideas into Digital Reality: The Purple Crayolá Process"  
            **Format:** Infographic showing: Discovery → Strategy → Design → Development → Launch → Optimize  
            **Purpose:** Builds trust through transparency
            """)
        
        with tab2:
            st.markdown("""
            ### "Day in the Life" Stories (Jan 13-15)
            
            - Follow different team members through their workday
            - Show office culture, brainstorming sessions, client calls
            - Use interactive stickers (polls, questions, quizzes)
            
            ---
            
            ### Culture Post (Jan 18)
            
            **Content:** "What makes Purple Crayolá different?"  
            **Format:** Photo carousel of team collaboration, office vibes, project work  
            **Style:** Authentic, candid shots with engaging caption
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Content
            
            - #MotivationMonday with tech/innovation quotes
            - Wednesday wisdom: Share a lesson learned from projects
            - Engage with industry conversations
            """)
    
    elif "Week 4" in week:
        st.markdown("## 🏆 Week 4: Authority Building (January 20-26)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Case Study Deep Dive (Jan 21)
            
            **Content:** Full case study of a successful project (e.g., the patient menu app)  
            **Format:** Challenge → Solution → Results → Client Impact  
            **Include:** Metrics/outcomes if possible
            
            ---
            
            ### Post 2: Industry Commentary (Jan 23)
            
            **Content:** Respond to a trending tech topic in Nigeria/Africa  
            **Purpose:** Position Purple Crayolá as thought leaders  
            **Include:** Data and insights
            """)
        
        with tab2:
            st.markdown("""
            ### Educational Carousel (Jan 22)
            
            **Content:** "5 Common Website Mistakes Killing Your Conversions"  
            **Purpose:** Demonstrate expertise with practical value  
            **Format:** Each slide = one mistake + quick fix
            
            ---
            
            ### Interactive Post (Jan 25)
            
            **Content:** "Caption this!" or "What feature would you add to your dream app?"  
            **Purpose:** Drive engagement and community building
            """)
        
        with tab3:
            st.markdown("""
            ### Weekly Engagement
            
            - Share blog post or article (if Purple Crayolá has one)
            - Tech Thursday: Industry insights
            - Weekend engagement: Light, fun tech-related content
            """)
    
    else:  # Week 5
        st.markdown("## 🎯 Week 5: Month-End Push (January 27-31)")
        
        tab1, tab2, tab3 = st.tabs(["LinkedIn", "Instagram", "Twitter/X"])
        
        with tab1:
            st.markdown("""
            ### Post 1: Success Metrics (Jan 28)
            
            **Content:** "The ROI of Digital Transformation: Real Numbers from Real Clients"  
            **Format:** Data visualization showing impact  
            **Purpose:** Build credibility with concrete results
            
            ---
            
            ### Post 2: CTA Campaign (Jan 30)
            
            **Content:** "Ready to Transform Your Digital Presence? Let's Talk."  
            **Format:** Professional design with clear CTA  
            **Offer:** Special January offer or free consultation
            """)
        
        with tab2:
            st.markdown("""
            ### Month in Review (Jan 29)
            
            - Recap of January content and highlights
            - Stories: "Swipe through our January journey"
            - Post: Carousel of best moments
            
            ---
            
            ### February Teaser (Jan 31)
            
            **Content:** "February is going to be exciting! Here's what's coming..."  
            **Purpose:** Build anticipation for next month's content
            """)
        
        with tab3:
            st.markdown("""
            ### Month-End Wrap Up
            
            - Wrap-up thread: "January insights from Purple Crayolá"
            - Engage with followers who interacted throughout the month
            - Weekend poll: "What content do you want to see in February?"
            """)

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
        'Date': ['Jan 2', 'Jan 3', 'Jan 4', 'Jan 5', 'Jan 7', 'Jan 8', 'Jan 9', 'Jan 10',
                 'Jan 14', 'Jan 16', 'Jan 18', 'Jan 21', 'Jan 22', 'Jan 23', 'Jan 25',
                 'Jan 28', 'Jan 29', 'Jan 30', 'Jan 31'],
        'Platform': ['LinkedIn', 'Instagram', 'LinkedIn', 'Instagram', 'LinkedIn', 'Instagram',
                     'LinkedIn', 'Instagram', 'LinkedIn', 'LinkedIn', 'Instagram', 'LinkedIn',
                     'Instagram', 'LinkedIn', 'Instagram', 'LinkedIn', 'Instagram', 'LinkedIn', 'Instagram'],
        'Content Type': ['Carousel', 'Stories', 'Infographic', 'Carousel', 'Post', 'Carousel',
                        'Article', 'Testimonial', 'Team Spotlight', 'Process Post', 'Culture Post',
                        'Case Study', 'Educational Carousel', 'Industry Commentary', 'Interactive Post',
                        'Success Metrics', 'Month Review', 'CTA Campaign', 'February Teaser'],
        'Theme': ['New Year', 'New Year', 'Trends', 'Transformation', 'Services', 'Services',
                 'Thought Leadership', 'Success Stories', 'Team', 'Team', 'Culture',
                 'Authority', 'Authority', 'Authority', 'Engagement',
                 'Results', 'Recap', 'CTA', 'Preview'],
        'Status': ['Pending'] * 19
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
    st.title("🎯 KPIs & Realistic Goals")
    
    st.markdown("""
    <div class="highlight">
    <h3>⚠️ Month 1 Philosophy: Foundation Over Growth</h3>
    <p>January is about building sustainable systems, learning the brand voice, and understanding 
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
        #### Why Conservative?
        - You're new and learning the brand
        - January is typically slow post-holidays
        - Algorithm needs time to understand posting patterns
        - Quality foundation > vanity metrics
        """)
    
    with col2:
        st.markdown("### ✅ Process Goals (Most Important)")
        
        goals = [
            "Get access to all accounts",
            "Audit current performance baseline",
            "Create content calendar template",
            "Establish approval workflow",
            "Post consistently (80-90% target)",
            "Build content templates library",
            "Set up analytics tracking",
            "Respond to all engagement within 24-48 hours",
            "Build relationships with 10-15 key accounts",
            "Generate 2-5 meaningful inquiries"
        ]
        
        for goal in goals:
            st.checkbox(goal, key=goal)
    
    st.divider()
    
    # Metrics to track
    st.markdown("### 📊 Key Metrics to Track")
    
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
        - Consultation bookings
        - Website traffic from social
        - Lead generation
        - Response time
        """)
    
    st.divider()
    
    # 90-day vision
    st.markdown("### 🚀 90-Day Growth Vision")
    
    months_data = {
        'Month': ['January', 'February', 'March'],
        'Focus': ['Foundation & Learning', 'Optimization & Growth', 'Scale & Acceleration'],
        'Expected Growth': ['1-3%', '5-8%', '10-15%'],
        'Key Activities': [
            'Build systems, learn audience, establish consistency',
            'Optimize based on data, increase frequency, test formats',
            'Scale successful content, launch campaigns, build community'
        ]
    }
    
    months_df = pd.DataFrame(months_data)
    st.table(months_df)
    
    st.markdown("""
    <div class="highlight">
    <h4>💡 Setting Expectations with Leadership</h4>
    <p><strong>Recommended approach:</strong> "I'm focused on building a strong foundation in January—consistent 
    quality content, understanding our audience, and establishing systems. I expect modest growth (1-3%) as we 
    learn what resonates, with acceleration in months 2-3 once we have performance data."</p>
    </div>
    """, unsafe_allow_html=True)

else:  # Resources
    st.title("🛠️ Resources & Tools")
    
    tab1, tab2, tab3, tab4 = st.tabs(["Content Creation", "Scheduling & Analytics", "Hashtag Strategy", "Quick Wins"])
    
    with tab1:
        st.markdown("## 🎨 Content Creation Tools")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Design Tools
            - **Canva Pro** - Graphics and carousels
            - **Adobe Creative Suite** - Professional designs
            - **Figma** - Collaborative design work
            - **Remove.bg** - Background removal
            - **Unsplash/Pexels** - Stock photos
            
            ### Video Tools
            - **CapCut** - Video editing
            - **InShot** - Mobile video editing
            - **Loom** - Screen recording
            - **Descript** - Video transcription & editing
            """)
        
        with col2:
            st.markdown("""
            ### Writing Tools
            - **Grammarly** - Grammar checking
            - **Hemingway Editor** - Readability
            - **Claude/ChatGPT** - Content ideation
            - **Google Docs** - Collaboration
            
            ### Asset Management
            - **Google Drive** - File storage
            - **Dropbox** - File sharing
            - **Notion** - Content organization
            - **Airtable** - Content database
            """)
    
    with tab2:
        st.markdown("## 📅 Scheduling & Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Scheduling Tools
            - **Buffer** - Multi-platform scheduling
            - **Hootsuite** - Social media management
            - **Later** - Instagram-focused
            - **Meta Business Suite** - FB/IG native
            - **LinkedIn Native** - LinkedIn scheduling
            
            ### Calendar Management
            - **Google Sheets** - Simple calendar
            - **Notion** - Visual calendar
            - **Trello** - Kanban-style planning
            - **Asana** - Project management
            """)
        
        with col2:
            st.markdown("""
            ### Analytics Tools
            - **Native Platform Insights** - Free analytics
            - **Google Analytics** - Website traffic
            - **Sprout Social** - Comprehensive analytics
            - **Iconosquare** - Instagram analytics
            - **LinkedIn Analytics** - Professional insights
            
            ### Reporting
            - **Google Data Studio** - Visual reports
            - **Canva** - Report design
            - **Excel/Google Sheets** - Data analysis
            """)
    
    with tab3:
        st.markdown("## #️⃣ Hashtag Strategy")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### Branded Hashtags
            Use these consistently:
            - #PurpleCrayolá
            - #DigitalTransformationNG
            - #UserExperienceByDesign
            """)
        
        with col2:
            st.markdown("""
            ### Industry Hashtags
            Mix and match:
            - #DigitalTransformation
            - #WebDevelopment
            - #DigitalMarketing
            - #TechInNigeria
            - #NigerianStartups
            - #BusinessGrowth
            - #UXDesign
            - #TechStartup
            - #Innovation
            """)
        
        with col3:
            st.markdown("""
            ### Engagement Hashtags
            Day-specific:
            - #MotivationMonday
            - #TechTuesday
            - #WednesdayWisdom
            - #ThrowbackThursday
            - #FridayThoughts
            - #WeekendVibes
            """)
        
        st.divider()
        
        st.markdown("""
        ### 📝 Hashtag Best Practices
        
        **LinkedIn:**
        - Use 3-5 hashtags per post
        - Mix branded + industry hashtags
        - Place hashtags naturally in copy or at end
        
        **Instagram:**
        - Use 10-15 hashtags per post
        - Mix of high, medium, and low competition tags
        - Can place in caption or first comment
        - Use all 10 hashtag slots in stories
        
        **Twitter/X:**
        - Use 1-2 hashtags per tweet
        - Keep them relevant and timely
        - Participate in trending conversations when appropriate
        """)
    
    with tab4:
        st.markdown("## 🚀 Quick Wins for First Week")
        
        st.markdown("""
        <div class="highlight">
        <h3>Day 1-2: Setup & Foundation</h3>
        <ul>
        <li>✅ Get access to all social media accounts</li>
        <li>✅ Audit current content and performance baseline</li>
        <li>✅ Introduce yourself via Instagram stories</li>
        <li>✅ Review brand guidelines and tone of voice</li>
        <li>✅ Set up content calendar template</li>
        </ul>
        </div>
        
        <div class="highlight">
        <h3>Day 3: Launch Content</h3>
        <ul>
        <li>📱 Post New Year vision content across all platforms</li>
        <li>📊 Monitor engagement and respond to comments</li>
        <li>🎯 Document what works/doesn't work</li>
        </ul>
        </div>
        
        <div class="highlight">
        <h3>Day 4: Build Momentum</h3>
        <ul>
        <li>📈 Share industry trends post on LinkedIn</li>
        <li>💬 Engage with 10-15 industry accounts</li>
        <li>📝 Start drafting Week 2 content</li>
        </ul>
        </div>
        
        <div class="highlight">
        <h3>Day 5: Establish Consistency</h3>
        <ul>
        <li>🎨 Post carousel about digital transformation signs</li>
        <li>📅 Schedule Week 2 content in advance</li>
        <li>📊 Review Week 1 analytics</li>
        </ul>
        </div>
        
        <div class="highlight">
        <h3>Weekend: Plan Ahead</h3>
        <ul>
        <li>📝 Create content for Week 2</li>
        <li>🎨 Design graphics and carousels</li>
        <li>📋 Prepare approval workflow with Joy/COO</li>
        <li>📊 Set up analytics tracking dashboard</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("## 💡 Pro Tips for Success")
        
        tips_col1, tips_col2 = st.columns(2)
        
        with tips_col1:
            st.markdown("""
            ### Content Creation Tips
            - **Batch create content** - Set aside 2-3 hours to create multiple posts at once
            - **Use templates** - Create reusable templates for faster production
            - **Keep a swipe file** - Save inspiring content from other brands
            - **Plan ahead** - Always have 3-5 posts ready in reserve
            - **Repurpose content** - One blog post = LinkedIn article + Instagram carousel + Twitter thread
            """)
        
        with tips_col2:
            st.markdown("""
            ### Engagement Tips
            - **Respond quickly** - Aim for <2 hour response time during business hours
            - **Ask questions** - End posts with engaging questions
            - **Tag strategically** - Mention relevant brands, partners, team members
            - **Use stories actively** - Post to stories daily for algorithm favor
            - **Engage first** - Spend 15 mins engaging with others before posting your content
            """)
        
        st.divider()
        
        st.markdown("## 📋 Monthly Checklist")
        
        checklist_items = [
            ("Week 1", "Foundation setup, access accounts, audit baseline, launch first posts"),
            ("Week 2", "Establish posting rhythm, test content types, engage with community"),
            ("Week 3", "Introduce team/culture, optimize based on early data, build relationships"),
            ("Week 4", "Showcase authority with case studies, increase engagement tactics"),
            ("Week 5", "Month-end push, review analytics, plan February content"),
        ]
        
        for week, tasks in checklist_items:
            st.checkbox(f"**{week}:** {tasks}", key=f"checklist_{week}")
        
        st.divider()
        
        st.markdown("""
        ## 🎯 Key Success Indicators
        
        By end of January, you should have:
        
        ✅ **Consistent Presence** - Posted 80-90% of planned content  
        ✅ **Systems Established** - Content calendar, approval workflow, analytics tracking  
        ✅ **Brand Understanding** - Clear grasp of Purple Crayolá's voice and audience  
        ✅ **Baseline Data** - Performance metrics to inform February strategy  
        ✅ **Community Building** - Relationships with 10-15 key industry accounts  
        ✅ **Lead Generation** - 2-5 meaningful business inquiries  
        ✅ **Template Library** - Reusable content templates for efficiency  
        ✅ **Approval Process** - Clear workflow with Joy and COO  
        """)

# Footer
st.divider()
st.markdown("""
    <div style='text-align: center; color: #6B46C1; padding: 20px;'>
        <p><strong>Purple Crayolá - January 2026 Content Strategy</strong></p>
        <p>Prepared by: Oluwatosin Daniel Adejumo | Content & Social Media Experience Manager</p>
        <p style='font-size: 0.9em; color: #888;'>Foundation Over Growth • Quality Over Quantity • Consistency Over Perfection</p>
    </div>
""", unsafe_allow_html=True)