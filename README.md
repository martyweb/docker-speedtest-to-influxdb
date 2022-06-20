# docker: speedtest-cli to Influxdb

This is a docker image to run the [speedtest-cli commandline tool](https://github.com/sivel/speedtest-cli)
for benchmarking ISP performance and send results to [InfluxDB](https://www.influxdata.com/)

### Build from docker file

If you want to build the docker container image yourself you can do so with the
following commands:

```bash
git clone https://github.com/martyweb/docker-speedtest-to-influxdb.git
cd docker-speedtest-to-influxdb
sudo docker build -t docker-speedtest-to-influxdb .
```

### Running the command line tool

Run the container:

```bash
sudo docker run --name docker-speedtest-to-influxdb \
-e influxdbhost="<ip>" \
-e influxdbusername="<username>" \
-e influxdbpass="<password>" \
 docker-speedtest-to-influxdb
```