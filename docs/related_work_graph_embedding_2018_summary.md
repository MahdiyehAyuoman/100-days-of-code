# Related Work Draft — Graph Embedding on Biomedical Networks (2018 Survey)

> **Context:** This draft is intended to follow the opening sentence below in the
> *Network Embedding and Feature-based Methods* sub-section of the Related Work.
> The summary covers the survey paper:
> Yue *et al.*, "Graph embedding on biomedical networks: methods, applications and
> evaluations," *BMC Systems Biology* (2018).
> DOI: [10.1186/s12918-018-0662-y](https://doi.org/10.1186/s12918-018-0662-y)

---

## English Draft

**Opening sentence (provided):**

> In recent years, network embedding methods have emerged as powerful tools for
> disease-gene prioritization by encoding the global and local structure of the
> interactome into informative feature vectors.

**Continuation (2–3 BMC-style sentences summarising the paper):**

A comprehensive survey of this research direction is presented by Yue et al.
\cite{yue2018graph}, who systematically reviewed graph embedding approaches
applied to a broad range of biomedical networks, including protein–protein
interaction networks, gene–disease association networks, and drug–target
interaction graphs.
The authors categorised existing methods according to their underlying
algorithmic paradigms—spanning matrix-factorisation-based, random-walk-based,
and deep-learning-based techniques—and demonstrated their applicability to
diverse downstream tasks such as disease-gene association prediction, drug
repositioning, and protein function annotation.
Importantly, the survey also addressed key evaluation considerations, including
the choice of negative sampling strategies, network incompleteness, and
appropriate benchmarking protocols, providing practical guidelines for
comparative assessment of embedding models on biomedical graphs.

---

## Persian Translation / ترجمه فارسی

**جملهٔ آغازین (ارائه‌شده توسط نویسنده):**

> در سال‌های اخیر، روش‌های جاسازی شبکه (*network embedding*) به‌عنوان ابزارهایی
> قدرتمند برای اولویت‌بندی ژن‌های بیماری مطرح شده‌اند؛ زیرا ساختار محلی و سراسری
> اینتراکتوم را در قالب بردارهای ویژگی اطلاعاتی رمزگذاری می‌کنند.

**ادامهٔ پیشنهادی (۲–۳ جملهٔ آکادمیک):**

مروری جامع بر این حوزه توسط Yue و همکاران \cite{yue2018graph} ارائه شده است؛
آن‌ها به‌طور نظام‌مند رویکردهای مختلف جاسازی گراف را بر روی طیف گسترده‌ای از
شبکه‌های زیست‌پزشکی، از جمله شبکه‌های برهم‌کنش پروتئین–پروتئین، شبکه‌های
ارتباط ژن–بیماری و گراف‌های برهم‌کنش دارو–هدف، بررسی کردند.
نویسندگان روش‌های موجود را بر اساس پارادایم‌های الگوریتمی زیربنایی — شامل
روش‌های مبتنی بر تجزیهٔ ماتریس، گشت تصادفی، و یادگیری عمیق — دسته‌بندی کرده
و کاربرد آن‌ها را در وظایف پایین‌دستی متنوعی نظیر پیش‌بینی ارتباط ژن–بیماری،
باز‌موقعیت‌دهی دارو و حاشیه‌نویسی عملکرد پروتئین نشان دادند.
مهم‌تر از آن، این مطالعه به ملاحظات کلیدی ارزیابی — از جمله انتخاب استراتژی
نمونه‌گیری منفی، ناقص‌بودن شبکه و پروتکل‌های مناسب معیارسنجی — نیز پرداخت
و راهنمای عملی برای مقایسهٔ مدل‌های جاسازی در شبکه‌های زیست‌پزشکی ارائه داد.

---

## BibTeX Entry

```bibtex
@article{yue2018graph,
  title     = {Graph embedding on biomedical networks: methods, applications and evaluations},
  author    = {Yue, Xiang and Wang, Zhen and Huang, Jingong and Parthasarathy, Srinivasan
               and Moosavinasab, Soheil and Huang, Yungui and Lin, Simon M and Zhang, Wen
               and Zhang, Ping and Sun, Huan},
  journal   = {BMC Systems Biology},
  year      = {2018},
  doi       = {10.1186/s12918-018-0662-y},
  publisher = {BioMed Central}
}
```
