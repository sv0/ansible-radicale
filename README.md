Radicale Ansible role v. 0.0.4
==============================
[![CI](https://github.com/sv0/ansible-radicale/actions/workflows/ci.yml/badge.svg)](https://github.com/sv0/ansible-radicale/actions/workflows/ci.yml)

- [Getting Started](#getting-started)
  - [Prerequisities](#prerequisities)
  - [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Authors](#authors)
- [License](#license)
- [Useful links](#useful-links)


## Getting Started

This ansible role installs **radicale**  CalDAV (calendars, to-do lists) and CardDAV (contacts) server.

It has been tested for the following Linux distributions:

* Debian Buster
* Debian Bullseye
* Debian Bookworm


### Prerequisities

Ansible 2.12 version installed.


### Installing

    ansible-galaxy role install sv0.radicale


## Usage

### Variables

Look at [defaults](defaults/main.yml) variables file to see the
possible configuration properties.

    # specify host domain where CalDAV/CardDAV service will be accessible
    radicale_domain: "cal.example.eu"


## Testing

    molecule test


## Authors

- [Slavik Svyrydiuk](https://slavik.svyrydiuk.eu)


## Useful links

- [Radicale. Free and Open-Source CalDAV and CardDAV Server](https://radicale.org/v3.html)
