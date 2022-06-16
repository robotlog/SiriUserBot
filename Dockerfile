# thx friday | please give credit | do not delete this line#

FROM python:3.9
WORKDIR .
ENV PYTHONUNBUFFERED=1

# Çalışma dizinine gereksinimleri kopyala ve yükle
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Çalışma dizinine yükleyiciyi kopyala ve çalıştır
COPY startup.sh .
RUN bash startup.sh
COPY . .
# Ve başlat
CMD ["python3", "-m", "userbot"]
