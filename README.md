# Data Modeling with Postgres
---

### Project for Udacity's Data Engineering Nanodegree

### By Raul Morales Delgado.

## Objective
The objective of this project is to model user activity data to create a database and ETL pipeline in Postgres and Python for a music streaming app.

## Scope
In this project, data from two different sources — namely, song data and log data — from a fictional company, Sparkify, will be modeled into a STAR schema facilitate downstream analytics user behavior. To do so, a database schema will be created based on fact and dimension tables, and a an ETL pipeline will be develop to ingest and normalize their data.

## Schema
As stated above, a STAR schema has been chosen for this database's schema design. Given the requirement by Sparkify to be able to simplify queries related to user behavior — e.g. what they are listening —, and given the proposed tables that they would be needing — one fact table with songs played and several dimensional ones with user, artist and so on data — a STAR schema solution satisfies the problem's contraints.

The STAR schema proposed for this database is shown below.

![ERD — STAR Schema](https://github.com/XXXXXXXX "Entity Relationship Diagram — STAR Schema")

## ETL Pipeline


## Project Structure
The structure of this project is depicted in the following directory tree:
```text
.
├── data
│   ├── log_data
│   └── song_data
├── extras
│   └── ERD.png
├── main.py
├── notebooks
│   ├── etl.ipynb
│   └── test.ipynb
├── README.md
└── src
    ├── create_tables.py
    ├── etl.py
    ├── __init__.py
    └── sql_queries.py
````

The `data` directory contains the data files of both songs and logs. `extras` contains ancillary files for this README.md. `main.py` is a bootstrap to run the entire pipeline, which includes the creation of the database, table, connection to the database, and the ETL processes as well.

The `notebooks` directory contains the Jupyter notebooks of this project and, finally, the `src` directory contains the Python modules upon which the entire process happens.


## Run Local
To run this project locally, clone this repository and start a local Postgres server. Then run:
```bash
python3 main.py
````

