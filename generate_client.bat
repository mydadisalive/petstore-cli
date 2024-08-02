@echo off
REM Disable path conversion for Git Bash/MinGW
set MSYS_NO_PATHCONV=1

REM Set the current directory as the output directory
set OUTPUT_DIR=%cd%\petstore-client

REM Ensure the output directory exists
if not exist "%OUTPUT_DIR%" mkdir "%OUTPUT_DIR%"

REM Run the OpenAPI Generator Docker container
docker run --rm -v "%OUTPUT_DIR%:/local" openapitools/openapi-generator-cli generate ^
    -i https://petstore.swagger.io/v2/swagger.json ^
    -g python ^
    -o /local

echo Client generated in %OUTPUT_DIR%
pause
