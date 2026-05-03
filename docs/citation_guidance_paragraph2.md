# Citation Guidance — Paragraph 2 (BMC Bioinformatics–Style Introduction)

## Context

The second paragraph of the introduction focuses on three related ideas:

1. **The challenge and expense of wet-lab validation** — experimental identification and validation of disease genes is costly and time-consuming.
2. **Computational / network-based approaches as an alternative** — methods that leverage the human interactome to prioritise candidate genes.
3. **Specific computational strategies** — disease-module discovery (expanding a seed set through the interactome) and gene-prioritisation via domain interactions.

The four papers listed below are all strong fits for this paragraph. Each maps onto a distinct claim within it, and together they provide methodological breadth without overlap.

---

## Paper-by-Paper Assessment

### 1. Ghiassian et al. (2015) — DIAMOnD

> S. D. Ghiassian, J. Menche, and A.-L. Barabási, "A DIseAse MOdule Detection (DIAMOnD) algorithm derived from a systematic analysis of connectivity patterns of disease proteins in the human interactome," *PLoS Comput Biol*, vol. 11, no. 4, e1004120, 2015.

**Fit:** ✅ Excellent — core methodological citation for disease-module discovery.

DIAMOnD is the canonical algorithm for iteratively expanding a seed set of known disease proteins through the human protein–protein interaction (PPI) network to identify disease modules. Citing it directly supports any claim about *computational module-discovery methods* and the network-disease-module paradigm.

**Suggested placement in paragraph 2:**

> "…several network-based methods have been proposed to identify disease modules by propagating information from known disease proteins through the interactome \[DIAMOnD\]…"

**BibTeX key:** `Ghiassian2015DIAMOnD`

```bibtex
@article{Ghiassian2015DIAMOnD,
  author    = {Ghiassian, Susan Dina and Menche, J{\"o}rg and Barab{\'a}si, Albert-L{\'a}szl{\'o}},
  title     = {A {DIseAse MOdule Detection (DIAMOnD)} algorithm derived from a
               systematic analysis of connectivity patterns of disease proteins
               in the human interactome},
  journal   = {PLoS Computational Biology},
  year      = {2015},
  volume    = {11},
  number    = {4},
  pages     = {e1004120},
  doi       = {10.1371/journal.pcbi.1004120}
}
```

---

### 2. Hormozdiari et al. (2015) — Autism Integrated Gene Networks

> F. Hormozdiari, O. Penn, E. Borenstein, and E. E. Eichler, "The discovery of integrated gene networks for autism and related disorders," *Genome Research*, vol. 25, no. 1, pp. 142–154, 2015.

**Fit:** ✅ Good — application-level citation demonstrating the value of integrating heterogeneous data for complex-disease gene discovery.

This paper integrates multi-omic and network data to discover gene networks underlying autism spectrum disorder (ASD). It exemplifies the broader claim that *heterogeneous biological data sources* (expression, PPI, co-expression, etc.) can be combined computationally to identify disease-associated genes, at a fraction of the cost of pure wet-lab screens.

**Suggested placement in paragraph 2:**

> "…integrating heterogeneous biological data within a network framework has enabled the identification of coordinated gene sets associated with neurodevelopmental disorders such as autism \[Hormozdiari2015Autism\]…"

**BibTeX key:** `Hormozdiari2015Autism`

```bibtex
@article{Hormozdiari2015Autism,
  author    = {Hormozdiari, Fereydoun and Penn, Osnat and Borenstein, Elhanan
               and Eichler, Evan E.},
  title     = {The discovery of integrated gene networks for autism and related disorders},
  journal   = {Genome Research},
  year      = {2015},
  volume    = {25},
  number    = {1},
  pages     = {142--154},
  doi       = {10.1101/gr.178855.114}
}
```

---

### 3. Tripathi et al. (2019) — Community Detection for Disease Modules

> B. Tripathi, S. Parthasarathy, H. Sinha, K. Raman, and B. Ravindran, "Adapting Community Detection Algorithms for Disease Module Identification in Heterogeneous Biological Networks," *Frontiers in Genetics*, vol. 10, p. 164, 2019.

**Fit:** ✅ Excellent — methodological citation for the community-detection branch of disease-module identification.

Tripathi et al. adapt classical graph-community-detection algorithms (e.g., Louvain, Infomap) to heterogeneous biological networks (PPI + pathway + co-expression) for the purpose of disease module identification. This complements DIAMOnD (a seed-propagation approach) by representing the *clustering / community-detection* family of methods.

**Suggested placement in paragraph 2:**

> "…complementary approaches based on community detection have been adapted to heterogeneous biological networks to delineate disease-relevant gene modules \[Tripathi2019Community\]…"

**BibTeX key:** `Tripathi2019Community`

