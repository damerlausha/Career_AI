import streamlit as st
import json

st.set_page_config(page_title="CareerAI", page_icon="🎓", layout="wide")

# Load data
with open("careers.json", encoding="utf-8") as f:
    careers = json.load(f)

# CSS
st.markdown("""
<style>
.stApp{background:linear-gradient(135deg,#eef2ff,#fff,#f5f3ff)}
[data-testid="stSidebar"]{background:linear-gradient(#172554,#4c1d95)}
.hero{background:linear-gradient(135deg,#2563eb,#7c3aed);color:white;
padding:25px;border-radius:20px;text-align:center;margin-bottom:20px}
.hero h1, .hero p, .hero h2, .hero h3, .hero h4, .hero h5, .hero h6, .hero *{color:white!important}
.card{background:white;padding:20px;border-radius:15px;
margin:12px 0;box-shadow:0 4px 15px #0001}
.metric{text-align:center;background:white;padding:20px;border-radius:15px;
box-shadow:0 4px 15px #0001}.num{font-size:30px;font-weight:bold;color:#2563eb}
.skill{display:inline-block;background:#eff6ff;color:#2563eb;padding:6px 10px;
margin:3px;border-radius:15px}.missing{display:inline-block;background:#fef2f2;
color:#dc2626;padding:6px 10px;margin:3px;border-radius:15px}
.step{background:#f5f3ff;padding:10px;margin:5px;border-radius:8px;color:#4c1d95}.stApp, .stApp p, .stApp li, .stApp label, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6,
.stApp .stMarkdown, .stApp .stTextInput, .stApp .stSelectbox, .stApp .stMultiselect,
.stApp .stSlider, .stApp .stRadio, .card, .metric, .step { color:#111!important; }
[data-testid="stSidebar"], [data-testid="stSidebar"] * { color:white!important; }
[data-testid="stSidebar"] p, [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label, [data-testid="stSidebar"] div, [data-testid="stSidebar"] span,
[data-testid="stSidebar"] .stRadio, [data-testid="stSidebar"] .stMarkdown { color:white!important; }</style>
""", unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    st.markdown(
        "<h1 style='text-align:center'>🎓 CareerAI</h1>"
        "<p style='text-align:center'>Smart Student Career Assistant</p>"
        "<p style='text-align:center'>🟢 Online</p>",
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        ["🏠 Home", "🎯 Analyzer", "📊 Explorer", "ℹ️ About"]
    )


# Header function
def header(title, text):
    st.markdown(
        f"<div class='hero'><h1>{title}</h1><p>{text}</p></div>",
        unsafe_allow_html=True
    )


def get_learning_roadmap(interest, missing_skills):
    roadmap_by_interest = {
        "Artificial Intelligence (AI)": [
            "Learn Python fundamentals", "Study linear algebra and probability",
            "Understand machine learning basics", "Practice model building with datasets",
            "Build an AI project", "Deploy and document your solution"
        ],
        "Machine Learning": [
            "Master Python and data handling", "Learn statistics and exploratory data analysis",
            "Study supervised and unsupervised learning", "Train models on real data",
            "Evaluate and optimize models", "Deploy a machine learning app"
        ],
        "Web Development": [
            "Learn HTML and CSS", "Practice responsive layouts",
            "Study JavaScript fundamentals", "Build frontend projects",
            "Learn backend basics and APIs", "Deploy a complete web app"
        ],
        "App Development": [
            "Choose Android or iOS path", "Learn app UI design principles",
            "Study app logic and state management", "Connect APIs and databases",
            "Build and test your app", "Publish to stores"
        ],
        "Data Science": [
            "Learn Python and SQL", "Study statistics and data cleaning",
            "Explore visualization and reporting", "Practice exploratory analysis",
            "Build predictive models", "Present insights with real projects"
        ],
        "Cybersecurity": [
            "Understand networking and operating systems", "Learn security fundamentals",
            "Study ethical hacking basics", "Practice vulnerability analysis",
            "Learn incident response", "Build a security-focused project"
        ],
        "Cloud Computing": [
            "Learn Linux and networking", "Understand cloud fundamentals",
            "Study compute, storage, and networking services", "Practice IAM and security",
            "Deploy an application in the cloud", "Automate with DevOps workflows"
        ],
        "Game Development": [
            "Learn programming basics", "Study game design and mechanics",
            "Build a simple 2D game", "Work with graphics and physics",
            "Add sound and UI", "Ship a complete playable game"
        ],
        "UI/UX Design": [
            "Study design principles and color theory", "Learn wireframing and prototyping",
            "Practice user flows and accessibility", "Design mobile and web interfaces",
            "Create a portfolio case study", "Iterate based on user feedback"
        ],
        "Robotics": [
            "Learn programming and electronics basics", "Study sensors and actuators",
            "Understand control systems and automation", "Build a simple robot prototype",
            "Integrate AI or vision", "Test and improve system performance"
        ],
        "Internet of Things (IoT)": [
            "Learn embedded programming", "Study sensors and microcontrollers",
            "Understand networking and communication protocols", "Build an IoT prototype",
            "Work on cloud connectivity", "Deploy and monitor a live device"
        ],
        "Data Analytics": [
            "Learn spreadsheet and SQL basics", "Practice data cleaning and transformation",
            "Study dashboards and reports", "Use Python for analysis",
            "Create business insights", "Share findings with stakeholders"
        ],
        "Software Development": [
            "Learn core programming concepts", "Practice OOP and data structures",
            "Build small applications", "Study testing and debugging",
            "Work on a real project", "Prepare for interviews"
        ],
        "Competitive Programming": [
            "Learn data structures", "Practice arrays, strings, and maps",
            "Solve greedy and graph problems", "Work on dynamic programming",
            "Increase speed and optimization", "Participate in coding contests"
        ],
        "Full-Stack Development": [
            "Learn frontend basics", "Study backend APIs and databases",
            "Understand authentication and security", "Build a full stack project",
            "Practice deployment and CI/CD", "Ship a production-ready app"
        ],
        "Blockchain": [
            "Learn distributed systems basics", "Study cryptography and consensus",
            "Explore smart contracts", "Build a blockchain mini project",
            "Study security and scalability", "Test and document your solution"
        ],
        "Computer Vision": [
            "Learn Python and image processing", "Study OpenCV basics",
            "Understand feature extraction", "Train object detection models",
            "Work with real datasets", "Build a vision project"
        ],
        "Natural Language Processing (NLP)": [
            "Learn Python text processing", "Study tokenization and embeddings",
            "Understand text classification", "Experiment with transformers",
            "Build an NLP application", "Evaluate and improve performance"
        ],
        "Database Management": [
            "Learn SQL fundamentals", "Study schema design and indexing",
            "Practice joins and queries", "Understand transactions and optimization",
            "Work with database normalization", "Build a data-driven application"
        ],
        "Automation and Scripting": [
            "Learn Python or shell scripting basics", "Practice file and system automation",
            "Work with APIs and scheduled tasks", "Build reusable scripts",
            "Automate repetitive workflows", "Deploy and monitor automation"
        ],
    }

    roadmap = roadmap_by_interest.get(interest, [
        "Learn the fundamentals of the selected domain",
        "Practice core concepts with mini projects",
        "Build a portfolio project",
        "Review and improve your skills",
        "Document your work and present it clearly"
    ])

    if missing_skills:
        roadmap = roadmap[:4] + [
            f"Practice {skill} in a mini project" for skill in missing_skills[:3]
        ] + roadmap[4:]

    return roadmap


def get_learning_resources(interest, step):
    learning_map = {
        "Artificial Intelligence (AI)": {
            "resources": [
                "Coursera: AI For Everyone by Andrew Ng",
                "fast.ai learning resources",
                "Google AI Education"
            ],
            "books": [
                "Artificial Intelligence: A Modern Approach",
                "Hands-On Machine Learning"
            ]
        },
        "Machine Learning": {
            "resources": [
                "Machine Learning Crash Course by Google",
                "Coursera: Machine Learning by Andrew Ng",
                "Scikit-learn Documentation"
            ],
            "books": [
                "Hands-On Machine Learning",
                "The Hundred-Page Machine Learning Book"
            ]
        },
        "Web Development": {
            "resources": [
                "MDN Web Docs",
                "freeCodeCamp",
                "The Odin Project"
            ],
            "books": [
                "HTML and CSS: Design and Build Websites",
                "JavaScript: The Good Parts"
            ]
        },
        "App Development": {
            "resources": [
                "Android Developer Docs",
                "Apple Developer Documentation",
                "Flutter Docs"
            ],
            "books": [
                "Flutter in Action",
                "Clean Architecture"
            ]
        },
        "Data Science": {
            "resources": [
                "Kaggle Learn",
                "DataCamp",
                "Python for Data Analysis tutorials"
            ],
            "books": [
                "Python for Data Analysis",
                "Practical Statistics for Data Scientists"
            ]
        },
        "Cybersecurity": {
            "resources": [
                "Cybrary",
                "TryHackMe",
                "OWASP Learning Resources"
            ],
            "books": [
                "The Web Application Hacker's Handbook",
                "Cybersecurity Essentials"
            ]
        },
        "Cloud Computing": {
            "resources": [
                "AWS Skill Builder",
                "Google Cloud Skills Boost",
                "Microsoft Learn"
            ],
            "books": [
                "Cloud Computing for Dummies",
                "Architecting the Cloud"
            ]
        },
        "Game Development": {
            "resources": [
                "Unity Learn",
                "Unreal Engine Documentation",
                "GameDev.tv"
            ],
            "books": [
                "Game Programming Patterns",
                "Learning C# by Developing Games with Unity"
            ]
        },
        "UI/UX Design": {
            "resources": [
                "Figma Learn",
                "Interaction Design Foundation",
                "Google UX Design Certificate"
            ],
            "books": [
                "Don't Make Me Think",
                "The Design of Everyday Things"
            ]
        },
        "Robotics": {
            "resources": [
                "ROS Wiki",
                "Robotics Academy",
                "MIT OpenCourseWare Robotics"
            ],
            "books": [
                "Probabilistic Robotics",
                "Introduction to Robotics"
            ]
        },
        "Internet of Things (IoT)": {
            "resources": [
                "Arduino Official Tutorials",
                "ESP32 Docs",
                "IoT Academy"
            ],
            "books": [
                "Getting Started with Arduino",
                "Internet of Things: A Hands-On Approach"
            ]
        },
        "Data Analytics": {
            "resources": [
                "SQLBolt",
                "Mode Analytics SQL Tutorial",
                "Khan Academy Data Analysis"
            ],
            "books": [
                "Storytelling with Data",
                "SQL Practice Problems"
            ]
        },
        "Software Development": {
            "resources": [
                "freeCodeCamp",
                "The Odin Project",
                "CS50 by Harvard"
            ],
            "books": [
                "Clean Code",
                "Head First Java"
            ]
        },
        "Competitive Programming": {
            "resources": [
                "Codeforces",
                "AtCoder",
                "HackerRank"
            ],
            "books": [
                "Competitive Programming 3",
                "Cracking the Coding Interview"
            ]
        },
        "Full-Stack Development": {
            "resources": [
                "The Odin Project",
                "freeCodeCamp",
                "Traversy Media"
            ],
            "books": [
                "Full-Stack React Projects",
                "Node.js Design Patterns"
            ]
        },
        "Blockchain": {
            "resources": [
                "Ethereum Docs",
                "Blockchain Council",
                "CryptoZombies"
            ],
            "books": [
                "Mastering Bitcoin",
                "Blockchain Basics"
            ]
        },
        "Computer Vision": {
            "resources": [
                "OpenCV Tutorials",
                "PyImageSearch",
                "LearnOpenCV"
            ],
            "books": [
                "Learning OpenCV",
                "Computer Vision: Algorithms and Applications"
            ]
        },
        "Natural Language Processing (NLP)": {
            "resources": [
                "Hugging Face Course",
                "spaCy Documentation",
                "NLTK Book"
            ],
            "books": [
                "Natural Language Processing with Python",
                "Speech and Language Processing"
            ]
        },
        "Database Management": {
            "resources": [
                "SQLBolt",
                "Mode SQL Tutorial",
                "PostgreSQL Documentation"
            ],
            "books": [
                "SQL Queries for Mere Mortals",
                "Database System Concepts"
            ]
        },
        "Automation and Scripting": {
            "resources": [
                "Automate the Boring Stuff with Python",
                "PowerShell Docs",
                "Bash Scripting Tutorials"
            ],
            "books": [
                "Automate the Boring Stuff with Python",
                "The Linux Command Line"
            ]
        },
    }

    return learning_map.get(interest, {
        "resources": [
            "Official documentation for the topic",
            "Free online courses and tutorials",
            "YouTube beginner tutorials"
        ],
        "books": [
            "A beginner-friendly book in this domain",
            "A project-based practical guide"
        ]
    })


# HOME
if page == "🏠 Home":

    header("🎓 CareerAI", "Smart Student Career Assistant")

    st.markdown("""
    <div class="card">
    <h2>👋 Welcome to CareerAI</h2>
    <p>Find suitable technology careers using your skills and interests.</p>
    <h3>How it works</h3>
    <p>👨‍🎓 Profile → 💻 Skills → ❤️ Interest → 🎯 Matching →
    📚 Skill Gap → 🛣️ Roadmap</p>
    </div>
    """, unsafe_allow_html=True)

    a,b,c = st.columns(3)

    for col,num,text in [
        (a,"12+","Career Paths"),
        (b,"50+","Skills"),
        (c,"100%","Interactive")
    ]:
        col.markdown(
            f"<div class='metric'><div class='num'>{num}</div>{text}</div>",
            unsafe_allow_html=True
        )


# ANALYZER
elif page == "🎯 Analyzer":

    header("🎯 Career Analyzer","Find the career matching your profile")

    c1,c2 = st.columns(2)

    with c1:
        name = st.text_input("👤 Name")
        degree = st.selectbox(
            "🎓 Degree",
            ["B.Tech","B.Sc","BCA","MCA","M.Tech","MBA","Other"]
        )
        percentage = st.slider("📊 Percentage",0,100,75)

    programming_languages = [
        "C Programming", "C++", "Java", "Python", "JavaScript", "TypeScript",
        "C#", "PHP", "Ruby", "Go (Golang)", "Rust", "Kotlin", "Swift",
        "R Programming", "SQL", "HTML", "CSS", "Dart", "MATLAB", "Scala",
        "Perl", "Shell Scripting", "Objective-C", "Visual Basic",
        "Julia", "Haskell", "Lua", "Elixir", "Solidity"
    ]

    skills_all = sorted(programming_languages)

    interests_all = [
        "Artificial Intelligence (AI)", "Machine Learning", "Web Development",
        "App Development", "Data Science", "Cybersecurity", "Cloud Computing",
        "Game Development", "UI/UX Design", "Robotics",
        "Internet of Things (IoT)", "Data Analytics", "Software Development",
        "Competitive Programming", "Full-Stack Development", "Blockchain",
        "Computer Vision", "Natural Language Processing (NLP)",
        "Database Management", "Automation and Scripting"
    ]

    normalized_careers = []
    for c in careers:
        skill_names = [s.strip() for s in str(c.get("skills", "")).split(",") if s.strip()]
        normalized_careers.append({
            **c,
            "skills": [s for s in skill_names if s in skills_all]
        })

    with c2:
        skills = st.multiselect("💻 Your Skills", skills_all)
        interest = st.selectbox("❤️ Interest", interests_all)

    if st.button("🚀 ANALYZE CAREER", type="primary",
                 use_container_width=True):

        if not name or not skills:
            st.warning("Enter your name and select your skills.")

        else:
            results = []

            for c in normalized_careers:
                matches = len(set(skills) & set(c["skills"]))
                score = matches / len(c["skills"]) * 75 if c["skills"] else 0
                score += 25 if interest in c["interests"] else 0

                results.append((
                    min(round(score),100),
                    c,
                    matches,
                    [s for s in c["skills"] if s not in skills]
                ))

            score,c,matches,missing = max(
                results,key=lambda x:x[0]
            )

            st.markdown(f"""
            <div class="hero">
            <h1>{c["icon"]} {c["career"]}</h1>
            <h1>{score}%</h1>
            <p>Career Match for {name}</p>
            </div>
            """, unsafe_allow_html=True)

            a,b,d = st.columns(3)

            a.metric("🎯 Match",f"{score}%")
            b.metric("💻 Matching Skills",matches)
            d.metric("📚 Skills to Learn",len(missing))

            st.markdown(
                "<div class='card'><h2>💻 Your Skills</h2>",
                unsafe_allow_html=True
            )

            st.markdown(
                "".join(
                    f"<span class='skill'>✅ {s}</span>"
                    for s in skills
                ),
                unsafe_allow_html=True
            )

            st.markdown("</div>",unsafe_allow_html=True)

            st.markdown(
                "<div class='card'><h2>📚 Skills to Learn</h2>",
                unsafe_allow_html=True
            )

            st.markdown(
                "".join(
                    f"<span class='missing'>❌ {s}</span>"
                    for s in missing
                ) or "🎉 No missing skills!",
                unsafe_allow_html=True
            )

            st.markdown("</div>",unsafe_allow_html=True)

            roadmap_steps = get_learning_roadmap(interest, missing)

            st.markdown(
                "<div class='card'><h2>🛣️ Learning Roadmap</h2>",
                unsafe_allow_html=True
            )

            for i, step in enumerate(roadmap_steps, 1):
                with st.expander(f"{i}️⃣ {step}"):
                    resources = get_learning_resources(interest, step)
                    st.markdown("**📚 Where to Learn This**")
                    for resource in resources["resources"]:
                        st.markdown(f"- {resource}")

                    st.markdown("**📖 Most Helpful Books**")
                    for book in resources["books"]:
                        st.markdown(f"- {book}")

            st.markdown("</div>",unsafe_allow_html=True)


# EXPLORER
elif page == "📊 Explorer":

    header("📊 Career Explorer","Explore available technology careers")

    for c in careers:
        with st.expander(f'{c["icon"]} {c["career"]}'):
            st.markdown(f"### {c['icon']} {c['career']}")

            st.markdown(
                """
                <div style='display:flex; gap:20px; flex-wrap:wrap;'>
                    <div style='flex:1; min-width:220px; background:#f8fafc; padding:12px; border-radius:12px;'>
                        <div style='display:flex; align-items:center; gap:8px; margin-bottom:8px; color:#111; font-weight:700;'>
                            <span>💻</span><span>Skills</span>
                        </div>
                        <ul style='margin:0; padding-left:18px; color:#111;'>
                            """ + "".join(f"<li>{skill}</li>" for skill in c["skills"]) + """
                        </ul>
                    </div>
                    <div style='flex:1; min-width:220px; background:#f8fafc; padding:12px; border-radius:12px;'>
                        <div style='display:flex; align-items:center; gap:8px; margin-bottom:8px; color:#111; font-weight:700;'>
                            <span>❤️</span><span>Interests</span>
                        </div>
                        <ul style='margin:0; padding-left:18px; color:#111;'>
                            """ + "".join(f"<li>{interest}</li>" for interest in c["interests"]) + """
                        </ul>
                    </div>
                    <div style='flex:1; min-width:220px; background:#f8fafc; padding:12px; border-radius:12px;'>
                        <div style='display:flex; align-items:center; gap:8px; margin-bottom:8px; color:#111; font-weight:700;'>
                            <span>🛣️</span><span>Roadmap</span>
                        </div>
                        <ul style='margin:0; padding-left:18px; color:#111;'>
                            """ + "".join(f"<li>{item}</li>" for item in c["roadmap"]) + """
                        </ul>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ABOUT
else:

    header("ℹ️ About CareerAI","Smart Student Career Assistant")

    st.markdown("""
    <div class="card">
    <h2>🎓 CareerAI</h2>
    <p>Career recommendation system for students.</p>
    <h3>🛠 Technologies</h3>
    <p>Python • Streamlit • JSON</p>
    <h3>🧠 Architecture</h3>
    <p>Profile → Skills → Matching → Career → Skill Gap → Roadmap</p>
    </div>
    """, unsafe_allow_html=True)