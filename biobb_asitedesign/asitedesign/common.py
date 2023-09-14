""" Common functions for package biobb_asitedesign.asitedesign """
import logging
import os
from pathlib import Path
from typing import List, Dict, Tuple, Mapping, Union, Set, Sequence
import typing
import zipfile

import yaml

from biobb_asitedesign.asitedesign.preset import SOFTWARE_PARAMS


def create_yaml(output_yaml_path: str, workflow_dict: Mapping[str, str], input_yaml_path: str = None,
                preset_dict: Mapping[str, str] = None, yaml_properties_dict: Mapping[str, str] = None, container_volume_path="/data",
                unique_dir = None):
    yaml_dict = {}  # : Dict[str, str]
    if preset_dict:
        for k, v in preset_dict.items():
            yaml_dict[k] = v
    if input_yaml_path:
        input_yaml_dict = read_yaml(input_yaml_path)
        for k, v in input_yaml_dict.items():
            yaml_dict[k] = v
    if yaml_properties_dict:
        for k, v in yaml_properties_dict.items():
            yaml_dict[k] = v
    
    name = yaml_dict['Name']
    yaml_dict['Name'] = f"{unique_dir}/{name}"
    yml = write_yaml(output_yaml_path, workflow_dict, yaml_dict, container_volume_path)
    
    return yml, name


def search_string_yaml(filename, string):
    with open(filename) as f:
        contents = f.read()
        return string in contents


def write_yaml(output_yaml_path: str, workflow_dict: Mapping[str, str], yaml_dict: Mapping[str, str], container_volume_path) -> str:
    yaml_final = {}
    if workflow_dict.get('PDB'):
        yaml_final['PDB'] = workflow_dict['PDB']
    if workflow_dict.get('ParameterFiles'):
        yaml_final['ParameterFiles'] = workflow_dict['ParameterFiles']
    if workflow_dict.get('nPoses'):
        yaml_final['nPoses'] = workflow_dict.get('nPoses')
    if workflow_dict.get('DesignResidues'):
        yaml_final['DesignResidues'] = workflow_dict.get('DesignResidues')
    if workflow_dict.get('CatalyticResidues'):
        yaml_final['CatalyticResidues'] = workflow_dict.get('CatalyticResidues')
    if workflow_dict.get('Ligands'):
        yaml_final['Ligands'] = workflow_dict.get('Ligands')
    if workflow_dict.get('Constraints'):
        yaml_final['Constraints'] = workflow_dict.get('Constraints')
    if workflow_dict.get('nIterations'):
        yaml_final['nIterations'] = workflow_dict.get('nIterations')
    if workflow_dict.get('nSteps'):
        yaml_final['nSteps'] = workflow_dict.get('nSteps')
    if workflow_dict.get('Time'):
        yaml_final['Time'] = workflow_dict.get('Time')

    for k, v in yaml_dict.items():
        # Update the reference file path of the constrain
        if k == 'Constraints':
            for const in v:
                if 'reference' in v[const].keys():
                    v[const]['reference'] = workflow_dict['PDB']
        if not k in yaml_final.keys():
            yaml_final[k] = v

    with open(output_yaml_path, 'w') as yaml_file:
        yaml.dump(yaml_final, yaml_file, default_flow_style=False)

    return output_yaml_path


def read_yaml(input_yaml_path: str) -> Dict[str, str]:
    with open(input_yaml_path) as yaml_file:
        #input_yaml_dict = yaml.full_load(yaml_file)
        input_yaml_dict = yaml.safe_load(yaml_file)

    return input_yaml_dict


def yaml_preset(simulation_type: str) -> Dict[str, str]:
    yaml_dict = {}
    if not simulation_type:
        raise ValueError("Specify the simulation type")

    if simulation_type == 'CatalyticSite':
        yaml_dict = SOFTWARE_PARAMS['CatalyticSite'].copy()

    if simulation_type == 'DirectEvolution':
        yaml_dict = SOFTWARE_PARAMS['DirectEvolution'].copy()

    return yaml_dict

def zip_list(zip_file: str, file_list: typing.Iterable[str], out_log: logging.Logger = None):
    file_list.sort()
    with zipfile.ZipFile(zip_file, 'w') as zip_f:
        inserted = []
        for index, f in enumerate(file_list):
            if os.path.exists(Path(f)):
                base_name = Path(f).name
                if os.path.isdir(Path(f)):
                    for root, dirs, files in os.walk(f):
                        for file in files:
                            zip_f.write(root+"/"+file)
                            inserted.append(file)
                if base_name in inserted:
                    base_name = 'file_' + str(index) + '_' + base_name
                inserted.append(base_name)
                zip_f.write(f)
    if out_log:
        out_log.info("Adding:")
        out_log.info(str(file_list))
        out_log.info("to: " + str(Path(zip_file).resolve()))