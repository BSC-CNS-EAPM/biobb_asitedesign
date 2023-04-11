from biobb_asitedesign.asitedesign.asitedesign_container import asitedesign_container


def main():
    prop = {
        "cpus": 4,
        "DesignResidues":
            {'28-A': 'ZX',
             '29-A': 'ZX',
             '30-A': 'ZX',
             '34-A': 'ZX',
             '57-A': 'ZX',
             '69-A': 'ZX',
             '93-A': 'ZX',
             '95-A': 'ZX',
             '120-A': 'ZX',
             '121-A': 'ZX',
             '125-A': 'ZX',
             '135-A': 'ZX',
             '139-A': 'ZX',
             '140-A': 'ZX',
             '143-A': 'ZX',
             '147-A': 'ZX',
             '154-A': 'ZX',
             '158-A': 'ZX',
             '155-A': 'ZX',
             '162-A': 'ZX',
             '183-A': 'ZX',
             '191-A': 'ZX',
             '195-A': 'ZX',
             '198-A': 'ZX',
             '199-A': 'ZX',
             '224-A': 'ZX',
             '225-A': 'ZX',
             '230-A': 'ZX'
             },
        "CatalyticResidues":
            {'RES1': 'H',
             'RES2': 'S',
             'RES3': 'D-E'
             },
        "Ligands": [{'1-L':
                         {'RigidBody': True,
                          'Packing': True,
                          'PerturbationMode': 'MC',
                          'PerturbationLoops': 1,
                          'nRandomTorsionPurturbation': 2,
                          'Energy': 'Full',
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
                          'ExcludedTorsions': [['C11', 'C14', 'C16', 'C17']]
                          },
                     },
                    ],
        "remove_tmp": False,
        "container_image": "/home/albertcs/GitHub/EAPM/AsiteDesign-container/asitedesign.sif",
        "container_path": "singularity"
    }

    rcode = asitedesign_container(
        input_pdb="/home/albertcs/GitHub/EAPM/biobb_asitedesign/biobb_asitedesign/test/data/asitedesign/Input_file.pdb",
        input_yaml="/home/albertcs/GitHub/EAPM/biobb_asitedesign/biobb_asitedesign/test/data/asitedesign/DesignCatalyticSite.yaml",
        params_folder="/home/albertcs/GitHub/EAPM/biobb_asitedesign/biobb_asitedesign/test/data/asitedesign/params",
        output_path="/home/albertcs/GitHub/EAPM/biobb_asitedesign/biobb_asitedesign/test/data/asitedesign/output.zip",
        properties=prop)


if __name__ == '__main__':
    main()
