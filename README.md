# Cal State Seer - Backend
Project for California State University to help administrators deal with the dramatic increase of students being forecasted in the upcoming decade. Will help identify bottlenecks in graduation rates when faced with the problem of how many students should be allowed in upcoming semesters. Also identifies graduation rates of students as they move along in their semesters and how many units they have previously taken. 

## Getting Started
* Make sure to have Python v3.6.0 and Django v2.2.0 or better installed, along with MongoDB 
* Clone github repo
* Switched into server directory
* Type into command line "python3 manage.py runserver"
* If missing any modules, go to moduleFile.py to see all needed modules from Django
* When installing modules, type into command line "pip3 install <insert module name here>"
 
## How Does it Work?
Using a Markov Chain Model that is trained on thousands of examples from previous semesters at California State Universitys, including multiple departments and colleges, we can provide accurate predictions based on what was seen in the past to help administrators better prepare for the future. A good website to help better understand Markov Chain's is https://setosa.io/ev/markov-chains/.
 

