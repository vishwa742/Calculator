FROM python:3.7

COPY . /web
WORKDIR /web
RUN pip install -r ./requirements.txt
ENTRYPOINT ["python"]
#CMD ["/web/Database/sqlite_create.py"]
CMD ["/web/Database/sqlAlchemy.py"]





#WORKDIR /web
#WORKDIR /web
