FROM python:3.11.6
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./src /code/src
CMD ["fastapi", "run", "src/gpac_api/app/main.py", "--port", "80"]
