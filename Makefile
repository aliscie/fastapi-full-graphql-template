up:
	#docker-compose build
	#docker-compose up -d
	docker-compose up

down:
	docker-compose down

test:
	pytest test

run:
	uvicorn core.main:app --reload

init_db:
	alembic init alembic

migrate:
	docker-compose run app alembic upgrade head
	docker-compose run app alembic revision --autogenerate -m "New Migration"

makemigratoins:
	alembic revision -m 'init'

restart:
	#pipenv install 	graphene
#	pipenv install 	graphql-core
#	pipenv install 	graphql-relay
#	pipenv install 	greenlet
