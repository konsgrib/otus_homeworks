# Блог ни о чём.
Реализована возможность 
- Добавлять, отображать, редактировать, удалаять пользователя
- Добавлять, отображать, отображать, редактировать, удалаять посты от имени пользователя
- Добавлять, отображать, удалаять комментарии к постам от имени пользователя

Так же реализована возможность поиска всех постов созданных конкретным автором и связаных с ними комментариев.

Для успешной работы необходимо уствновить зависимости.
```python
pip install -r requirements.txt
```

Далее нужно подготовить базу данных запустив сначала команду
```bash
docker-compose up -d pg
```
а затем:
```python
python make_db.py
```
Эти команды создадут докер контейнер и развернут в нем постгрес базу данных, попутно заполнив её тестовыми данными.

Программа запускается 
```python
python main.py
```
Функция "main" Содержит в себе вызовы функций. Можно раскомментировать их все.

```python
def main():
    session = get_session()
    # user_crud.create_user(session, "test.user2@test.com", "password123")
    user = user_crud.get_user(session, "test.user2@test.com")
    # print(user.password)
    # user_crud.delete_user(session, "test.user2@test.com")
    # fields = {"password": "NewPassword121", "is_active": False}
    # user_crud.update_user(session, "test.user2@test.com", **fields)
    # article_crud.create_article(
    #     session,
    #     "Yet Another Title",
    #     "Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blahLorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah,Lorem ipsum blah blah blah",
    #     user,
    # )
    # print(article_crud.get_article_by_id(session, 1))
    # print(article_crud.get_articles_by_user(session, user))
    # print(comment_crud.get_comments_by_user(session, user))
    print(user_crud.get_user_articles_comments(session, user.email))
    session.close()
```



Основной функционал покрыт юнит тестами
Юнит тесты можно запустить так:
```python
pytest -v
```
На время тестирования будет созданна тестовая база данных на движке sqlite3.
Для каждого теста база данных будет пересоздаваться и удалится по завершении тестов.

тестовые данные можно постотреть в файле: make_db.py

Предназначение файлов
- *_crud.py
    - Файлы, описывающие операции уровня ДБ 
- models.py
    - Содержит описание классов User, Article, Comment
- test_crud.py
    - Юнит тесты
- utils.py
    - Содержит утилиты хеширования и валидации паролей
- database.py
    - Отвечает за генерацию сессий 


