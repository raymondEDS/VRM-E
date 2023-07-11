# ACL2023: Causal Matching with Text Embeddings: A Case Study in Estimating the Causal Effects of Peer Review Policies
This README.md provides an overview of the code repositories contained here 
and instructions on running the experiments described in the [paper]([https://2023.aclweb.org/program/accepted_findings/#short-papers](https://aclanthology.org/2023.findings-acl.83/):  
```bash
@inproceedings{zhang-etal-2023-causal-matching,
    title = "Causal Matching with Text Embeddings: A Case Study in Estimating the Causal Effects of Peer Review Policies",
    author = "Zhang, Raymond  and
      Kennard, Neha Nayak  and
      Smith, Daniel  and
      McFarland, Daniel  and
      McCallum, Andrew  and
      Keith, Katherine",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2023",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.findings-acl.83",
    pages = "1284--1297",
    abstract = "A promising approach to estimate the causal effects of peer review policies is to analyze data from publication venues that shift policies from single-blind to double-blind from one year to the next. However, in these settings the content of the manuscript is a confounding variable{---}each year has a different distribution of scientific content which may naturally affect the distribution of reviewer scores. To address this textual confounding, we extend variable ratio nearest neighbor matching to incorporate text embeddings. We compare this matching method to a widely-used causal method of stratified propensity score matching and a baseline of randomly selected matches. For our case study of the ICLR conference shifting from single- to double-blind review from 2017 to 2018, we find human judges prefer manuscript matches from our method in 70{\%} of cases. While the unadjusted estimate of the average causal effect of reviewers{'} scores is -0.25, our method shifts the estimate to -0.17, a slightly smaller difference between the outcomes of single- and double-blind policies. We hope this case study enables exploration of additional text-based causal estimation methods and domains in the future.",
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
