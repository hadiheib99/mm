def create_dockerfile():
    """Generate a Dockerfile for containerizing the Models Manager."""
    dockerfile_content = """
    FROM python:3.9-slim
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD ["python", "main.py"]
    """
    with open("Dockerfile", "w") as file:
        file.write(dockerfile_content)
    print("Dockerfile created.")