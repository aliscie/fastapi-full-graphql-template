up:
        docker-compose build
	docker-compose up
	docker-compose run app alembic revision --autogenerate -m "New Migration"
	docker-compose run app alembic upgrade head
	
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

more_packages:
	#pipenv install 	graphene
#	pipenv install 	graphql-core
#	pipenv install 	graphql-relay
#	pipenv install 	greenlet
