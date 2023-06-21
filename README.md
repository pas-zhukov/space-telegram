# Space Telegram Bot and Parser (NASA, SpaceX)

---
Телеграм-бот для автопостинга фотографий космоса от NASA и SpaceX в выбранном телеграм-канале.

Проект состоит из двух основных частей:  
- Парсеры API NASA, SpaceX
- Телеграм-бот

Можно использовать в работе только одну из них или обе.

## Установка зависимостей
Первым делом, скачайте код:
``` 
git clone https://github.com/pas-zhukov/space-telegram.git
```
Для работы скрипта понадобятся библиотеки, перечисленные в `reqirements.txt`.
Их можно установить при помощи pip:
```
pip install -r requirements.txt
```

## Получение необходимых токенов

TODO: токен телеграм-бота
TODO: токен наса

## Запуск бота

```
python main.py
```

## Использование парсера

```
from space-telegram.parsers import NASA, SpaceX
```