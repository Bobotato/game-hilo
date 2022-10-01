FROM postgres:alpine

ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB hilo

COPY init.sql /docker-entrypoint-initdb.d/

EXPOSE 1337
