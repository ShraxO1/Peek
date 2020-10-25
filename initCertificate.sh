#!/bin/bash

if ! [ -x "$(command -v openssl)" ]; then
  echo 'Error: openssl is not installed.' >&2
  exit 1
fi

openssl req -x509 -newkey rsa:4096 -keyout cert.key -out cert.crt -days 365
