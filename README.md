# mist.ai PyPortfolio agent

## Documentation
UV: [UV Documentation](https://github.com/astral-sh/uv)

Fast API: [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Setup you Environment

```bash
# setup uv in you machine (globally)
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# if need (locally)
# With pip.
pip install uv
```

```bash
# install virtual env and activate
uv venv --python 3.12.0
source .venv/bin/activate
```

### Note: `Set your IDE to use .venv as your interpriter`

```bash
# install packages using pyproject.toml
uv pip install -r pyproject.toml

# install a specific package
uv add pydantic
```

### Setup .env File
* create a `.env file` in the root directory and project will read the variables at the runtime

### How to run the server

```bash
# run using fastapi
fastapi run src/app.py
```
