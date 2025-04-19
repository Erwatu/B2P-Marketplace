BASE_DIR := $(shell pwd)/app

run:
	poetry run python $(BASE_DIR)/main.py

