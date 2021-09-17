# Change Log

All notable changes will be documented in this file.

## Head

## 0.7.7 &ndash; 2021-09-20

## 0.7.6 &ndash; 2021-09-02

## 0.7.5 &ndash; 2021-08-08

## 0.7.4 &ndash; 2021-07-20

## 0.7.3 &ndash; 2021-07-06

## 0.7.2 &ndash; 2021-06-20

## 0.7.1 &ndash; 2021-05-30

### Added

* The `roq-fix-bridge` role

### Removed

* The `influxdb` and `roq-influxdb` roles

## 0.7.0 &ndash; 2021-04-15

## 0.6.1 &ndash; 2021-02-19

### Changed

* Service names now matching binaries

  * `clickhouse-server`
  * `redis-server`

## 0.6.0 &ndash; 2021-02-02

### Changed

* All Roq services now use `flags` (instead of `options`)
* Using Miniforge3

* Added

  * roq-tools
  * roq-kafka

### Removed

* gogs
* teamcity
* virtualbox
* vagrant

## 0.5.0 &ndash; 2020-12-04

### Changed

* Deribit

  * Now excluding all USDT symbols by default.
    The reason for this is that some symbols cause failure on
    market data subscription, e.g. BTC-USDT-VIX.

* Directory changes to match Linux' FSH

  * /opt/conda -- Miniconda3
  * /usr/local/etc -- configurations
  * /run/roq -- unix sockets
  * /var/lib/roq -- event-logs

* Ubuntu 20.04 support

  * using python3/pip3 instead of python/pip

### Removed

* roq-simulator

* chrony

## 0.4.5 &ndash; 2020-11-09

### Changed

* Add publish port (Docker) for the redis systemd service

### Added

* roq-clickhouse
* roq-redis

## 0.4.4 &ndash; 2020-09-20

### Changed

* All gateways are now installed by re-using common tasks and templates

## 0.4.3 &ndash; 2020-09-02

### Changed

* NGINX config has been simplified
* As a result of removing the Postgres dependency:
  * Grafana now uses sqlite3
  * Gogs now uses sqlite3
  * TeamCity now uses HSQLDB

### Added

* ClickHouse as a new (experimental) time-series database

### Removed

* The following roles have been removed
  * certbot
  * fail2ban
  * netdata
  * nexus
  * sshd
  * sysadmin
  * sysstat
* The Postgres dependency was removed due to hard-to-automate complexities
  around database upgrades

## 0.4.2 &ndash; 2020-07-27

## 0.4.1 &ndash; 2020-07-17

## 0.4.0 &ndash; 2020-06-30

## 0.3.9 &ndash; 2020-06-09

## 0.3.8 &ndash; 2020-06-06

### Changed

* Documentation has been reviewed

## 0.3.7 &ndash; 2020-05-27

### Changed

* Gateway options (flags) haved been simplified (by removing artificial data structures)

## 0.3.6 &ndash; 2020-05-02

## 0.3.5 &ndash; 2020-04-22

## 0.3.4 &ndash; 2020-04-08

## 0.3.3 &ndash; 2020-03-04
