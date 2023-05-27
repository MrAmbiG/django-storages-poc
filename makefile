.PHONEY: runserver ftpup
runserver:
	python files/manage.py runserver

ftpup:
	docker compose -f storages/ftp/ftp.docker-compose.yaml up -d

ftpdown:
	docker compose -f storages/ftp/ftp.docker-compose.yaml down

s3up:
	docker compose -f storages/s3/s3.docker-compose.yaml up -d

s3down:
	docker compose -f storages/s3/s3.docker-compose.yaml down