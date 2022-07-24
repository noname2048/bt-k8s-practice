#!/bin/bash
dockerdocker run --rm -it -p 8000:8000 simple-fastapi-app:1.0 uvicorn main:app --host=0.0.0.0
