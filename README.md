# Glowing Remarks server

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


