# Use Python image
FROM python:3.8-slim

# Set working directory
WORKDIR /rest

# Copy requirements file
COPY ./requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy code
COPY . .

# Start server
CMD alembic upgrade head && \
    uvicorn app.main:app --host 0.0.0.0 --port 5000