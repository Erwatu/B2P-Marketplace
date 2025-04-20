BASE_DIR := $(shell pwd)/app

run:
	poetry run python $(BASE_DIR)/main.py

#docker-compose
ENV_FILE=$(shell pwd)/app/core/.env
COMPOSE_FILE=$(shell pwd)/docker/docker-compose.yaml

docker-up:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up

docker-up-detached:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d

docker-down:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) down

docker-restart: docker-down docker-up

docker-db:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up -d pg

docker-app:
	docker compose --env-file $(ENV_FILE) -f $(COMPOSE_FILE) up app