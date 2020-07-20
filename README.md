# cybsafeserver
Flask server to receive process information from cybsafeclient and log it to file every 5 seconds.

# Prep:
source venv/bin/activate
flask run
(ensure port 5000 is open on server)
run cybsafeclient
monitor cybserver.log using tail or similar which is created in root directory of this project.
