import glob
import json
from collections import namedtuple
def extract_info_from_sdf(sdf_file,filter_file,filter_bool):
  F= open(sdf_file,'r')
  lines=F.read().split('\n')
  F.close()

  f_smiles = open(filter_file,'r')
  tem=f_smiles.read().split('\n')
  f_smiles.close()
  smiles_known={}
  for t in tem:
    smiles_known[t.split('&')[0]] =t.split('&')[1].split(' ')[1]

  mark=[]
  for (i,line) in enumerate(lines):#seperate sdf files
    if line=='$$$$':
      mark.append(i+1)

  information=[]
  for mi in range(len(mark)):
    if mi ==0:
      context=lines[:mark[0]]
    elif mi == len(mark):
      context = lines[mark[mi]:]
    else:
      context = lines[mark[mi-1]:mark[mi]]

    for ci in range(len(context)): #in each single sdf file, get pdbID, smiles
      if context[ci]=='>  <PdbId>':
        xtal_ID = context[ci+1]
      if context[ci]=='>  <SMILES>':
        smiles = context[ci+1]

    if filter_bool:
      if smiles in smiles_known.values():   #if smiles in 141 dataset
        information.append(xtal_ID+' '+smiles)
    else:
      information.append(xtal_ID+' '+smiles)
  information = list(set(information))
  return information,smiles_known


RCSB_sdf_file ="Ligands_noHydrogens_noMissing_397_Instances.sdf"
known141_file ="ligand_information.dat"
information,smiles_known =extract_info_from_sdf(RCSB_sdf_file,known141_file,True)


json_file = open("template.json", 'w')
for info in information:
  for s in smiles_known.keys(): # search from 141
    smile = info.split(' ')[1]  # get SMILE string from RCSD sdf file
    name = s
    binding_status = 'binder' #found holo crystal structure in RCSB
    if info.split(' ')[1] == smiles_known[s]: # search SMILES in sdf files
      xtal_ID = info.split(' ')[0] # PDB IDs
      thermal_DOI = ' '
      dG = ' '
      dG_er = ' '
      dH = ' '
      dH_er = ' '
      ITC_DOI = ' '
      xtal_DOI = ' '
      d = {
      "name":name,
      "SMILES":smile,
      "Binding Data":{
      "Thermal Shift":{
      "Binding":binding_status,
      "DOI": thermal_DOI
        },
      "Isothermal Titration Calorimetry":{
      "Delta G": dG,
      "Delta G error": dG_er,
      "Delta H": dH,
      "Delta H error": dH_er,
      "DOI": ITC_DOI
                    }
            },
      "Crystallographic structures":{
        xtal_ID:xtal_DOI
          }
        }
      if d !='':
        str = json.dumps(d) + ','
        json_file.write(str + '\n\n')
json_file.close()
