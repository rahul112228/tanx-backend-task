FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

COPY . .

EXPOSE 8000

ENTRYPOINT ["conda", "run", "-n", "myenv", "bash", "/app/django.sh"]
