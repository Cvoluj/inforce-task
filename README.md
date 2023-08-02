# inforce-task
This was the first project where I got acquainted with REST, but most of all, it was my task, which I did for 20 hours in a row. It was a very interesting experience.
# Installation
Probably, it will never run on your devices, but you can try

## Install Docker:
If you haven't already, you need to install Docker on your system. Docker allows you to create, manage, and run containers. You can download and install Docker from the official website: 
https://www.docker.com/get-started

## Clone Repository or download it: 
Clone your project's repository to your local machine using Git. You can use the following command to clone the repository:
```
git clone https://github.com/Cvoluj/inforce-task.git
```

## Build the Docker Image:
Navigate to the root directory of your project in the terminal, where the `Dockerfile` is located. Build the Docker image using the following command:
```
docker-compose build
```

## Run the Docker Containers:
Once the image is built, you can run the Docker containers using the following command:
```
docker-compose up
```

## Migrate the Database:
After the containers are up and running, you need to apply the database migrations to set up the database. Open a new terminal window, navigate to the root directory of your project, and execute the following command:
```
docker-compose exec web python manage.py makemigrations
```
```
docker-compose exec web python manage.py migrate
```
## Create a Superuser:
I recommend to create superuser, because only he can gives **is_staff** permission, which uses for creating **Restaurant** and **Menus**

To give **is_staff** permission just click CheckBox to make **staff** active

In my project superuser requiers mail, keep that in my mind.

I hope it will work, afterall be patient

## Install Postman or simillar app to make JSON request

https://www.postman.com/downloads/

# Documentation
This part of README explain non-obvious part of my code

In helpers app you can find TrackingModel which gives all his herits will have created and updated fields

**Employee** is new User model that herit TrackingModel
It has own JWD authorization and registration
Employee has logic as User and also Staff, which has options to create **Restraunt** and etc.

## JSON and API
_and example how will look request in postman and in general_
<br>
**link/with/smt** - it's your url for API testing<br>
POST/GET etc. - type of request<br>
{<br>
 context of your request sended as JSON<br>
}<br>
<br>
<br>
**http://localhost:8000/api/register/** <br>
POST<br>
{   <br>
    "username": "test",<br>
    "email":"test@gmail.com",<br>
    "password":"password"<br>
}<br>
<br>
**http://localhost:8000/api/login/**<br>
POST<br>
}<br>
    "email":"test@gmail.com",<br>
    "password":"password"<br>
}<br>
after this request you will get token, you should copy it and place in<br>
Postman -> Authorization -> Choose Type Baerer Token -> paste<br>
also you can visit<br>
**http://localhost:8000/api/user/** <br>
GET<br>
If you have several account you probably will see not your account, because i didn`t made logout<br>
<br>
for restaurant.views.py documentation very nice and clear<br>
<br>
menu.views.py have almost same documentation as restaurant.views.py but more complicated: <br>
**http://localhost:8000/api/menus/** <br>
POST<br>
{<br>
    "name": "Unique menu",<br>
    "restaurant_name": "Portfolio",<br>
    "date": "2023-08-02",<br>
    "menu_items": [<br>
        {<br>
            "name": "New Item 1",<br>
            "description": "New Item 1 Description",<br>
            "price": "12.34"<br>
        },<br>
        {<br>
            "name": "New Item 2",<br>
            "description": "New Item 2 Description",<br>
            "price": "45.67"<br>
        }<br>
    ]<br>
}<br>
<br>
<br>
voting app not fully maded, but with<br>
**http://localhost:8000/api/current/** <br>
GET<br>
you will get somthing like this, with all menus dated for today<br>
[<br>
    {<br>
        "name": "FAL Menu",<br>
        "date": "2023-08-02",<br>
        "items": [<br>
            {<br>
                "id": 77,<br>
                "created_at": "2023-08-02",<br>
                "updated_at": "2023-08-02",<br>
                "name": "Updated Item 1",<br>
                "description": "Updated Item 1 Description",<br>
                "price": "99.99"<br>
            },<br>
            {<br>
                "id": 78,<br>
                "created_at": "2023-08-02",<br>
                "updated_at": "2023-08-02",<br>
                "name": "New Item 3",<br>
                "description": "New Item 3 Description",<br>
                "price": "78.90"<br>
            }<br>
        ]<br>
    },<br>
    {<br>
        "name": "FAL Menu",<br>
        "date": "2023-08-02",<br>
        "items": [<br>
            {<br>
                "id": 79,<br>
                "created_at": "2023-08-02",<br>
                "updated_at": "2023-08-02",<br>
                "name": "adfag Item 1",<br>
                "description": "Updated Item 1 Description",<br>
                "price": "91239.99"<br>
            },<br>
            {<br>
                "id": 80,<br>
                "created_at": "2023-08-02",<br>
                "updated_at": "2023-08-02",<br>
                "name": "afgags ftem 3",<br>
                "description": "New Item 3 Description",<br>
                "price": "78.90"<br>
            }<br>
        ]<br>
    }<br>
]<br>
<br>
**http://localhost:8000/api/vote/** <br>
POST (it takes only id's or pk's, but not for all menus created pk's)<br>
{<br>
    "menu": "1",<br>
    "employee": "3"<br>
}<br>
<br>
A most weak part of code, but I already spend much time for this project and in fact that it's my first meeting with REST i'm fully satisfied with the result.


