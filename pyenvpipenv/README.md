# Pyenv + pipenv

## Steps to reproduce:

1 - Prepare the environment to [install pyenv](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)

2 - Follow [the instructions](https://github.com/pyenv/pyenv#installation) to install pyenv.

3 - Follow [the instructions](http://pipenv.readthedocs.io/en/latest/install/#installing-pipenv) to install pipenv.

4 - Create a Procfile with this content

```toml
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true

[dev-packages]

[packages]
requests = "*"

[requires]
python_version = "3.5"
```

5 - Run `pipenv install`

6 - Voilá, you have an environment with python 3.5 and requests.

![It's magic](../assets/magic.gif "It's magic")
