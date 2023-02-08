#!/usr/bin/env python3

"""Module containing the TemplateContainer class and the command line interface."""
import argparse
import os
import shutil
from pathlib import Path

from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.configuration import settings
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger


# 1. Rename class as required
class AsitedesignContainer(BiobbObject):
    """
    | biobb_asitedesignsitedesign Asitedesign
    | Wrapper of the AsiteDesign module.
    | repository combines the PyRosetta modules with enhanced sampling techniques to design both the catalytic and non-catalytic residues in given active sites.

    Args:
        input_pdb (str): Path to the input file pdb. File type: input. Accepted formats: PDB (edam:format_1476).
        input_yaml (str): Path to the input file yaml. File type: input. Accepted formats: YAML (edam:format_3750).
        params_folder (str): Path to the params folder. File type: input. Accepted formats: PARAMS (edam:format_).
        output_path (str): Path to the output file. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **name** (*str*) - ('DesignCatalyticSite_job') Name of the job, which will be used for the output folders.
            * **DesignResidues** (*list*) - (None) List of residues that want to be mutable during the simulation.
            * **CatalyticResidues** (*list*) - (None) Specify the number of residues of the active site that wants to be added (RES1, RES2 ... RESN: H).
            * **Ligands** (*list*) - (None) 1-L (you have to specify the ligand by giving the residue number and the chain of the specific LIG). Also, the torsions that want to be excluded must be specified by the user ("ExcludedTorsions").
            * **Constraints** (*list*) - (None) Add the distance and sequence constraints that you want. The distance constraints should be added by passing two residues (with residue_number-chain) and two atoms (atomname) and to which values you want to constraint them (lb: value in angstroms, hb: value in angstroms).
            * **nIterations** (*int*) - (20) Number of adaptive sampling epochs that want to be performed.
            * **nSteps** (*int*) - (5) Number of steps performed in each epoch/iteration.
            * **nPoses** (*int*) - (20) Number of final poses (mutants/designs) to be reported (each one given to a processor/CPU).
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
                'name': 4,
                'DesignResidues':
                    {'28-A'   : 'ZX'
                    '29-A'   : 'ZX'
                    '30-A'   : 'ZX'
                    '34-A'   : 'ZX'
                    '57-A'   : 'ZX'
                    '69-A'   : 'ZX'
                    '93-A'   : 'ZX'
                    '95-A'   : 'ZX'
                    '120-A'  : 'ZX'
                    '121-A'  : 'ZX'
                    '125-A'  : 'ZX'
                    '135-A'  : 'ZX'
                    '139-A'  : 'ZX'
                    '140-A'  : 'ZX'
                    '143-A'  : 'ZX'
                    '147-A'  : 'ZX'
                    '154-A'  : 'ZX'
                    '158-A'  : 'ZX'
                    '155-A'  : 'ZX'
                    '162-A'  : 'ZX'
                    '183-A'  : 'ZX'
                    '191-A'  : 'ZX'
                    '195-A ' : 'ZX'
                    '198-A'  : 'ZX'
                    '199-A'  : 'ZX'
                    '224-A'  : 'ZX'
                    '225-A'  : 'ZX'
                    '230-A'  : 'ZX'
                    }
                'CatalyticResidues':
                    {'RES1': 'H'
                    'RES2': 'S'
                    'RES3': 'D-E'
                    }
                'Ligands':
                    {1-L:
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
    def __init__(self, input_pdb, input_yaml, params_folder, output_path, properties=None, **kwargs) -> None:
        properties = properties or {}

        # 2.0 Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # 2.1 Modify to match constructor parameters
        # Input/Output files
        self.io_dict = {
            'in': {'input_pdb': input_pdb, 'input_yaml': input_yaml, 'params_folder': params_folder},
            'out': {'output_path': output_path}
        }

        # 3. Include all relevant properties here as
        # Properties specific for BB
        self.name = properties.get('name', 'DesignCatalyticSite_job')
        self.DesignResidues = properties.get('DesignResidues', None)
        self.CatalyticResidues = properties.get('CatalyticResidues', None)
        self.Ligands = properties.get('Ligands', None)
        self.Constraints = properties.get('Constraints', None)
        self.nIterations = properties.get('nIterations', 20)
        self.nSteps = properties.get('nSteps', 5)
        self.nPoses = properties.get('nPoses', 20)
        self.Time = properties.get('Time', 48)
        self.container_volume_path = properties.get('container_volume_path', '')
        self.database_folder = properties.get('database_folder', )
        self.container_path = properties.get('container_path', 'docker')
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
        if self.check_restart(): return 0
        self.stage_files()

        # Creating temporary folder
        # self.tmp_folder = fu.create_unique_dir()
        # fu.log('Creating %s temporary folder' % self.tmp_folder, self.out_log)

        # 5. Prepare the command line parameters as instructions list
        instructions = []


        # 6. Build the actual command line as a list of items (elements order will be maintained)
        self.cmd = [self.binary_path,
                    ' '.join(instructions),
                    '-i', os.path.basename(self.stage_io_dict['in']['input_path'])]
        fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)

        # 8. Uncomment to check the command line
        print(' '.join(self.cmd))

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        # self.copy_to_host()

        # Make zip file
        list_to_zip = [os.path.join(self.stage_io_dict.get('unique_dir'), f) for f in
                       os.listdir(self.stage_io_dict.get('unique_dir'))]
        fu.zip_list(self.io_dict['out']['output_path'], list_to_zip)

        # Remove temporary file(s)
        self.tmp_files.extend([
            self.stage_io_dict.get('unique_dir')
        ])
        self.remove_tmp_files()

        # Check output arguments
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def asitedesign_container(input_path: str, output_path: str,
                          properties: dict = None, **kwargs) -> int:
    """Create :class:`TemplateContainer <template.template_container.TemplateContainer>` class and
    execute the :meth:`launch() <template.template_container.TemplateContainer.launch>` method."""

    return AsitedesignContainer(input_path=input_path,
                                output_path=output_path,
                                properties=properties, **kwargs).launch()


def main():
    """Command line execution of this building block. Please check the command line documentation."""
    parser = argparse.ArgumentParser(description='Description for the template container module.',
                                     formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=99999))
    parser.add_argument('--config', required=False, help='Configuration file')

    # 10. Include specific args of each building block following the examples. They should match step 2
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('--input_path', required=True,
                               help='Description for the first input file path. Accepted formats: top.')
    required_args.add_argument('--output_path', required=True,
                               help='Description for the output file path. Accepted formats: zip.')

    args = parser.parse_args()
    args.config = args.config or "{}"
    properties = settings.ConfReader(config=args.config).get_prop_dic()

    # 11. Adapt to match Class constructor (step 2)
    # Specific call of each building block
    asitedesign_container(input_path=args.input_path,
                      output_path=args.output_file_path,
                      properties=properties)


if __name__ == '__main__':
    main()

# 13. Complete documentation strings
