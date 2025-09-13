# 🚀 Celery Project with Django & Docker

The repo can be treated as docs to utilize celery using redis and rabbitmq

## 📋 Setup Instructions

### Step 1: 🐳 Setting up Django Project in Docker

This step covers the complete setup of a Django project running in a Docker container.

#### Prerequisites Setup
```bash
# Create and activate conda environment
conda create -n celery python=3.12 
conda activate celery 

# Install required packages
pip install django   
pip install celery   
pip install redis
```

#### Django Project Creation
```bash
# Create Django project
django-admin startproject djangoprojcelery

# Generate requirements file
pip freeze > requirements.txt
```

#### Docker Setup
```bash
# Make entrypoint script executable
chmod +x ./entrypoint.sh 

# Build and run the Docker containers
docker-compose up -d --build
```

#### 🎯 What This Achieves
- ✅ Django project created and configured
- ✅ Docker containerization setup
- ✅ Development environment ready
- ✅ Application accessible at `http://localhost:8001`

#### 📁 Project Structure
```
celery/
├── djangoprojcelery/          # Django project directory
│   ├── djangoprojcelery/      # Django settings and config
│   ├── manage.py              # Django management script
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile            # Docker configuration
│   └── entrypoint.sh         # Container startup script
├── docker-compose.yml        # Multi-container setup
└── README.md                 # This file
```
