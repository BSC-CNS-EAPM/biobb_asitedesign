SIMULATION_PARAMS = {
    'ActiveSiteSampling': 'Coupled',
    'LigandSampling': 'Coupled',
    'DynamicSideChainCoupling': False,
    'SoftRepulsion': False,
    'MimimizeBackbone': True,
    'nNoneCatalytic': 1,
    'Ligands': {'1-L':
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
                },

    'Anneal': True,
    'kT_high': 500,
    'kT_low': 1,
    'kT_decay': True,
    'kT_highScale': True,
    'WriteALL': True,

    'RankingMetric': 'FullAtom',
    'SpawningMethod': 'Adaptive',
    'SpawningMetric': 'Split',
    'SpawningMetricSteps':
        ['0.8 FullAtomWithConstraints',
         '1.0 FullAtom'],

    'Time': 48

}
