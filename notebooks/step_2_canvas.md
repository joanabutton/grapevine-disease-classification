# 1. Business Challenge
Wine is an important Portuguese industry, especially in the North, where vineyards are widespread. Managers and agronomists must monitor vines for visible disease, since timely detection supports earlier expert assessment and treatment. The challenge is to help teams identify disease symptoms and prioritise which grapevines need expert inspection.
# 2. Evidence from Reality
Portugal has nearly 170,000 hectares of vineyards and exported €954 million in wine in 2025 (Instituto da Vinha e do Vinho). Portuguese agricultural authorities document Black Rot in northern vineyards and emphasise monitoring disease symptoms to inform appropriate protection strategies (Estação de Avisos de Entre Douro e Minho, 2025).
# 3. People envolved
Vineyard workers collect leaf photographs following a systematic protocol. Agronomists assess flagged cases and recommend treatments. Vineyard managers and wine producers oversee operations and allocate resources. Data scientists develop and monitor the AI assisted solution. Wine merchants benefit indirectly from more reliable production.
# 4. Opportunity question
How could we use systematically collected vineyard photographs to prioritise which vines receive expert inspection and follow-up, while keeping agronomists in control of diagnosis and treatment decisions?
# 5. AI enabled move
Vineyard workers photograph leaves with mobile devices, through systematic sampling, during routine rounds. A CNN classifies images as Healthy, Black Rot, Esca or Leaf Blight, flagging potential disease symptoms for expert inspection. Agronomists retain responsibility for diagnosis and treatment.
# 6. Data and sources
Labelled grapevine leaf photographs (healthy and diseased) are needed. We use GVLiD v5 (Mendeley Data), containing 2,407 usable images from Indian vineyards after cleaning. Class imbalance, label inconsistencies and geographical differences limit generalisation. Expert-validated Portuguese vineyard images are needed for a future pilot.
# 7. Human workflow
1. Vineyard workers photograph leaves following a systematic sampling protocol.
2. Model classifies images and flags potential disease symptoms for expert review.
3. Agronomists inspect the vines with flagged leaves in situ.
4. Agronomists decide whether to monitor, investigate further or recommend treatment.
5. Expert-validated outcomes are logged for future model evaluation and improvement.
# 8. Trust and controls
# 9. Test horizons