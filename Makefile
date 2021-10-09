up:
#	docker-compose run app alembic revision --autogenerate -m "New Migration"
#	docker-compose run app alembic upgrade head
	#docker-compose build
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
	docker-compose run app alembic revision --autogenerate -m "New Migration"

restart:
#	pipenv install 	graphql-core
#	pipenv install 	graphql-relay
#	pipenv install 	greenlet
