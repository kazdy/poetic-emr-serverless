setup:
	poetry 
	poetry config virtualenvs.in-project true
	poetry enc use python3.7
	poetry install

test:
	poetry run pytest tests/

bundle-venv:
	rm -rf poeticemrbundle
	poetry bundle venv poeticemrbundle --without dev
	tar -czvf poeticemrbundle.tar.gz -C $(shell pwd)/poeticemrbundle .
	rm -rf poeticemrbundle

pww:
	pwd