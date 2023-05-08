# BioBB ASITEDESIGN Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Asitedesign
Wrapper of the AsiteDesign module.
### Get help
Command:
```python
asitedesign -h
```
    /bin/sh: asitedesign: command not found
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_pdb** (*string*): Path to the input file pdb. File type: input. [Sample file](None). Accepted formats: PDB
* **input_yaml** (*string*): Path to the input file yaml. File type: input. [Sample file](None). Accepted formats: YAML
* **params_folder** (*string*): Path to the params folder. File type: input. [Sample file](None). Accepted formats: PARAMS
* **output_path** (*string*): Path to the output file. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cpus** (*integer*): (21) Number of cpus for the job..
* **name** (*string*): (DesignCatalyticSite_job) Name of the job, which will be used for the output folders..
* **DesignResidues** (*array*): (None) List of residues that want to be mutable during the simulation..
* **CatalyticResidues** (*array*): (None) Specify the number of residues of the active site that wants to be added (RES1, RES2 ... RESN: H)..
* **Ligands** (*array*): (None) 1-L (you have to specify the ligand by giving the residue number and the chain of the specific LIG). Also, the torsions that want to be excluded must be specified by the user ("ExcludedTorsions")..
* **Constraints** (*array*): (None) Add the distance and sequence constraints that you want. The distance constraints should be added by passing two residues (with residue_number-chain) and two atoms (atomname) and to which values you want to constraint them (lb: value in angstroms, hb: value in angstroms)..
* **nIterations** (*integer*): (20) Number of adaptive sampling epochs that want to be performed..
* **nSteps** (*integer*): (5) Number of steps performed in each epoch/iteration..
* **nPoses** (*integer*): (20) Number of final poses (mutants/designs) to be reported (each one given to a processor/CPU)..
* **Time** (*integer*): (48) Time in the queue (if it's run in a cluster)..
* **remove_tmp** (*boolean*): (True) Remove temporal files..
* **restart** (*boolean*): (False) Do not execute if output files exist..
* **container_path** (*string*): (docker) Container path definition..
* **container_image** (*string*): (bsceapm/asitedesign:X.X) Container image definition..
* **container_volume_path** (*string*): (/home/projects) Container volume path definition..
* **container_working_dir** (*string*): (/home/projects) Container working directory definition..
* **container_user_id** (*string*): (None) Container user_id definition..
* **container_shell_path** (*string*): (/bin/bash) Path to default shell inside the container..
### YAML
### JSON
