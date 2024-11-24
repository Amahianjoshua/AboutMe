class AboutMe:
    def __init__(self, personal_info, skills, introduction):
        self.personal_info = personal_info
        self.skills = skills
        self.introduction = introduction

    def display_profile(self):
        print("About Me: ")
        print(self.introduction)
        print("\n")

        print("Here's a little about me: ")
        for info in self.personal_info:
            print(f" {info}")
        print("\n")

        print("Here are ths skills I've developed: ")
        for skill in self.skills:
            print(f" -{skill}")
        print("\n")

# Introduction
introduction ="""👋 Hi! I’m a Statistician and passionate Data Analyst skilled in transforming 
data into actionable insights. I specialize in using tools like Python, Pandas, Matplotlib, and 
Seaborn for data manipulation, visualization, and analysis. Currently diving deeper into exploratory 
data analysis (EDA) and machine learning to enhance my analytical and predictive capabilities. 
Open to collaborating on data science projects and always eager to learn new techniques!"""

# Personal info
personal_info=[
    "Name: Amahian Osewe Joshua",
    "Education : B.Sc Statistics (2018- 2023)",
    "Email: joshuaosewe6@gmail.com",
    "GitHub: https://github.com/Amahianjoshua",
    "Whatsapp: +2348143572576",
    "LinkedIn: https://www.linkedin.com/in/amahianjoshua"

]

# skills
skills=[
    "Python Programming",
    "Numpy",
    "Exploratory Data Analysis (EDA)",
    "Data Visualization"
]

# Create an AboutMe instance and display the profile
about_me=AboutMe(personal_info, skills, introduction)
about_me.display_profile()
