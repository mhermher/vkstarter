# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /workspace

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files into the container
COPY backend/pyproject.toml backend/poetry.lock* ./

# Install the dependencies
RUN poetry install

# Copy the rest of the working directory contents into the container
COPY backend/ .

# Expose the port FastAPI will run on
EXPOSE 8000

# Set the default command to run when starting the container
CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]