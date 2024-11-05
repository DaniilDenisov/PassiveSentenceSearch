# PassiveSentenceSearch
Flask service to search for the passive voice sentences in the text given. Returns all the passive sentences in their order.

Requires Python virtual environment according to the requirements.txt.

1. Download, unpack wherever you want. Open CMD shell.
2. Create python venv (for example in C:\Users\user\Desktop\PassiveSentenceSearch)
C:\Users\user\Desktop>cd PassiveSentenceSearch
C:\Users\user\Desktop\PassiveSentenceSearch>C:\Users\user\AppData\Local\Programs\Python\Python312\python.exe -m venv ven
v
3. Activate venv and install requirements.
> C:\Users\user\Desktop\PassiveSentenceSearch\venv\Scripts\activate.bat
(venv)> pip install requirements.txt
4. Run the application:
(venv)> python PassiveSentenceSearch.py
5. Access the http://127.0.0.1:5000/get_passive_sentences with curl or postman as
follows:
curl --location 'http://127.0.0.1:5000/get_passive_sentences' \
--header 'Content-Type: application/json' \
--data '{"text":"The cake was eaten by the children. The children ate the cake."}'

6. You can also use SimpleClient.py to connect the Flast service running.
For this you open another cmd window , activate the venv and type:
python SimpleClient.py
The client asks for the text and performs request to http://127.0.0.1:5000/get_passive_sentences.
7. In Windows Docker Desktop should run to build and rin images as containers. Commands to run and build images
are provided in bat files.
