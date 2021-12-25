# a2

## Approach to Part 1: Raichu
<h2>Abstraction:</h2><br><br>
<b>Set of Valid States: </b>
<p>All legal moves made by the player's pichu(w/b) , pikachu(W,B) and raichu(@,$).</p><br><br>
<b>Successor Function:</b>
<p>This function takes board as a parameter and return the list of legal possible moves of the player pieces by validating all scenarios.</p><br><br>
<b>Cost Function:</b>
<p>Cost of generating legal move for the pieces available is uniform.</p><br><br>
<b>Goal State:</b>
<p>The goal state, according to the problem statement, is the best possible legal move for the board that maximizes the likelihood of a player winning within a defined timeframe.</p><br><br>
<b>Initial State:</b>
<p>Board consiting of pieces of two players to determine possible next move.</p><br><br>

<b>Description of Successor Function:</b><br>
<p>It takes board as a parameter.</p><br>
<b>Valid Pichu moves:</b>
<ol>
<li>Pichu can travel diagonally forward, i.e. left and right for one step which should be empty.</li>
<li>Furthermore, pichu can jump over other player single pichu, eliminating them from the board, and placing our pichu on the second step, which should be empty.</li>
</ol><br>
<b>Valid Pikachu moves:</b>
<ol>
<li>Pikachu can travel forward, left and right for one and two steps which should be empty.</li>
<li>Furthermore, Pikachu can jump over other player's single Pichu or Pikachu, eliminating them from the board, and placing our pikachu on second and third step, which should be empty.</li>
</ol><br>
<b>Valid Raichu Moves:</b>
<ol>
<li>Raichu is generated in the board whenever pichu or pikachu reaches the oppsoite end of the board.</li>
<li>Raichu can travel forward,left,right and diagonally as long as empty squares.</li>
<li>Furthermore, raichu can jump over other player's single Pichu,Pikachu and raichu as well, eliminating them from the board, and placing our raichu on any sqaure as long as empty sqaures in between.</li>
</ol>
<br>
<p>Based on the above rules, player generates all the legal moves and add them into the list which will be used to generate best possible move using min max algorithm.</p><br><br> 


<b>Description of Algorithm:</b><br>
<p>Implemented the <b>MIN-MAX</b> Algorithm along with <i>alpha-beta pruning</i> to disregard some states in order to determine the best next move for the given board.</p><br>
<ol>
<li>This algorithm takes (board,depth,maxplayer as boolean value,alpha,beta) values and returns the max move after exploring specified depth.</li>
<li>Algorithm creates a recursive tree starting with max moves and min moves recursively for specified depth and when it reaches the leaf node, evaluation function is invoked to calculate the score of the leaf board.</li>
<li>Using this algorithm, determines the optimal move among all the possible moves which increases the chance of winning by exploring the opponent's move by the move we make in recursive manner by minimizing their chance of winning and after certain depth evaluates the score of the leaf board and by bottom up approach takes the min score and gives to their parent board and max score of those will be given to their parent.when this reaches to the root move, we get the max move out of all the possible moves which can be safe and increase our chance of winning game.</li>
<li>We use alpha beta pruning, for ignoring some of the states which may not lead to the solution by expanding those moves.So we check alpha and beta everytime we expand, such that when beta value is less than the max value of min boards explored we ignore expanding those moves in same level.
Similarly when the alpha value is greater than the min value of max boards explored we ignore expanding that moves in same level.</li>
</ol>

<bR><br>

<b>Evaluation Function:</b>
<br>
<ol>
<li>Calculating the difference between left over pieces on board of each player.</li>
<li>Along with the above one, assigned some weights for pieces such that some pieces get more preference when they are present on board.
Calculating the weighted difference between left over pieces on board of each player.</li>
<li>Weights Assigned are:
<ul>
<li><b>Pichu:</b>1</li>
<li><b>Pikachu:</b> 10</li>
<li><b>Raichu:</b> 50 </li>
</ul></li></ol><br><br>

<p>Increasing depth everytime for minmax algorithm starting from 1, since there is a time limit by which the program gets killed.Thought of having atleast one move before exceeding the timelimit. So used this approach iteratively.</p><br>
<p>It was nice experience playing with AI on tank server ended in couple of draws and win.</p>

## Approach to Part 2: Tetris

The given problem statement asked us to implement an AI to play a tetris game.
The game has 6 types of figures that will be generated at random and at random orientations. 
The first thing we did was to create a successor function.  
The successor function gets the list of all possible moves for the figures being generated. Possible moves include moves in left and right directions as well as flipping the pieces. The next function holes_count gets a list of all the empty blocks in the board. The count_blocks function is used to count the number of spaces in the board that have 'x' in them. The get_best_move function uses the dictionary of successor moves. The function on a high level works in a DFS manner. It uses the dictionary of SUCC moves and checks for obstacles as well checks the best moves to get a row completely filled so as to get the highest possible score. The best moves are encoded as a string and then passed for the game to run. The program seems to run and returns a different score each time. Sometimes the program gets stuck in an infinte loop as well. Theoretically our ideas to implement the program worked well on paper but we faced a lot of difficulties in implementing it via code.

## Approach to Part 3: Truth be Told

<p>Initially, prepocessing the data by cleaning the train_data by removing stop words(most frequently used english word) which may result into wrong classification. Converting everything into lowercase letters by removing alpha-numeric characters in the train_data which results in improving accuracy of classification.</p><br>
<p>After cleaning the data, maintaining the occurrences of each words with label in a dictionary to look up when needed.</p><br>
<p>Applying Baye's rule to calculate posterior probability P(label|review_words) <i>i.e P(label|review_words)= P(review_words|label) *P(label). </i></p><br>
<p>Here, labels are Truth and deceptive. We ignore denominator P(review_words) in Bayes rule, because it is the same for both labels.</p>
<br>
<p>Based on the independence assumption in Baye's law, P(review_words|label) can be written as the product: P(w1|label)*.... * P(wn|label), for all words in the review. P(w1|label) is the frequency of word associated with the label, divided by all words associated with the label.
</p><br>
<p>In our first attempt, we got an classification accuracy of around 52%.</p>
<p>To improve accuracy and to handle zero word occurrencies which result in zero probability, used <i>Laplace smoothing</i> technique. Which will push the likelihood towards a values of 0.5 when using higher alpha values(1 in my case) and denominator is added with k*aplha where k is 2 i.e., the probability of a word equal to 0.5 for both the labels.</p><br>
<p>In our second attempt after introducing Laplace smmothing, we got an classification accuracy of around 78%.</p><br>
<p>We found that multiplying very small numbers will lead to even smaller numbers. To avoid those tried using log probabilities, which helped us in increasing accuracy to 85.75%.</p>

<b>For introducing log probabilites, We need to remember that multiplication operation becomes an addition in the logarithm space. So, taking the logarithm of the whole equation gives us below equation such as:</b><br>
<img src="https://github.iu.edu/cs-b551-fa2021/pdasari-hkande-hagana-a2/blob/master/part3/Log%20Probability%20formula.png"></img>

<p>References:</p>
For log Probabilites: https://www.baeldung.com/cs/naive-bayes-classification-performance
<br>
https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/

    

