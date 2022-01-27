#!/usr/bin/env python

import os

print("Test running")
print(os.environ)
print(os.getenv('EMAIL_HOST_USER'))
print(os.environ('EMAIL_HOST_USER'))