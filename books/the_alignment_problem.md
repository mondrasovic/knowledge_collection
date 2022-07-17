# The Alignment Problem - Brian Christian
## Chapter 1: "*Representation*"

### Problems with data

* **Lack of diversity**.
  * An example of `class imbalance` problem.
  * `Labeled Faces in the Wild` (`LFW`) dataset contains $77\%$ males, and more than $83\%$ white people. It contains more pictures of George W. Bush than all the black females combined.
* **Easy dissemination**.
  * Any inherent bias becomes pervasive.
* `Shirley Card` - Shirley Page, a Kodak employee, was the first person to pose for the `color-balance benchmark` test picture.
  * Dataset is the *Shirley Card* of some machine learning models.
* At the beginning, photos of black people were not of good quality due to not paying attention to proper calibration.
  * It changed in the 60s and 70s when the furniture and chocolate industries focused on improving their pictures.
  * In the 90s the marketing was "*dark horse in low light*".
* Contrary to popular belief, many big tech companies and banks move glacially. Thus, if their models are trained on biased datasets, it becomes very problematic to change them down the road.

### Embeddings

* Unlike the `Bag-of-Words` (`BOW`) approach, i.e., word counting, embeddings are `distributed representations` that do not suffer from the `curse of dimensionality` as much. In a BOW approach, every word is the "same distance away" from others.
* **Training**.
  * `Contextual Bag-of-Words` (`CBOW`) - given a context, predict the middle word.
  * `Skip Grams` - given the middle word, predict a context.
* A useful tool to monitor society, both in retrospective and prospective ways (a "*big brother*").
* **Bias reinforcement**.
  * Resumé screening. The built-in bias reinforces who gets hired, thereby producing more biased data for subsequent model training.
* **De-biasing**.
  * It is like putting "*lipstick on a pig.*"
  * `Principal Component Analysis` (`PCA`) was used to find the dimension that explained the greatest amount of variation between word pairs such as "*male*" and "*female*", or "*kind*" and "*queen*". The assumption was that the *gender* was responsible.
  * Removal of problematic relationships does not work.
    * In 1952, Boston Symphony Orchestra began holding its auditions with a screen placed between the performer and the judge. Others followed suit in the 70s and 80s. However, they also had to instruct the candidates to remove their shoes before walking onto the wooden floor of the audition hall.
      * "*Machine learning models can hear the shoes!*"


## Chapter 2: "*Fairness*"

* `COMPAS` - Correctional Offender Profiling for Alternative Sanctions.
  * A **linear model** based on a weighted average of features like age, age of the first arrest, criminal history, etc.
  * Its **prediction** was whether the defendant would re-offend within $1$-$3$ years.
  * `Exploratory data analysis` revealed that for black defendants, the distribution of re-offense scores was pretty uniform, whereas, in the case of white defendants, it was substantially skewed towards low-risk values.
  * `Calibration` was meant to assure that risk scores indicated equal probabilities of re-offending regardless of the race, which was shown to be correct.
    * Even though calibration is generally desirable, it provides little guarantee that decisions are equitable.
  * **Inherent flaw** in predictions was this. The model was $61$\% accurate. When its prediction was correct, race did not play a role. However, when the model was wrong, it was wrong in strikingly different ways for different races.
    * Black defendants were twice as likely to be rated as a higher risk but not re-offend. And white defendants were twice as likely to be charged with new crimes after being classed as lower risk.
* `Differential privacy` (**DP**) - A concept that allows companies to collect data about a population of users while maintaining the privacy of the individual users themselves.
  * It is a system for publicly sharing information about a dataset by describing the patterns of groups within the dataset while withholding information about individuals in the dataset.
  * Learn nothing about an individual while learning a lot about a population.
* `Redundant encoding` - When an attribute is **strongly correlated** with **other** attributes.
  * Thinking that removing an attribute indicating a race group will prevent a model from being discriminatory toward a particular group is flawed due to redundant encoding.
  * Simply omitting the `protected attribute` makes it impossible not only to measure the bias but also to mitigate it.
* **Cambridge Analytica** (**CA**) has been suspected of directly influencing political campaigns.
  * In $2016$, Donald Trump's campaign was supported by the work of CA.
    * The approach seemed innocuous at first. Roughly $300\ 000$ people received a survey in which they used a scale from "strongly agree" to "strongly disagree" they were supposed to indicate their preference (or lack thereof) regarding various personality traits. Moreover, they were paid less than $5$\$. However, a requirement was to log in with their Facebook account. Thus, their location, name, liked pages and everything else were exploited in conjunction with their questionnaire response.
* **Equalizing** `False Positive Rates` **(**`FPR`**)** - There is a **threat of asymmetry**. The issue is that once there is an endeavor to equalize FPR in a risk-assessment context, i.e., ensuring that defendants who won't re-offend are no more likely to be improperly detained whether they are black or white, would entail different standards as long as the actual offense rates between the two groups are different.
* Crime generally occurs within the community, not between communities.
* One of the most important things in any prediction is to make sure that you're actually predicting what you think you are.
  * In the context of criminal behavior. Does the data actually capture reoffense or is it rather rearrest or reconviction? The data shows samples of criminal behavior that were punished, not the ones that evaded capture.
  * These models are trained to predict crime that becomes known to the police. In other words, they are predicting policing, not a crime.
  * Criminals who manage to evade getting caught will be treated as low-risk, thereby influencing the models so that similar people would get released on the basis of such a prediction trained using biased data.
  * There is a threat of a potential **long-term feedback loop**.
  * In this setting, `selection bias` meets `confirmation bias`.
    * The system begins to sculpt the very reality it is meant to predict in the first place.
    * There is an old adage **Use Only As Directed**.
    * Imagine a model which predicts that the most reckless drivers are male. As a result, the police start aggressively pulling over male drivers. At the same time, female drivers realize they are less likely to be reprimanded or even punished with a fine, therefore, they become even more careless.
    
