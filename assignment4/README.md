# hkande-pdasari-pkapil-a3

a3 created for hkande-pdasari-pkapil

### Part 1: Part-of-speech tagging

- A basic problems in Natural Language Processing is part-of-speech tagging, in which the goal is to mark every word in a sentence with its part of speech (noun, verb, adjective, etc.)
- Implementing Parts of speech Tagging in three methods:

  - Simplified Model (Implemented using Naives Bayes )
  - Hidden Markov Model (Implemented using Viterbi algorithm)
  - Complicated Model (Implemented using MCMC- Gibb's Sampling Technique)

- First Step is to train the given data:

  - Storing the occurences of word with specificed pos label using dictionary of dictionaries.
  - Calculating the transition occurences of present label from the previous label using dictionary of dictionaries.
  - Maintaing the occurences of pos labels over all the sentences in file using dictionary.

- **Naives Bayes(Simplified Model)**

  - Probability is calculated as follows:
    - $P(label|Word) = max{P(Word|label)\, P(label) / P(Word)}$
  - Initialzed an array of particular sentence size with nouns.
  - Obtaining and storing all distinct parts of speech labels from the training data in a list.
  - For each word in a sentence,
    - Evaluate the likelihood for each distinct part of speech label by multiplying the emission probability of the word provided that is this pos label by the probability of that label in training data.
    - By comparing the probability to the probability of the preceding label, the maximum probability and associated label are maintained.
    - In a simplified model, the label with the maximum probability is allocated to the word.
  - After scanning the entire sentence, the array with labels is returned.

  - If any word is not detected in the training data, this model will fail. I'm presuming it's a noun so that it can cover various scenarios.

- **HMM - Viterbi**

  - Viterbi is dynamic programming technique to solve HMM model. Here, I used table of dictionaries to store the probabilities at each state for all hidden labels.
  - For the first word in a sentence we calculate initial probability as the probability of that label and multiplied with the emission probability of the word and store that into viterbi table.
  - Then, By iterating over all other words by calculating transition probabilities multiplied with the product of previous viterbi probability stored in that table and emission probability of that word. At each step for each label we store only the max probability obatined by computing the previous equation. Along with that, we also store the label from which this is transitioned.
  - We continue this step till the end of the sentence.
  - From the max probability obtained for the label at the last word we backtrack and get all the labels from where we transitioned and get to the start word and store all the labels into a list.

- **MCMC Gibbs Sampling**

  - To solve Complicated model, we are sampling the data using Gibbs sampling method.
  - Initially, I have taken a sample that is generated for simplified model for the sentence.
  - For each word I am sampling them with all distinct pos labels and calculating the posterior probabilities for each word over severla iterations and storing every value in a list.
  - Applied log for the probabilities since it generating lower values.
  - Then For every word in a sentence generated some number of samples and their posterior probabilities. From those we are taking the max posterior probability for every word to refine the label which is the best for the word.
  - Finally, we get a sample for every word which has high posterior probability from those we again pick max occurences of label for particular word and return the list of labels for the sentence.

- Challenges Faced:

  - While training the data initially, I was storing the occurences of word in dictionaries with bucket of values which has part of speech labels at even indices and their count of occurences in odd indices of the bucket to restrict collisions.
  - But it was very to difficult to find the probabilitis when needed iterating over the bucket consumed lot of time. Then thought using dictionary of dictionaries because of the faster lookup instead of using list as a buket tried using dictionary as a bucket which was a great relief.

  - For storing transition probabilities, to store first word label it was very difficult so I have 'start' to the transition of first word in sentence for a label.

### Part 2: Ice tracking

Problem Statement :In the given image we need to determine the airice and icerock boundary for this We need to determine the row number for every column with the highest image gradient for both airice and icerock boundary using three methods: simple, HMM - viterbi, and human feedback, given the edge strength map that quantifies how strong the image gradient is at each place.

1. Simple Technique:
   To find the airice boundary we searched for the row in each column with the maximum pixel value and used those rows to draw the boundary.
   And to find the icerock boundary too we searched for the row in each column with the maximum pixel value and there is atlest 10 rows difference below the airice boundary and used those rows to draw the boundary.

2.Bayes Net - Using Viterbi:
Emission Probability is for each row and each column edge_strength[current_row][current_col]/sum(edge_strength[:,current_col]).
Initial Probability : For each row we considered the emission probability in first column.
Transition probability : The Transition probability from one state to another is solely determined by the previous column. When the row difference between the columns is small, the transition probability is high; when the row difference is large, the transition probability is low. As we iterate through the column list, values that are close together have a higher chance of convergent to the transition function's maximum value. The main idea behind this method is that the horizon is constantly smooth, hence there should be no gaps between the rows.

Then by iterating over all the rows in each column and calculate the probability as log(Emission Probability)+log(previous viterbi probability stored in that table)+log(Transition probability). At each step for each label we store only the max probability obatined by computing the previous equation. Along with that, we also store the row number.

Repeat the previous step until we reach the last column

Likewise we detemine the airice and icerock boundaries using viterbi algorithm.

Note: We used log to avoid very small numbers (/NaN) during multiplication of probabilities.

3. Human Feedback:
   For human feedback we just used the previous viterbi algorithm and applied it from the given human feedback row and column.
   we have applied the viterbi in two directions one for the left side columns of the given column and the other one is for the right side of the given columns and at the end we combine the rows returned from the both sides.

### Part 3: Reading text

- In this question we were asked to implement a solution for recognizing letters in an image. We were asked to solve this problem using simple bayes net and HMM (viterbi algorithm)

- For solving this problem we made a custom class (DetectLetters) which trains on a text dataset and returns the solution for a simple bayes net and viterbi algorithm.

- **Training Phase**

  1. We read the text file and clean that file by removing all the characters which are not valid english language character.
  2. Calculate the initial probabilities. These are the probability of a character being used as the first letter of a sentence in the given text file. We took log of these probabilities for getting rid of numeric underflow problem.
  3. Calculate transition probabilities. These are the probability that a character is followed by another character. We calculate this from the training text file. We took log of these probabilities for getting rid of numeric underflow problem.
  4. Calculate emission probabilities. These are the probability of a test character looking similar to a train character. We calculate this by getting the matching pixels between a train and test pattern and then apply naive bayes on it. We took log of these probabilities for getting rid of numeric underflow problem.

- **Simple Bayes Net**

  - In the simple bayes net for each test character we just return the corresponding train character with the highest emission probability.

- **Viterbi Algorithm**

  - In viterbi algorithm we consider the transition probability, emission probability and probability of best part till that state

  - For the first word in a sentence we calculate initial probability as the probability of that label and multiplied with the emission probability of the word and store that into viterbi table.
  - Then, By iterating over all other words by calculating transition probabilities multiplied with the product of previous viterbi probability stored in that table and emission probability of that word. At each step for each label we store only the max probability obatined by computing the previous equation. Along with that, we also store the label from which this is transitioned.
  - We continue this step till the end of the sentence.
  - From the max probability obtained for the label at the last word we backtrack and get all the labels from where we transitioned and get to the start word and store all the labels into a list.
