# Crypto bot

Данное приложение позволяет узнать стоимость криптовалюты по курсу доллара.
Для начала работы необходимо выполнить следущее:

## Зарегистрировать своего бота
Для регистрации своего бота необходимо в телеграме найти [@BotFather](https://t.me/BotFather) и выполнить все
указанные пункты для регистрации.
##Работа с приложением
### Начало работы
Приложение использует сервис [Ngrok](https://ngrok.com/docs) в качестве хостинга. Для
начала работы нужно получить ngrok auth-token и домен.

Далее нужно скопировать файл `.env.example`, перенести его в папку `CryptoBot`,
убрать из названия файла `.example` и вставить туда все необходимые переменные.

После этого остается исполнить команду из корневой директории проекта:
```shell
 sudo docker-compose --env-file ./CryptoBot/.env up --build
```
В дальнейшем при запуске ключ `--build` не понадобится.

Переходим к боту, пишем команду `/start` и пользуемся.
