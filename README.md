# FastForums

A forums website made using FastAPI.

## Project structure

| Directory      |   Description   |
| :------------- | :-------------: |
| [`rest`](rest) | Python REST API |

## Running the project

You can easily run the project using Docker. We use Nginx for load balancing and proxying all the services.

```bash
$ docker-compose up
```

If you run the project with Docker Compose, it will use Nginx to proxy all the requests to the services. The following routes on the proxy correspond to services.

| Routes | Description |
| :----- | :---------: |
| `/api` |  REST API   |

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
