# Cal State Seer - Backend
## Project Description
Application for the California State University (CSU) System to help administrators deal with the dramatic increase of students being forecasted in the upcoming decade. Helps identify bottlenecks in graduation rates when faced with the problem of how many students should be allowed in upcoming semesters. Also identifies graduation rates of students as they move along in their semesters depending on how many units the student has previously taken. 

## Getting Started 
* Clone github repo
* Make sure to have at least Python 3.7.0 and Django 2.2.0 installed
* Check requirements.txt page for all needed pip modules
* When installing modules, type into command line "pip install (insert module name here)"
* Make sure [MongoDB](https://treehouse.github.io/installation-guides/mac/mongo-mac.html) is running in the background
* Switch into server directory
* Type into command line "python manage.py runserver"
* Then type http://localhost:8000/login into your browser and you're ready to start! 

## How Does it Work?
Using a Markov Chain Model that is trained on thousands of examples from previous semesters at California State Universities, including multiple departments and colleges, we can provide accurate predictions based on what was seen in the past to help administrators better prepare for the future. 
* Good reference for [Markov Chains](https://setosa.io/ev/markov-chains/)
* The example below is an interactive chart administrators will see when testing the model with a changing number of incoming students

<p align="center">
  <img src="https://github.com/djbursch/csuSeer-server/blob/master/images/Screen%20Shot%202020-03-29%20at%206.02.48%20PM.png" width="400" height="350" title="Example Graph of Incoming Students">
</p>
* Due to our application being a work in progress, more graphs with multiple different formats will be added soon

## Security
### Verification
* Uses Json Web Tokens (JWT) to provide secure authentication for users
* Since this is mainly for administrative use, only invited users are allowed to make accounts
### Permissions
* We have strict permission control to ensure the safety of student data
* The tree graph below describes the different permissions users are able to attain when using our application

<p align="center">
  <img src="https://github.com/djbursch/csuSeer-server/blob/master/images/Permission%20Hierarchy.png" width="500" height="350" title="Permission Hierarchy">
</p>

## Versioning

* Version 1

## Credits
* Daniel Jackson Bursch - Backend
* Ignacio Saenz de Navarrete Munar - [Frontend](https://github.com/ignacioSaenzdeN/Csu_FE_MainApp)

## License
* GNU GENERAL PUBLIC LICENSE - Version 3, 29 June 2007


