#!/usr/bin/env python3

"""Module containing the TemplateContainer class and the command line interface."""
import argparse
import os
from pathlib import Path
import shutil
import zipfile

from biobb_asitedesign.asitedesign import common as com
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger


# 1. Rename class as required
class Asitedesign(BiobbObject):
    """
    | biobb_asitedesignsitedesign Asitedesign
    | Wrapper of the AsiteDesign module.
    | repository combines the PyRosetta modules with enhanced sampling techniques to design both the catalytic and non-catalytic residues in given active sites.

    Args:
        input_pdb (str): Path to the input file pdb. File type: input. Accepted formats: PDB (edam:format_1476).
        input_yaml (str): Path to the input file yaml. File type: input. Accepted formats: YAML (edam:format_3750).
        params_zip (str): Path to the params folder. File type: input. Accepted formats: PARAMS (edam:format_).
        output_path (str): Path to the output file. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dict):
            * **cpus** (*int*) - (2) Number of cpus for the job.
            * **name** (*str*) - ('DesignCatalyticSite_job') Name of the job, which will be used for the output folders.
            * **DesignResidues** (*list*) - (None) List of residues that want to be mutable during the simulation.
            * **CatalyticResidues** (*list*) - (None) Specify the number of residues of the active site that wants to be added (RES1, RES2 ... RESN: H).
            * **Ligands** (*list*) - (None) 1-L (you have to specify the ligand by giving the residue number and the chain of the specific LIG). Also, the torsions that want to be excluded must be specified by the user ("ExcludedTorsions").
            * **Constraints** (*list*) - (None) Add the distance and sequence constraints that you want. The distance constraints should be added by passing two residues (with residue_number-chain) and two atoms (atomname) and to which values you want to constraint them (lb: value in angstroms, hb: value in angstroms).
            * **nIterations** (*int*) - (2) Number of adaptive sampling epochs that want to be performed.
            * **nSteps** (*int*) - (2) Number of steps performed in each epoch/iteration.
            * **nPoses** (*int*) - (2) Number of final poses (mutants/designs) to be reported (each one given to a processor/CPU).
            * **Time** (*int*) - (48) Time in the queue (if it's run in a cluster).
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **container_path** (*str*) - (docker) Container path definition.
            * **container_image** (*str*) - ('bsceapm/asitedesign:X.X') Container image definition.
            * **container_volume_path** (*str*) - ('/home/projects') Container volume path definition.
            * **container_working_dir** (*str*) - ('/home/projects') Container working directory definition.
            * **container_user_id** (*str*) - (None) Container user_id definition.
            * **container_shell_path** (*str*) - ('/bin/bash') Path to default shell inside the container.
    Examples:
        This is a use example of how to use the building block from Python::
            from biobb_asitedesign.asitedesign.asitedesign_container import asitedesign_container
            prop = {
                'cpus': 21,
                'DesignResidues':
                    {'28-A'   : 'ZX',
                    '29-A'   : 'ZX',
                    '30-A'   : 'ZX',
                    '34-A'   : 'ZX',
                    '57-A'   : 'ZX',
                    '69-A'   : 'ZX',
                    '93-A'   : 'ZX',
                    '95-A'   : 'ZX',
                    '120-A'  : 'ZX',
                    '121-A'  : 'ZX',
                    '125-A'  : 'ZX',
                    '135-A'  : 'ZX',
                    '139-A'  : 'ZX',
                    '140-A'  : 'ZX',
                    '143-A'  : 'ZX',
                    '147-A'  : 'ZX',
                    '154-A'  : 'ZX',
                    '158-A'  : 'ZX',
                    '155-A'  : 'ZX',
                    '162-A'  : 'ZX',
                    '183-A'  : 'ZX',
                    '191-A'  : 'ZX',
                    '195-A ' : 'ZX',
                    '198-A'  : 'ZX',
                    '199-A'  : 'ZX',
                    '224-A'  : 'ZX',
                    '225-A'  : 'ZX',
                    '230-A'  : 'ZX'
                    }
                'CatalyticResidues':
                    {'RES1': 'H',
                    'RES2': 'S',
                    'RES3': 'D-E'
                    }
                'Ligands':
                    {'1-L':
                        {'RigidBody': True,
                        'Packing': True,
                        'PerturbationMode': 'MC',
                        'PerturbationLoops': 1,
                        'nRandomTorsionPurturbation': 2,
                        'Energy': 'Reduced',
                        'SimulationRadius': 5.0,
                        'SideChainCoupling': 0.005,
                        'TranslationSTD': 0.5,
                        'RotationSTD': 2.0,
                        'TranslationLoops': 20,
                        'RotationLoops': 50,
                        'ClashOverlap': 0.6,
                        'NeighbourCutoff': 15.0,
                        'SasaConstraint': 10,
                        'SasaScaling': True,
                        'SasaCutoff': 0.6,
                        'TranslationScale': -1,
                        'RotationScale': -1,
                        'PackingLoops': 1,
                        'NumberOfGridNeighborhoods': 2,
                        'MaxGrid': 4,
                        'MinGrid': 4,
                        'GridInterval': -4,
                        'ExcludedTorsions': ['C11', 'C14', 'C16', 'C17']
                        }
                    }
                'Constraints':
                    {'cst0':
                        {'type': 'B',
                        'resi': '1-L',
                        'atomi': 'C1',
                        'resj': 'RES1',
                        'atomj': 'OG',
                        'lb': 3.0,
                        'hb': 4.0,
                        'sd': 100.0
                        }
                    }
                ,
                'nIterations': 20,
                'nSteps': 5,
                'nPoses': 20,
                'Time': 48,
                'container_path': 'docker',
                'container_image': 'bsceapm/asitedesign:X.X',
                'container_volume_path': '/home/projects'
            }
            asitedesign_container(input_path='/path/to/my.fasta',
                            output_file_path='/path/to/newCompressedFile.zip',
                            cpus= 21,
                            properties=prop)
    Info:
        * wrapped_software:
            * name: AsiteDesign
            * version: >=1.0
            * license: BSD 3-Clause
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl
    """

    # 2. Adapt input and output file paths as required. Include all files, even optional ones
    def __init__(self, input_pdb, input_yaml, params_zip, output_path, properties=None, **kwargs) -> None:

        properties = properties or {}

        # 2.0 Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # 2.1 Modify to match constructor parameters
        # Input/Output files
        self.io_dict = {
            'in': {'input_pdb': input_pdb},
            'out': {'output_path': output_path}
        }
        self.input_yaml = input_yaml

        # Get a list of the parameters files
        
        self.params_files = []
        if os.path.isdir(Path(params_zip)):
            for root, dirs, files in os.walk(params_zip):
                for file in files:
                    if file.endswith('.params'):
                        self.io_dict['in'][file] = os.path.join(root, file)
                        self.params_files.append(os.path.join(root, file))
        elif zipfile.is_zipfile(Path(params_zip)):
            self.zip_directory = fu.create_unique_dir()
            self.params_files = fu.unzip_list(params_zip, dest_dir=self.zip_directory)
            for path in self.params_files:
                self.io_dict['in'][Path(path).name] = path
        else:
            if os.path.exists(Path(params_zip)):
                self.params_files = [params_zip]


        # 3. Include all relevant properties here as
        # Properties specific for BB
        self.cpus = properties.get('cpus', 1)
        self.name = properties.get('name', 'DesignCatalyticSite_job')
        self.designResidues = properties.get('DesignResidues', None)
        self.catalyticResidues = properties.get('CatalyticResidues', None)
        self.ligands = properties.get('Ligands', None)
        self.constraints = properties.get('Constraints', None)
        self.nIterations = properties.get('nIterations', 5)
        self.nSteps = properties.get('nSteps', 2)
        self.nPoses = properties.get('nPoses', 3)
        self.time = properties.get('Time', 48)
        self.container_path = properties.get('container_path', 'singularity')
        #self.container_image = properties.get('container_image', '/home/ubuntu/biobb/singularity/asitedesign.sif')
        self.container_image = properties.get('container_image', '/home/albertcs/GitHub/EAPM/AsiteDesign-container/asitedesign.sif')
        self.simulation_type = properties.get('simulation_type', 'CatalyticSite')
        self.container_volume_path = properties.get('container_volume_path', '/data')
        self.container_generic_command = properties.get('container_generic_command', 'exec')
        # self.container_shell_path = properties.get('container_shell_path', '/bin/bash')
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        # Check the arguments
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`TemplateContainer <template.template_container.TemplateContainer>` object."""

        # 4. Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Copy params files to the unique directory
        for path in self.params_files:
            shutil.copy(path, self.stage_io_dict['unique_dir'])
                    
        # Dict with the yaml properties form properties
        workflow_dict = {'PDB': self.stage_io_dict['in']['input_pdb'],
                         'ParameterFiles': [f"{self.container_volume_path}/{Path(path).name}" for path in self.params_files],
                         'nPoses': self.nPoses,
                         'Name': self.name,
                         'DesignResidues': self.designResidues,
                         'CatalyticResidues': self.catalyticResidues,
                         'Ligands': self.ligands,
                         'Constraints': self.constraints,
                         'nIterations': self.nIterations,
                         'nSteps': self.nSteps,
                         'Time': self.time,
                         'simulation_type': self.simulation_type
                         }

        self.input_yaml_path_final = com.create_yaml(output_yaml_path=str(Path(self.stage_io_dict['unique_dir']).joinpath('input.yaml')),
                                                     workflow_dict=workflow_dict,
                                                     input_yaml_path=self.input_yaml,
                                                     preset_dict=com.yaml_preset(workflow_dict['simulation_type']),
                                                     container_volume_path=self.container_volume_path)

        if self.input_yaml_path_final:
            self.stage_io_dict['in']['input_yaml'] = f"{self.container_volume_path}/{self.input_yaml_path_final.split('/')[-1]}"
        
        # Append the mpirun with the cpus in front of the whole command execution
        # if self.cpus:
        #    self.container_path = f"mpirun -n {self.cpus} " + self.container_path

        self.cmd = [f"mpirun -n {self.cpus} python -m ActiveSiteDesign"]
        if self.input_yaml_path_final:
            self.cmd.append(f"{self.stage_io_dict['in']['input_yaml']}")

        self.cmd.append("> output.out")

        fu.log("Creating command line with instructions and required arguments", self.out_log, self.global_log)
        print(self.cmd)

        # Run Biobb block
        self.run_biobb()

        # Make zip file
        list_to_zip = [os.path.join(self.stage_io_dict.get('unique_dir'), f) for f in
                       os.listdir(self.stage_io_dict.get('unique_dir'))]
        list_to_zip.append("DesignCatalyticSite_job_final_pose")
        list_to_zip.append("DesignCatalyticSite_job_output")
        list_to_zip.append("output.out")
        com.zip_list(self.io_dict['out']['output_path'], list_to_zip, self.out_log)

        # Remove temporary file(s)
        self.tmp_files.extend([
            self.stage_io_dict.get('unique_dir')
        ])
        self.tmp_files.append("DesignCatalyticSite_job_final_pose")
        self.tmp_files.append("DesignCatalyticSite_job_output")
        self.tmp_files.append("output.out")
        self.tmp_files.extend(self.params_files)
        self.remove_tmp_files()

        # Check output arguments
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def asitedesign(input_pdb: str, input_yaml: str, params_zip: str, output_path: str,
                properties: dict = None, **kwargs) -> int:
    """Create :class:`AsitedesignContainer <asitedesign.asitedesign_container.AsitedesignContainer>` class and
    execute the :meth:`launch() <asitedesign.asitedesign_container.AsitedesignContainer.launch>` method."""

    return Asitedesign(input_pdb=input_pdb,
                       input_yaml=input_yaml,
                       params_zip=params_zip,
                       output_path=output_path,
                       properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description='Wrapper of the AsiteDesign.',
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('-c', '--config', required=False, help='Configuration yaml file')

    # 10. Include specific args of each building block following the examples. They should match step 2
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_pdb', required=True,
                               help='Path of the pdb file. Accepted formats: pdb.')
    required_args.add_argument('--params_zip', required=True,
                               help='Path to the params folder.')
    required_args.add_argument('--input_yaml', required=True,
                               help='Path to the yaml file')
    required_args.add_argument('--output_path', required=True,
                               help='Path for the output file.')

    args = parser.parse_args()
    config = args.config if args.config else None
    properties = settings.ConfReader(config=config).get_prop_dic()

    # 11. Adapt to match Class constructor (step 2)
    # Specific call of each building block
    asitedesign(input_pdb=args.input_pdb,
                input_yaml=args.input_yaml,
                params_zip=args.params_zip,
                output_path=args.output_path,
                properties=properties)


if __name__ == '__main__':
    main()

# 13. Complete documentation strings
