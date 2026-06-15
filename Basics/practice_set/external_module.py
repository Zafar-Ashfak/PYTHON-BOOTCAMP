import pyttsx3

import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

myIntro = """
Hello, I'm Md Ashfak Alam.

I am a Software Engineer with a strong foundation in building scalable, high-performance applications. I specialize in Java backend development using Core Java, Spring, Spring Boot, RESTful APIs, JDBC, Hibernate/JPA, and MySQL.
I am also bring solid frontend experience with React.js, Redux Toolkit, Context API, HTML5, and CSS3.With strong proficiency in Data Structures & Algorithms, Java, C, and C++, I focus on writing clean, efficient, and maintainable code. I am actively seeking opportunities as a Java Backend Developer or Full Stack Developer where I can contribute to impactful projects and continue growing as an engineer.
"""

engine.say(myIntro)
engine.runAndWait()