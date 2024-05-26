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

### Unit Tests

VS Code is configured to use `unittest` and knows where the tests are (see `.vscode/settings.json`). You can run your tests by opening the Test Explorer (the beaker icon in the Activity Bar on the side), and then clicking on the `Run All Tests` button (the play button at the top of the Test Explorer).

Alternatively, you can press `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows) and start typing _Test: Run All Tests_.

The results of the tests will appear in the Test Explorer. You can click on a test to see its output in the Output pane.

To add a new tests simply add new file starting with `test_*.py` to `tests/` folder as per configured discovery mechanism. See [unittest](https://docs.python.org/3/library/unittest.html) Python Unit testing framework documentation.
