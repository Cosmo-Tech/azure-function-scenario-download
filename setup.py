# Copyright (c) Cosmo Tech corporation.
# Licensed under the MIT license.
from setuptools import setup

setup(
    name='cosmotech_scenario_download',
    version='0.0.1',
    packages=['cosmotech_scenario_download'],
    url='https://github.com/Cosmo-Tech/azure-function-scenario-download',
    license='MIT',
    author='afossart',
    author_email='alexis.fossart@cosmotech.com',
    description='Cosmotech Azure function base for scenarios',
    install_requires=["azure-functions",
                      "azure-digitaltwins-core",
                      "azure-identity",
                      "openpyxl",
                      "cosmotech_api @ git+https://github.com/Cosmo-Tech/cosmotech-api-python-client.git#egg=cosmotech_api"]
)
