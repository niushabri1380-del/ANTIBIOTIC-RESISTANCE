# RNA-seq Differential Gene Expression Analysis — Stress Response Signature (2025)
# NOTES (by Niusha)

- I structured this as a real portfolio project with:
  - reproducible scripts
  - clean folder layout
  - evaluation plots
  - a short written report
- In a real hospital dataset, I would also explore:
  - class imbalance and calibration
  - temporal split (train on earlier months, test on later months)
  - stewardship-relevant thresholds (high recall for resistant cases)

**Timeframe:** 2025  
**Context:** Transcriptomics / omics analysis (anonymized count matrix)

---

## Background (Why this matters)
RNA-seq enables genome-wide measurement of gene expression. Differential expression analysis identifies genes that significantly change between conditions (e.g., **control vs stress treatment**).  
These signatures help interpret biological pathways and can support biomarker discovery and downstream validation experiments.

---

## Key results
- **Approach:** log2 fold-change (TRT vs CTRL) + Welch’s t-test per gene + BH FDR correction  
- **Output table:** `outputs/differential_expression_results.csv`
- **Top genes (by FDR):**
- **Gene_133** (log2FC=-1.34, FDR=0.017)
- **Gene_154** (log2FC=2.00, FDR=0.017)
- **Gene_096** (log2FC=1.36, FDR=0.017)
- **Gene_039** (log2FC=-2.14, FDR=0.038)
- **Gene_061** (log2FC=-1.69, FDR=0.070)

---

## Outputs (plots)

### Volcano plot
![Volcano Plot](outputs/volcano_plot.png)

### Heatmap (Top 20 genes)
![Top 20 Heatmap](outputs/top20_heatmap.png)

---

## How to run

```bash
pip install -r requirements.txt
python scripts/rnaseq_de_analysis_v3.py
```

---

## Folder structure
- `data/` — anonymized RNA-seq counts  
- `scripts/` — analysis script  
- `outputs/` — plots + DE results  
- `report/` — short interpretation + personal notes  

---

## Author
**Niusha Bagheri** — portfolio project (2025)

---

## Tags
`python` · `rnaseq` · `omics` · `differential-expression` · `bioinformatics` · `data-analysis`

Run log (auto-generated)
ROC-AUC LR: 0.676
ROC-AUC RF: 0.617
