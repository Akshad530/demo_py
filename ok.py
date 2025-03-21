import time
import streamlit as st
st.balloons()

st.title("Python")
st.subheader("Before learning Python , Please enter the following info below:")
name = st.text_input("Enter your name :")
mobile = st.text_input("Enter your mobile number:")
adress = st.text_area("Enter your Address:")
classd = st.selectbox("Choose your STD",(1,2,3,4,5,6,7,8,9,10))

button= st.button("Done!")
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
if button:
    st.markdown(f"""
Name = {name}


Mobile Number = {mobile}


Adresss = {adress}


Class = {classd}

""")
st.warning("Please fill all the information before learning")
st.subheader("Let's Learn Python !")
st.header("What is Python ?")
st.write("""
Python is a programming language that is used for a variety of tasks, including web development, data science, and software development. It is a general-purpose language that is easy to learn and use. 

         
         """)
VIDEO_URL = "https://www.youtube.com/watch?v=xkZMUX_oQX4&list=PLP9IO4UYNF0UgPfkTBECSKIJGdc_9FYZ9.mp4"
st.video(VIDEO_URL,"subtitles.vtt")

st.header("Features of Python :-")
st.write("""
Easy to learn : Python is a beginner-friendly language with easy-to-read syntax. 

Versatile : Python can be used for a variety of tasks, including scientific computing, web development, and automation. 

Open-source : Python is an open-source community language, so many independent programmers are constantly building libraries and functionality for it. 


""")
st.header("Uses of Python:-")
st.write("""


         
Web development : Python is used to create websites and web applications. 

Data science : Python is used for data analysis, data visualization, and machine learning. 

Software development  : Python is used to develop software, including software testing, bug tracking, and build control. 

Automation : Python is used to automate tasks, such as organizing finances. 



""")
st.subheader("Now! we will take a few examples of Python:")
st.code("""
        
        print("Hello World")
        
        """)
st.write("In the above example the statement PRINT is used to display , if we write firstly PRINT and then add brackets , add double quotes and write Hello World in it , it will display Hello World in terminal box ")
st.subheader("Python Indentation")
st.write("""
Indentation refers to the spaces at the beginning of a code line.

Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.

Python uses indentation to indicate a block of code.

""")
st.code("""

if 5 > 2:
  print("Five is greater than two!")
""")
st.write("Python will give you an error if you skip the indentation:")
st.subheader("Python Syntax")
st.write("""



Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.
         """)
st.code("""
#This is a comment
print("Hello, World!")


""")
st.subheader("Variable")
st.write("""
Variables are containers for storing data values.

""")
st.subheader("Creating a Variable")
st.write("""
         
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it. 
         
         """)
st.code("""

a = 4
A = "Sally"
#A will not overwrite a
""")
st.subheader("Python Data Types")
st.write("""

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type :	str
         
Numeric Types :	int, float, complex
         
Sequence Types :	list, tuple, range
         
Mapping Type :	dict
         
Set Types :	set, frozenset
         
Boolean Type :	bool
         
Binary Types :	bytes, bytearray, memoryview
         
None Type :	NoneType
         



""")
st.code("""




x = 5
print(type(x))
        """)
st.subheader("Python Numbers")
st.write("""There are three numeric types in Python:

int
float
complex
Variables of numeric types are created when you assign a value to them
         """)
st.subheader("Example :")
st.code("""




x = 1    # int
        
y = 2.8  # float
        
z = 1j   # complex
        
        """)
st.subheader("Int")
st.write("""



Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
         """)
st.subheader("Example :")
st.write("""

x = 1
         
y = 35656222554887711
         
z = -3255522
         

print(type(x))
         
print(type(y))
         
print(type(z))
         
         """)
st.subheader("Float")
st.write("""

Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
         """)
st.subheader("Examples :")
st.code("""


x = 1.10
        
y = 1.0
        
z = -35.59
        

print(type(x))
        
print(type(y))
        
      
print(type(z))

        """)
st.subheader("Random")
st.write("""


Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:""")
st.subheader("Example :")
st.code("""


import random

print(random.randrange(1, 10))
        """)
