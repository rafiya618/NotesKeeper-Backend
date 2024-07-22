# NotesKeeper-Backend
Notes Keeper is a web application built with React for the frontend and Django for the backend, featuring robust JWT authentication. The app includes secure private routes, efficient CORS configuration, and persistent user sessions via local storage. It manages token lifespans to ensure ongoing security and provides a seamless logout functionality. Designed to streamline note-taking and management, this app offers a user-friendly interface for maintaining and accessing notes effortlessly.

![image](https://github.com/user-attachments/assets/40f939b8-2569-430b-ba9f-f5ce64ac61e7)

![image](https://github.com/user-attachments/assets/cba4bb6e-16f8-49d7-8f51-97a359a67e67)

![image](https://github.com/user-attachments/assets/6ef55254-426b-47b8-b817-f7001ee2c9d8)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# To run this follow the following steps:
## Install Dependencies:
pip install -r requirements.txt
## Apply Migrations:
python manage.py makemigrations
python manage.py migrate
## Create Superuser:
python manage.py createsuperuser
=> Note: superusers and users added by superusers can only use the NotesKeeper App
## Run the Development Server:
python manage.py runserver



