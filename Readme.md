# Run the following commands in this order:

    docker-compose up --build

    docker ps


# Get the CONTAINER ID of the django app and log into it to create/run migrations

    docker exec -t -i CONTAINER ID bash
    
    python manage.py makemigrations images

    python manage.py migrate


# Now the app should be running at *http://localhost:8000/*

   ## To test the api you can 
  > ### Send get request at *http://localhost:8000/images/process* to list all image informations
  > ### Send post request with body *{"url": "some_url"}* using Postman(or some other tool) to endpoint *http://localhost:8000/images/process*
