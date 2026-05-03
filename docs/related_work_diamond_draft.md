# Related Work — DIAMOnD Opening Paragraph (Draft)

## English Version (BMC Bioinformatics style)

Numerous computational approaches have been proposed to identify disease-associated genes and proteins by exploiting the topological structure of the human protein–protein interaction (PPI) network.
Among seed-based module-expansion methods, the DIAMOnD algorithm (Disease Module Detection) stands out as a principled and widely adopted approach.
Rather than relying solely on shared connectivity, DIAMOnD employs a *connectivity significance* measure—derived from the hypergeometric distribution—to rank candidate proteins by the statistical significance of their links to a growing seed set of known disease genes.
At each iteration, the highest-ranked candidate is added to the seed set, progressively expanding the disease module until a user-defined number of disease-associated components has been recovered [Ghiassian *et al.*, PLOS Computational Biology, 2015].
This iterative, statistically grounded strategy enables DIAMOnD to uncover disease-module members that would be missed by simpler neighbourhood-overlap heuristics, while remaining interpretable and computationally efficient on genome-scale interactomes.

---

## Persian Version (با اصطلاحات علمی انگلیسی جاسازی‌شده)

پژوهش‌های بسیاری رویکردهای محاسباتی متنوعی را برای شناسایی ژن‌ها و پروتئین‌های مرتبط با بیماری، با استفاده از ساختار توپولوژیکی شبکهٔ تعاملات پروتئین–پروتئین (protein–protein interaction; PPI)، پیشنهاد داده‌اند.
در میان روش‌های مبتنی بر گسترش از ژن‌های دانه (seed-based module expansion)، الگوریتم DIAMOnD (Disease Module Detection) به‌عنوان یکی از رویکردهای اصولی و پرکاربرد در این حوزه شناخته می‌شود.
این الگوریتم به‌جای تکیهٔ صرف بر اشتراک پیوندها، از یک معیار *معنی‌داری اتصال* (connectivity significance) برپایهٔ توزیع هیپرژئومتریک بهره می‌گیرد تا پروتئین‌های کاندیدا را بر اساس معنی‌داری آماری پیوندشان با مجموعهٔ بذر در حال رشد رتبه‌بندی کند.
در هر مرحله از اجرای تکرار (iteration)، بالاترین کاندیدا به مجموعهٔ seed افزوده می‌شود و به این ترتیب ماژول بیماری (disease module) به‌صورت گام‌به‌گام گسترش می‌یابد تا تعداد دلخواهی از اجزای مرتبط با بیماری بازیابی شود [Ghiassian *et al.*، PLOS Computational Biology، 2015].
این استراتژی تکرارشونده و آماری‌محور، DIAMOnD را قادر می‌سازد تا اعضای disease module را که با ابتکارهای ساده‌تر مبتنی بر همپوشانی همسایگی از دست می‌رفتند شناسایی کند، و در عین حال قابل‌تفسیر و از نظر محاسباتی کارآمد بر روی interactome‌های مقیاس ژنومی باقی بماند.
