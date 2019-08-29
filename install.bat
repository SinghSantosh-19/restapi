REM Install dependency
pip install -r requirements.txt

REM start application and server
start python app.py

REM pause for 10 sec
timeout 10

REM start unittest
python test.py 