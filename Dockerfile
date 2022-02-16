# start from an official image
FROM python:3.8

# arbitrary location choice: you can change the directory
RUN mkdir -p /opt/services/codingChallenge/src
WORKDIR /opt/services/codingChallenge/src

# install dependencies
RUN apt update
# install dependencies
RUN pip install --upgrade pip
RUN apt-get install -y gunicorn
# copy our project code
COPY . /opt/services/codingChallenge/src
RUN pip install -r requirements.txt




# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
# CMD ["gunicorn", "--chdir", "codingChallenge", "--bind", ":8000", "codingChallenge.wsgi:application"]