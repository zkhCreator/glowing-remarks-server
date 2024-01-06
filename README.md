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

### Target

- [ ]增加聊天的能力
    - [ ] 增加 2 层的能力，一定用户定义，一层表达。
    - [ ] 数据结构
        - [ ] 
- [ ]在聊天的基础上，增加 views 生成的能力
- [ ]在 views 的基础上，chat 对于 view 的关联能力。
- [ ]测试 gpt4 对于意图的理解，gpt3.5 对于数据的解析能力
- [ ]建立 benchmark 能力