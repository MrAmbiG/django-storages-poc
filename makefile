.PHONEY: runserver ftpup
runserver:
	python files/manage.py runserver

ftpup:
	docker compose -f storages/ftp/ftp.docker-compose.yaml up -d

ftpdown:
	docker compose -f storages/ftp/ftp.docker-compose.yaml down