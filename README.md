# ACL2023: Causal Matching with Text Embeddings: A Case Study in Estimating the Causal Effects of Peer Review Policies
This README.md provides an overview of the code repositories contained here 
and instructions on running the experiments described in the [paper](TBD):  
```bash
@inproceedings{TBD,
    title = "",
    author = "",
    booktitle = "",
    month = may,
    year = "2023",
    address = "",
    publisher = "Association for Computational Linguistics",
    url = "",
    pages = "",
    abstract = "",
}

```
The directories included contains the original code developed during the research process, adapted code for replication, and data from various models. It is suggested for reproduction to use the code in the 'new_notebooks' directory which has refactored code that follows proper programming design patterns.

## Directories

- ``data`` contains all the raw data, results, and evaluation data for the paper. The ''data/evaluation_data'' subfolder contains the title rating of the three raters for human evaluation.

- ``jupyter_notebooks`` contains notebooks for development during the research process and a one-click replication notebook ``jupyter_notebooks/text_causal_inference_word_embedding_matching.ipynb``

- ``new_notebooks`` contains notebooks for the different methods used within the paper labeled by section

- ``r_notebooks`` contains an R notebook used to create visualizations

## Setup

1. Clone this repository
2. Install dependencies
   ```bash
   conda env create -f environment.yml
   ```
3. Start jupyter notebooks
