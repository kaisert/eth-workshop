#!/usr/bin/env python3
import os

import connexion

from swagger_server import encoder


def main():
    options = {
        "swagger_ui": True
    }
    app = connexion.App(__name__, specification_dir='./swagger/',
                        options=options)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'User Microservice'})
    app.run(port=8080)


if __name__ == '__main__':
    main()
