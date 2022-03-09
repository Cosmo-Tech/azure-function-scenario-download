# Copyright (c) Cosmo Tech corporation.
# Licensed under the MIT license.
from CosmoTech_Acceleration_Library.Accelerators.scenario_download.azure_function_main import generate_main


def apply_update(content: dict, scenario_data: dict) -> dict:
    """
    Apply update is the function you will have to implement to specify the logic of your function
    :param content: Contains all datasets and parameters downloaded from the API
    :param scenario_data: The data associated to your scenario downloaded from the API
    :return: A dict of data that should be json equivalent that will be sent as the body of the response of your function call
    """
    return content


main = generate_main(apply_update=apply_update)
