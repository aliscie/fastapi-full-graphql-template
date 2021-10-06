up:
	docker-compose run app alembic revision --autogenerate -m "New Migration"
	docker-compose run app alembic upgrade head
	docker-compose build
	docker-compose up
down:
	docker-compose down
test:
	pytest test

run:
	uvicorn main:app --reload

init_db:
	alembic init alembic

migrate:
	docker-compose run app alembic revision --autogenerate -m "New Migration"

restart:
	#pipenv install 	black
	#pipenv install 	graphene
	#pipenv install 	graphene-sqlalchemy
#	pipenv install 	graphql-core
#	pipenv install 	graphql-relay
#	pipenv install 	greenlet
	pipenv install 	h11
	pipenv install 	Mako
	pipenv install 	MarkupSafe
	pipenv install 	mypy-extensions
	pipenv install 	pathspec
	pipenv install 	promise
	pipenv install 	psycopg2
	pipenv install 	pycparser
	pipenv install 	pydantic
	pipenv install 	PyJWT
	pipenv install 	python-dateutil
	pipenv install 	python-dotenv
	pipenv install 	python-editor
	pipenv install 	regex
	pipenv install 	Rx
	pipenv install 	singledispatch
	pipenv install 	six
	pipenv install 	SQLAlchemy
	pipenv install 	starlette
	pipenv install 	toml
	pipenv install 	typing-extensions
