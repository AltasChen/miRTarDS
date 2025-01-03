# miRTarDS
miRTarDS including **1,220,904** MTIs from miRTarbase, miRDB, and miRWalk, involving **6,085 genes** and **1,261 pre-miRNAs**. 

**Feature and Label**
The 'Support Type' column was further modified to serve as the label for classifying Pre-miRNA and Target Gene relationships. Relationships are categorized as 'Protein-level Interaction' when 'Functional MTI' is present but 'Functional MTI (Weak)' is not. This distinction is important because 'Functional MTI (Weak)' is identified through low-sensitivity experimental methods, such as sequencing and microarray. If only 'miRWalk' or 'miRDB' (or both) are present, the relationship is classified as 'Prediction Interaction'. The 'Hist' column was then utilized as a feature for performing binary classification between 'Protein-level Interaction' and 'Prediction Interaction' using a Random Forest classifier. The trained model has been saved as 'Random_Forest.pkl'. The data follows CC BY-NC 4.0.

**Data Reliability**
Our method is trained with MTIs from miRTarBase 2022. The data reliability can be assessed with the **2025_update_MTI** file, which contains new Functional MTIs validated via western blot and reporter assays from miRTarBase 2025. miRTarDS accurately recognized **518 out of 574 MTIs** using my method.

# License
Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

You are free to:

Share — copy and redistribute the material in any medium or format.
Adapt — remix, transform, and build upon the material.
The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

Suggested attribution:
"miRTarDS Database by Baiming Chen (baimingchen@link.cuhk.edu.cn) is licensed under CC BY-NC 4.0."

NonCommercial — You may not use the material for commercial purposes.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Notices:

You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.
No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.
For more information, visit the full license at:
https://creativecommons.org/licenses/by-nc/4.0/

# Citing the Data

If you use the data or any part of this project in your research or publication, please cite the following paper:

Chen, Baiming. "Refining Protein-Level MicroRNA Target Interactions in Disease from Prediction Databases Using Sentence-BERT." *bioRxiv*, Cold Spring Harbor Laboratory, 2024, doi:10.1101/2024.05.17.594604. Available at: https://www.biorxiv.org/content/10.1101/2024.05.17.594604v7.

Please use the following format for citation:
```
@article {Chen2024.05.17.594604,
	author = {Chen, Baiming},
	title = {Refining Protein-Level MicroRNA Target Interactions in Disease from Prediction Databases Using Sentence-BERT},
	elocation-id = {2024.05.17.594604},
	year = {2024},
	doi = {10.1101/2024.05.17.594604},
	publisher = {Cold Spring Harbor Laboratory},
	abstract = {miRNAs (microRNAs) regulate gene expression by binding to mRNAs, inhibiting translation, or promoting mRNA degradation. miRNAs are of great importance in the development of diseases. Currently, a variety of miRNA target prediction tools are available, which analyze sequence complementarity, thermodynamic stability, and evolutionary conservation to predict miRNA-target interactions (MTIs) within the 3{\textquoteright} untranslated region (3{\textquoteright}UTR). We propose a concept for further screening sequence-based predicted MTIs by considering the disease similarity between miRNA and gene to establish a prediction database of disease-specific MTIs. We fine-tuned a Sentence-BERT model to calculate disease semantic similarity. The method achieved an F1 score of 0.88 in accurately distinguishing protein-level experimentally (Western Blot, Reporter Assay, etc.) validated MTIs and predicted MTIs. Moreover, the method exhibits exceptional generalizability across different databases. The proposed method was utilized to calculate the similarity of disease in 1,220,904 MTIs from miRTarbase, miRDB, and miRWalk, involving 6,085 genes and 1,261 pre-miRNAs. The study holds the potential to offer valuable insights into comprehending miRNA-gene regulatory networks and advancing progress in disease diagnosis, treatment, and drug development.Competing Interest StatementThe authors have declared no competing interest.},
	URL = {https://www.biorxiv.org/content/early/2024/10/07/2024.05.17.594604},
	eprint = {https://www.biorxiv.org/content/early/2024/10/07/2024.05.17.594604.full.pdf},
	journal = {bioRxiv}
}
```


