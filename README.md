# Night Bull

Simple Python application to experiment with venv, dependencies, pytest,
flake8 and FastAPI.

## Getting Started

```console
$ docker build -t nightbull:0.1
```

## Usage

```console
$ docker run --rm -it -p 8080:8080 nightbull:0.1
```

```
INFO:     Started server process [7]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

## Documentation

The application is using FastAPI which uses Redoc to generate OpenAPI
documentations. To access the generated documentation after the application
started, visit the `/redoc` endpoint.

![Documentation](/documentation.png)

## Contributing

Please read the [CONTRIBUTING.md](/CONTRIBUTING.md) file to discover how to
set up the project to be able to contribute, run lints, tests...