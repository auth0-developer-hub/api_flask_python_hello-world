# Hello World API: Flask Auth0 Sample

This Python code sample demonstrates how to implement authorization in a Flask API server using Auth0.

## Run the Project

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
AUTH0_AUDIENCE=
AUTH0_DOMAIN=
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

### 🔐 Get protected message

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

### 🔐 Get admin message

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
