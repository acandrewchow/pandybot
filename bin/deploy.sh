# Build Docker image
echo "Building Docker image..."
docker build -t pandybot .

# Run Docker container
echo "Starting Docker container..."
docker run --name discordbot -d pandybot

# Verify deployment
echo "Verifying deployment..."
docker ps
