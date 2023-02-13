# Yatube API

  
  

**Привет, меня зовут Алексей. Представляю проект Yatube API - интерфейс социальной сети.**

  

### О проекте

  
**Стек:**

 ![Python version](https://img.shields.io/badge/Python-3.7.16-yellow)  ![SQLite version](https://img.shields.io/badge/SQlite-3-lightgrey) ![Django: 3.2.16 (shields.io)](https://img.shields.io/badge/Django-3.2.16-yellowgreen) ![Django REST Framework: 3.12.4 (shields.io)](https://img.shields.io/badge/Django%20REST%20Framework-3.12.4-yellowgreen)  ![Simple JWT: 4.7.2 (shields.io)](https://img.shields.io/badge/Simple%20JWT-4.7.2-lightgrey) ![Djoser: 2.1.0 (shields.io)](https://img.shields.io/badge/Djoser-2.1.0-blue) ![JSON: (shields.io)](https://img.shields.io/badge/JSON-%20-lightgrey) ![BASE: 64 (shields.io)](https://img.shields.io/badge/BASE-64-yellow)
<br>

  

**Описание**

  API спроектирован на основе REST архитектуры.

Приложение "api" реализует архитектуру взаимодействия с моделями постов.
В проекте реализованы подписки на авторов, добавление комментариев и присвоение групп для публикаций. Есть возможность обмена изображениями при добавлении к публикациям.

Авторизация реализована через доступ по JWT токену.

**Срок действия токена 1 день.**

<hr>  

<br>

## Развернуть проект

<br>

**Команды актуальны для Git Bash/OS Windows**

  

Установка виртуального окружения :

  

  

	python -m venv venv

  

  

Активация виртуального окружения :

  

  

	source venv/Scripts/activate

  

  

В requirements добавлены все нужные для работы библиотеки.:

  

  

	pip install --upgrade pip

	pip install -r requirements.txt

  

  

Применение миграций:

  

  

	python manage.py migrate

  

Старт сервера разработки:

  

	python manage.py runserver

  

<br>

  

## Эндпоинты и доступы

  

**Аутентификация**

	Получить jwt токен: .../api/v1/jwt/create/
	Обновить jwt токен: .../api/v1/jwt/refresh/
	Проверить jwt токен: .../api/v1/jwt/verify/

  

**Список доступных эндпоинтов:**

<br>

    Посты: `.../api/v1/posts/`

<br>

    Группы: `.../api/v1/groups/`

<br>

    Подписки: `.../api/v1/follow/`

<br>

    Комментарии: `.../api/v1/posts/{post_id}/comments/`

  
<hr>
### Лицензия: BSD License

<hr>
<br>
  

### Благодарности:

  

> Благодарю команду Яндекса за помощь в обучении и разработке проекта.

> Отдельное спасибо Валерию Щепаку и Алексею Фролову за вклад в решение
> ошибок и оптимизацию (рефакторинг) кода.

<br>

### Мои контакты:

email: satangeremy@icloud.com
<br>
telegram: @qartjackie
<br>
[QartJackie (Alexey Kravtsov) (github.com)](https://github.com/QartJackie)
