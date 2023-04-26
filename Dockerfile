FROM python:3.9-slim

COPY . /home

WORKDIR /home/scripts/

RUN apt-get update && \
    apt-get upgrade -y && \
    python3 -m pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 8501

ENTRYPOINT streamlit run main.py