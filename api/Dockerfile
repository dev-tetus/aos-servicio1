FROM alpine:3.16.0

WORKDIR /api
RUN apk update

RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN apk add python3-dev


# ENV PATH="/usr/lib/python3.10/bin/:/usr/local/lib/pyenv/versions/3.10/bin:${PATH}"

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3" , "./main.py" ]