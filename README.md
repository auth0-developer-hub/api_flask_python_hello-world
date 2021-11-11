# Hello World API: Flask Auth0 Sample

You can use this sample project to learn how to secure a simple Flask API server using Auth0.

The `starter` branch offers a working API server that exposes three public endpoints. Each endpoint returns a different type of message: public, protected, and admin.

The goal is to use Auth0 to only allow requests that contain a valid access token in their authorization header to access the protected and admin data. Additionally, only access tokens that contain a `read:admin-messages` permission should access the admin data, which is referred to as [Role-Based Access Control (RBAC)](https://auth0.com/docs/authorization/rbac/).

## Get Started

Create a virtual environment under the root project directory:

**macOS/Linux:**

```bash
python3 -m venv venv
```

**Windows:**

```bash
py -3 -m venv venv
```

Activate the virtual environment:

**macOS/Linux:**

```bash
. venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file under the root project directory and populate it with the following content:

```bash
CLIENT_ORIGIN_URL=http://localhost:4040
```

Run the project in development mode:

```bash
flask run
```

## API Endpoints

The API server defines the following endpoints:

### 🔓 Get public message

```bash
GET /api/messages/public
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "message": "The API doesn't require an access token to share this message."
}
```

### 🔓 Get protected message

> You need to protect this endpoint using Auth0.

```bash
GET /api/messages/protected
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "message": "The API successfully validated your access token."
}
```

### 🔓 Get admin message

> You need to protect this endpoint using Auth0 and Role-Based Access Control (RBAC).

```bash
GET /api/messages/admin
```

#### Response

```bash
Status: 200 OK
```

```json
{
  "message": "The API successfully recognized you as an admin."
}
```