st.subheader("Python Arithmetic Operators")
st.write("""



Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	Example	Try it
         
+	Addition	x + y	 
         
-	Subtraction	x - y	
         
*	Multiplication	x * y	
         
/	Division	x / y	
         
%	Modulus	x % y	
         
**	Exponentiation	x ** y	
         
//	Floor division	x // y	
         

         """)
st.subheader("Python List")
st.write("""


Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
         """)
st.code("""


thislist = ["apple", "banana", "cherry"]
print(thislist)
        """)
st.subheader("Python Tuples")
st.write("""

Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
         """)
st.code("""
thistuple = ("apple", "banana", "cherry")
print(thistuple)
        """)
st.subheader("Python Loops")
st.write("""

Python has two primitive loop commands:

while loops
         
for loops
         
The while Loop
         
With the while loop we can execute a set of statements as long as a condition is true.
         """)
st.code("""
        i = 1
      
while i < 6:
        
  print(i)
        
  i += 1
        
  """)
st.subheader("The Break Statement")
st.write("""
With the break statement we can stop the loop even if the while condition is true
  """)
st.code("""
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
""")
import streamlit as st
import random

# Define simple quiz questions for beginners
questions = [
    # Multiple Choice Questions
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".py", ".pyt", ".pt", ".python"],
        "answer": ".py",
        "type": "mcq"
    },
    {
        "question": "Which function is used to display output in Python?",
        "options": ["display()", "print()", "output()", "show()"],
        "answer": "print()",
        "type": "mcq"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["//", "#", "/* */", "--"],
        "answer": "#",
        "type": "mcq"
    },
    {
        "question": "How do you create a variable in Python?",
        "options": ["var x = 5", "x = 5", "int x = 5", "declare x = 5"],
        "answer": "x = 5",
        "type": "mcq"
    },
    {
        "question": "Which data type is used to store text in Python?",
        "options": ["int", "float", "string", "bool"],
        "answer": "string",
        "type": "mcq"
    },
    {
        "question": "What will be the output of print(3 + 2 * 2)?",
        "options": ["10", "7", "8", "9"],
        "answer": "7",
        "type": "mcq"
    },
    {
        "question": "Which keyword is used to create a function in Python?",
        "options": ["function", "define", "def", "func"],
        "answer": "def",
        "type": "mcq"
    },
    # True/False Questions
    {
        "question": "Python is case-sensitive.",
        "options": ["True", "False"],
        "answer": "True",
        "type": "tf"
    },
    {
        "question": "Indentation is optional in Python.",
        "options": ["True", "False"],
        "answer": "False",
        "type": "tf"
    },
    {
        "question": "The 'print' function is used to take user input.",
        "options": ["True", "False"],
        "answer": "False",
        "type": "tf"
    }
]

# Shuffle questions for randomness
random.shuffle(questions)

def quiz_app():
    st.title("Simple Python Quiz for Beginners")
    
    # Initialize session state
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'current_q' not in st.session_state:
        st.session_state.current_q = 0
    if 'answers' not in st.session_state:
        st.session_state.answers = []
    
    # Display questions systematically
    if st.session_state.current_q < len(questions):
        q = questions[st.session_state.current_q]
        st.subheader(f"Question {st.session_state.current_q + 1}")
        st.write(q["question"])
        
        # Display answer choices
        choice = st.radio("Select your answer:", q["options"], key=st.session_state.current_q)
        
        if st.button("Submit"):
            if choice == q["answer"]:
                st.session_state.score += 1
            st.session_state.answers.append({"question": q["question"], "your_answer": choice, "correct": q["answer"]})
            st.session_state.current_q += 1
            st.experimental_rerun()
    else:
        # Display final score and review answers
        st.subheader("Quiz Completed!")
        st.write(f"Your Score: {st.session_state.score} / {len(questions)}")
        st.write("Review your answers:")
        for ans in st.session_state.answers:
            st.write(f"Q: {ans['question']}")
            st.write(f"Your Answer: {ans['your_answer']}")
            st.write(f"Correct Answer: {ans['correct']}")
            st.write("---")
        
        if st.button("Restart Quiz"):
            st.session_state.score = 0
            st.session_state.current_q = 0
            st.session_state.answers = []
            random.shuffle(questions)
            st.experimental_rerun()

if __name__ == "__main__":
    quiz_app()