#!/bin/bash
# wait-for-local-db

set -e

# Color formatting
RED='\033[0;31m'
NO_COLOR='\033[0m'

MAX_WAIT_TIME=30 # seconds
WAIT_TIME=0

DB_NAME="${DB_NAME:=${PGDATABASE}}"

DOCKER_DB_SERVICE_NAME="${DOCKER_DB_SERVICE_NAME:=database}"

# Use pg_isready to wait for the DB to be ready to accept connections
# We check every 3 seconds and consider it failed if it gets to 30+
# https://www.postgresql.org/docs/current/app-pg-isready.html
until pg_isready -h localhost -d "${DB_NAME}" -q;
do
  echo "waiting on Postgres DB to initialize..."
  sleep 3

  WAIT_TIME=$(($WAIT_TIME+3))
  if [ $WAIT_TIME -gt $MAX_WAIT_TIME ]
  then
    echo -e "${RED}ERROR: Database appears to not be starting up, running \"docker logs ${DOCKER_DB_SERVICE_NAME}\" to troubleshoot.${NO_COLOR}"
    docker logs "${DOCKER_DB_SERVICE_NAME}"
    exit 1
  fi
done

echo "Postgres DB is ready after ~${WAIT_TIME} seconds"


