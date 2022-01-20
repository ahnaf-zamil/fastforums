# FastForums REST API

## Running the API

Requirements: - Have Python 3.6+ - Install PostgreSQL 11+

First, rename the `.env.example` file in the `rest` directory to `.env` and fill up the credentials.

Now open your terminal, and cd into the `rest` directory.

```bash
$ cd ./rest
```

Then install the dependencies

```bash
$ pip install -r requirements.txt
```

Now run the API using the Uvicorn server

```bash
$ uvicorn app.main:app --reload
```

## Run REST API pipelines

Open your terminal, and cd into the `rest` directory.

```bash
$ cd ./rest
```

Then install the dependencies

```bash
$ pip install -r requirements.txt -r dev-requirements.txt
```

Now run the pipelines with nox

```bash
$ nox
```
