# Movie Rating App

This project is a backend internship project at Lifemote Networks.

## Project Structure

- **client/**: Contains frontend code.
- **mysql/**: Database related files.
- **server/**: Backend code for the application.
- **.env.example**: Example environment configuration file.
- **docker-compose.yml**: Docker Compose configuration file for setting up the development environment.

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mkilic20/Movie-Rating-App.git
    cd Movie-Rating-App
    ```

2. Copy the example environment file and adjust the configuration:
    ```bash
    cp .env.example .env
    ```

3. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

### Usage

Access the application at `http://localhost:8000`.

### Development

To run the development server:
```bash
docker-compose up
