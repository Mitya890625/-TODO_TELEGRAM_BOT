# How to start


OS:
```python
#Windows:
  py -m venv venv
  .\venv\Scripts\Activate.ps1
  pip install -r requirements.txt

#Linux:
  python3 -m venv venv
  source ./venv/bin/activate
  pip install -r requirements.txt
```

Docker:
```docker
docker build -t mybot .
docker run -d mybot
```