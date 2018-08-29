# T4 Lysozyme L99A Binding Data

This contains binding data for the L99A mutant of T4 lysozyme, in JSON format.

## Source information
The source JSON material here was provided by Bing Xie and David Minh of the Illinois Institute of Technology and contains a set of 140 molecules for the T4 lysozyme L99A binding site from their [JCTC study](http://dx.doi.org/10.1021/acs.jctc.6b01183). Some of these are binders and some non-binders, and for a subset of the binders, binding affinity data is available.
The set was provided by Bing Xie in JSON format in December 2016, with additional supporting files provided in August, 2018.

The set was obtained via the following procedure (per Bing Xie):
> Firstly, I searched  “T4 lysozyme L99A” in http://www.rcsb.org, and collected all ligands information associated with the T4 lysozyme L99A in a csv file. (RCSB can do it) Since I already have the ligands SMILE strings (which are in ‘ligand_information.dat’), I matched them to the .csv file to get the PDB IDs.  For the crystal protein DOI (searched from RCSB), thermal DOI (from paper), ITC DOI (from paper) and ITC (from paper), I searched them manually.
When finished searching the PDB IDs from .csv file, I checked the IDs again and deleted the PDB IDs which are not exact mutant L99A. (the search function in RCSB is not very precise, it may contain some similar information with the search content)

In the JSON, some DeltaG (binding free energy) values are listed as `UNKNOWN` and otehrs are listed as `NOT ENTERED`. The difference between these is:
- `UNKNOWN`: The ligand was judged to be a binder based on thermal upshift and/or ITC and there is no binding affinity given in the literature (OR (?) there is no PDB code?)
- `NOT ENTERED`: The ligand is a nonbinder based on thermal upshift and/or ITC and there is no binding free energy available.

## Manifest
- `template.json`: Template file used by `new_json.py` which builds the full `T4_ligand_information.json` file
- `T4_ligand_information.json`: Full set of ligands with binding data, PDB codes, etc. when available.
- `Ligands_noHydrogens_noMissing_397_Instances.sdf`: SDF file containing PDB ligands
- `ligand_information.dat`: LaTeX-style document containing 141 known ligands with SMILES strings
- `new_json.py`: Extracts MUCH of the information in `T4_ligand_information.json` from the SDF file from the PDB, but does not extract quantitative values for binding (as these are not present in the PDB and had to be manually pulled from the literature, along with other binding data).

## To-dos:
- Add a "putative binder" column or similar, to handle cases where binding is detected (such as by ITC) but no thermal upshift is detected. This is unusual, but if I (Mobley) remember correctly happens occasionally.
- Consider adding space to indicate method for determining DeltaG's to accommodate other methods
- Add one or more "literature reference(s)" columns to have DOIs for the relevant papers; probably would be the last field as it could be wrong.
- Add a "notes" field for human-readable notes that might be relevant, such as "Binds two copies of the ligand in the binding site". This would not be useful for a machine, but otherwise it is unclear what should be done with this (important) information.
- Add script(s) to extract JSON to other useful formats
- Consider adding temperature and pH information
