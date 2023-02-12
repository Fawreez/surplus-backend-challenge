# surplus-backend-challenge

Framework: FastAPI 0.91.0

Language: Python 3.10.7

Database: Mysql 8.0.32


## Setup
1. Create a python virtual environment by running `python -m venv venv`
2. activate venv by running `.\venv\scripts\activate.bat`
3. Install requirements by running `pip install -r requirements.txt`
4. configure database info in config.py if necessary
5. Populate the database by importing data from the provided .csv files located in the `seed_data` folder

## Running the program
1. To run the program simply run main.py. Once running, a uvicorn server should start on `localhost:8000`
2. To check if the server is running, go to `localhost:8000`. It should look like the image below
![image](https://user-images.githubusercontent.com/44045536/218298554-70ff7104-7844-41bf-ba92-77b789a1bf5a.png)
3. With FastAPI, APIs could be easily accessed by going to `localhost:8000/docs`. A list of all available API should be displayed like in the image below
![image](https://user-images.githubusercontent.com/44045536/218298601-96db3e4a-3fd7-4a26-97ac-5dfecd43134f.png)
4. Through `localhost:8000/docs` APIs can be accessed and run manually.
![image](https://user-images.githubusercontent.com/44045536/218298676-27611351-245a-4dcf-9572-d61561459e0f.png)
