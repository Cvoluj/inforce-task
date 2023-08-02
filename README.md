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

## Install Postman or simmilar app to make JSON request

https://www.postman.com/downloads/

# Documentation
This part of README explain non-obvious part of my code

In helpers app you can find TrackingModel which gives all his herits will have created and updated fields

**Employee** is new User model that herit TrackingModel
It has own JWD authorization and registration
Employee has logic as User and also Staff, which has options to create **Restraunt** and etc.

## JSON and API
_and example how will look request in postman and in general_

**link/with/smt** - it`s your url for API testing<br>
POST/GET etc. - type of request<br>
{<br>
 context of your request sended as JSON<br>
}<br>


**http://localhost:8000/api/register/**
POST
{   
    "username": "test",
    "email":"test@gmail.com",
    "password":"password"
}
**http://localhost:8000/api/login/**
POST
}
    "email":"test@gmail.com",
    "password":"password"
}
after this request you will get token, you should copy it and place in
Postman -> Authorization -> Type = Baerer -> paste
also you can visit
**http://localhost:8000/api/user/**
GET
If you have several account you probably will see not your account, because i didn`t made logout

for restaurant.views.py documentation very nice and clear

menu.views.py have almost same documentation as restaurant.views.py but more complicated: 
**http://localhost:8000/api/menus/**
POST
{
    "name": "Unique menu",
    "restaurant_name": "Portfolio",
    "date": "2023-08-02",
    "menu_items": [
        {
            "name": "New Item 1",
            "description": "New Item 1 Description",
            "price": "12.34"
        },
        {
            "name": "New Item 2",
            "description": "New Item 2 Description",
            "price": "45.67"
        }
    ]
}


voting app not fully maded, but with
**http://localhost:8000/api/current/**
GET
you will get somthing like this, with all menus dated for today
[
    {
        "name": "FAL Menu",
        "date": "2023-08-02",
        "items": [
            {
                "id": 77,
                "created_at": "2023-08-02",
                "updated_at": "2023-08-02",
                "name": "Updated Item 1",
                "description": "Updated Item 1 Description",
                "price": "99.99"
            },
            {
                "id": 78,
                "created_at": "2023-08-02",
                "updated_at": "2023-08-02",
                "name": "New Item 3",
                "description": "New Item 3 Description",
                "price": "78.90"
            }
        ]
    },
    {
        "name": "FAL Menu",
        "date": "2023-08-02",
        "items": [
            {
                "id": 79,
                "created_at": "2023-08-02",
                "updated_at": "2023-08-02",
                "name": "adfag Item 1",
                "description": "Updated Item 1 Description",
                "price": "91239.99"
            },
            {
                "id": 80,
                "created_at": "2023-08-02",
                "updated_at": "2023-08-02",
                "name": "afgags ftem 3",
                "description": "New Item 3 Description",
                "price": "78.90"
            }
        ]
    }
]

**http://localhost:8000/api/vote/**
POST (it takes only id`s or pk`s, but not for all menus created pk`s)
{
    "menu": "1",
    "employee": "3"
}

A most weak part of code, but I already spend much time for this project and in fact that it`s my first meeting with REST i`m fully satisfied with the result.


