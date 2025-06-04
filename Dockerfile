FROM python:3.12-slim-bookworm

WORKDIR /server

# Install system dependencies and Python dependencies
COPY requirements.txt /server/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir uvicorn

# Copy project
COPY . /server/

# Expose the port the app runs in
EXPOSE 8000

# Define the command to start the container
CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]