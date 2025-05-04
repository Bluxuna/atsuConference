# Social Forum API

A simple FastAPI-based forum/social media API with user registration, post management, and admin moderation features. This API uses SQLite as the database backend.

## Features

- User registration and authentication with JWT tokens
- Create, read, update, and delete posts
- Admin moderation system for approving or deleting posts
- Role-based access control
- SQLite database for easy setup

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn app:app --reload
```

## API Endpoints

### Authentication
- `POST /token` - Login and get access token

### Users
- `POST /users/` - Register a new user
- `GET /users/me/` - Get current user info
- `GET /users/` - List all users

### Posts
- `POST /posts/` - Create a new post
- `GET /posts/` - List all approved posts (or all posts for admins)
- `GET /posts/{post_id}` - Get a specific post
- `PUT /posts/{post_id}` - Update a post
- `DELETE /posts/{post_id}` - Delete a post

### Admin
- `GET /admin/pending-posts/` - Get all pending posts
- `PUT /admin/approve-post/{post_id}` - Approve a post

## Requirements

```
# requirements.txt
fastapi==0.104.0
uvicorn==0.23.2
sqlalchemy==2.0.22
pydantic==2.4.2
pydantic-extra-types==2.1.0
pyjwt==2.8.0
bcrypt==4.0.1
python-multipart==0.0.6
email-validator==2.0.0
```

## Creating an Admin User

To create an admin user, you'll need to use the SQLite database directly after creating a regular user:

```bash
# First register a regular user through the API
# Then access SQLite database
sqlite3 forum.db

# Update the user to be an admin
UPDATE users SET is_admin = 1 WHERE username = 'your_admin_username';
```

## Usage Example

### Register a new user
```bash
curl -X 'POST' \
  'http://localhost:8000/users/' \
  -H 'Content-Type: application/json' \
  -d '{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword"
}'
```

### Get authentication token
```bash
curl -X 'POST' \
  'http://localhost:8000/token' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'username=testuser&password=securepassword'
```

### Create a post
```bash
curl -X 'POST' \
  'http://localhost:8000/posts/' \
  -H 'Authorization: Bearer YOUR_TOKEN_HERE' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "My First Post",
  "content": "This is the content of my first post!"
}'
```