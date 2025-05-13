FROM seleniarm/standalone-chromium:latest

USER root

WORKDIR /app
COPY . .

RUN apt update && apt install -y python3-pip

RUN pip install --upgrade pip --break-system-packages
RUN pip install --break-system-packages -r requirements.txt

CMD ["python3", "-m", "pytest"]