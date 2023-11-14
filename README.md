Radicale Ansible role
=====================

This ansible role installs **radicale**  CalDAV (calendars, to-do lists) and CardDAV (contacts) server.

It has been tested for the following Linux distributions:

* Debian Buster
* Debian Bullseye
* Debian Bookworm


- [Getting Started](#getting-started)
  - [Prerequisities](#prerequisities)
  - [Installing](#installing)
- [Usage](#usage)
- [Testing](#testing)
- [Authors](#authors)
- [License](#license)
- [Useful links](#useful-links)


## Getting Started


### Prerequisities

Ansible 2.12 version installed.


## Usage

Look at [defaults](defaults/main.yml) variables file to see the
possible configuration properties.


### Variables

    radicale_domain: "cal.example.eu"  # domain where CalDAV/CardDAV service will be accessible


## Testing

    molecule test


## Authors

- [Slavik Svyrydiuk](https://slavik.svyrydiuk.eu)

## Useful links

- [Radicale. Free and Open-Source CalDAV and CardDAV Server](https://radicale.org/v3.html)
