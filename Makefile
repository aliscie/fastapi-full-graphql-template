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