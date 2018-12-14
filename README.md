# CITe_Id

Sample information for CITe-Id and phosphoproteomics experiments from:

> Browne, C. M. _et al._ A Chemoproteomic Strategy for Direct and Proteome-wide Covalent Inhibitor Target-site Identification. _J Am Chem Soc_, doi:10.1021/jacs.8b07911 (2018).

### CITe-Id Experiments:

- Follow instructions for installing multiplierz proteomics library from https://github.com/BlaisProteomics/multiplierz \
    See also:
    > Alexander WM, et al.  Multiplierz v2.0: a python-based ecosystem for shared access and analysis of native mass spectrometry data. _Proteomics_ 2017;17:1700091.

- Spectral Processing script:
   - Download from https://github.com/BlaisProteomics/CITe-Id
   - Requireds argument (use one): THZ1-dtb or JZ128-dtb
   - The script takes a previously extracted .mgf file and writes a new processed .mgf to facilitate identification of covalent probe-modified peptides by Mascot . Details are described in: 
     >   Ficarro SB, B. C., Card JD, Alexander WM, Zhang T, Park E, McNally R, Dhe-Paganon S, et al. Leveraging gas-phase fragmentation pathways for improved identification and selective detection of targets modified by covalent probes. _Anal Chem._ **88** , 12248-12254 (2016).

### Common Mascot search parameters for all CITe-Id experiments:

- Precursor ion tolerance: 10 ppm
- Fragment ion tolerance: 0.025 da
- Proteome Database: latest human proteome from https://www.uniprot.org/proteomes
- Maximum precursor charge: +8 (inhibitor modification increases the average peptide charge state)
- Enzyme: trypsin
- Maximum missed cleavages: 2
- Fixed modifications: carbamidomethyl +57.021464 (C), iTRAQ4plex +144.102063 (N-term, K)
- Variable modifications: oxidation +15.994915 (M), deamidation +0.9848 (NQ)

#### THZ1 experiments:

- Included are two biological replicate multidimensional LC-MS/MS experiments of purified THZ1-dtb-labeled tryptic peptides. The competing inhibitor was THZ1.
- .Mgf files are created using the Spectral Processing script, with THZ1-dtb as the argument..
- iTRAQ reporter channels: 114: DMSO, 115: 350 nM THZ1, 116: 1 µM THZ1, 117: 5 µM THZ1
- Additional variable modification:  THZ1-dtb +993.462786 (C) (chemical structure: C(51) Cl H(64) N(11) O(8)) (modification includes a potential neutral loss of C(51) Cl H(64) N(11) O(8))

#### THZ531 experiments:

- Included are three (separated by date) biological replicate multidimensional LC-MS/MS experiments of purified THZ1-dtb-labeled tryptic peptides. The competing inhibitor was THZ531.
- .Mgf files are created using the Spectral Processing script, with THZ1-dtb as the argument.
- iTRAQ reporter channels: 114: DMSO, 115: 350 nM THZ531, 116: 1 µM THZ531, 117: 5 µM THZ531
- Additional variable modification:  THZ1-dtb +993.462786 (C) (chemical structure: C(51) Cl H(64) N(11) O(8)) (modification includes a potential neutral loss of C(51) Cl H(64) N(11) O(8))

#### JZ128 experiments:

- Included are two biological replicate multidimensional LC-MS/MS experiments of purified JZ128-dtb-labeled tryptic peptides. The competing inhibitor was JZ128.
- .Mgf files are created using the Spectral Processing script, with JZ128-dtb as the argument.
- iTRAQ reporter channels: 114: DMSO, 115: 350 nM JZ128, 116: 1 µM JZ128, 117: 5 µM JZ128
- Additional variable modification:  JZ128-dtb +987.533058 (C) (chemical structure: C(53) H(69) N(11) O(8)) (modification includes a potential neutral loss of C(53) H(69) N(11) O(8))

#### Phosphoproteomic Experiments:

- Included are two biological replicate multidimensional LC-MS/MS experiments of purified phosphopeptides. The order of conditions is reversed between the two experiments.

#### Mascot Search parameters:

- Precursor ion tolerance: 10 ppm
- Fragment ion tolerance: 0.025 da
- Proteome Database: latest human proteome from https://www.uniprot.org/proteomes
- Enzyme: trypsin
- Maximum missed cleavages: 2
- Fixed modifications: carbamidomethyl +57.021464 (C), TMT10plex +229.162932 (N-term, K)
- Variable modifications: oxidation +15.994915 (M), deamidation +0.9848 (NQ), phosphorylation +79.966331 (STY)

#### Reporter channel information:

##### Bio Rep 1 (2018-03-29 dates)

- PC3 PKN3 KO background with WT PKN3 expression via pCMV vector:
  - 126: DMSO, 127N: 1 µM JZ128, 127C: 1 µM THZ1, 128N: 1 µM JZ128-R
- PC3 PKN3 KO background with C840S PKN3 expression via pCMV vector:
  - 128C: DMSO, 129N: 1 µM JZ128, 129C: 1 µM THZ1, 130N: 1 µM JZ128-R
- PC3 PKN3 KO background with GFP expression via pCMV vector:
  - 130C: DMSO, 131N: 1 µM JZ128, 131C: 1 µM THZ1

##### Bio Rep 2 (2018-04-27 dates)

- PC3 PKN3 KO background with WT PKN3 expression via pCMV vector:
  - 131C: DMSO, 131N: 1 µM JZ128, 130C: 1 µM THZ1, 130N: 1 µM JZ128-R
- PC3 PKN3 KO background with C840S PKN3 expression via pCMV vector:
  - 129C: DMSO, 129N: 1 µM JZ128, 128C: 1 µM THZ1, 128N: 1 µM JZ128-R
- PC3 PKN3 KO background with GFP expression via pCMV vector:
  - 127C: DMSO, 127N: 1 µM JZ128, 126: 1 µM THZ1
