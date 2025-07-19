# Use official Python 3.10 image from Docker Hub
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy project files into container
COPY . .

# Install all required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit default port
EXPOSE 8501

# Start the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false", "--server.enableXsrfProtection=false"]