> The act of givingg a reason is the antithesis of authority. When the voice of authority fails, the voice of reason emerges, or vice versa.
* Predictions are not an end in themselves. You should not predict just to predict.
  * What is better. A world in which we are $99$\% sure when and where a crime will happen, or where there is $99$\% less crime in general?
* One of the fundamental assumptions of machine learning practice is that your training data matches the distribution of your test data. However, this flatly contravenes many common use cases in which there is an attempt to intervene with the future and change it.


## Chapter 3: "*Transparency*"

* People should have a right for an **explanation** of **algorithmically made decisions** influencing them.
* A real-world use case of machine learning for **predicting** whether to treat a patient as **inpatient or outpatient**. The found rule was the following: *If a patient has a history of asthma, then they are low-risk and you should treat them as such.*
  * The reason is that the data **captures a significant fact in an inappropriate way**. Asthma is considered as such a serious factor for pneumonia patients, that not only are they put in the hospital, but they are often treated right in the ICU. And fact causes such patient to appear to be low-risk since the attention they receive is enormous due to their history.
* `Generalized Additive Models`. A collection of graphs, each of which represents the influence of a single variable. It is basically a generalized linear model.
* `Explainable Artificial Intelligence` (`XAI`).
* `General Data Protection Regulation` (`GDPR`). In the context of deep learning, this is an intriguing problem. Getting intelligible **explanations out of a deep neural network** is an **unsolved scientific problem**, yet GDPR demands it.
* **Clinical vs. statistical prediction**. There was a case of a patient who thought that he was growing breasts. As a result, he was suspected to have been sufferring from schizophrenia. However, no one actually cared to see whether he could have been right. Well, he, as it turned out, was right. He suffered from **Klinefelter syndrome**, a genetic conditions caused by an additional X chromosome, that involves the development of breast tissue.
* **Linear model vs. a psychology expert**. The input to the model consisted of the student's high school class rank and their college aptitute test scores. On the other hand, the psychologist did not only have this information, but also results of additional tests, notes from the interview, and their firsthand impression of the student. There was **no measurable difference** between the two predictions.
  * The reason is that the student counselors themselvees did not place too much emphasis on the additional data, they also primarily relied on the school rank and test scores. However, their weighting was not as consistents as that of the model. And, obviously, the model can tune the weighting in an optimal fashion, therefore, achieving a slight competitive advantage.
* **Statistical analysis vs. human judgement**. The statistical analysis was thought to provide a floor to which the judgemnet of the experienced clinian could be compared. The floor turned out to be a ceiling. What's worse, even if the **clinian was provided with the model prediction, their judgement was still worse**.
  * However, these models were not just random linear combinations of random properties. They were random linear combinations of precisely the things that humans have established to be the most relevant and predictive things to consider through decades if not generations of best practices.
  * The **human expertise** is characterized by **knowing what to look for**, and **not** by **knowing the best way to integrate** that **information**.
* **Linear model to predict relationship harmony**. The linear prediction is the quintessence of simplicity. Subtract the rate of arguments from the rate of secual interaction. A positive difference means happiness, a negative one unhappiness. **This model turned out to be an extremely accurate predictor**.
  * `Conditionally monotone independence`. Despite enormous complexity of the real world, many high-level relationships are known as **conditionally monotone**, i.e., they do not interact with each other in particularly complex ways.
* **History is more relevant than symptoms**. Analysis of predictive models for patient health-related issues revealed that patient history was far more important for predictions than their immediate symptoms. In fact, even including the ongoing symptoms did not yield much of an improvement.
* `Cooperative eye hypothesis`. Why do we have distinctly large and visible sclera? Cooperation has been uncommonly important in our survival as species, to the point that the benefits of shared attention outweight the loss of a certain degree of privacy. In the context of machine learning, this is related to `saliency`.
* A neural network was trained to classify whether an image contains an animal or not. It turned out that it based its classification output solely on the presence of **Bokeh effect**.
  * `Bokeh effect`. The central image is focused whereas the background is blurred, creating an artistic impression.
* A neural network was trained to classify tumors (malignant vs. bening). It learned that the presence of a ruler in malignant tumors is a relevant feature to look for.
  * `Multi-task learning` helps to diminish these effects since the model is forced to output more things which may be useful for validation as well as reduction of overfitting.
* Dumbbell classification without a presence of an arm was severly impaired as well.
* Patient's gender and age can be determined purely based on the image of their retina. A neural network actually discovered a way to interpret blood vessels appropriately.

---

## Top quotes

> Out of the crooked timber of humanity, no truly straight thing was ever made.

> Our law punishes people for what they do, not who they are. Dispensing punishment on the basis of an immutable characteristic flatly contravenes this guiding principle.

> Fairness through blindness does not work.

> Your scientists were so preoccupied with whether or not they could... that they didn't stop to think whether they should.

> Sometimes the "ground truth" is not the ground truth.

> Providing overwhelming amount of information without adeuqate structure is not transparency.

> The act of givingg a reason is the antithesis of authority. When the voice of authority fails, the voice of reason emerges, or vice versa.

> The whole trick is to know what variables to consider and then  to know how to add.

## Top trivia

## References
