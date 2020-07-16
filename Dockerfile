FROM python:3
ENV influxdbhost=""
ENV influxdbport="8086"
ENV influxdbusername=""
ENV influxdbpass=""
ENV influxdbdatabase="speedtest"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/usr/local/bin/speedtest-cli --json"]

COPY . .
CMD python ./getWeather.py --influxdbhost $influxdbhost --influxdbport $influxdbport --influxdbusername $influxdbusername --influxdbpass $influxdbpass --influxdbdatabase $influxdbdatabas

