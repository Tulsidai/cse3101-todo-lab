# CSE3101 Lab Worksheet I

a todo app 

## Functionalities

- Add a task
- See all tasks and look at one task
- Edit a task and tick it done
- Delete a task (it asks first)

Tasks show **unfinished first, oldest first**.

## Made with

| Part | Tool |
|---|---|
| Language | Python |
| Framework | Django |
| Database | PostgreSQL |

## How to run it

1. Make a virtual environment and turn it on:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install the packages:
   ```
   pip install django psycopg[binary]
   ```
3. Make a PostgreSQL database called `tododb` and a user called `todo_user` with permission on it.
4. Set the database login in the terminal:
   ```
   $env:DB_USER="todo_user"
   $env:DB_PASSWORD="your_password"
   $env:DB_PORT="5432"
   ```
5. Set up the tables and start the server:
   ```
   python manage.py migrate
   python manage.py runserver
   ```
6. Go to http://127.0.0.1:8000/tasks/

## Pages

| Page | URL |
|---|---|
| Task list | `/tasks/` |
| Task detail | `/tasks/1/` |
| New task | `/tasks/new/` |
| Edit task | `/tasks/1/edit/` |
| Delete task | `/tasks/1/delete/` |

ฅ^•ﻌ•^ฅ 