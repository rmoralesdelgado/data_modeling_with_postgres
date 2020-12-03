# Data Modeling with Postgres

### Project for Udacity's Data Engineering Nanodegree
By Raul Morales Delgado.

## Objective
The objective of this project is to model user activity data to create a database and ETL pipeline in Postgres and Python for a music streaming app.

## Scope
In this project, data from two different sources — namely, song data and log data — from a fictional company, Sparkify, will be modeled into a STAR schema to facilitate downstream analytics user behavior. To do so, a database schema will be created based on fact and dimension tables, and an ETL pipeline will be develop to ingest, normalize their data and load it back to the database.

## Schema
As stated above, a STAR schema has been chosen for this database's schema design. Given the requirement by Sparkify to be able to simplify queries related to user behavior — e.g. what they are listening —, and given the proposed tables that they would be needing — one fact table with songs played and several dimensional ones with user, artist and so on data — a STAR schema solution satisfies the problem's contraints.

The STAR schema proposed for this database is shown below.

<img src='https://github.com/rmoralesdelgado/data_modeling_with_postgres/blob/main/extras/ERD.png' alt="ERD — STAR Schema" width=700>

## ETL Pipeline
In this section, the ETL pipeline will be explained.

### Creation of database
The first step in this pipeline is dropping a previously existing `sparkifydb` database and creating a new one. This process is described in `src/create_tables.py`'s `create_database` function.

### Creation of schema
The next step consists on creating the schema. This STAR schema consists of five tables — one fact and four dimensional ones. First, any preexisting tables are dropped and then a new set is created.

This process is described in `src/create_tables.py`'s `create_tables` and `drop_tables` functions.

### ETL
The ETL processes are described in `src/etl.py`. From a high-level, this module defines functions to extract the data from the data files and transforms these data for each of the tables previously mentioned.

Finally, the transformed data is loaded back into the tables at `sparkifydb` database.

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
To run this project locally, clone this repository and start a local Postgres server. 

Then, run:
```bash
python3 main.py
````

The `main.py` file will create the database, schema and run the ETL pipeline. 
