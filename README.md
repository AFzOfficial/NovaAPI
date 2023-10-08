# NovaAPI

Simple rest api for blog with jwt authentication

### Technologies
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue) ![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white) ![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)

## How to Run?
### Clone the project
```bash
git clone https://github.com/AFzOfficial/NovaAPI.git

cd NovaAPI
```

### Setup env
```bash
python3 -m venv .venv
source .venv/bin/activate
```
### Install Depends
```bash
pip install -r requirements.txt
```
### Run Development Server
```bash
uvicorn main:app
```
open [127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser
