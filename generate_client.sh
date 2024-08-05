#!/bin/bash

# If this doesn't work use generate_client.bat instead

# Disable path conversion for Docker
export MSYS_NO_PATHCONV=1

# Set the output directory to a Unix-style path, compatible with Docker
OUTPUT_DIR="$(pwd)/petstore-client"

# Ensure the output directory exists
mkdir -p "$OUTPUT_DIR"

# Run the OpenAPI Generator Docker container
docker run --rm -v "$OUTPUT_DIR:/local" openapitools/openapi-generator-cli generate \
    -i https://petstore.swagger.io/v2/swagger.json \
    -g python \
    -o /local

echo "Client generated in $OUTPUT_DIR"
