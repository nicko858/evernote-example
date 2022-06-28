# Укрощаем Evernote

Проект представляет собой набор программ для автоматизации работы с сервисом заметок [evernote](https://evernote.com/intl/ru)
Текущий функционал позволяет:
 - Создавать заметки по шаблону
 - Получать список блокнотов с заметками
 - Получать текст всех заметок из блокнота

## Предварительные требования

`Python2` должен быть установлен на компьютере 

## Как установить и настроить проект

Помимо "боевой среды", сервис предоставляет возможность работать в тестовой среде(песочнице).  
Нужно определиться на какой из них вы будете работать.

`sandbox.evernote.com` - песочница  
`www.evernote.com` - боевая среда

1) Зарегистрируйтесь на сайте [evernote](https://evernote.com/intl/ru) или используйте существующую учетную запись
2) Сгенерируйте api-ключ по [ссылке](https://dev.evernote.com/#apikey). Вы получите `consumer key` и `consumer secret` 
3) Получите auth-токен по [ссылке](https://dev.evernote.com/get-token/). Тут нужно будет выбрать в какой среде будем создавать auth-токен

4) Скачайте код проекта, создайте виртуальное окружение и установите зависимости:
   
   ```bash
        git clone https://github.com/nicko858/evernote-example.git
        cd evernote-example
        virtualenv --python=$(which python2) venv
        . venv/bin/activate
        pip install -r requirements.txt
   ```
5) В корне проекта создайте файл `.env` со следующим содержимым:  
   
   ```bash
        EVERNOTE_CONSUMER_KEY=<consumer key, полученный на 2м шаге>
        EVERNOTE_CONSUMER_SECRET=<consumer secret, полученный на 2м шаге>
        EVERNOTE_PERSONAL_TOKEN=<auth-токен, полученный на 3м шаге>
        JOURNAL_TEMPLATE_NOTE_GUID=
        JOURNAL_NOTEBOOK_GUID=
        INBOX_NOTEBOOK_GUID=
        SANDBOX=<Укажите признак песочницы. False или True>
   ```
   Остальные переменные заполним на следующем шаге.

6) В веб-интерфейсе `evernote`, создайте тестовую заметку с произвольным содержимом. Она будет использоваться как шаблон.
   
7) Запустите скрипт `list_notebooks.py`. В выводе вы должны увидеть guid блокнота и guid заметок этого блокнота. 
   
    ```bash
        (venv) nicko@nicko-Laptop:~/Yandex.Disk/devman_new/evernote-example$ python list_notebooks.py 
        5510f791-66c9-46be-8f30-4bb16cc27db5 - Первый блокнот
        Список заметок - ['448ae3ba-22df-42fd-a798-81a6b29b6fc7']
    ```
Здесь мы видим guid тестовой заметки созданной на 6м шаге.

8) Заполним остальные переменные `.env`:
   
   ```bash
        JOURNAL_TEMPLATE_NOTE_GUID=<guid тестовой заметки из 7го шага>
        JOURNAL_NOTEBOOK_GUID=<guid блокнота из 7го шага>
        INBOX_NOTEBOOK_GUID=<guid блокнота из 7го шага>
   ```

## Описание программ

### config.py

Читает `.env`-файл проекта и возвращает словарь с необходимыми переменными.


### list_notebooks.py

Выводит список блокнотов и их заметок. Пример запуска:  

```bash
    (venv) nicko@nicko-Laptop:~/Yandex.Disk/devman_new/evernote-example$ python list_notebooks.py 
    5510f791-66c9-46be-8f30-4bb16cc27db5 - Первый блокнот
    Список заметок - ['448ae3ba-22df-42fd-a798-81a6b29b6fc7']
```

### add_note2journal.py

Создает точную копию заметки из заметки-шаблона. См. переменные `JOURNAL_TEMPLATE_NOTE_GUID`, `JOURNAL_NOTEBOOK_GUID`. Пример запуска: 

```bash
    (venv) nicko@nicko-Laptop:~/Yandex.Disk/devman_new/evernote-example$ python add_note2journal.py 
    Title Context is:
    {
        "date": "2022-06-26", 
        "dow": "воскресенье"
    }
    Note created: Заметка Николая
    Done
```

### dump_inbox.py

Выводит текст всех заметок из блокнота. См. переменную `INBOX_NOTEBOOK_GUID`. Пример запуска:

```bash
    (venv) nicko@nicko-Laptop:~/Yandex.Disk/devman_new/evernote-example$ python dump_inbox.py 

    --------- 1 ---------


    ТестТестТест

    --------- 2 ---------


    ТестТестТест

```