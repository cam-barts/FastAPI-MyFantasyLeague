# FastAPI MyFantasyLeague Wrapper

This project is a Python wrapper built around the MyFantasyLeague.com API using FastAPI. It aims to provide a more Pythonic way of interacting with MyFantasyLeague's API for fantasy football enthusiasts and developers alike. Built with Python 3.11 and leveraging the simplicity and power of FastAPI, this wrapper simplifies the process of fetching and managing data from MyFantasyLeague.com.

## Features

- Easy-to-use FastAPI routes for fetching MyFantasyLeague.com data.
- Docker support for easy setup and deployment.
- Utilization of `pipenv` for simple dependency management.
- Secure handling of environment secrets for API authentication.
- Development setup with `ruff` for linting.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.11
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) (optional, for Docker-based setups)

## Installation

1. **Clone the repository:**
    
    ```bash
    git clone https://github.com/cam-barts/FastAPI-MyFantasyLeague.git
    cd FastAPI-MyFantasyLeague
    ```
    
2. **Set up your environment variables:**
    
    Copy the `example.env` file to a `.env` file and fill in your details.
    
    ```bash
    cp example.env .env
    ```
    
3. **Install dependencies with pipenv:**
    
    ```bash
    pipenv install
    ```
    
    Or, if using Docker:
    
    ```bash
    docker-compose up --build
    ```
    

## Usage

To start the server locally using `pipenv`:


```bash
pipenv run uvicorn src.main:app --reload
```

For Docker users:

```bash
docker-compose up
```

Navigate to `http://localhost:8000/docs` in your web browser to view the automatically generated Swagger UI documentation for your API endpoints.

## Development

This project uses [ruff](https://astral.sh/ruff) for linting. To check your code style:


```bash
# Install dev packages, including ruff
pipenv install --dev

# Run ruff check and allow for it to fix fixable issues 
pipenv run ruff check --fix .
```

### Adding new dependencies:

Whenever you add a new package:


```bash
# To install dependancies needed for the app to actually function
pipenv install <package-name>

# To install dependancies required only for development
pipenv install --dev <package-name>
```

Make sure to test your changes and, if necessary, update the project documentation.

### Environment Variables

This wrapper requires certain environment variables to be set, which can be found and explained in the `example.env` file. These include API keys and other configuration needed to securely interact with MyFantasyLeague's API.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

Please check our `CONTRIBUTING.md` for our code of conduct.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [MyFantasyLeague.com](https://www44.myfantasyleague.com/2024/api_info) for their open API.
- The FastAPI community for the awesome framework.
