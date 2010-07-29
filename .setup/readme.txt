����������� ����� ����� ��������� ���� ��� � ������ ������ �� �������. ������ �������� ��������� ������!

I. ��������� Django

	1. ������ Python. �������� ������ �� 2.4 �� 2.7 (����� ����� ���: http://www.python.org/download/releases/2.6.5/)
	2. ������������� Python (����� ����� � ���������� ����� �������� ���� � ������������ �����).
	3. ������ Django. ��������� ������ �����: http://www.djangoproject.com/download/
		(�������� ���: http://media.djangoproject.com/releases/1.2/Django-1.2.1.tar.gz)
	4. ������������� Django. ������������� tar-�����. ������� � ������������� ����� � ���� �������: python setup.py install 
		

II. �������� ��������� ������ ����

	1. ������ Git (http://git-scm.com/download). ��� ����� ���� ��� ������: � GUI (http://code.google.com/p/tortoisegit/) � ��� (http://code.google.com/p/msysgit/).
		� ���������� ��� GUI � portable: http://code.google.com/p/msysgit/downloads/detail?name=PortableGit-1.7.0.2-preview20100309.7z
	2. ������������� � ��������� git-bash.bat
	3. ��������� � ������� (���� �� �� ������) � ������� ����� ������ ����������� � ���� ��� ...../src
	4. ���� �������: git clone git://github.com/InvisibleMan/Software-Inspector.git trunk (������ � ���� ���� ��� ��������� ������ �������!)
	5. ����������� ������. ��� ����� �������� ���� .setup/mysettings.py � ���������� settings � ������ ���������.
		����� ������������ ���� SqlLite, ���� � ����������� �������� �������� ���:
		
		DATABASE_ENGINE = 'django.db.backends.sqlite3'
		DATABASE_NAME = 'c:/soft/src/db/sqlite3.db' 
		TEMPLATE_DIRS = 'c:/soft/src/trunk/templates'
		STATIC_DOC_ROOT = 'd:/soft/src/trunk//templates/styles'
		����������: ���������� c:/soft/src/db/ ������ ������������!
		
III. ������������ ������� ������
	1. �������� ��������� ������ �� �����������:
	git pull � ���������� ������� (�� � �������� �������� git://github.com/InvisibleMan/Software-Inspector.git)
	2. ��������� ����:
	python manage.py syncdb
	3. ��������� ������:
	python manage.py runserver
	
������ ���������� ��. �����:
	http://docs.djangoproject.com/en/1.2/