# FastForums

A forums website made using FastAPI.

## Running the REST API

Requirements:
    - Have Python 3.6+
    - Install PostgreSQL 11+

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

## Run REST API tests
 
Open your terminal, and cd into the `rest` directory.

```bash
$ cd ./rest
```

Then install the dev dependencies

```bash
$ pip install -r dev-requirements.txt
```

Now run the tests with pytest

```bash
$ pytest
```
## License

MIT License

Copyright (C) 2022 DevGuyAhnaf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.