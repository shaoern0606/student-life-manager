# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Set API key environment variable
ENV GOOGLE_API_KEY=YOUR_API_KEY_HERE

# Run ADK Web
CMD ["adk", "web", "--host", "0.0.0.0", "--port", "8000"]