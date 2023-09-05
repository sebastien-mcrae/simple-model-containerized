# Run with Docker (recommended)

### Build the Docker image
```bash
docker build -t api .
```

### Run the container
```bash
docker run -p 8000:8000 api
```
# Run with Poetry

### Install Poetry

See instructions [here](https://python-poetry.org/docs/#installation).

### Install the dependencies in a virtual environment
```bash
poetry install
```

### Start the API

```bash
poetry run api
```

# Poetry commands

### Format the code
```bash
poetry run format
```

### Lint the code
```bash
poetry run lint
```

### Fix linting errors
```bash
poetry run lint --fix
```
