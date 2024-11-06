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

curl --location 'http://127.0.0.1:5000/get_passive_sentences' \
--header 'Content-Type: application/json' \
--data '{
  "text": "You have to be tested on your English grammar. John might be promoted next year. She wants to be invited to the party. I expect to be surprised on my birthday. You may be disappointed. I remember being taught to drive. The children are excited about being taken to the zoo. Most film stars hate being interviewed. Poodles like to be pampered."
}
'

6. You can also use SimpleClient.py to connect the Flast service running.
For this you open another cmd window , activate the venv and type:
python SimpleClient.py
The client asks for the text and performs request to http://127.0.0.1:5000/get_passive_sentences.
7. In Windows Docker Desktop should run to build and rin images as containers. Commands to run and build images
are provided in bat files.

8. In non-container mode, download NLTK pre-trained tagging libraries to your venv with:
python -m nltk.downloader punkt averaged_perceptron_tagger
For spacy:
python -m spacy download en_core_web_sm
Dockerfile does this with corresponding command.



------------------- Text samples ------------------

Simple two sentences

The cake was eaten by the children. The children ate the cake.

All passive possible

You have to be tested on your English grammar. John might be promoted next year.
She wants to be invited to the party. I expect to be surprised on my birthday.
You may be disappointed. I remember being taught to drive. The children are excited
about being taken to the zoo. Most film stars hate being interviewed. Poodles like
to be pampered.

No Passive text sample

The Growing Importance of Data Audit in Modern Infrastructure
As data science tools and libraries become more user-friendly, data-driven
insights become more accessible. Elasticsearch, a powerful search and analytics
engine, processes millions of records daily. Therefore, maintaining an Elasticsearch
database activity history of important server activities is essential for modern
organizations.
Elasticsearch takes security seriously through multiple initiatives. They maintain
an active bug bounty program on HackerOne, where security researchers can report
vulnerabilities and receive compensation for their findings. The company regularly
publishes security announcements and updates through their official security advisory
portal, ensuring users stay informed about potential risks and fixes.
Did you know? Organizations face an average cost of $4.88 million per data breach
in 2024. This makes proper audit trailing not just a security measure, but a
financial necessity.
Basic Concepts of Elasticsearch Database Activity History
Elasticsearch offers built-in audit capabilities through its security features. These
features track user actions, system changes, and data access patterns. The audit
system monitors user authentication attempts and records all significant events
within the database environment. Through careful tracking of index operations and
document modifications, organizations can maintain a comprehensive database activity
history. The system also logs search queries and configuration changes, providing a
complete picture of database usage.
Getting Started with Elasticsearch Audit Trail
The audit capability in Elasticsearch comes as a trial feature. To explore these
functions, you’ll need to activate the 30-day trial period (you can extend this
period). During this time, you can test audit logging and user activity monitoring
capabilities. This trial period helps organizations understand the basic security
requirements of their Elasticsearch deployment.