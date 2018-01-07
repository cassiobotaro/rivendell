# pipenv + tox

## Steps to reproduce

1 - Follow [the instructions](http://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) to install pipenv.

2 - start an empty project with clean setup.py, e.g.

setup.py

```python
#!/usr/bin/env python

from distutils.core import setup

setup(name='toxpipenv',
      version='1.0',
      description='Just some tests',
      author='Cássio Botaro',
      author_email='cassiobotaro@gmail.com',
      packages=['toxpipenv'],
      )
```

2 - add simple code and tests

toxpipenv/core.py

```python
def square(number):
    """Calculates square of a number.

    :number: a number
    :returns: square of a number

    """
    return number ** 2
```

tests/test_core.py

```python
from toxpipenv.core import square


def test_square():
    assert square(2) == 4
```

3 - Install requirements

tox

`pipenv install tox --dev`

own package

`pipenv install -e . --dev`

4 - configure tox to run using pipenv and pytest

```
[tox]
envlist = py27,py36

[testenv]
passenv = HOME
deps = pipenv
commands =
    pipenv install --dev
    pipenv run python -m pytest tests
```

5 - Voilá. Tox is configured and running two different versions of python!

`pipenv run tox`
