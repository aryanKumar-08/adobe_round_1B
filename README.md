# Round 1B - Persona-Driven Document Intelligence

## Build
docker build --platform linux/amd64 -t round1b-intelligence .

## Run
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none round1b-intelligence
