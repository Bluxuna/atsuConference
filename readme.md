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

4. Access the API documentation at http://localhost:8000/docs

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
- `PUT /admin/promote-user/{user_id}` - Promote a user to admin status

### Password Management
- `PUT /admin/change-password` - Change current user's password

## Creating an Admin User

There are three ways to get an admin user in the system:

### 1. Default Admin User (Automatic)

The system automatically creates a default admin account on first startup:
- Username: `admin`
- Password: `admin`
- Email: `admin@example.com`

**IMPORTANT**: Change the default admin password immediately after first login using the `/admin/change-password` endpoint.

### 2. Promote a User to Admin (API)

An existing admin can promote any user to admin status using the API:

```bash
# Get your auth token first
curl -X 'PUT' \
  'http://localhost:8000/admin/promote-user/2' \
  -H 'Authorization: Bearer YOUR_ADMIN_TOKEN_HERE'
```

### 3. Manual Database Update

If needed, you can directly update the database:

```bash
# Access SQLite database
sqlite3 forum.db

# Update the user to be an admin
UPDATE users SET is_admin = 1 WHERE username = 'your_admin_username';
```

## Usage Examples

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

### Change password
```bash
curl -X 'PUT' \
  'http://localhost:8000/admin/change-password' \
  -H 'Authorization: Bearer YOUR_TOKEN_HERE' \
  -H 'Content-Type: application/json' \
  -d '{
  "current_password": "admin",
  "new_password": "new_secure_password"
}'
```