# Locals.org test task
## Описание

Разработать API для мини-аукциона котиков/ёжиков. Пользователи делают ставки на интересующие их лоты. 

### Необходимые модели

- **Пользователь**, поля:
    - баланс денежных средств
- **Котик и Ёжик**, поля:
    - порода
    - кличка
    - владелец (пользователь)
- **Лот,** поля**:**
    - ссылка на котика или ёжика
    - цена
    - владелец (пользователь)
- **Ставка**, поля:
    - значение ставки
    - автор ставки (пользователь)

### Функциональность

1. Пользователи выставляют лоты на продажу
2. Другие пользователи могут сделать ставку на лот
3. Автор лота принимает одну любую ставку

Готовое решение обернуть в docker compose и выложить на github/bitbucket/<что_то_еще>

### Технологии:

- Django/DRF/PostgreSQL
- Docker compose

# Pre-requisites
First thing to do is to install the docker compose:
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
In case of a key error run the following command and then run the installation command again: 
```
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```
# Running the app
To run the app, first thing is to do is to create the migrations and the to migrate:
```
sudo docker-compose run web python manage.py makemigrations
sudo docker-compose run web python manage.py migrate
```
Then, the docker compose can do its job:
```
docker compose up
```
# Possible problems and fixes for them
If there's a problem with the access to the local files (since the files the container creates belong to root), try giving the current user the required privileges: 
```
sudo chown -R $USER:$USER src
```

If there's a database access error due to the default sqlite was changed for the postgres, try running these commands:
```
sudo docker-compose run web python manage.py migrate --fake sessions zero
sudo docker-compose run web python manage.py migrate --fake-initial
```
