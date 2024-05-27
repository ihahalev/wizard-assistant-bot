#  Publish Package to Python Package Index (PyPi)

## Configure Build Backend and Project Metadata

This project is using a `pyporject.toml` and configured with `setuptools` build backend

```toml
[build-system]
requires      = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"
```

The rest of the `pyproject.toml` document meaning is explained in the [guideline](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata)

## Prepare Distribution Package

The next step is to generate [distribution packages](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package) for the package. These are archives that are uploaded to the Python Package Index and can be installed by pip.

Make sure you have the latest version build tools installed

```bash
pip install -r requirements.txt
```

### Update an App Version

Make sure your git working directory is clean, should be no uncommitted files.
Then run the following command 

```bash
bumpver update -m
```

Here `-m` is to increment minor version. Also available `-p` for patch, `--major` for major in `major.minor.patch`.

Run `bumpver update -h` for full list of commands.


### Build a Package

Now run this command from the same directory where `pyproject.toml` is located:

```bash
python3 -m build
```

This command should output a lot of text and once completed should generate two new versioned files files in the `dist` directory

```bash
dist
├── wizards_remembrall-1.1.0-py3-none-any.whl
└── wizards_remembrall-1.1.0.tar.gz
```

## Publish Package to TestPyPi

Finally, it’s time to upload your package to the Python Package Index!

### Prerequisite

The first thing you’ll need to do is register an account on TestPyPI, which is a separate instance of the package index intended for testing and experimentation.

1. Register at https://test.pypi.org/
2. Verify email
3. Save recovery codes
4. Generate API Token

### Upload to TestPyPi

Run Twine to upload all of the archives under `dist`

```bash
python3 -m twine upload --repository testpypi dist/*
```

You will be prompted for a password. Use the token value, including the pypi- prefix.

After the command completes, you should see output similar to this:

```bash
Uploading wizards_remembrall-1.1.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 27.5/27.5 kB • 00:00 • 40.0 MB/s
Uploading wizards_remembrall-1.1.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 26.3/26.3 kB • 00:00 • 34.0 MB/s
```

Once uploaded, your package should be viewable on TestPyPI; for example:

https://test.pypi.org/project/wizards-remembrall/1.1.0/

### Installing your newly uploaded package

You can use pip to install your package and verify that it works.

1. Create a new tmp dir in any place of your system
2. Create a virtual environment `python3 -m venv .venv`
3. And activate it `source .venv/bin/activate` (Mac) or `.\.venv\Scripts\activate.ps1` (Windows)
4. Install your package from TestPyPI:
   ```bash
   pip install -i https://test.pypi.org/simple/ wizards-remembrall==1.1.0
   ```
5. Test the application by running its executable file
   ```bash
   remembrall
   ```

## Publish Package to PyPi

The same as TestPyPi, but need to register again at https://pypi.org/

And the Twine's upload command will be targeting another repo:

```bash
python3 -m twine upload --repository pypi dist/*
```

Usually you don't need to run this command manually, but it's part of CI process and executed by GitHub Actions.

Continue reading on [how to configure GitHub actions for publishing a package to PyPI](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python#publishing-to-package-registries).

## References

* [https://packaging.python.org/en/latest/tutorials/packaging-projects/](Packaging Python Projects)