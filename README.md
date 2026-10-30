# InPost Label Fixer

A CLI and API that accepts an InPost A4 shipping label and outputs the cropped 4x6" label for use with a label printer.

## Usage

```
# CLI
uv run src/process.py -i input.pdf -o output.pdf

# API
uv run uvicorn api:app --app-dir src
curl -F file=@input.pdf localhost:8000/process -o label.pdf
```

## Development

```
# CLI
uv run src/process.py -i input.pdf -o output.pdf

# API
uv run uvicorn api:app --app-dir src --reload
```
