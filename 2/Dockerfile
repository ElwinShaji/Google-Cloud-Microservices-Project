FROM tiangolo/uwsgi-nginx-flask

# Create app directory
WORKDIR /usr/src/app


COPY elwin2.py .
RUN pip install requests


EXPOSE 2222
CMD [ "python", "elwin2.py" ]
