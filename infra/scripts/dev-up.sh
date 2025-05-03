#!/bin/bash

set -e

echo "🧱 Starting Developer Sandbox Bootstrap..."

# Step 1: Initialize Docker Swarm if not already initialized
if ! docker info | grep -q "Swarm: active"; then
    echo "🔧 Initializing Docker Swarm..."
    docker swarm init
else
    echo "✅ Swarm already initialized."
fi

# Step 2: Deploy Traefik or other reverse proxy (optional placeholder)
if [ -f "../swarm/traefik/docker-compose.traefik.yml" ]; then
    echo "🚀 Deploying Traefik reverse proxy..."
    docker stack deploy -c ../swarm/traefik/docker-compose.traefik.yml traefik
else
    echo "⚠️  Traefik config not found, skipping reverse proxy setup."
fi

# Step 3: Deploy sample service stack
if [ -f "../swarm/sample-stack/docker-compose.yml" ]; then
    echo "📦 Deploying sample microservice stack..."
    docker stack deploy -c ../swarm/sample-stack/docker-compose.yml sample
else
    echo "⚠️  Sample stack config not found, skipping service deployment."
fi

echo "✅ Developer environment is up and running!"