# Contributing

## Getting Started

```console
python -m venv venv && source ./venv/bin/activate && pip install -r requirements_dev.txt
```

## Lint

```console
flake8 src/ tests/
```

## Tests

```console
PYTHONPATH=src pytest
```
