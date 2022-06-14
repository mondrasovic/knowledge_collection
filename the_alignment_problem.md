# The Alignment Problem - Brian Christian

## Chapter 1: "*Representation*"

### Problems with data

* **Lack of diversity**.
  * An example of `class imbalance` problem.
  * `Labeled Faces in the Wild` (`LFW`) dataset contains $77\%$ males, and more than $83\%$ white people. It contains more pictures of George W. Bush than all the black females combined.
* **Easy dissemination**.
  * Any inherent bias becomes pervasive.
* `Shirley Card` - Shirley Page, a Kodak employee, was the first person to pose for the `color-balance benchmark` test picture.
  * Dataset is the *Shirley Card* of some machine learning model.
* At the beginning, photos of black people were not of a good quality due to not paying attention to proper calibration.
  * It changed in the 60s and 70s, where furniture and chocolate industries focused on improving their pictures.
  * In the 90s the markerting was "*dark horse in low light*".
* Contrary to popular belief, many big tech companies and banks move glacially. Thus, if their models are trained on biased datasets, it becomes very problematic to change it down the road.

### Embeddings

* Unlike the `Bag-of-Words` (`BOW`) approach, i.e., word counting, embeddings are `distributed representations` that do not suffer from the `curse of dimensionality` as much. In a BOW approach, every word is the "same distance away" from others.
* **Training**.
  * `Contextual Bag-of-Words` (`CBOW`) - given a context, predict the middle word.
  * `Skip Grams` - given the middle word, predict a context.
* A useful tool to monitor society, both in retrospective and prospective ways (a "*big brother*").
* **Bias reinforcement**.
  * Resumé screening. The built-in bias reinforces who gets hired, thereby producing more biased data for subsequent model training.
* **De-biasing**.
  * It is like putting a "*lipstick on a pig.*"
  * `Principal Component Analysis` (`PCA`) was used to find the dimension that explained the greatest amount of variation between words pairs such as "*male*" and "*female*", or "*kind*" and "*queen*". The assumption was that the *gender* was responsible.
  * Removal of problematic relationships does not work.
    * In 1952, Boston Symphony Orchestra began holding its auditions with a screen placed between the performer and the judge. Others followed suit in the 70s and 80s. However, they also had to instruct the candidates to remove their shoes before walking onto the wooden floor of the audition hall.
      * "*Machine learning models can hear the shoes!*"


## Chapter 2: "*Fairness*"

## Top quotes

## Top trivia

## References