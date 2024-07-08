<h1 align="center">
  <br>
  <b>SQLite TIA Portal ETL</b>
  <b>By: Luis Enrique</b>
  <br>
</h1>

<p align="center">
  ETL for SQLite database from tia portal program</a>.
  <br>
</p>


## Description

ETL for SQLite database from tia portal program

## Technologies Used

- Python 3 ![Python](https://img.shields.io/badge/Python-3.11-blue)

## Project Objective

ETL for SQLite database from tia portal program

## Analysis Section

N/A

## Prerequisites

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate sqlite_tia_portal_etl
```

or 

```bash
mamba env create -f environment.yml
activate sqlite_tia_portal_etl
```

### The resulting directory structure

The directory structure of your new project will look something like this (depending on the settings that you choose):

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
```