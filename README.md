# wizard-assistant-bot

Remembrall is an assistant bot for wizards of the academy.


## Installing

You can install the Remembrall from [PyPI](https://pypi.org/project/wizards-remembrall/):
```bash
python -m pip install wizards-remembrall
```

Once installed the _Remembrall_ is avaialbe as a command line application, named `remembrall`.

```bash
remembrall [command] [args1, args2, ...]
```

List the avaialble commands:
```bash
remembrall help
```

## Development

Set up a virtual environment (venv) by running the following command in your project directory:
```bash
python -m venv .venv
```

Activate the virtual environment. On Windows, run:
```bash
.\.venv\Scripts\activate.ps1
```
On macOS and Linux, run:
```bash
source .venv/bin/activate
```

Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

Start developing your wizard assistant bot!

Remember to update a `requirements.txt` file in the project directory if you add new dependencies by running the

```bash
pip freeze > requirements.txt
```

For local development, you can install your package in editable mode:
```bash
pip install -e .
```

And it become available as `remembrall` programm.

Or can be launched as
```bash
python src/remembrall/__main__.py
```
