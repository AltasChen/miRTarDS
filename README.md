# miRTarDS
miRTarDS including **1,220,904** MTIs from miRTarbase, miRDB, and miRWalk, involving **6,085 genes** and **1,261 pre-miRNAs**. 

**Feature and Label**
The 'Support Type' column was further modified to serve as the label for classifying Pre-miRNA and Target Gene relationships. Relationships are categorized as 'Protein-level Interaction' when 'Functional MTI' is present but 'Functional MTI (Weak)' is not. This distinction is important because 'Functional MTI (Weak)' is identified through low-sensitivity experimental methods, such as sequencing and microarray. If only 'miRWalk' or 'miRDB' (or both) are present, the relationship is classified as 'Prediction Interaction'. The 'Hist' column was then utilized as a feature for performing binary classification between 'Protein-level Interaction' and 'Prediction Interaction' using a Random Forest classifier. The trained model has been saved as 'Random_Forest.pkl'. The data follows CC BY-NC 4.0.

**Data Reliability**
Our method is trained with MTIs from miRTarBase 2022, miRDB & miRWalk. The data reliability can be assessed with the **2025_update_MTI** file, which only contains new Functional MTIs validated via western blot and reporter assays from miRTarBase 2025. miRTarDS accurately identified **90% (518 out of 574) NEW MTIs**, which perfectly aligns with the recall rate of identified functional MTIs in miRTarBase 2022 (90%, as derived from miRTarDS and RF_classifier.py). This demonstrates that the model is convergent and capable of effectively handling new data.

**MeSHDS Dataset**
The training dataset MeSHDS used for fine-tuning SBERT model is available at: https://huggingface.co/datasets/Baiming123/MeSHDS

**Fine-tuned Model**
The Sentence-BERT (SBERT) model for calculating disease similarity associations between miRNAs and genes is available at: https://huggingface.co/Baiming123/Calcu_Disease_Similarity

# Application
To use miRTarDS, please follow these steps:
1. **Clone the Repository**: Clone the miRTarDS repository to local.
2. **Merge miRTarDS Parts**: Navigate to the miRTarDS folder and merge the components by running:
```
python merge_miRTarDS.py
```
3. **Run the Random Forest Classifier**: Benchmark miRTarDS by executing the Random Forest classifier with the following command:
```
python RF_classifier.py
```
Upon execution, the output will include model evaluation metrics (ROC and PRC curves, etc) and, optionally, the Random_Forest_Classifier.pkl file, which will be saved in the same folder.

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

Chen, Baiming. "Refining Protein-Level MicroRNA Target Interactions in Disease from Prediction Databases Using Sentence-BERT." *bioRxiv*, Cold Spring Harbor Laboratory, 2024, doi:10.1101/2024.05.17.594604. Available at: https://www.biorxiv.org/content/10.1101/2024.05.17.594604v8.

Please use the following format for citation:
```
@article {Chen2024.05.17.594604,
	author = {Chen, Baiming},
	title = {miRTarDS: High-Accuracy Refining Protein-level MicroRNA Target Interactions from Prediction Databases Using Sentence-BERT},
	elocation-id = {2024.05.17.594604},
	year = {2025},
	doi = {10.1101/2024.05.17.594604},
	publisher = {Cold Spring Harbor Laboratory},
	abstract = {MicroRNAs (miRNAs) regulate gene expression by binding to mRNAs, inhibiting translation, or promoting mRNA degradation. miRNAs are of great importance in the development of various diseases. Currently, numerous sequence-based miRNA target prediction tools are available, however, only 1\% of their predictions have been experimentally validated. In this study, we propose a novel approach that leverages disease similarity between miRNAs and genes as a key feature to further refine and screen human sequence-based predicted miRNA target interactions (MTIs). To quantify the semantic similarity of diseases, we fine-tuned the Sentence-BERT model. Our method achieved an F1 score of 0.88 in accurately distinguishing human protein-level experimentally validated MTIs (functional MTIs, validated through western blot or reporter assay) and predicted MTIs. Moreover, this method exhibits exceptional generalizability across different databases. We applied the proposed method to analyze 1,220,904 human MTIs sourced from miRTarbase, miRDB, and miRWalk, encompassing 6,085 genes and 1,261 pre-miRNAs. Our model was trained in miRTarBase 2022. However, we accurately identified 90\% (518/574) of the updated functional MTIs in miRTarbase 2025. This study has the potential to provide valuable insights into the understanding of miRNA-gene regulatory networks and to promote advancements in disease diagnosis, treatment, and drug development.Competing Interest StatementThe authors have declared no competing interest.},
	URL = {https://www.biorxiv.org/content/early/2025/01/04/2024.05.17.594604},
	eprint = {https://www.biorxiv.org/content/early/2025/01/04/2024.05.17.594604.full.pdf},
	journal = {bioRxiv}
}
```


