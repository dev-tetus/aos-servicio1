#!/bin/sh -e

until nc -vz db:3306 > /dev/null; do
    >&2 echo "db:3306 is unavailable - sleeping"
    sleep 2
  done
  >&2 echo "db:3306 is up"

python3 main.py

exit 0