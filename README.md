# Hospital Management
Hospital management system is a small project to manage the hospital activities.



# What's New In This Project: 
  - Performed automatically tasks by celery.
  - Used Signals to control booked turns model activity.
  - Used Postgresql as a database.
  - Used Customized Model Permissions for users. 
  - Used Docker to containerize the project.
  - Tried to write maintanable and scalable codes.
  
  
# What Are The Prject's Features:
  - Add Doctors 
  - Add Nurses
  - Add Hospital Operators
  - Add Patients 
  - Booked a turn date for patients
  - Cancel the turns those the patients didnot paid and not referred to doctor on time, automatically.
  - Send notification to patients just one day before the turn, automatically.
  - Send notification to doctor and patient after created the turn.
   
  
# How To Run This Project:
  - clone the project from:
    - https://github.com/amirasadi13/hospital-management.git
  - run docker on your system or download from https://docs.docker.com/engine/install/
  - run commands:
    - docker compose build 
    - docker compose up
