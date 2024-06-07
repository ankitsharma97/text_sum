# Text Summarization API

This project provides an API for summarizing text using Django and an external summarization service.

## Prerequisites

- Python 3.7+
- Git
- Virtualenv

## Setup Instructions

1. **Install Python:** [Download and install Python](https://www.python.org/downloads/).

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    ```

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

3. **Clone the Project:**

    ```bash
    git clone https://github.com/ankitsharma97/text_sum.git
    cd text_sum
    ```

4. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

- `POST /api/register/` - Register a new user
- `POST /api/login/` - Log in a user
- `POST /api/logout/` - Log out a user
- `GET /api/user/<int:pk>/` - Retrieve details of a specific user
- `GET /api/users/` - Find users
- `POST /api/summarize/` - Summarize text

## Testing the API

Use Postman to test the API endpoints.

### 1. Register a New User

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/api/register/`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
    ```json
    {
      "username": "yourusername",
      "password": "yourpassword",
      "email": "youremail@example.com"
    }
    ```

### 2. Log in a User

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/api/login/`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
    ```json
    {
      "username": "yourusername",
      "password": "yourpassword"
    }
    ```

### 3. Log out a User

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/api/logout/`
- **Headers:**
  - `Authorization: Token your-auth-token`

### 4. Retrieve User Details

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/user/<int:pk>/`
- **Headers:**
  - `Authorization: Token your-auth-token`

### 5. Find Users

- **Method:** GET
- **URL:** `http://127.0.0.1:8000/api/users/`
- **Headers:**
  - `Authorization: Token your-auth-token`

### 6. Summarize Text

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/api/summarize/`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
    ```json
    {
      "text": "Your text to summarize goes here."
    }
    ```
