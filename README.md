# Digital Assistant server

## Installation

pip install -r requirements.txt

## Dependencies

FastAPI, MySQL, SQLAlchemy, PyJWT, bcrypt, FastAPI-Users, Pydantic

## Upgrade Database

### local

```bash
alembic revision --autogenerate -m "message"
```
### Remote
    
```bash
# upgrade
alembic upgrade head

# revert
alembic downgrade -1
```

### Notice

1. Open AI Assistant reflect to feature type
2. Open AI Thread reflect to user config
3. Open AI run reflect to user received message


start note:
`brew services start postgresql@15`