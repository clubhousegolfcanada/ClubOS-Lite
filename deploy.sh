#!/bin/bash

echo "🔧 Starting ClubOS Lite Deployment"

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Install it and try again."
    exit 1
fi

# Check for Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Install Docker and try again."
    exit 1
fi

# Pull environment if needed
if [ ! -f .env ]; then
    echo "⚠️  .env not found. Creating placeholder..."
    echo "OPENAI_API_KEY=your-key-here" > .env
    echo "OPENAI_MODEL=gpt-4o" >> .env
fi

# Start Docker build + run
echo "🐳 Building Docker container..."
docker-compose up --build -d

echo "✅ Deployment complete. App should now be running at http://localhost:8000"