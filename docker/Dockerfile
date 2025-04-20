FROM python:3.11.12-bullseye AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip wheel "poetry==1.8.2" \
 && poetry config virtualenvs.create false \
 && poetry install --no-dev --no-interaction --no-ansi \
 \
 # Очистка кешей
 && rm -rf /root/.cache/pip /root/.cache/pypoetry \
 \
 # Удаление pip и wheel
 && rm -f /usr/local/bin/pip /usr/local/bin/pip3 \
 && rm -rf /usr/local/lib/python3.11/site-packages/pip* \
 && rm -rf /usr/local/lib/python3.11/site-packages/wheel* \
 \
 # Удаление poetry и зависимостей
 && rm -f /usr/local/bin/poetry \
 && rm -rf /usr/local/lib/python3.11/site-packages/poetry* \
 && rm -rf /usr/local/lib/python3.11/site-packages/cleo* \
 && rm -rf /usr/local/lib/python3.11/site-packages/installer* \
 && rm -rf /usr/local/lib/python3.11/site-packages/poetry_core* \
 && rm -rf /usr/local/lib/python3.11/site-packages/p*poetry* \
 \
 # На всякий случай — удалить __pycache__ и .pyc
 && find /usr/local/lib/python3.11/site-packages -type d -name '__pycache__' -exec rm -r {} + \
 && find /usr/local/lib/python3.11/site-packages -name '*.pyc' -delete \
 \
 # Удаление man, gcc, libc-dev, curl
 && apt-get update  \
 && apt-get remove -y man gcc libc-dev curl  \
 && apt-get autoremove -y \
 && apt-get clean \
 \
 # Финальный сброс кешей
 && rm -rf /root/.cache


FROM python:3.11.12-bullseye

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN useradd -m myuser
USER myuser

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /app /app
COPY app /app

CMD ["python", "main.py"]