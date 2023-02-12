# Yatube API

**Привет, меня зовут Алексей. Представляю проект Yatube API - интерфейс социальной сети.**

### О проекте

Проект выполнен на Django REST в рамках обучения.
Приложение "api" реализует архитектуру взаимодействия с моделями постов. 
В проекте реализованы подписки на авторов, добавление комментариев и присвоение групп для публикаций. Есть возможность обмена изображениями для добавления к публикациям.

**Срок действия токена 1 день.**


## Развернуть проект

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
Посты:  `.../api/v1/posts/`
Группы:  `.../api/v1/groups/`
Подписки:  `.../api/v1/follow/`
Комментарии:  `.../api/v1/posts/{post_id}/comments/` 
### Лицензия: BSD License
<br>

### Благодарности:

> Благодарю команду Яндекса за помощь в обучении и разработке проекта.
> Отдельное спасибо Валерию Щепаку и Алексею Фролову за вклад в решение
> ошибок и оптимизацию (рефакторинг) кода.

<br>

### Мои контакты:

email: satangeremy@icloud.com
telegram: @qartjackie 
[QartJackie    (Alexey Kravtsov) (github.com)](https://github.com/QartJackie)
