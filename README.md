# Money-bot
[![Build Status](https://travis-ci.com/summer-school-2019/money-bot.svg?branch=develop)](https://travis-ci.com/summer-school-2019/money-bot)

Основная ветка - develop.

### Конфигурация 
Для того, чтобы задать конфигурационные параметры для локального использования:
1. `cp example_config.py local_config.py`
2. Редактируем *local_config.py*

Словами:
Создаем новый файл *local_config.py*, в него копируем все из *example_config.py*, меняем
*local_config.py* 

## Code check 
Run from the root of the project
1. ```black money_bot```. Чек код стайла
2. ```isort -rc money_bot```. Чек импортов
3. ```pylint money_bot ```. Чек всего

Перед мержем ваших изменений, в пулл реквесте будет отмечено, пройдены ли эти проверки вашим кодов, или нет.



## Для добавления изменений: 
1. Создаем новую ветку `git branch new_cool_feature`
2. Переходим на нее `git checkout new_cool_feature`
3. Делаем классные коммиты просто `git commit`
4. После всех коммитов заливаем на гитхаб с помощью `git push origin new_cool_feature`
5. Делаем Pull request на гитхабе. Мержим из вашей ветки в develop

## Downloading on local pc:
1. `git clone git@github.com:summer-school-2019/money-bot.git`
2. `python3.7 -m virtualenv .venv` Создаем новое окружение. Возможно, у вас на пк нужно заменить на
`python3 -m virtualenv .venv`
3. `source .venv/bin/activate` - *nix
   `.venv/bin/activate.exe` - windows (но это не точно)
4. `pip install -r requirements.txt`

## Prerequirements

### Black
Сам отформатирует ваш код. После установки заходим в 
`Tools -> External Tools -> Black/isort`
 
Инструкция по установке black:
[here](https://github.com/psf/black#pycharmintellij-idea) 

![black config](https://i.ibb.co/cgnr7Cr/image.png)


### Isort
Сам отсортирует импорты.


![isort config](https://i.ibb.co/sVn0MFT/image.png)
