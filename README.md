
# Stage0 API

A simple Django REST API that provides information such as email, current datetime, and a GitHub URL. This project was developed as part of a backend task.

## Features
- Provides basic API data for demonstration.
- Lightweight and straightforward setup.
  
## API Documentation

### Endpoint URL
- **GET:** `/api/info/`

### Request/Response Format
**Request:**  
```bash
GET /api/info/

Response example:
{
  "email": "daniel.olusesi20@gmail.com",
  "datetime": "2025-01-29T19:12:28.886844+00:00",
  "github_url": "https://github.com/Dannysesi/Stage0_API"
}
```

To fetch the API data, you can use tools like curl:

```bash
curl http://<base-url>/api/info/
```

Setup Instructions
Clone the repository:
```
git clone https://github.com/Dannysesi/Stage0_API.git
cd Stage0_API

Create a virtual environment and activate it:
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Access the API at:
http://127.0.0.1:8000/api/info/
```

Looking to hire skilled Python developers? Visit [Hire a Python Developer](https://hng.tech/hire/python-developers).