```bibtex
@article{Tripathi2019Community,
  author    = {Tripathi, Biplav and Parthasarathy, Srinivasan and Sinha, Himanshu
               and Raman, Karthik and Ravindran, Balaraman},
  title     = {Adapting Community Detection Algorithms for Disease Module
               Identification in Heterogeneous Biological Networks},
  journal   = {Frontiers in Genetics},
  year      = {2019},
  volume    = {10},
  pages     = {164},
  doi       = {10.3389/fgene.2019.00164}
}
```

---

### 4. Wang et al. (2020) — Protein Domain Interaction Network for Gene Prioritisation

> W. Wang, Y. Zhou, M.-T. Cheng, Y. Wang, C.-H. Zheng, Y. Xiong, P. Chen, Z. Ji, and B. Wang, "Potential pathogenic genes prioritization based on protein domain interaction network analysis," *IEEE/ACM Transactions on Computational Biology and Bioinformatics*, 2020.

**Fit:** ✅ Good — citation for the *gene-prioritisation* branch of network approaches, specifically using domain-level interaction data.

Rather than working at the gene/protein level, this paper builds a protein-domain interaction network and uses it to rank candidate pathogenic genes. It therefore supports the claim that finer-grained interaction representations (domain–domain interactions, DDIs) can improve prioritisation accuracy, complementing PPI-level methods.

**Suggested placement in paragraph 2:**

> "…gene prioritisation has also been achieved using protein-domain interaction networks, which capture functional specificity beyond coarse protein-level interactions \[Wang2020Domain\]…"

**BibTeX key:** `Wang2020Domain`

```bibtex
@article{Wang2020Domain,
  author    = {Wang, Wei and Zhou, Yue and Cheng, Meng-Tao and Wang, Yan
               and Zheng, Chun-Hou and Xiong, Yi and Chen, Peng and Ji, Zhichao
               and Wang, Bing},
  title     = {Potential pathogenic genes prioritization based on protein domain
               interaction network analysis},
  journal   = {IEEE/ACM Transactions on Computational Biology and Bioinformatics},
  year      = {2020},
  doi       = {10.1109/TCBB.2020.2968752}
}
```

---

## Recommended Citation Order in Paragraph 2

Below is a fully annotated sample sentence sequence showing where each citation fits naturally in a BMC Bioinformatics–style paragraph. Insert your own BibTeX `\cite{}` calls (or numbered `[]` references) at the positions marked:

```
Identifying disease-associated genes is an important goal in biomedical
research because it supports the discovery of drug targets and biomarkers
for complex diseases; however, the systematic experimental validation of
candidate genes remains costly and time-consuming. Consequently, a wide
range of computational methods have been developed to leverage molecular
interaction networks for candidate gene identification and prioritisation
[Ghiassian2015DIAMOnD, Tripathi2019Community]. Within this framework,
disease modules — locally clustered subnetworks of the human interactome
whose components collectively participate in disease-relevant processes —
can be identified by iterative network-propagation from known disease
seeds [Ghiassian2015DIAMOnD] or by adapting community-detection
algorithms to heterogeneous biological networks [Tripathi2019Community].
Integration of multi-omic data has further enabled the discovery of
coordinated gene networks underlying specific complex disorders such as
autism spectrum disorder [Hormozdiari2015Autism]. Complementary
approaches exploit protein-domain interaction networks to achieve finer-
grained prioritisation of pathogenic gene candidates [Wang2020Domain].
```

---

## Summary Table

| Paper | BibTeX key | Role in paragraph 2 | Priority |
|-------|-----------|----------------------|----------|
| Ghiassian et al. 2015 (DIAMOnD) | `Ghiassian2015DIAMOnD` | Canonical disease-module discovery method (seed-propagation) | **High** |
| Tripathi et al. 2019 (community detection) | `Tripathi2019Community` | Complementary module-discovery via community detection | **High** |
| Hormozdiari et al. 2015 (autism networks) | `Hormozdiari2015Autism` | Application example: integrating heterogeneous data for complex disease | Medium |
| Wang et al. 2020 (domain interaction networks) | `Wang2020Domain` | Gene prioritisation via protein-domain interaction networks | Medium |

All four citations are appropriate and strengthen the paragraph. `Ghiassian2015DIAMOnD` and `Tripathi2019Community` are the most critical as they directly represent the two main families of disease-module discovery methods; `Hormozdiari2015Autism` and `Wang2020Domain` add concrete application evidence and a domain-level prioritisation perspective.

---

## Notes on Repository Bibliography Structure

This repository does not currently contain a `.bib` file or LaTeX/Markdown bibliography infrastructure. If you add one, place it at `docs/references.bib` and copy the BibTeX entries above into it. For a BMC Bioinformatics submission, BMC accepts both numbered Vancouver-style references and BibTeX-generated bibliographies via their LaTeX template (`bmcart.cls`).
