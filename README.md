# Team Member Management App

This is a Django based web application, which is for managing team members.

With this app, you can list all of the team members in your team, add a team member, edit a team member or delete a team member.

Every member has a profile including first name, last name, phone number and email address. Meanwhile, members can be an admin member or a regular one. Admin member will be shown as "Admin" when listed in the member list page.

## Set Up

You will need to install Django first to run this app. After clone it to your device, navigate to the folder which has a "manage.py" file, and execute:

`python manage.py runserver`

Then open this page in your browser:

http://localhost:8000/users/

## How to use

Click "+ Team member" on the index page to add a member. You will need to fill in the member's information, and whether she/he is an admin.

Click any team member listed in the page to edit her/his profile. You can also delete the member in the editing page.