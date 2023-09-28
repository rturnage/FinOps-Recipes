# Python Transform

Steps to transform source data to target common data schema.

## Development

```bash
# Windows
# virtualenv \path\to\.venv -p path\to\specific_version_python.exe
# C:\Users\!Admin\AppData\Local\Programs\Python\Python310\python.exe -m venv .venv
# .venv\scripts\activate

# Linux
# virtualenv .venv /usr/local/bin/python3.10
# python3.10 -m venv .venv
# python3 -m venv .venv
python3 -m venv .venv
source .venv/bin/activate

# Update pip
python -m pip install --upgrade pip

deactivate
```

Install dependencies and configure environment file.

```bash
# Install dependencies
pip install -r requirements_dev.txt

# Replace settings in local.env
cp env.example .env
```