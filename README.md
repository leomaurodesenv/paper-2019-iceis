# Detecting Influencers in Very Large Social Networks of Games

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1dce6011250d440bbb1ddec95d02886d)](https://www.codacy.com/app/leomaurodesenv/paper-2019-iceis?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leomaurodesenv/paper-2019-iceis&amp;utm_campaign=Badge_Grade)

This repository present three temporal feature extractors. Each extractor captures a specific characteristic of the a data stream. We used these extractors to infer features about players of well-known Super Mario Maker game (Nintendo Inc., Kyoto, Japan).   

_Paper:_ Leonardo Mauro Pereira Moraes, and Robson Leonardo Ferreira Cordeiro. **Detecting Influencers in Very Large Social Networks of Games**. _In 21th International Conference on Enterprise Information Systems (ICEIS), Crete, Greece, 2019_. ([Presentation](presentation.pdf))   
   
_Abstract:_ Online games have become a popular form of entertainment, reaching millions of players. Among these players are the game influencers, that is, players with high influence in creating new trends by publishing online content (_e.g._, videos, blogs, forums). Other players follow the influencers to appreciate their game contents. In this sense, game companies invest in influencers to perform marketing for their products. However, how to identify the game influencers among millions of players of an online game? This paper proposes a framework to extract temporal aspects of the players' actions, and then detect the game influencers by performing a classification analysis. Experiments with the well-known Super Mario Maker game (Nintendo Inc., Kyoto, Japan) show that our approach is able to detect game influencers of different nations with high accuracy.   
   
---
## Code

The pseudo-code is available on the paper, the following code is in **Python** (folder `/python/`).   

```python
#- Import the Extractors
from python/lr_extractor import LR_Extractor
from python/dr_extractor import DR_Extractor
from python/ca_extractor import CA_Extractor

#- Data Stream
X = [1, 2, 3, 4, 5, 6, 7] # time
Y = [0, 1, 4, 6, 6, 8, 9] # values

#- Features Extraction
ext1 = LR_Extractor()
ext2 = DR_Extractor()
ext3 = CA_Extractor()

feature1 = ext1.compute(X, Y)
feature2 = ext2.compute(X, Y)
feature3 = ext3.compute(X, Y)
```
   
-   See the commented code with an example in [Jupyter Notebook](jupyter/6-feature-extractors-example.ipynb).
   
---
## Also look ~

-   License: [Apache 2.0](LICENSE)
-   Created by Leonardo Mauro ~ [leomaurodesenv](https://github.com/leomaurodesenv/)
