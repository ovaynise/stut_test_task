# stuttgart_test_task

## Для запуска проекта:

1. Скопируйте проект на локальный компьютер из репозитория GutHUB
```yaml
https://github.com/ovaynise/stuttgart_test_task
```

2. Для запуска контейнеров запустите docker compose файл 
(Внимание у вас должен быть установлен докер и докер компос)
в директории где лежит docker-compose.yml:
```yaml
docker compose up --build
```
3. Выполните миграции Базы данных в директории где лежит docker-compose.yml:
```yaml
docker compose exec backend python manage.py migrate
```
7. Перезапустите контейнеры:
```yaml
docker compose stop
docker compose up
```
7. При желании создайте суперпользователя для доступа
в админку в директории где лежит docker-compose.yml::
```yaml
docker compose exec backend python manage.py createsuperuser
```
## Работа проекта:

### Эндпоинт: http://127.0.0.1:8000/api/

#### POST запрос на эндпоинт с телом
{
  "articules": "198347293"
}
где у ключа articules - значение это артикул товара , внесет запись
в базу данных с различными данными

#### GET запрос на эндпоинт без параметров
выведет всю информацию о записях в базе данных