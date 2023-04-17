# Night Bull

Simple Python application to experiment with [venv][venv], dependencies,
[pytest][pytest], [flake8][flake8] and [FastAPI][fastapi].

## Getting Started

```console
$ docker compose up
```

```
INFO:     Started server process [7]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

## Documentation

The application is using FastAPI which uses [Redoc][redoc] to generate OpenAPI
documentations. To access the generated documentation after the application
started, visit the `/redoc` endpoint.

## Contributing

Please read the [CONTRIBUTING.md](/CONTRIBUTING.md) file to discover how to
set up the project to be able to contribute, run lints, tests...

[fastapi]: https://fastapi.tiangolo.com/
[flake8]: https://flake8.pycqa.org/en/latest/
[pytest]: https://docs.pytest.org/en/7.3.x/
[redoc]: https://github.com/Redocly/redoc
[venv]: https://docs.python.org/3/library/venv.html
