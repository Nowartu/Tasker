# Tasker

Simple  application for task lists with nginx and ELK log collection. \
Allows you to create tasks, complete them and add comments. All operations are logged and visible in elastic.

## Installation

Just run:
```bash
docker compose up 
```

## Available services

- localhost/api - api for Tasker operations
- localhost/api/docs - FastAPI openAPI docs
- localhost/kibana - Elastic webpage

## Project folders

- backend - contains REST API for Tasker
- filebeat - filebeat configuration (collects logs from nginx and puts them to elastic)
- nginx - web server, hosts whole application 