# Lysozyme binding data
This repository serves as an aggregator of binding data of small molecules to model binding sites in T4 lysozyme mutants, as popularized by Matthews, Shoichet and others.
Such data has been extremely useful both experimentally and computationally as a model system for tests/applications of binding free energy calculations, so an updated repository providing all key binding data is important for the community.
Formerly, such data was aggregated on the Shoichet lab website under take-aways, but that data seems to have gone out of date and is not under version control, so we plan to instead maintain it here.


## Manifest

### Currently present
- `L99A`: Data on the T4 lysozyme L99A (apolar) cavity mutant, which binds benzene, toluene, and other nonpolar ligands.

### To be added
- `L99A/M102Q`: Data on the T4 lysozyme L99A/M102Q (polar) cavity mutant, which has similarities to L99A but also binds phenol.
- Possibly other cavities of interest (there are some recent variants of interest)

## Goals

The goals of this repository are to:
a) Provide a machine-parseable set of all known binding data for these binding sites, including literature references, PDB codes, affinities, etc.
b) Provide human access to the material of (a)
c) Provide additional annotations to (a) that may be of additional value to people, such as notes relating to multiple binding modes, multiple occupancy, etc.

## Contributors
(This lists contributors *to this repository*; for the data, we are obviously indebted to the many experimentalists who have collected the data in the Shoichet and Matthews labs and others. We list citations to the relevant papers with the data itself to the extent possible.)
- David Mobley (UCI)
- David Minh (Illinois Institute of Technology)
- Bing Xie (Illinois Institute of Technology)

## Licensing

Any code/software made available here is provided under the [MIT license](LICENSE) and any content/data is made available under the [CC-BY 4.0 license](LICENSE_cc).

## Change Log
- 8/23/18: Create repo and add L99A data from Minh/Xie.
