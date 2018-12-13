# CITe-Id Scripts Repository



Code repository for:

Browne, C.M., Jiang, B., Ficarro, S.B., Doctor, Z.M., Johnson, J.L., Card, J.D., Sivakumaren, S.C., Alexander, W.M., Yaron, T., Murphy, C.J. and Kwiatkowski, N.P., 2018. A Chemoproteomic Strategy for Direct and Proteome-wide Covalent Inhibitor Target-site Identification. Journal of the American Chemical Society.


## To use the inhibitor fragment subtractor:
* Follow instructions for [installing multiplierz](https://github.com/BlaisProteomics/multiplierz/wiki/Installation)
* Download the [inhibitor fragment subtractor script](https://github.com/BlaisProteomics/CITe-Id/blob/master/Inhibitor%20Fragment%20Ion%20Subtractor.py)
* Run from the command line with the appropriate argument: THZ1-dtb or JZ128-dtb

The script takes a previously extracted .mgf file and writes a new .mgf minus a number of high intensity fragment ions common to each inhibitor-modified peptide spectrum that greatly hinder peptide assignment by Mascot.
