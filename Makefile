# Makefile for Phase 0 Developer Sandbox

.PHONY: up down restart status logs

up:
	./infra/scripts/dev-up.sh

down:
	./infra/scripts/dev-down.sh

restart: down up

status:
	docker node ls || echo "Docker Swarm not running"
	docker stack ls

logs:
	docker service ls && echo "---" && docker service logs --tail 50 --follow sample_service_name