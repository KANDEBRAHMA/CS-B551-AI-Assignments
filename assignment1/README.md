# a0

## Approach to Question 1 - Navigation

<h3>Abstraction:</h3>
<u><b>Set of Valid states</b></u>: Set of all probable locations on the map wherein pichu(<i>p</i>) cannot pass through a wall(<i>X</i>).<br><br>
<u><b>Successor Function</b></u>: This function takes the map, the visited nodes fringe, the path travelled, and the current location and returns a list of possible directions with respect to the current position, validating that movements should contain(<i>'.'</i>) and not a visited location that isn't on our path.<br><br>
<u><b>Cost Function</b></u>: The cost of a valid successor move is uniform: 1.<br><br>
<u><b>Goal State</b></u>: The position when we reach agent <i>@</i> in the shortest distance possible in the map is referred as goal state.<br><br>
<u><b>Initial State</b></u>: Pichu(<i>p</i>) and agent(<i>@</i>) are surrounded by walls(<i>X</i>) and valid positions(<i>.</i>) in the initial state, which is depicted by the map provided.<br><br>
<br><br>
<i><b>Finding the source of the program's failure based on my understanding of the problem statement?</b></i><br>
<p>The goal of this problem is to get Pichu to the agent in the quickest time feasible.<br><br>
When I first tried to comprehend the skeleton code, I discovered that it first locates the pichu<i>(p)</i> location by traversing the entire map and then stores the location in the fringe.
Then the successor function <b>moves</b> is invoked to traverse in four directions: <i>D-Down, U-Up, L-Left, R-Right</i>, attaching the valid direction(<i>conatins '.'</i>) to the fringe with the distance traveled thus far.
Finally, the <i>solve</i> function return the traveeled distance when pichu reaches agent, i.e., <i>@</i>.
However, if it chooses the wrong ways while traversing, this will enter an infinite loop since it will keep reviewing frequently accessed nodes which might or might not be part of the solution.</p>
<br>

<b><i>Included few validations for getting shortest path:</i></b>
<ol>
<li> My approach to the <i>infinite loop</i> problem is to keep a fringe with all the visited nodes and a validation in the successor function <i>moves</i> that not to pick already visited nodes. </li>
<li> I added the directions of move in the successor function when picking the next move to maintain track of the path. </li>
<li> When there is no path from pichu to agent, the skeleton code prints 'None.' Instead, I return <i>-1</i> when there is no path. </li> 
</ol>
<br><br>

## Approach to Question 2 - Hide & Seek
<h3>Abstraction:</h3>
<b>Directions</b>: Same Row, Same Column and Diagonally</b><br><br>
<u><b>Set of Valid states</b></u>: Set of all probable locations on the map wherein pichu(<i>p</i>) can be placed in a position that contains(<i>'.'</i>).<br><br>
<u><b>Successor Function</b></u>: This function takes the map and validates the position that has '.' and places the pichu at that position when it can't see any other pichu in all possible directions and returns the map.<br><br>
<u><b>Cost Function</b></u>: The cost of a valid successor move is uniform: 1.<br><br>
<u><b>Goal State</b></u>: The map's goal state is that a certain number of pichus are positioned in diverse positions so that no pichus can see each other.<br><br>
<u><b>Initial State</b></u>: Only one Pichu(<i>p</i>) and agent(<i>@</i>) are surrounded by walls(<i>X</i>) and valid positions(<i>.</i>) in the initial state, which is depicted by the map provided.<br><br>
<br><br>
<i><b>Finding the source of the program's failure based on my understanding of the problem statement and provided function?</b></i><br>
<p>Iterating over the map, the successor function adds all of the stated number of pichus in valid places (<i>'.'</i>) and returns the map as a solution, which is likely incorrect because most of the pichus can see each other.<br>
</p>
<br><br>
<b>My Approach to rearrange the placed pichus to reach goal state is as follows:</b>
<p>Along with checking the valid position('.'), I've introduced a function(<i>isSafe loc</i>) in the successor function that tells us the location where we can add pichu so that no other pichu is visiblefrom that position.<br>
My assumptions for approaching safe position is as follows:
<ul><li> If we encouter a wall('X') or agent('@') in any direction with no pichus visible then it is considered as safe position.</li><br>
<li>If we find other pichu in any one direction then it is considered as unsafe position and we dont place pichu there.</li></ul>

<br><br>
<b>Validations Included in new function(isSafe_loc):</b>
<p>Iterating over the map in all eight possible directions (Row upwards/downwards, Column upwards/downwards, Diagonally in all four directions) and ensuring that no other pichu is visible in all directions, we choose that spot and place the pichu.</br>
We evaluate whether the map has attained the goal state after placing each pichu in a safe location. If True, we return the most recent map in the fringe, with all required pichus put; otherwise, we try to iterate till we find a solution. </br>Finally, if no solution is found, we print False.</p>

