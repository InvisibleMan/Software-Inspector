Большинство шагов нужно проделать один раз и больше ничего не трогать. Только забирать последнюю версию!

I. Установка Django

	1. Качаем Python. Подходит версия от 2.4 до 2.7 (Лучше взять эту: http://www.python.org/download/releases/2.6.5/)
	2. Устанавливаем Python (Лучше сразу в переменные среды добавить путь к исполняемому файлу).
	3. Качаем Django. Последняя версия здесь: http://www.djangoproject.com/download/
		(Например эта: http://media.djangoproject.com/releases/1.2/Django-1.2.1.tar.gz)
	4. Устанавливаем Django. Распаковываем tar-архив. Заходим в распакованную папку и даем команду: python setup.py install 
		

II. Забираем последнюю версию кода

	1. Качаем Git (http://git-scm.com/download). Для винды есть две версии: с GUI (http://code.google.com/p/tortoisegit/) и без (http://code.google.com/p/msysgit/).
		Я рекомендую без GUI и portable: http://code.google.com/p/msysgit/downloads/detail?name=PortableGit-1.7.0.2-preview20100309.7z
	2. Распаковываем и запускаем git-bash.bat
	3. Переходим в каталог (если он не создан) в котором будет лежать репозиторий у меня это ...../src
	4. Даем команду: git clone git://github.com/InvisibleMan/Software-Inspector.git trunk (теперь у тебя есть код последней версии проекта!)
	5. Настраиваем проект. Для этого копируем файл .setup/mysettings.py в директорию settings и правим настройки.
		Будем использовать базу SqlLite, файл с настройками примерно выглядит так:
		
		DATABASE_ENGINE = 'django.db.backends.sqlite3'
		DATABASE_NAME = 'c:/soft/src/db/sqlite3.db' 
		TEMPLATE_DIRS = 'c:/soft/src/trunk/templates'
		STATIC_DOC_ROOT = 'd:/soft/src/trunk//templates/styles'
		Примечание: директория c:/soft/src/db/ должна существовать!
		
III. Стандрартный порядок работы
	1. Забираем последнюю версию из репозитория:
	git pull в директории проекта (по у молчанию источник git://github.com/InvisibleMan/Software-Inspector.git)
	2. Обнволяем базу:
	python manage.py syncdb
	3. Запускаем сервер:
	python manage.py runserver
	
Больше информации см. Здесь:
	http://docs.djangoproject.com/en/1.2/