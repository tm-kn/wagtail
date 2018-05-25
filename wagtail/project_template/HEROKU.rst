Deploy to Heroku
================

This project template comes with ``Dockerfile`` and ``heroku.yml`` configured
to easily deploy to Heroku. In order to deploy to Heroku you must follow the
steps below.

This guide assumes that you have installed
`Heroku CLI <https://devcenter.heroku.com/articles/heroku-cli>`_.

Create your app
~~~~~~~~~~~~~~~
You have to set the stack to be ``container`` so Heroku knows to
use your Dockerfile rather than its Python runtime.

.. code-block:: sh

   heroku apps:create --stack container your-app-name

Set environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~
Next step is to set your environemnt variables.

.. code-block:: sh

   heroku config:set SECRET_KEY=[your-generated-secret-key] \
                     ALLOWED_HOSTS=[your-app-name].herokuapp.com

Create database
~~~~~~~~~~~~~~~

Create PostgreSQL database. This will automatically set the ``DATABASE_URL``
environment variable for your app.

.. code-block:: sh

   heroku addons:add heroku-postgresql


Push your code
~~~~~~~~~~~~~~

Push your code to the remote that Heroku set for you. You will have to run
``git init`` to initialise your git repository if you have not done that yet.

.. code-block:: sh

   git push heroku

Persistent storage
~~~~~~~~~~~~~~~~~~
Heroku does not come with persistent storage configured out of the box. We
recommend using AWS S3 with `django-storages` and `boto3` packages.
