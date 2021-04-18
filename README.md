# spendy
![build](https://github.com/timhealz/spendy/actions/workflows/main.yml/badge.svg)
[![codecov](https://codecov.io/gh/timhealz/spendy/branch/main/graph/badge.svg)](https://codecov.io/gh/timhealz/spendy)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This is a library that I use to clean and parse financial data from my various different bank accounts. The objective is to transform the different formats that each bank provides into a clean normalized schema for ingestion into a locally hosted database.

This also supports exporting data from the database into a [ledger-cli](https://www.ledger-cli.org/) journal format.