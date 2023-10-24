# FastAPI, SqlAlchemy, Postgres setup Boilerplate

FastAPI Boilerplate is a robust and highly customizable REST API template built with FastAPI, a modern, fast, web framework for building APIs with Python 3.6+ based on standard Python type hints. This boilerplate includes easy-to-use definitions and functionalities for handling roles, database migrations with Alembic, and more. It is designed to kickstart your FastAPI projects and simplify the development process.

## Features

- **FastAPI**: Utilizes the power of FastAPI for high-performance API development.
- **Swagger**: Swagger api documentation available
- **Database Migrations**: Integrated with Alembic for seamless database schema migrations.
- **Customizable**: Easily customizable and extendable to fit your specific project requirements.
- **Security**: Basic implementation secure password hashing and JWT (JSON Web Tokens) for user authentication.
- **Role-Based Access Control**: Provides predefined user roles (superadmin, admin, staff, and others) with easy-to-use functionalities for role-based access control.
- **Exception Handling**: Comprehensive error handling and detailed exception messages for easier debugging.
- **Requirements**: Includes a `requirements.txt` file for easy dependency installation with pip.

## Usage

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd fastapi-boilerplate
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**:

   - Set up your database connection string in `config.py`.
   - Run database migrations using Alembic:

     ```bash
     alembic upgrade head
     ```

4. **Run the FastAPI Server**:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be accessible at `http://localhost:8000`.

## API Documentation

The API documentation (Swagger UI) is available at `http://localhost:8000/docs`. Use this interactive documentation to explore and test the API endpoints.

## Customization

- **Roles**: Modify the predefined roles or add new roles in `svr/core/dependencies.py`.
- **Endpoints**: Add new API endpoints in `svr/api/v1/<app-name>/routes.py` or modify existing ones in `svr/api/v1/users/routes.py`.
- **Exception Handling**: Customize exception messages and responses in the `exceptions.py` file.
- **Database Models**: Define your database models in the `svr/database/models.py` file and create corresponding CRUD operations in the `ops/<your-model>.py` file or try modifying the exisiting ones in `svr/database/ops/users.py`.
- **Authentication**: Adjust the authentication logic in the `svr/api/v1/users/auth.py` file, including token expiration and issuer information.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests to help improve this FastAPI boilerplate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.