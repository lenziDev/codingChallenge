# <a name="config"></a>Configuration
- Copy the file .env.example and add your credentials to a new file called .env
- Set a summarize method, you can find more on [Documentation](https://documenter.getpostman.com/view/16968523/UVkiRxbJ), possible SUMMARIZE_METHOD values are 
    - **LSA**
    - **LexRank**
    - **Luhn**
# Installation

- Install dependencies

        pip install -r requirements.txt

- Run migrations (On root project directory)

        python manage.py migrate

# Run application

- Run the app

        python manage.py runserver

# Using Docker-Compose

- The configuration .env must be specified [too](#config)

- Build project images

        docker-compose build

- Run the containers

        docker-compose up

# Testing

- You can use the following command on the project root

        python manage.py test
# Documentation

You can find the documentation on [LINK](https://documenter.getpostman.com/view/16968523/UVkiRxbJ)
