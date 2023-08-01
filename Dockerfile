FROM apache/airflow:2.6.3
USER airflow
RUN pip install --upgrade pip
RUN pip install klym-telemetry==0.1.10
RUN pip install importlib-metadata==4.13.0
