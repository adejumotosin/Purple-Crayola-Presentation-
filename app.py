import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Purple Crayolá - January 2026 Content Calendar",
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
    
    .content-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.07);
        margin-bottom: 20px;
        border-top: 3px solid #6B46C1;
    }
    
    .post-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 15px;
        border-left: 3px solid #6B46C1;
    }
    
    .asset-badge {
        display: inline-block;
        background: #EDE9FE;
        color: #6B46C1;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        margin: 3px;
    }
    
    .platform-badge {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 15px;
        font-size: 11px;
        font-weight: 600;
        margin: 2px;
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
    
    .author-badge {
        background: rgba(255,255,255,0.1);
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        margin-top: 20px;
        backdrop-filter: blur(10px);
    }
    
    .caption-box {
        background: #f8fafc;
        padding: 15px;
        border-radius: 8px;
        border-left: 3px solid #6B46C1;
        font-size: 14px;
        line-height: 1.6;
        margin: 10px 0;
    }
    
    .visual-brief {
        background: #fef3c7;
        padding: 15px;
        border-radius: 8px;
        border-left: 3px solid #f59e0b;
        font-size: 14px;
        line-height: 1.6;
        margin: 10px 0;
    }
    
    .video-brief {
        background: #dbeafe;
        padding: 15px;
        border-radius: 8px;
        border-left: 3px solid #3b82f6;
        font-size: 14px;
        line-height: 1.6;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <h3 style="color: white; margin: 5px 0;">Purple Crayolá</h3>
            <p style="color: rgba(255,255,255,0.8); font-size: 12px; margin: 0;">Content Strategy Dashboard</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.title("📊 Navigation")
    
    page = st.radio(
        "Select Section:",
        ["📋 Overview", "📅 Week 1 (Jan 12-17)", "📅 Week 2 (Jan 19-24)", "📅 Week 3 (Jan 26-31)", 
         "🎨 Design Assets Tracker", "📊 Content Analytics", "📥 Export & Resources"]
    )
    
    st.divider()
    
    # Author section
    st.markdown("""
        <div class="author-badge">
            <p style="font-size: 11px; margin: 0; opacity: 0.8;">PREPARED BY</p>
            <p style="font-size: 15px; font-weight: 600; margin: 5px 0;">Oluwatosin Adejumo</p>
            <p style="font-size: 11px; margin: 0; opacity: 0.8;">Content & Social Media Manager</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.caption("**Strategy Period:** January 12-31, 2026")
    st.caption("**Version:** 1.0")
    st.caption("**Last Updated:** January 8, 2026")

# Main content
if page == "📋 Overview":
    st.title("🎨 Purple Crayolá - January 2026 Content Strategy")
    st.markdown("### Digital Transformation Through Strategic Content")
    st.markdown("**Strategy Period:** January 12 - January 31, 2026 (3 Weeks)")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Total Posts</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">34</p>
                <p style="font-size: 13px; color: #10b981; margin-top: 8px;">↑ Across 3 weeks</p>
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
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Design Assets</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">16</p>
                <p style="font-size: 13px; color: #f59e0b; margin-top: 8px;">→ Carousels & Graphics</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
            <div style="background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.07); border-left: 4px solid #6B46C1; min-height: 140px;">
                <p style="font-size: 14px; font-weight: 500; color: #64748b; margin-bottom: 10px;">Video Assets</p>
                <p style="font-size: 36px; font-weight: 700; color: #1e293b; margin: 0;">3</p>
                <p style="font-size: 13px; color: #3b82f6; margin-top: 8px;">→ 30-60 second videos</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Content Mix Strategy
    st.markdown("## 🎯 Content Mix Strategy")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Pie chart
        content_mix = {
            'Category': ['Promotional', 'Educational', 'Thought Leadership', 'Engagement'],
            'Percentage': [30, 30, 20, 20],
            'Count': [10, 10, 7, 7]
        }
        
        fig = go.Figure(data=[go.Pie(
            labels=content_mix['Category'],
            values=content_mix['Percentage'],
            hole=.4,
            marker_colors=['#6B46C1', '#9F7AEA', '#D6BCFA', '#EDE9FE'],
            textinfo='label+percent',
            textfont_size=14
        )])
        
        fig.update_layout(
            title="Content Distribution by Category",
            height=400,
            showlegend=True,
            font=dict(family="Inter, sans-serif")
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
        <h4>Content Breakdown</h4>
        <p><strong>30% Promotional</strong><br>
        Core services, Presence launch, packages</p>
        
        <p><strong>30% Educational</strong><br>
        Tips, how-tos, frameworks, guides</p>
        
        <p><strong>20% Thought Leadership</strong><br>
        Industry insights, positioning, visibility</p>
        
        <p><strong>20% Engagement</strong><br>
        Polls, questions, community conversations</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Weekly Overview
    st.markdown("## 📅 Weekly Overview")
    
    weeks_col1, weeks_col2, weeks_col3 = st.columns(3)
    
    with weeks_col1:
        st.markdown("""
        <div class="content-card">
        <h3>Week 1: Jan 12-17</h3>
        <p><strong>Focus:</strong> Foundation Building</p>
        <p><strong>Posts:</strong> 11</p>
        <p><strong>Design Assets:</strong> 4</p>
        <p><strong>Videos:</strong> 1</p>
        <hr>
        <p style="font-size: 13px;">Introduce core services, establish authority, begin visibility conversation</p>
        </div>
        """, unsafe_allow_html=True)
    
    with weeks_col2:
        st.markdown("""
        <div class="content-card">
        <h3>Week 2: Jan 19-24</h3>
        <p><strong>Focus:</strong> Authority Building</p>
        <p><strong>Posts:</strong> 11</p>
        <p><strong>Design Assets:</strong> 5</p>
        <p><strong>Videos:</strong> 1</p>
        <hr>
        <p style="font-size: 13px;">Educational content, soft Presence positioning, thought leadership</p>
        </div>
        """, unsafe_allow_html=True)
    
    with weeks_col3:
        st.markdown("""
        <div class="content-card">
        <h3>Week 3: Jan 26-31</h3>
        <p><strong>Focus:</strong> Presence Launch</p>
        <p><strong>Posts:</strong> 12</p>
        <p><strong>Design Assets:</strong> 7</p>
        <p><strong>Videos:</strong> 1</p>
        <hr>
        <p style="font-size: 13px;">Official Presence launch, package reveal, month-end reflection</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Key Highlights
    st.markdown("## ⭐ Key Strategy Highlights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight">
        <h4>🎯 Strategic Approach</h4>
        <ul>
        <li><strong>Week 1:</strong> Build credibility with Purple Crayolá's core services</li>
        <li><strong>Week 2:</strong> Establish authority through educational content</li>
        <li><strong>Week 3:</strong> Launch Presence after building trust</li>
        <li><strong>Consistent:</strong> 3-4 posts per week across platforms</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight">
        <h4>💡 Content Philosophy</h4>
        <ul>
        <li>LinkedIn & Instagram content is identical for efficiency</li>
        <li>Twitter/X provides real-time engagement and threads</li>
        <li>Balance promotional content with genuine value</li>
        <li>Build community through consistent engagement</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Platform Strategy
    st.markdown("## 📱 Platform Strategy")
    
    platform_data = pd.DataFrame({
        'Platform': ['LinkedIn', 'Instagram', 'Twitter/X'],
        'Posts per Week': ['3-4', '3-4', '5-7'],
        'Primary Focus': ['B2B, Thought Leadership', 'Visual Storytelling', 'Real-time Engagement'],
        'Content Types': ['Carousels, Articles, Videos', 'Carousels, Reels, Stories', 'Threads, Single Tweets']
    })
    
    st.dataframe(platform_data, use_container_width=True, hide_index=True)

elif page in ["📅 Week 1 (Jan 12-17)", "📅 Week 2 (Jan 19-24)", "📅 Week 3 (Jan 26-31)"]:
    # Extract week number
    if "Week 1" in page:
        week_num = 1
        week_date = "January 12-17, 2026"
        week_focus = "Foundation Building"
    elif "Week 2" in page:
        week_num = 2
        week_date = "January 19-24, 2026"
        week_focus = "Authority Building"
    else:
        week_num = 3
        week_date = "January 26-31, 2026"
        week_focus = "Presence Launch"
    
    st.title(f"📅 Week {week_num}: {week_date}")
    st.markdown(f"### Focus: {week_focus}")
    
    # Week summary
    if week_num == 1:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Posts", "11", help="Across all platforms")
        with col2:
            st.metric("Design Assets", "4", help="Carousels & graphics needed")
        with col3:
            st.metric("Video Assets", "1", help="Videos needed")
        with col4:
            st.metric("Platforms", "3", help="LinkedIn, Instagram, Twitter/X")
    elif week_num == 2:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Posts", "11", help="Across all platforms")
        with col2:
            st.metric("Design Assets", "5", help="Carousels & graphics needed")
        with col3:
            st.metric("Video Assets", "1", help="Videos needed")
        with col4:
            st.metric("Platforms", "3", help="LinkedIn, Instagram, Twitter/X")
    else:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Posts", "12", help="Across all platforms")
        with col2:
            st.metric("Design Assets", "7", help="Carousels & graphics needed")
        with col3:
            st.metric("Video Assets", "1", help="Videos needed")
        with col4:
            st.metric("Platforms", "3", help="LinkedIn, Instagram, Twitter/X")
    
    st.divider()
    
    # Day selector
    if week_num == 1:
        days = ["Monday, Jan 12", "Tuesday, Jan 13", "Wednesday, Jan 14", "Thursday, Jan 15", "Friday, Jan 16", "Saturday, Jan 17"]
    elif week_num == 2:
        days = ["Monday, Jan 19", "Tuesday, Jan 20", "Wednesday, Jan 21", "Thursday, Jan 22", "Friday, Jan 23", "Saturday, Jan 24"]
    else:
        days = ["Monday, Jan 26", "Tuesday, Jan 27", "Wednesday, Jan 28", "Thursday, Jan 29", "Friday, Jan 30", "Saturday, Jan 31"]
    
    selected_day = st.selectbox("Select Day:", days)
    
    st.divider()
    
    # Week 1 Content
    if week_num == 1:
        if "Jan 12" in selected_day:
            st.markdown("## 📱 MONDAY, JANUARY 12, 2026")
            
            # LinkedIn & Instagram Post
            st.markdown("### LinkedIn & Instagram Post")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Photo Post | **Mix:** Promotional (30%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Design Requirements:</h4>
                <p><strong>Asset Type:</strong> Photo Post / Graphic</p>
                <p><strong>Dimensions:</strong> Square (1080x1080px) for Instagram, can adapt for LinkedIn</p>
                
                <p><strong>Visual Elements:</strong></p>
                <ul>
                <li>Purple gradient background (#6B46C1 to #553C9A)</li>
                <li>Modern, clean design with text overlay</li>
                <li>Purple Crayolá logo placement</li>
                </ul>
                
                <p><strong>Text on Image:</strong></p>
                <ul>
                <li><strong>Main Text:</strong> "Digital Transformation Starts Here"</li>
                <li><strong>Supporting Text:</strong> "Strategy • Design • Development • Growth"</li>
                </ul>
                
                <p><strong>Design Style:</strong> Professional, modern, clean, bold typography</p>
                </div>
                """, unsafe_allow_html=True)
            
            with st.expander("📝 CAPTIONS", expanded=False):
                st.markdown("#### LinkedIn Caption:")
                st.markdown("""
                <div class="caption-box">
                "Digital Transformation in 2026: Are You Ready?

The businesses winning in 2026 aren't just adopting technology—they're transforming how they connect with customers, operate internally, and scale their impact.

At Purple Crayolá, we partner with forward-thinking organizations to:
🎯 Build digital strategies that align with business goals
💻 Develop web and mobile solutions that users love
📱 Create digital marketing campaigns that drive measurable results
🎨 Design brand identities that stand out

Whether you're a startup looking to establish your digital presence or an established business ready to scale, we're here to transform your vision into reality.

What's your biggest digital challenge in 2026? Drop it in the comments—we'd love to help.

#DigitalTransformation #PurpleCrayolá #BusinessGrowth #TechInNigeria #DigitalStrategy"
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("#### Instagram Caption:")
                st.markdown("""
                <div class="caption-box">
                "Digital Transformation in 2026: Are You Ready? 🚀

The businesses winning in 2026 aren't just adopting technology—they're transforming experiences.

Purple Crayolá delivers:
🎯 Digital Strategy
💻 Web & Mobile Development
📱 Digital Marketing
🎨 Brand Design

From startups to established businesses—we transform vision into reality.

What's your biggest digital challenge in 2026? Drop it in the comments 👇

#DigitalTransformation #PurpleCrayolá #BusinessGrowth #TechInNigeria #DigitalStrategy #StartupLife #WebDevelopment #DigitalMarketing"
                </div>
                """, unsafe_allow_html=True)
            
            st.divider()
            
            # Twitter Thread
            st.markdown("### Twitter/X Thread")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 2:00 PM WAT | **Type:** Thread (6 tweets) | **Mix:** Educational (30%)")
            
            with st.expander("🐦 THREAD CONTENT", expanded=False):
                st.markdown("""
                <div class="caption-box">
                <p><strong>Tweet 1 (Hook):</strong><br>
                "6 signs your business needs digital transformation in 2026:

(Most companies ignore #3 until it's too late) 🧵"</p>

<p><strong>Tweet 2:</strong><br>
"1/ Your competitors are reaching customers faster

They're on social. They have mobile apps. They're sending targeted emails.

You're still relying on word-of-mouth and hoping people find you.

Speed matters in 2026."</p>

<p><strong>Tweet 3:</strong><br>
"2/ Your website looks (and feels) outdated

If your site isn't mobile-responsive, loads slowly, or confuses visitors—you're losing customers every day.

First impressions are digital now."</p>

<p><strong>Tweet 4:</strong><br>
"3/ You have no idea where your customers come from

No analytics. No tracking. No data.

You're spending money on marketing but can't measure what works.

That's guessing, not strategy."</p>

<p><strong>Tweet 5:</strong><br>
"4/ Your team is drowning in manual processes

Tasks that should take minutes are taking hours.
Automation exists. Use it."</p>

<p><strong>Tweet 6:</strong><br>
"5/ You're not showing up online consistently

No social media presence. No content strategy. No digital footprint.

In 2026, if you're not visible online, you don't exist to most customers."</p>

<p><strong>Tweet 7:</strong><br>
"6/ You know you need to change but don't know where to start

That's where we come in.

Digital transformation doesn't have to be overwhelming.

Purple Crayolá: Strategy. Design. Development. Growth.

Let's talk: purplecrayola.com"</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 13" in selected_day:
            st.markdown("## 📱 TUESDAY, JANUARY 13, 2026")
            
            # LinkedIn & Instagram Carousel
            st.markdown("### LinkedIn & Instagram Carousel")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Carousel (7 slides) | **Mix:** Educational (30%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Design Requirements:</h4>
                <p><strong>Asset Type:</strong> Carousel (7 slides)</p>
                <p><strong>Dimensions:</strong> 1080x1080px per slide</p>
                
                <p><strong>Design Style:</strong> Clean, professional, readable text, consistent branding</p>
                <p><strong>Color Scheme:</strong> Purple Crayolá brand colors with modern, minimalist aesthetic</p>
                
                <p><strong>Slide Breakdown:</strong></p>
                
                <p><strong>Slide 1 - Cover:</strong></p>
                <ul>
                <li>Title: "5 Digital Marketing Mistakes Costing You Customers"</li>
                <li>Subtitle: "Are you making these errors?"</li>
                <li>Purple Crayolá logo</li>
                </ul>
                
                <p><strong>Slide 2:</strong></p>
                <ul>
                <li>Headline: "Mistake #1: No Clear Strategy"</li>
                <li>Body text: "Posting randomly on social media without a content plan, target audience definition, or measurable goals. Result: Wasted time and money."</li>
                <li>Icon/visual element</li>
                </ul>
                
                <p><strong>Slide 3:</strong></p>
                <ul>
                <li>Headline: "Mistake #2: Ignoring Mobile Users"</li>
                <li>Body text: "Over 70% of Nigerian internet users access the web via mobile. If your site isn't mobile-optimized, you're losing 7 out of 10 potential customers."</li>
                <li>Icon/visual element</li>
                </ul>
                
                <p><strong>Slide 4:</strong></p>
                <ul>
                <li>Headline: "Mistake #3: Not Tracking Results"</li>
                <li>Body text: "You can't improve what you don't measure. Without analytics, you're flying blind—spending money without knowing what works."</li>
                <li>Icon/visual element</li>
                </ul>
                
                <p><strong>Slide 5:</strong></p>
                <ul>
                <li>Headline: "Mistake #4: Inconsistent Branding"</li>
                <li>Body text: "Different logos, colors, and messaging across platforms confuse customers and weaken brand recognition. Consistency builds trust."</li>
                <li>Icon/visual element</li>
                </ul>
                
                <p><strong>Slide 6:</strong></p>
                <ul>
                <li>Headline: "Mistake #5: No SEO Strategy"</li>
                <li>Body text: "If your website doesn't show up on Google, potential customers can't find you. SEO isn't optional—it's essential for visibility."</li>
                <li>Icon/visual element</li>
                </ul>
                
                <p><strong>Slide 7 - CTA:</strong></p>
                <ul>
                <li>Headline: "Ready to Fix These Mistakes?"</li>
                <li>Body: "Purple Crayolá builds data-driven digital marketing strategies that deliver results."</li>
                <li>CTA: "Get your free consultation → purplecrayola.com"</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with st.expander("📝 CAPTIONS", expanded=False):
                st.markdown("#### LinkedIn Caption:")
                st.markdown("""
                <div class="caption-box">
                "5 Digital Marketing Mistakes Costing You Customers (Save This) 💸

Most businesses are leaving money on the table because of preventable digital marketing mistakes.

Here are the 5 most common errors we see—and how to fix them:

1️⃣ No Clear Strategy
Random posts without goals = wasted resources. Define your audience, platforms, and KPIs first.

2️⃣ Ignoring Mobile Users
70%+ of Nigerian users are on mobile. Mobile-first design isn't optional anymore.

3️⃣ Not Tracking Results
No analytics = no improvement. Track everything: traffic, conversions, engagement.

4️⃣ Inconsistent Branding
Inconsistent visuals and messaging confuse customers. Build a brand guide and stick to it.

5️⃣ No SEO Strategy
If Google can't find you, customers can't either. Invest in SEO from day one.

At Purple Crayolá, we help businesses build digital marketing strategies that are strategic, measurable, and results-driven.

Which mistake are you working to fix? Let us know in the comments.

Need help? Let's talk: purplecrayola.com

#DigitalMarketing #MarketingStrategy #SEO #BusinessGrowth #PurpleCrayolá #ContentMarketing #SocialMediaMarketing"
                </div>
                """, unsafe_allow_html=True)
            
            st.divider()
            
            # Twitter Engagement
            st.markdown("### Twitter/X Engagement Tweet")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 3:00 PM WAT | **Type:** Engagement Tweet | **Mix:** Engagement (20%)")
            
            with st.expander("🐦 TWEET CONTENT", expanded=False):
                st.markdown("""
                <div class="caption-box">
                <p><strong>Main Tweet:</strong><br>
                "Quick question for business owners:

What's your #1 struggle with digital marketing right now?

A) Creating consistent content
B) Getting quality traffic
C) Converting visitors to customers
D) Measuring ROI

Drop your answer below 👇"</p>

                <p><strong>Follow-up Strategy:</strong><br>
                Reply to every response with helpful tips or questions to continue the conversation.</p>
                
                <p><strong>Example Replies:</strong></p>
                <ul>
                <li>For A: "Consistency is tough! Have you tried batching content? Create a week's worth in one sitting."</li>
                <li>For B: "Quality > quantity. Focus on SEO + targeted social ads for your specific audience."</li>
                <li>For C: "Conversion is about trust. Are you using social proof, clear CTAs, and simplifying the process?"</li>
                <li>For D: "Analytics are key. Start simple: Google Analytics + UTM codes. Track what matters to your business."</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 14" in selected_day:
            st.markdown("## 📱 WEDNESDAY, JANUARY 14, 2026")
            
            st.markdown("### LinkedIn & Instagram Post")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Photo Post | **Mix:** Thought Leadership (20%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Design Requirements:</h4>
                <p><strong>Asset Type:</strong> Quote Graphic</p>
                <p><strong>Dimensions:</strong> 1080x1080px</p>
                
                <p><strong>Design Style:</strong> Bold, professional graphic with quote-style design</p>
                <p><strong>Visual Elements:</strong></p>
                <ul>
                <li>Purple gradient background</li>
                <li>Modern typography, inspirational but professional</li>
                <li>Purple Crayolá logo in corner</li>
                </ul>
                
                <p><strong>Text on Image:</strong></p>
                <ul>
                <li><strong>Main Text:</strong> "Your website is your digital storefront. Make it worth visiting."</li>
                <li><strong>Supporting Text:</strong> "— Purple Crayolá"</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with st.expander("📝 CAPTIONS", expanded=False):
                st.markdown("#### LinkedIn Caption:")
                st.code("""Your Website Is Your Digital Storefront. Make It Worth Visiting.

Think about it: Before customers walk into your office, book a call, or sign a contract—they visit your website.

In that moment, they're judging:
• Is this business professional?
• Can I trust them?
• Do they understand my needs?
• Is this worth my time?

Your website answers these questions in seconds.

A slow, outdated, or confusing website tells customers: "We're not ready for your business."

A fast, modern, user-friendly website says: "We're professional, trustworthy, and here to help."

At Purple Crayolá, we build websites that don't just look good—they convert visitors into customers. Every design decision is rooted in user experience, performance, and business goals.

Your digital storefront matters. Is yours working for you or against you?

If you're ready to upgrade your website, let's talk: purplecrayola.com

#WebDevelopment #WebDesign #UserExperience #DigitalTransformation #PurpleCrayolá #BusinessGrowth #UXDesign""")
            
            st.divider()
            
            st.markdown("### Twitter/X Tweet")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 2:00 PM WAT | **Type:** Single Tweet | **Mix:** Thought Leadership (20%)")
            
            with st.expander("🐦 TWEET CONTENT", expanded=False):
                st.code("""Your website isn't just a digital brochure.

It's your 24/7 salesperson.

Is it:
✅ Fast and mobile-friendly?
✅ Clear about what you offer?
✅ Easy to navigate?
✅ Converting visitors to customers?

If not, you're losing sales every day.

Fix it.""")
        
        elif "Jan 15" in selected_day:
            st.markdown("## 📱 THURSDAY, JANUARY 15, 2026")
            
            st.markdown("### LinkedIn & Instagram Video")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Video (30-45 seconds) | **Mix:** Promotional (30%)")
            
            with st.expander("🎥 VIDEO BRIEF FOR VIDEO EDITOR", expanded=True):
                st.markdown("""
                <div class="video-brief">
                <h4>Video Production Requirements:</h4>
                <p><strong>Duration:</strong> 30-45 seconds</p>
                <p><strong>Format:</strong> Square (1080x1080px) for Instagram/LinkedIn</p>
                <p><strong>Style:</strong> Professional with motion graphics</p>
                
                <p><strong>Visual Elements:</strong></p>
                <ul>
                <li>Purple Crayolá branding throughout</li>
                <li>Text overlays for key points</li>
                <li>Background music: Upbeat, modern, professional (not too loud)</li>
                <li>B-roll: Digital interfaces, laptop/mobile screens, design elements (stock footage acceptable)</li>
                </ul>
                
                <p><strong>Scene Breakdown:</strong></p>
                
                <p><strong>Scene 1 (0-7s) - Hook:</strong></p>
                <ul>
                <li>Text: "Is Your Business Ready for Digital Transformation?"</li>
                <li>Visual: Split screen - basic website vs modern digital experience</li>
                </ul>
                
                <p><strong>Scene 2 (8-15s) - Problem:</strong></p>
                <ul>
                <li>Text: "The Difference?"</li>
                <li>Visual: Graphs showing growth, engagement metrics</li>
                <li>Narration: "Being online means you have a website. Being transformed means results."</li>
                </ul>
                
                <p><strong>Scene 3 (16-25s) - Solution:</strong></p>
                <ul>
                <li>Text: "Purple Crayolá: Full-Service Digital Transformation"</li>
                <li>Visual: Quick showcase of services with icons</li>
                </ul>
                
                <p><strong>Scene 4 (26-35s) - Services:</strong></p>
                <ul>
                <li>Text: "What We Do:"</li>
                <li>Bullet points appear: Digital Strategy, Development, Marketing, Design, Product Management</li>
                </ul>
                
                <p><strong>Scene 5 (36-45s) - CTA:</strong></p>
                <ul>
                <li>Text: "Ready to Transform?"</li>
                <li>CTA: "purplecrayola.com" + "Book Your Free Consultation"</li>
                <li>Purple Crayolá logo</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with st.expander("📝 VIDEO CAPTIONS", expanded=False):
                st.markdown("#### LinkedIn Caption:")
                st.code("""Digital Transformation vs. Just Being Online—What's the Difference?

Most Nigerian businesses have websites. But having a website doesn't mean you're digitally transformed.

Being online = You exist on the internet
Being transformed = Your digital presence drives measurable business results

At Purple Crayolá, we deliver full-service digital transformation:

🎯 Digital Strategy - Aligned with your business goals
💻 Web & Mobile Development - User-friendly, fast, scalable
📱 Digital Marketing - SEO, content, social media, PPC
🎨 Brand Design - Identities that stand out
📊 Product Management - From concept to launch

We don't just build websites. We transform how you connect with customers, operate internally, and scale your business.

Ready to move beyond "just online" to digitally transformed?

Book your free consultation: purplecrayola.com

#DigitalTransformation #WebDevelopment #DigitalMarketing #PurpleCrayolá #BusinessGrowth #TechInNigeria #NigerianStartups""")
            
            st.divider()
            
            st.markdown("### Twitter/X Tweets")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            
            with st.expander("🐦 TWEET CONTENT", expanded=False):
                st.markdown("**Tweet 1 (12:00 PM WAT):**")
                st.code("""Having a website ≠ Digital Transformation

One puts you on the internet.
The other transforms your business.

Purple Crayolá delivers full-service digital transformation:
• Strategy
• Development
• Marketing
• Design
• Growth

Ready to transform? purplecrayola.com""")
                
                st.markdown("**Follow-up Tweet (1 hour later):**")
                st.code("""What does 'digital transformation' mean to your business?

For some, it's a new website.
For others, it's automation, data analytics, or customer experience.

There's no one-size-fits-all answer.

What's your digital transformation goal? 👇""")
        
        elif "Jan 16" in selected_day:
            st.markdown("## 📱 FRIDAY, JANUARY 16, 2026")
            
            st.markdown("### LinkedIn & Instagram Carousel")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Carousel (8 slides) | **Mix:** Educational (30%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Design Requirements:</h4>
                <p><strong>Asset Type:</strong> Carousel (8 slides)</p>
                <p><strong>Dimensions:</strong> 1080x1080px per slide</p>
                
                <p><strong>Design Style:</strong> Professional, easy-to-read, shareable</p>
                <p><strong>Color Scheme:</strong> Purple Crayolá branding with icons and visual hierarchy</p>
                
                <p><strong>Slide Structure:</strong></p>
                
                <p><strong>Slide 1 - Cover:</strong></p>
                <ul>
                <li>Title: "6 Essential Elements Every Business Website Needs"</li>
                <li>Subtitle: "Is your website missing any of these?"</li>
                </ul>
                
                <p><strong>Slides 2-7:</strong> Each slide covers one element with:</p>
                <ul>
                <li>Headline with element name</li>
                <li>Body text explaining the element</li>
                <li>Icon representing the element</li>
                </ul>
                
                <p><strong>Elements:</strong></p>
                <ol>
                <li>Clear Value Proposition (Target icon)</li>
                <li>Mobile Responsiveness (Mobile phone icon)</li>
                <li>Fast Load Speed (Speedometer icon)</li>
                <li>Clear Call-to-Action (Button/cursor icon)</li>
                <li>Social Proof (Star/rating icon)</li>
                <li>Easy Navigation (Compass icon)</li>
                </ol>
                
                <p><strong>Slide 8 - CTA:</strong></p>
                <ul>
                <li>Headline: "Is Your Website Missing Any of These?"</li>
                <li>CTA: "Book your consultation → purplecrayola.com"</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with st.expander("📝 CAPTIONS", expanded=False):
                st.markdown("See full captions in content calendar document")
            
            st.divider()
            
            st.markdown("### Twitter/X Thread")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 11:00 AM WAT | **Type:** Thread (8 tweets) | **Mix:** Educational (30%)")
            
            with st.expander("🐦 THREAD OUTLINE", expanded=False):
                st.markdown("""
                - Tweet 1: Hook about 6 essential elements
                - Tweets 2-7: One element per tweet
                - Tweet 8: CTA with purplecrayola.com link
                
                Full thread content available in content calendar document.
                """)
        
        elif "Jan 17" in selected_day:
            st.markdown("## 📱 SATURDAY, JANUARY 17, 2026")
            
            st.markdown("### Twitter/X Only")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Engagement Tweet | **Mix:** Engagement (20%)")
            
            with st.expander("🐦 TWEET CONTENT", expanded=False):
                st.code("""Weekend question for business owners:

If you could improve ONE thing about your website on Monday, what would it be?

A) Speed
B) Design
C) Mobile experience
D) Content/messaging
E) Something else (tell us!)

👇👇👇""")
                
                st.markdown("""
                <p><strong>Follow-up Strategy:</strong> Engage with every response with tips</p>
                """, unsafe_allow_html=True)
    
    # Week 2 Content
    elif week_num == 2:
        if "Jan 19" in selected_day:
            st.markdown("## 📱 MONDAY, JANUARY 19, 2026")
            st.markdown("### LinkedIn & Instagram Carousel - SEO in 2026")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Carousel (8 slides) | **Mix:** Educational (30%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Carousel: "SEO in 2026: What Actually Works"</h4>
                <p><strong>Slides:</strong> 8 slides total</p>
                <p><strong>Cover + 6 SEO elements + CTA slide</strong></p>
                
                <p>Elements to cover:</p>
                <ol>
                <li>Mobile-First Indexing</li>
                <li>Quality Content Over Keywords</li>
                <li>Page Speed Is Critical</li>
                <li>Local SEO for Nigerian Businesses</li>
                <li>User Experience Signals</li>
                <li>Build Quality Backlinks</li>
                </ol>
                
                <p>Full design brief in content calendar document.</p>
                </div>
                """, unsafe_allow_html=True)
            
            st.divider()
            
            st.markdown("### Twitter/X Thread")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 2:00 PM WAT | **Type:** Thread (8 tweets) | **Mix:** Educational (30%)")
        
        elif "Jan 20" in selected_day:
            st.markdown("## 📱 TUESDAY, JANUARY 20, 2026")
            st.markdown("### LinkedIn & Instagram Quote Post")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Photo Post | **Mix:** Thought Leadership (20%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Quote Graphic</h4>
                <p><strong>Main Text:</strong><br>
                "Visibility without strategy is noise.<br>
                Strategy without execution is a dream.<br>
                Excellence without visibility is invisible."</p>
                
                <p><strong>Supporting Text:</strong> "Build all three."</p>
                <p><strong>Footer:</strong> "— Purple Crayolá"</p>
                
                <p><strong>Style:</strong> Bold, inspiring, professional on purple gradient</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 21" in selected_day:
            st.markdown("## 📱 WEDNESDAY, JANUARY 21, 2026")
            st.markdown("### LinkedIn & Instagram Video")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Video (35-50 seconds) | **Mix:** Promotional (30%)")
            
            with st.expander("🎥 VIDEO BRIEF FOR VIDEO EDITOR", expanded=True):
                st.markdown("""
                <div class="video-brief">
                <h4>Video: "Why Most Digital Marketing Campaigns Fail"</h4>
                <p><strong>Duration:</strong> 35-50 seconds</p>
                
                <p><strong>Scene Structure:</strong></p>
                <ol>
                <li>Hook: Why campaigns fail (0-8s)</li>
                <li>Problem 1: No Clear Strategy (9-18s)</li>
                <li>Problem 2: Not Tracking Results (19-28s)</li>
                <li>Solution: Purple Crayolá approach (29-38s)</li>
                <li>CTA (39-50s)</li>
                </ol>
                
                <p>Full video brief in content calendar document.</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 22" in selected_day:
            st.markdown("## 📱 THURSDAY, JANUARY 22, 2026")
            st.markdown("### LinkedIn & Instagram Carousel - Social Media Guide")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Carousel (8 slides) | **Mix:** Educational (30%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Carousel: "Social Media Platform Guide for Nigerian Businesses"</h4>
                <p><strong>Slides:</strong> 8 slides</p>
                
                <p><strong>Platforms covered:</strong></p>
                <ul>
                <li>LinkedIn (B2B + Professional)</li>
                <li>Instagram (Visual Brands)</li>
                <li>Twitter/X (Real-Time)</li>
                <li>Facebook (Community + Local)</li>
                <li>WhatsApp Business (Customer Communication)</li>
                </ul>
                
                <p>Full design brief in content calendar document.</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 23" in selected_day:
            st.markdown("## 📱 FRIDAY, JANUARY 23, 2026")
            st.markdown("### LinkedIn & Instagram Post - Soft Presence Introduction")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Photo Post | **Mix:** Thought Leadership (20%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Quote Graphic - Visibility Theme</h4>
                <p><strong>Main Text:</strong><br>
                "Your expertise is undeniable.<br>
                But is your visibility matching your impact?"</p>
                
                <p><strong>Supporting Text:</strong> "Excellence without visibility is invisible."</p>
                
                <p><strong>Note:</strong> This subtly introduces Presence themes before official launch</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 24" in selected_day:
            st.markdown("## 📱 SATURDAY, JANUARY 24, 2026")
            st.markdown("### Twitter/X Engagement Only")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Engagement Tweet | **Mix:** Engagement (20%)")
            
            with st.expander("🐦 TWEET CONTENT", expanded=False):
                st.code("""Weekend reflection:

What's one professional goal you're committing to in 2026?

(No judgment. No pressure. Just share what you're working toward.)""")
    
    # Week 3 Content
    elif week_num == 3:
        if "Jan 26" in selected_day:
            st.markdown("## 📱 MONDAY, JANUARY 26, 2026")
            st.markdown("### LinkedIn & Instagram Motivational Post")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Photo Post | **Mix:** Thought Leadership (20%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Inspirational Quote Graphic</h4>
                <p><strong>Main Text:</strong><br>
                "Your expertise is your foundation.<br>
                Your voice is your tool.<br>
                Your visibility is your bridge.<br>
                Your impact is your legacy."</p>
                
                <p><strong>Supporting Text:</strong> "Build all four."</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 27" in selected_day:
            st.markdown("## 📱 TUESDAY, JANUARY 27, 2026")
            st.markdown("### 🎉 PRESENCE OFFICIAL LAUNCH")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Carousel (10 slides) | **Mix:** Promotional (30%)")
            
            st.info("⭐ **MAJOR ASSET:** This is the official Presence launch carousel - high priority!")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>🎉 Presence Launch Carousel - PREMIUM DESIGN</h4>
                <p><strong>Slides:</strong> 10 slides</p>
                <p><strong>Design Priority:</strong> HIGH - This is the official launch</p>
                
                <p><strong>Design Style:</strong> Premium, sophisticated, elevated aesthetic</p>
                <p><strong>Visual Theme:</strong> Include prism imagery/metaphors</p>
                
                <p><strong>Slide Structure:</strong></p>
                <ol>
                <li>Cover: "Introducing PRESENCE by Purple Crayolá"</li>
                <li>The Problem: "You're Excellent. But Are You Visible?"</li>
                <li>The Solution: Presence personal branding system</li>
                <li>PRISM Framework™ visual</li>
                <li>PRISM Breakdown (P-R-I-S-M)</li>
                <li>Who It's For (Part 1)</li>
                <li>Who It's For (Part 2)</li>
                <li>What You Get (Presence Toolkit)</li>
                <li>Real Results (Testimonial)</li>
                <li>CTA: "Own Your Story. Command Your Space."</li>
                </ol>
                
                <p><strong>Full detailed brief in content calendar document.</strong></p>
                </div>
                """, unsafe_allow_html=True)
            
            st.divider()
            
            st.markdown("### Twitter/X Thread")
            st.markdown('<span class="platform-badge twitter-badge">Twitter/X</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 3:00 PM WAT | **Type:** Thread (10 tweets) | **Mix:** Promotional (30%)")
        
        elif "Jan 28" in selected_day:
            st.markdown("## 📱 WEDNESDAY, JANUARY 28, 2026")
            st.markdown("### LinkedIn & Instagram Video - Content Pillars")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Video (40-60 seconds) | **Mix:** Educational (30%)")
            
            with st.expander("🎥 VIDEO BRIEF FOR VIDEO EDITOR", expanded=True):
                st.markdown("""
                <div class="video-brief">
                <h4>Video: "5 Content Pillars Every Professional Brand Needs"</h4>
                <p><strong>Duration:</strong> 40-60 seconds</p>
                
                <p><strong>Pillars to cover:</strong></p>
                <ol>
                <li>Educational</li>
                <li>Inspirational</li>
                <li>Thought Leadership</li>
                <li>Social Proof</li>
                <li>Behind-the-Scenes</li>
                </ol>
                
                <p>Full video brief in content calendar document.</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 29" in selected_day:
            st.markdown("## 📱 THURSDAY, JANUARY 29, 2026")
            st.markdown("### LinkedIn & Instagram Carousel - Presence Packages")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Carousel (6 slides) | **Mix:** Promotional (30%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Presence Packages Carousel</h4>
                <p><strong>Slides:</strong> 6 slides</p>
                
                <p><strong>Packages to showcase:</strong></p>
                <ul>
                <li>🟣 Presence Core (Foundation & Clarity)</li>
                <li>🟣 Presence Pro (Align & Activate)</li>
                <li>🟣 Presence Elite (Scale with Influence)</li>
                <li>✳️ Presence Launchpad (Consistent Content)</li>
                </ul>
                
                <p><strong>Design Style:</strong> Clean comparison format, easy to scan</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 30" in selected_day:
            st.markdown("## 📱 FRIDAY, JANUARY 30, 2026")
            st.markdown("### LinkedIn & Instagram Engagement Post")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 9:00 AM WAT | **Type:** Photo Post | **Mix:** Engagement (20%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>Engagement Graphic</h4>
                <p><strong>Main Text:</strong> "What's one professional goal you're committed to in 2026?"</p>
                <p><strong>Supporting Text:</strong> "Share yours in the comments 👇"</p>
                <p><strong>Style:</strong> Approachable, conversational, inviting</p>
                </div>
                """, unsafe_allow_html=True)
        
        elif "Jan 31" in selected_day:
            st.markdown("## 📱 SATURDAY, JANUARY 31, 2026")
            st.markdown("### LinkedIn & Instagram Carousel - Month-End Reflection")
            st.markdown('<span class="platform-badge linkedin-badge">LinkedIn</span> <span class="platform-badge instagram-badge">Instagram</span>', unsafe_allow_html=True)
            st.markdown("**Time:** 10:00 AM WAT | **Type:** Carousel (6 slides) | **Mix:** Thought Leadership (20%)")
            
            with st.expander("📋 VISUAL BRIEF FOR DESIGNER", expanded=True):
                st.markdown("""
                <div class="visual-brief">
                <h4>January 2026 Reflection Carousel</h4>
                <p><strong>Slides:</strong> 6 slides</p>
                
                <p><strong>Theme:</strong> Reflective month-end wrap-up</p>
                
                <p><strong>Key Messages:</strong></p>
                <ol>
                <li>Excellence Without Visibility Is Invisible</li>
                <li>Strategy Without Execution Is Just a Dream</li>
                <li>Your Voice Is Your Competitive Advantage</li>
                <li>Presence Isn't Vanity—It's Stewardship</li>
                <li>February Preview</li>
                </ol>
                
                <p><strong>Style:</strong> Warm, professional, thoughtful</p>
                </div>
                """, unsafe_allow_html=True)

elif page == "🎨 Design Assets Tracker":
    st.title("🎨 Design Assets Tracker")
    st.markdown("### Complete list of all design and video assets needed")
    
    # Create comprehensive assets dataframe
    assets_data = {
        'Week': [
            'Week 1', 'Week 1', 'Week 1', 'Week 1',
            'Week 2', 'Week 2', 'Week 2', 'Week 2', 'Week 2', 'Week 3', 'Week 3', 'Week 3', 'Week 3', 'Week 3', 'Week 3', 'Week 3'
        ],
        'Date': [
            'Jan 12', 'Jan 13', 'Jan 14', 'Jan 15', 'Jan 16',
            'Jan 19', 'Jan 20', 'Jan 21', 'Jan 22', 'Jan 23',
            'Jan 26', 'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30', 'Jan 31'
        ],
        'Asset Type': [
            'Graphic', 'Carousel', 'Graphic', 'Video', 'Carousel',
            'Carousel', 'Graphic', 'Video', 'Carousel', 'Graphic',
            'Graphic', 'Carousel', 'Video', 'Carousel', 'Graphic', 'Carousel'
        ],
        'Asset Name': [
            'Digital Transformation Graphic',
            'Digital Marketing Mistakes Carousel (7 slides)',
            'Website Storefront Quote Graphic',
            'Digital Transformation Video (30-45s)',
            'Website Essentials Carousel (8 slides)',
            'SEO 2026 Carousel (8 slides)',
            'Visibility/Strategy/Excellence Quote',
            'Digital Marketing Fails Video (35-50s)',
            'Social Media Platform Guide (8 slides)',
            'Expertise vs Visibility Quote',
            'Expertise/Voice/Visibility/Impact Quote',
            'PRESENCE LAUNCH CAROUSEL (10 slides)',
            'Content Pillars Video (40-60s)',
            'Presence Packages Carousel (6 slides)',
            'Professional Goals Graphic',
            'Month-End Reflection Carousel (6 slides)'
        ],
        'For Designer': [
            '✅', '✅', '✅', '❌', '✅',
            '✅', '✅', '❌', '✅', '✅',
            '✅', '✅', '❌', '✅', '✅', '✅'
        ],
        'For Video Editor': [
            '❌', '❌', '❌', '✅', '❌',
            '❌', '❌', '✅', '❌', '❌',
            '❌', '❌', '✅', '❌', '❌', '❌'
        ],
        'Priority': [
            'Medium', 'High', 'Medium', 'High', 'High',
            'High', 'Medium', 'High', 'High', 'Medium',
            'Medium', '🔥 CRITICAL', 'High', 'High', 'Low', 'Medium'
        ],
        'Status': [
            'Pending', 'Pending', 'Pending', 'Pending', 'Pending',
            'Pending', 'Pending', 'Pending', 'Pending', 'Pending',
            'Pending', 'Pending', 'Pending', 'Pending', 'Pending', 'Pending'
        ]
    }
    
    assets_df = pd.DataFrame(assets_data)
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_design = assets_df[assets_df['For Designer'] == '✅'].shape[0]
        st.metric("Design Assets", total_design, help="Total graphics and carousels needed")
    
    with col2:
        total_video = assets_df[assets_df['For Video Editor'] == '✅'].shape[0]
        st.metric("Video Assets", total_video, help="Total videos needed")
    
    with col3:
        critical_assets = assets_df[assets_df['Priority'] == '🔥 CRITICAL'].shape[0]
        st.metric("Critical Priority", critical_assets, delta="Presence Launch", help="High priority assets")
    
    with col4:
        pending = assets_df[assets_df['Status'] == 'Pending'].shape[0]
        st.metric("Pending", pending, help="Assets awaiting completion")
    
    st.divider()
    
    # Filters
    st.markdown("### 🔍 Filter Assets")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        week_filter = st.multiselect(
            "Filter by Week:",
            options=assets_df['Week'].unique(),
            default=assets_df['Week'].unique()
        )
    
    with col2:
        type_filter = st.multiselect(
            "Filter by Type:",
            options=assets_df['Asset Type'].unique(),
            default=assets_df['Asset Type'].unique()
        )
    
    with col3:
        priority_filter = st.multiselect(
            "Filter by Priority:",
            options=assets_df['Priority'].unique(),
            default=assets_df['Priority'].unique()
        )
    
    # Filter dataframe
    filtered_assets = assets_df[
        (assets_df['Week'].isin(week_filter)) &
        (assets_df['Asset Type'].isin(type_filter)) &
        (assets_df['Priority'].isin(priority_filter))
    ]
    
    st.divider()
    
    # Display filtered assets
    st.markdown("### 📋 Assets List")
    st.dataframe(
        filtered_assets,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Priority": st.column_config.TextColumn(
                "Priority",
                help="Asset priority level",
                width="medium"
            ),
            "Status": st.column_config.SelectboxColumn(
                "Status",
                options=["Pending", "In Progress", "Completed"],
                width="medium"
            )
        }
    )
    
    st.divider()
    
    # Asset breakdown by week
    st.markdown("### 📊 Asset Distribution by Week")
    
    week_breakdown = assets_df.groupby('Week').agg({
        'Asset Name': 'count',
        'Asset Type': lambda x: x.value_counts().to_dict()
    }).reset_index()
    
    fig = px.bar(
        assets_df.groupby(['Week', 'Asset Type']).size().reset_index(name='Count'),
        x='Week',
        y='Count',
        color='Asset Type',
        title='Assets Needed Per Week by Type',
        color_discrete_map={
            'Graphic': '#9F7AEA',
            'Carousel': '#6B46C1',
            'Video': '#3b82f6'
        }
    )
    
    fig.update_layout(
        xaxis_title="Week",
        yaxis_title="Number of Assets",
        font=dict(family="Inter, sans-serif")
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    
    # Design vs Video breakdown
    st.markdown("### 👥 Team Workload Distribution")
    
    col1, col2 = st.columns(2)
    
    with col1:
        design_count = assets_df[assets_df['For Designer'] == '✅'].shape[0]
        video_count = assets_df[assets_df['For Video Editor'] == '✅'].shape[0]
        
        fig_pie = go.Figure(data=[go.Pie(
            labels=['Designer', 'Video Editor'],
            values=[design_count, video_count],
            marker_colors=['#6B46C1', '#3b82f6'],
            hole=.4
        )])
        
        fig_pie.update_layout(
            title="Assets Distribution by Team",
            font=dict(family="Inter, sans-serif")
        )
        
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
        <h4>Team Breakdown</h4>
        
        <p><strong>Designer Tasks:</strong></p>
        <ul>
        <li>13 Graphics/Carousels total</li>
        <li>5 simple quote graphics</li>
        <li>8 multi-slide carousels</li>
        <li>1 critical: Presence Launch (10 slides)</li>
        </ul>
        
        <p><strong>Video Editor Tasks:</strong></p>
        <ul>
        <li>3 Videos total (30-60 seconds each)</li>
        <li>Week 1: Digital Transformation (30-45s)</li>
        <li>Week 2: Marketing Fails (35-50s)</li>
        <li>Week 3: Content Pillars (40-60s)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Critical assets highlight
    st.markdown("### 🔥 High Priority Assets")
    
    high_priority = assets_df[assets_df['Priority'].isin(['High', '🔥 CRITICAL'])]
    
    for idx, row in high_priority.iterrows():
        with st.container():
            st.markdown(f"""
            <div class="post-card">
            <h4>{row['Asset Name']}</h4>
            <p><strong>Week:</strong> {row['Week']} | <strong>Date:</strong> {row['Date']} | <strong>Priority:</strong> {row['Priority']}</p>
            <p><strong>Type:</strong> {row['Asset Type']}</p>
            <p><strong>Assigned to:</strong> {"Designer" if row['For Designer'] == '✅' else "Video Editor"}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "📊 Content Analytics":
    st.title("📊 Content Analytics & Tracking")
    st.markdown("### Key Performance Indicators to Monitor")
    
    # KPI Categories
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Growth Metrics", "💬 Engagement Metrics", "🎯 Content Performance", "📅 Weekly Tracking"])
    
    with tab1:
        st.markdown("## 📈 Growth Metrics to Track")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="content-card">
            <h4>LinkedIn</h4>
            <ul>
            <li>Follower count (start vs end)</li>
            <li>Profile views</li>
            <li>Search appearances</li>
            <li>Connection requests received</li>
            <li>Page impressions</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="content-card">
            <h4>Instagram</h4>
            <ul>
            <li>Follower count (start vs end)</li>
            <li>Profile visits</li>
            <li>Website clicks</li>
            <li>Reach (accounts reached)</li>
            <li>Impressions</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="content-card">
            <h4>Twitter/X</h4>
            <ul>
            <li>Follower count (start vs end)</li>
            <li>Profile visits</li>
            <li>Tweet impressions</li>
            <li>Mentions</li>
            <li>Top tweets</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("### 🎯 Target Growth Rates")
        
        target_data = pd.DataFrame({
            'Metric': ['Follower Growth', 'Engagement Rate', 'Profile Visits', 'Website Clicks'],
            'Target': ['1-3%', '2-4%', '10-15%', '5-10%'],
            'Notes': [
                'Conservative for Month 1',
                'Baseline establishment',
                'Increased visibility',
                'Driven by CTA optimization'
            ]
        })
        
        st.dataframe(target_data, use_container_width=True, hide_index=True)
    
    with tab2:
        st.markdown("## 💬 Engagement Metrics to Track")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="content-card">
            <h4>Per Post Metrics</h4>
            <ul>
            <li><strong>Likes:</strong> Track per post and calculate average</li>
            <li><strong>Comments:</strong> Track quantity and quality</li>
            <li><strong>Shares/Retweets:</strong> Indicator of value</li>
            <li><strong>Saves:</strong> (Instagram) High-intent action</li>
            <li><strong>Click-through rate:</strong> Link clicks / impressions</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="content-card">
            <h4>Engagement Rate Formula</h4>
            <p><strong>Engagement Rate =</strong></p>
            <p>(Likes + Comments + Shares + Saves) / Reach × 100</p>
            <hr>
            <p><strong>Benchmarks:</strong></p>
            <ul>
            <li>LinkedIn: 2-5% is good</li>
            <li>Instagram: 1-3% is good</li>
            <li>Twitter/X: 0.5-1% is good</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("### 📊 Sample Engagement Tracking Table")
        
        sample_engagement = pd.DataFrame({
            'Date': ['Jan 12', 'Jan 13', 'Jan 14', 'Jan 15'],
            'Platform': ['LinkedIn', 'LinkedIn', 'LinkedIn', 'LinkedIn'],
            'Post Type': ['Graphic', 'Carousel', 'Quote', 'Video'],
            'Reach': [850, 1200, 650, 1500],
            'Likes': [42, 68, 31, 89],
            'Comments': [5, 12, 3, 18],
            'Shares': [8, 15, 4, 22],
            'Engagement Rate': ['6.5%', '7.9%', '5.8%', '8.6%']
        })
        
        st.dataframe(sample_engagement, use_container_width=True, hide_index=True)
        
        st.info("💡 **Note:** Track all posts in a similar format to identify top performers")
    
    with tab3:
        st.markdown("## 🎯 Content Performance Analysis")
        
        st.markdown("""
        <div class="highlight">
        <h4>What to Track Per Post</h4>
        <p>For each post, record the following in a spreadsheet:</p>
        <ul>
        <li>Date published</li>
        <li>Platform</li>
        <li>Post type (graphic, carousel, video, text)</li>
        <li>Content theme (Educational, Promotional, Thought Leadership, Engagement)</li>
        <li>Reach/Impressions</li>
        <li>Engagement (likes, comments, shares, saves)</li>
        <li>Engagement rate</li>
        <li>Website clicks (if applicable)</li>
        <li>Key learnings/observations</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("### 📊 Content Type Performance Comparison")
        
        # Sample performance data
        content_performance = pd.DataFrame({
            'Content Type': ['Graphics', 'Carousels', 'Videos', 'Text Posts'],
            'Avg Engagement Rate': [4.2, 6.8, 7.5, 3.1],
            'Avg Reach': [800, 1200, 1400, 600],
            'Best For': [
                'Quick quotes, announcements',
                'Educational content, guides',
                'Product demos, storytelling',
                'Thought leadership, discussions'
            ]
        })
        
        st.dataframe(content_performance, use_container_width=True, hide_index=True)
        
        st.markdown("**Note:** These are example benchmarks. Your actual performance will vary.")
        
        st.divider()
        
        st.markdown("### 🏆 Top Performing Content Indicators")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="content-card">
            <h4>✅ Signs of Success</h4>
            <ul>
            <li>Engagement rate above platform average</li>
            <li>High comment quality (thoughtful responses)</li>
            <li>Multiple shares/saves</li>
            <li>Increased profile visits after posting</li>
            <li>Direct inquiries in DMs</li>
            <li>Website traffic spikes</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="content-card">
            <h4>⚠️ Areas to Improve</h4>
            <ul>
            <li>Low reach compared to follower count</li>
            <li>High views but low engagement</li>
            <li>No comments or shares</li>
            <li>Declining engagement trend</li>
            <li>Audience mismatch (wrong platform/time)</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("## 📅 Weekly Tracking Template")
        
        st.markdown("""
        <div class="highlight">
        <h4>Weekly Reporting Checklist</h4>
        <p>At the end of each week, compile:</p>
        <ol>
        <li><strong>Posts Published:</strong> Total count per platform</li>
        <li><strong>Top 3 Performing Posts:</strong> With metrics and insights</li>
        <li><strong>Worst Performing Post:</strong> Analysis of why</li>
        <li><strong>Total Reach:</strong> Across all platforms</li>
        <li><strong>Total Engagement:</strong> Combined likes, comments, shares</li>
        <li><strong>Follower Growth:</strong> Net change from previous week</li>
        <li><strong>Key Learnings:</strong> What worked, what didn't</li>
        <li><strong>Action Items:</strong> Adjustments for next week</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.divider()
        
        st.markdown("### 📋 Sample Weekly Report Format")
        
        weekly_report = pd.DataFrame({
            'Week': ['Week 1', 'Week 2', 'Week 3'],
            'Posts Published': [11, 11, 12],
            'Total Reach': ['12,500', '15,200', '18,900'],
            'Total Engagement': [450, 580, 720],
            'Follower Growth': ['+25', '+38', '+52'],
            'Avg Engagement Rate': ['4.5%', '5.2%', '5.8%'],
            'Top Performing Type': ['Carousel', 'Video', 'Carousel']
        })
        
        st.dataframe(weekly_report, use_container_width=True, hide_index=True)
        
        st.divider()
        
        st.markdown("### 💡 Monthly Summary Points")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="content-card">
            <h4>What Worked Well</h4>
            <ul>
            <li>Educational carousels (highest engagement)</li>
            <li>Presence launch generated strong interest</li>
            <li>Twitter threads drove meaningful conversations</li>
            <li>Consistent posting built momentum</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="content-card">
            <h4>Areas for Improvement</h4>
            <ul>
            <li>Increase video content (highest engagement)</li>
            <li>Optimize posting times based on data</li>
            <li>More engagement with comments</li>
            <li>A/B test different CTA formats</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

elif page == "📥 Export & Resources":
    st.title("📥 Export & Resources")
    st.markdown("### Download and Share Options")
    
    st.markdown("""
    <div class="highlight">
    <h4>📋 Available Resources</h4>
    <p>This dashboard provides a comprehensive view of the January 2026 content strategy. For the complete detailed content calendar with full captions, design briefs, and video scripts, please refer to the main content calendar document.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Quick Reference Guide
    st.markdown("## 📖 Quick Reference Guide")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="content-card">
        <h4>Content Mix</h4>
        <ul>
        <li>30% Promotional</li>
        <li>30% Educational</li>
        <li>20% Thought Leadership</li>
        <li>20% Engagement</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
        <h4>Posting Schedule</h4>
        <ul>
        <li>LinkedIn: 3-4x/week</li>
        <li>Instagram: 3-4x/week (same as LinkedIn)</li>
        <li>Twitter/X: 5-7x/week</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Asset Summary
    st.markdown("## 🎨 Asset Production Summary")
    
    asset_summary = pd.DataFrame({
        'Asset Type': ['Graphics (Quote/Single)', 'Carousels', 'Videos', 'Twitter Threads'],
        'Quantity': [5, 8, 3, 15+],
        'Responsibility': ['Designer', 'Designer', 'Video Editor', 'Content Manager'],
        'Average Time': ['2-3 hours', '4-6 hours', '8-12 hours', '1-2 hours']
    })
    
    st.dataframe(asset_summary, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # Key Contacts
    st.markdown("## 👥 Team Contacts")
    
    st.markdown("""
    <div class="content-card">
    <h4>Content Strategy Team</h4>
    <ul>
    <li><strong>Content Manager:</strong> Oluwatosin Adejumo</li>
    <li><strong>Approval:</strong> COO</li>
    <li><strong>Design Team:</strong> Graphic Designer</li>
    <li><strong>Video Team:</strong> Video Editor</li>
    </ul>
    
    <h4>Important Links</h4>
    <ul>
    <li><strong>Website:</strong> purplecrayola.com</li>
    <li><strong>Presence Landing Page:</strong> purplecrayola.com/presence</li>
    <li><strong>Email:</strong> presence@purplecrayola.com</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Approval Workflow
    st.markdown("## ✅ Content Approval Workflow")
    
    st.markdown("""
    <div class="highlight">
    <h4>Recommended Approval Process</h4>
    <ol>
    <li><strong>Week Start (Monday):</strong> Content Manager shares weekly content briefs</li>
    <li><strong>Tuesday-Wednesday:</strong> Design/Video teams create assets</li>
    <li><strong>Thursday:</strong> COO reviews and approves all assets for the week</li>
    <li><strong>Friday:</strong> Final revisions and scheduling</li>
    <li><strong>Following Week:</strong> Content goes live as scheduled</li>
    </ol>
    
    <p><strong>Emergency/Last-Minute Posts:</strong> Follow same approval chain but expedited (24-hour turnaround)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Next Steps
    st.markdown("## 🚀 Next Steps")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="content-card">
        <h4>Immediate Actions</h4>
        <ol>
        <li>Review and approve content calendar</li>
        <li>Assign assets to design/video teams</li>
        <li>Set up analytics tracking spreadsheet</li>
        <li>Schedule COO review sessions</li>
        <li>Establish emergency approval process</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-card">
        <h4>Week 1 Priorities</h4>
        <ol>
        <li>Complete all Week 1 design assets by Jan 9</li>
        <li>Complete Week 1 video by Jan 10</li>
        <li>COO approval by Jan 11</li>
        <li>Schedule posts for Week 1</li>
        <li>Begin Week 2 asset production</li>
        </ol>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Critical Dates
    st.markdown("## 📅 Critical Dates")
    
    critical_dates = pd.DataFrame({
        'Date': ['Jan 12', 'Jan 19', 'Jan 27', 'Jan 31'],
        'Event': [
            'Content Calendar Launch',
            'Week 2 Start - Authority Building',
            'PRESENCE OFFICIAL LAUNCH',
            'January Wrap-up & February Planning'
        ],
        'Priority': ['High', 'Medium', '🔥 CRITICAL', 'Medium'],
        'Notes': [
            'First week of content goes live',
            'Educational focus continues',
            'Major product launch - all assets must be ready',
            'Month-end reflection + February preview'
        ]
    })
    
    st.dataframe(critical_dates, use_container_width=True, hide_index=True)
    
    st.divider()
    
    st.success("✅ **Dashboard Complete!** Use the sidebar navigation to explore all sections of the January 2026 content calendar.")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; padding: 30px 20px; background: white; border-radius: 12px; margin-top: 40px;">
    <h4 style="color: #6B46C1; margin-bottom: 10px;">🎨 Purple Crayolá Content Strategy Dashboard</h4>
    <p style="color: #64748b; margin: 5px 0;">January 2026 - Strategic Digital Transformation</p>
    <p style="font-size: 12px; color: #94a3b8; margin-top: 15px;">Prepared by Oluwatosin Adejumo • Version 1.0 • Last Updated: January 8, 2026</p>
</div>
""", unsafe_allow_html=True)