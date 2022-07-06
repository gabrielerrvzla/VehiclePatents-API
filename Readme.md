### Vehicle patents
REST API to generate and verify vehicle license plates

#### Features
- Obtain vehicle license based on an id (number)

- Obtain id (number) based on a vehicle patent

#### Run application
- Run git clone https://github.com/gabrielerrvzla/VehiclePatents-API.git

- Run `python3 -m venv env (create virtual environment)`

- Run `source/env/bin/activate`

- Run `pip install -r requirements.txt`

- Run `pytest`

- run `cd/app`

- Run `uvicorn main:app --reload`

- Go to http://localhost:8000/docs

#### Run application with docker
- Run `docker build -t patent_api`

- Run `docker run -p 8000:8000 patent_api`