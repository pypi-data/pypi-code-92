#!/usr/bin/env python

'''
Ironhouse extends Stonehouse with client public key authentication.

This is the strongest security model we have today, protecting against every
attack we know about, except end-point attacks (where an attacker plants
spyware on a machine to capture data before it's encrypted, or after it's
decrypted).

Author: Chris Laws
'''

import logging
import os
import sys

import zmq
import zmq.auth
from zmq.auth.thread import ThreadAuthenticator


def run():
    ''' Run Ironhouse example '''

    # These directories are generated by the generate_certificates script
    base_dir = os.path.dirname(__file__)
    keys_dir = os.path.join(base_dir, 'certificates')
    public_keys_dir = os.path.join(base_dir, 'public_keys')
    secret_keys_dir = os.path.join(base_dir, 'private_keys')

    if not (
        os.path.exists(keys_dir)
        and os.path.exists(public_keys_dir)
        and os.path.exists(secret_keys_dir)
    ):
        logging.critical(
            "Certificates are missing - run generate_certificates.py script first"
        )
        sys.exit(1)

    ctx = zmq.Context.instance()

    # Start an authenticator for this context.
    auth = ThreadAuthenticator(ctx)
    auth.start()
    auth.allow('127.0.0.1')
    # Tell authenticator to use the certificate in a directory
    auth.configure_curve(domain='*', location=public_keys_dir)

    server = ctx.socket(zmq.PUSH)

    server_secret_file = os.path.join(secret_keys_dir, "server.key_secret")
    server_public, server_secret = zmq.auth.load_certificate(server_secret_file)
    server.curve_secretkey = server_secret
    server.curve_publickey = server_public
    server.curve_server = True  # must come before bind
    server.bind('tcp://*:9000')

    client = ctx.socket(zmq.PULL)

    # We need two certificates, one for the client and one for
    # the server. The client must know the server's public key
    # to make a CURVE connection.
    client_secret_file = os.path.join(secret_keys_dir, "client.key_secret")
    client_public, client_secret = zmq.auth.load_certificate(client_secret_file)
    client.curve_secretkey = client_secret
    client.curve_publickey = client_public

    server_public_file = os.path.join(public_keys_dir, "server.key")
    server_public, _ = zmq.auth.load_certificate(server_public_file)
    # The client must know the server's public key to make a CURVE connection.
    client.curve_serverkey = server_public
    client.connect('tcp://127.0.0.1:9000')

    server.send(b"Hello")

    if client.poll(1000):
        msg = client.recv()
        if msg == b"Hello":
            logging.info("Ironhouse test OK")
    else:
        logging.error("Ironhouse test FAIL")

    # stop auth thread
    auth.stop()


if __name__ == '__main__':
    if zmq.zmq_version_info() < (4, 0):
        raise RuntimeError(
            "Security is not supported in libzmq version < 4.0. libzmq version {0}".format(
                zmq.zmq_version()
            )
        )

    if '-v' in sys.argv:
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level, format="[%(levelname)s] %(message)s")

    run()
