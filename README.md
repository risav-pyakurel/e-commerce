# E-Commerce Django Project

Welcome to my Django e-commerce project! This project is an online shopping website built using the Django framework. The frontend uses templates from external sources, and the backend has been entirely developed by me.

## Running Locally with Docker Compose

This project uses Docker Compose to run both Django and PostgreSQL in containers.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

### Quick Start

1. **Clone this repository:**
    ```bash
    git clone "https://github.com/risav-pyakurel/e-commerce.git"
    cd e-commerce
    ```

2. **Update environment variables:**
    - Edit `docker-compose.yaml` and set your desired database name, user, and password.
    - Make sure your Django `settings.py` uses these environment variables for the database connection.

3. **Build and start the containers:**
    ```bash
    docker compose up --build
    ```

    If port 5432 is already in use, change the Postgres port mapping in `docker-compose.yaml`:
    ```yaml
    ports:
      - "5433:5432"
    ```
    And update your Django `DATABASE_PORT` accordingly.

4. **Access the app:**
    - Open your web browser and go to [http://localhost:8000](http://localhost:8000)

5. **Stopping the containers:**
    ```bash
    docker compose down
    ```

### Troubleshooting

- If you see `address already in use` for port 5432, stop any local Postgres server or change the port mapping.
- If Django cannot connect to the database, ensure the `DATABASE_HOST` is set to `db` (the service name in Docker Compose).

---

## Project Structure

- `Dockerfile` – Builds the Django app image.
- `docker-compose.yaml` – Defines and runs multi-container Docker applications.
- `requirements.txt` – Python dependencies.
- `runtime.txt` – Python version for deployment platforms.

---

## Database Configuration Example

In `docker-compose.yaml`:
```yaml
services:
  db:
    image: postgres:14
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    ports:
      - "5432:5432"
  web:
    build: .
    environment:
      - DATABASE_NAME=mydb
      - DATABASE_USER=myuser
      - DATABASE_PASSWORD=mypassword
      - DATABASE_HOST=db
      - DATABASE_PORT=5432
    depends_on:
      - db
    ports:
      - "8000:8000"
```

In `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST', 'db'),
        'PORT': os.environ.get('DATABASE_PORT', '5432'),
    }
}
```

---

If you encounter any issues, feel free to contact me.

Thank you.
