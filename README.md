# ThatThingILike

An app that lists things I like divided by location and tag. A tag being something like "Running Races". Can then find things I previously liked by choosing a location and tag from the dropdowns.

![Alt text](screenshot.png?raw=true "site")

## Key features
- Uses Postgres as the database
- Uses python-decouple to seperate out env variables.
- Pagination using Django's Paginator

## Environment variables required

For the database connection
- DB_HOST
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_PORT

For Django
- SECRET_KEY