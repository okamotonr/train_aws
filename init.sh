# /bin/bash

env PYHONPATH=. gunicorn train_aws.app:app
