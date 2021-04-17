# spendy

This is a library that I use to clean and parse financial data from my various different bank accounts. The objective is to transform the different formats that each bank provides into a clean normalized schema for ingestion into a locally hosted database.

This also supports exporting data from the database into a [ledger-cli](https://www.ledger-cli.org/) journal format.

### Release Notes
```
1.0.0
    - initial commit
    - adds csv handlers for Ally, AMEX, Chase, and Target data exports
    - data model built out using SQLAlchemy interface
    - some work done on exporting to journal format for ledger-cli, but still some work to be done here
    - readme added
```