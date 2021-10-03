#The main content of this file came from : https://github.com/joyzoursky/docker-python-chromedriver . some modifications were made to meet the tutorilal needs
FROM python:3.9

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install selenium

#set the working directory
WORKDIR /usr/workspace

#run this command on entry
ENTRYPOINT ["python"]
#copy the tests in the container - this is not adviced. 
#COPY . .

#CMD - adding this for people who cannot access git and are using playground , this image was selenium_docker_with_ptest 
#CMD ["test_python.py"]

