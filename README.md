# Simple to use FastAPI, SqlAlchemy, Postgres setup Boilerplate

FastAPI Boilerplate is a robust and highly customizable REST API template built with FastAPI, a modern, fast, web framework for building APIs with Python 3.6+ based on standard Python type hints. This boilerplate includes easy-to-use definitions and functionalities for handling roles, database migrations with Alembic, and more. It is designed to kickstart your FastAPI projects and simplify the development process.

## Features

- **FastAPI**: Utilizes the power of FastAPI for high-performance API development.
- **Swagger**: Swagger API documentation available at `http://localhost:8000/docs`.
- **Database Migrations**: Integrated with Alembic for seamless database schema migrations.
- **Customizable**: Easily customizable and extendable to fit your specific project requirements.
- **Security**: Basic implementation of secure password hashing and JWT (JSON Web Tokens) for user authentication.
- **Role-Based Access Control**: Provides predefined user roles (superadmin, admin, staff, and others) with easy-to-use functionalities for role-based access control.
- **Exception Handling**: Comprehensive error handling and detailed exception messages for easier debugging.
- **Dockerized Setup**: Easily deploy the application using Docker and Docker Compose, with support for PostgreSQL database and Adminer for database management.
- **Requirements**: Includes a `requirements.txt` file for easy dependency installation with pip.



## Setup (Dcoker environment)

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:tecelit/fast-api-boilerplate.git
   cd fast-api-boilerplate/svr/
   ```

2. Create a .env file in the project root based on .env.docker-example.
Modify the necessary environment variables in the .env file, including your database connection string and other configuration settings.

3. Run with Docker Compose:
   ```bash
   docker-compose up -d
   ```
This command builds and starts the services defined in the docker-compose.yml file. The FastAPI application will be accessible at http://localhost:8000. If you want to check the API documentation it shall be available at http://localhost:8000/docs

4. To stop the services, run -
   ```bash
   docker-compose down
   ```



## Setup (Dev environment)

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:RtjShreyD/excelus_app.git
   cd excelus_app/svr/
   ```

2. **Create a Virtual Environment (Windows)**:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Create a Virtual Environment (Linux/Mac)**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   - Create a `.env` file in the project root based on the provided `.env.example`.
   - Fill in the required environment variables in the `.env` file, including your database connection string and other configuration settings.

5. **Database Setup**:
   - Run database migrations using Alembic:

     ```bash
     alembic upgrade head
     ```

6. **Run the FastAPI Server**:

   ```bash
   uvicorn main:app --reload
   ```

The API will be accessible at `http://localhost:8000`.


## Applications Access

- The API server will be accessible at `http://localhost:8000`.

- The API documentation (Swagger UI) is available at `http://localhost:8000/docs`. Use this interactive documentation to explore and test the API endpoints.

- The PostgreSQL server will be accessible at - 
`postgresql://username:password@localhost:5433/database_name`
username and password shall be same as that set inside the .env file

- The Adminer Database viewer will be accessible at `http://localhost:5557` login with same credentials as in the .env file


## Customization

- **Roles**: Modify the predefined roles or add new roles in `svr/core/dependencies.py`.
- **Endpoints**: Add new API endpoints in `svr/api/v1/<app-name>/routes.py` or modify existing ones in `svr/api/v1/users/routes.py`.
- **Exception Handling**: Customize exception messages and responses in the `exceptions.py` file.
- **Database Models**: Define your database models in the `svr/database/models.py` file and create corresponding CRUD operations in the `ops/<your-model>.py` file or try modifying the existing ones in `svr/database/ops/users.py`.
- **Authentication**: Adjust the authentication logic in the `svr/api/v1/users/auth.py` file, including token expiration and issuer information.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

