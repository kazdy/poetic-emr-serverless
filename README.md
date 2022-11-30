# poetic-emr-serverless

## prerequisites
install poetry: https://python-poetry.org/docs/#installation  
install poetry bundle plugin: https://github.com/python-poetry/poetry-plugin-bundle  

::: note  
you must use python 3.7.10 and amazon linux 2 for this to work with emr 6.9 .  
:::

`make install` - installs dependencies

`make test` - run tests

`make bundle` - bundle venv (only non-dev dependencies) and package to tar.gz, creates poeticemrbundle.tar.gz similar to venv-pack but with content of poematic_emr_serverless dir as a python package, no need to provide it additionally as .zip file!

see `./Makefile` for implementation details


Run as if you'd use venv-pack.  
entrypoint.py - main entrypoint file   
poeticemrbundle.tar.gz - upload to s3 and use as if it was created via venv-pack   