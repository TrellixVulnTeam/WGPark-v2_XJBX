# coding=UTF-8
import os

class ProductionConfig():

    # Deleta todo e qualquer cache para carregar as modificações feitas no programa
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SECRET_KEY = os.urandom(24)
