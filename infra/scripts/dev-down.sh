#!/bin/bash

set -e

echo "🧹 Cleaning up Developer Sandbox..."

# Step 1: Remove sample stack if exists
echo "🔻 Removing sample stack..."
docker stack rm sample || echo "Sample stack not found."

# Step 2: Remove Traefik stack if exists
echo "🔻 Removing Traefik stack..."
docker stack rm traefik || echo "Traefik stack not found."

# Step 3: Leave swarm mode if active
if docker info | grep -q "Swarm: active"; then
    echo "🔻 Leaving Docker Swarm..."
    docker swarm leave --force
else
    echo "✅ Swarm already inactive."
fi

echo "✅ Developer environment cleaned up."