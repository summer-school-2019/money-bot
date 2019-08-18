# Money-bot
Основная ветка - develop.

### Конфигурация 
Для того, чтобы задать конфигурационные параметры для локального использования:
1. `cp example_config.py local_config.py`
2. Редактируем *local_config.py*

Словами:
Создаем новый файл *local_config.py*, в него копируем все из *example_config.py*, меняем
*local_config.py* 

## Для добавления изменений: 
1. Создаем новую ветку `git branch new_cool_feature`
2. Переходим на нее `git checkout new_cool_feature`
3. Делаем классные коммиты просто `git commit`
4. После всех коммитов заливаем на гитхаб с помощью `git push origin new_cool_feature`
5. Делаем Pull request на гитхабе. Мержим из вашей ветки в develop

## Downloading on local pc:
1. `git clone git@github.com:summer-school-2019/money-bot.git`
2. `python3.7 -m virtualenv .venv` Создаем новое окружние. Возможно, у вас на пк нужно заменить на
`python3 -m virtualenv .venv`
3. `source .venv/bin/activate` - *nix
   `.venv/bin/activate.exe` - windows (но это не точно)
 
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
