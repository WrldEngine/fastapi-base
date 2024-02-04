.PHONY: poetry
poetry:
	poetry install
	poetry shell


.PHONY: migration
migration:
	alembic revision \
	  --autogenerate \
	  --rev-id $(shell python migrations/_get_next_revision_id.py) \
	  --message $(message)

.PHONY: migrate
migrate:
	alembic upgrade head