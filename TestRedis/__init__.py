# Copyright (c) Cosmo Tech corporation.
# Licensed under the MIT license.
from CosmoTech_Acceleration_Library.Accelerators.scenario_download.azure_function_main import generate_main

import tempfile
import shutil
import os
from csv import DictWriter

from CosmoTech_Modelops_Library.core.importer.model_importer import ModelImporter
import time


def apply_update(content: dict, scenario_data: dict) -> dict:
    """
    Apply update is the function you will have to implement to specify the logic of your function
    :param content: Contains all datasets and parameters downloaded from the API
    :param scenario_data: The data associated to your scenario downloaded from the API
    :return: A dict of data that should be json equivalent that will be sent as the body of the response of your function call
    """

    ts = int(time.time())
    tmp_folder = "./temp_test_redis"
    os.makedirs(tmp_folder, exist_ok=True)
    for dataset_name, dataset in content['datasets'].items():
        mi = ModelImporter(host='localhost', port=6379, name=f'Graph{ts % 1000000}')
        dirpath = tempfile.mkdtemp(dir=tmp_folder)
        d_content = dataset['content']
        keys = d_content.keys()
        entities = []
        relations = []
        for k in keys:
            p = os.path.join(dirpath, k + '.csv')
            is_relation = False
            if d_content[k]:
                e = d_content[k][0]
                if 'source' in e and 'target' in e:
                    relations.append(p)
                    is_relation = True
                else:
                    entities.append(p)
                with open(p, "w") as _f:
                    local_keys = set()
                    for r in d_content[k]:
                        local_keys.update(set(r.keys()))
                    ordered_keys = ['id'] if not is_relation else ['source', 'target']
                    for _k in ordered_keys:
                        if _k in local_keys:
                            local_keys.remove(_k)
                    ordered_keys.extend(local_keys)
                    w = DictWriter(_f, ordered_keys)
                    w.writeheader()
                    w.writerows(d_content[k])
        try:
            mi.bulk_import(twin_file_paths=entities,
                           relationship_file_paths=relations)
        except SystemExit:
            pass
    shutil.rmtree(tmp_folder)
    return content


main = generate_main(apply_update=apply_update)
