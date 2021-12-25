# a1

## Approach to Part 1: The 2021 Puzzle

<h3>Abstraction:</h3>
<u><b>Set of Valid states</b></u>: Set of all probable boards which contains all unique numbers<br><br>
<u><b>Successor Function</b></u>: This function takes the board, generates all the possible boards by performing rotations i.e.,<b>{'R1','R2','R3','R4','R5','L1','L2','L3','L4','L5','U1','U2','U3','U4','U5','D1','D2','D3','D4','D5','Oc','Ic','Occ','Icc'}</b><br>
<p style="margin-left: 30px;">  where <b>R</b> stands for Right rotation of row for specified row,<br>
      <b>L</b> stands for Left rotation of row for specified row,<br>
      <b>U</b> stands for Up rotation of column for specified row,<br>
      <b>D</b> stands for Down rotation of column for specified row,<br>
      <b>Ic</b> stands for Inner clockwise rotation,<br>
      <b>Icc</b> stands for Inner counter-clockwise rotation,<br>
      <b>Oc</b> stands for Outer clockwise rotation,<br>
      <b>Occ</b> stands for Outer Counter clockwise rotation.<br></p>
After generating all the successor boards it calculates the heuristic_score for all boards and stores into the list.<br><br>
<u><b>Cost Function</b></u>: The cost of a generating successor is uniform: 1.<br><br>
<u><b>Goal State</b></u>: Board which contains all numbers from 1 to 25 in correct positions.<br><br>
<u><b>Initial State</b></u>: The board provided which has all unique numbers which are misplaced after certain valid rotations.<br><br>
<u><b>Heuristic Functions</b></u>: The first heuristic function I have used and thought of heuristic which was <b>Number of Misplaced Tiles</b> comparing to the goal state. Later in the process, I found it is overestimating for some boards along with that it was taking more amount to solve the board.

So, We thought of optimizing the heuristic function, so instead of above one tried implementing <b>Manhattan Distances</b> of each successor board which is better than the previous heuristic function which takes less time and got to know that this will be inadmissible when we are nearing the goal state.<br><br>

<br>
<i><h3>Description of Algorithm:</h3></i>
Implemented using uniform cost search algorithm with an heuristic and cost function.
<ol>
<li>I have used frontier(fringe) which is Priority Queue implemented using heapq module to store all the boards.Initially pushing the initial board on to the frontier.</li>
<li>Maintaing explored states which is empty at the initial point.</li>
<li>Looping till the frontier is not empty:</li>
<ol><li>Pop the board using heappop method in heapq module which gives the minheap board which has less heuristic score.</li>
<li>Checking whether the board popped is the goal state. If yes, the return and print the board.</li>
<li>Otherwise, add this board to explored list</li>
<li>Generate all the successors boards for this board.</li>

<ol>
<li>For each successor board, calculates the F_score which is the sum of heuristic score and no of rotations taken from the initial state to reach successor state.</li>
<li>If the successor board is not in explored and not in frontier, then heappush the board into frontier with f_score of that board.</li>
<li>If the successor board is in frontier with high f_score then the current successor board, then replace it with the current board.</li>
</ol></ol>
</ol></ol>

<b>1. In this problem, what is the branching factor of the search tree?</b><br>
The branching factor of this search tree is we get 24 childs(successors) everytime for a board.<br><br>

<b>2. If the solution can be reached in 7 moves, about how many states would we need to explore before we found it if we used BFS instead of A* search? A rough answer is fine.</b><br>
If we are implementing using BFS, we expand the board in level(breadth) from left to right wise. So for every board we get 24 child boards and for every child board we get other 24 childs so on till we get the goal board.

The branching factor is 24 because we have 24 valid rotations.<br>
<b>'R1','R2','R3','R4','R5','L1','L2','L3','L4','L5','U1','U2','U3','U4','U5','D1','D2','D3','D4','D5','Oc','Ic','Occ','Icc'}</b><br>
<br>
The simplified equation for finding how many states while using BFS approach is:
<br><p style="margin-left: 100px;"><b>
&sum;<sub>k=0</sub><sup>N</sup> 24<sup>k</sup>
    <br>where N here is 7 moves.</b>
</p>


## Approach to Part 2: Road trip!

<h3>Abstraction:</h3>
<u><b>Set of Valid states</b></u>: Set of all probable segments which has routes in road-segments file.<br><br>
<u><b>Successor Function</b></u>: Set of all possible segments has route from city1 which consists of parameters such as <b>distance,speedlimit,city1,city2,highwayname</b><br>
After generating all the successor routes we calculate the heuristic_score and cost_function for specified cost_attribute.<br><br>
<u><b>Cost Function</b></u>: We have four cost functions such as:
<br><ol><li>
    <b>Segments:</b>The cost for this is uniform 1 since we have only one edge from city1 to city2.
</li>
<li>
    <b>Distance:</b> The cost for this is the distance between city1 and city2 which is specified in road-segments file.
</li>
<li>
    <b>Time:</b> The cost for this is the time taken to travel from city1 to city2 which is evaluated by distance divided by speed_limit provided in road-segmensts file.
</li>
<li>
    <b>Delivery:</b> The cost for this is the time taken to deliver a product from city1 to city2. This will be evaluated by following conditions.
    <ul>
        <li>If the speed_limit is above 50 then there is 5% chance of falling out of the truck and the product gets damaged. So, while using this the probability of mistake is calculated as tanh(distance/1000)</li>
        <li>So the time taken would incrase by two times because he has to go back to start city and pick the product.</li>
        <li>If the speed_limit is less than 50 then there is no extra time_taken to deliver the product.</li>
    </ul>
</li>
</ol>
<br>
<u><b>Goal State</b></u>: Reaching end city on shortest possible cost function which will be specified by the user.<br><br>
<u><b>Initial State</b></u>: Initial state is the start city provided by the user.<br><br>
<u><b>Heuristic Functions</b></u>: Finding distance using latitude and longitude from current city to destination city which are provided in city-gps file.
For some of the cities, langitudes and longitudes are missing so for the city which is missing we are considering the heuristic score of the previous city and adding to to the current path distance which will be used as current city's heuristic score.
<br>
<i><h3>Description of Algorithm:</h3></i>
Implemented using A<sup>*</sup> algorithm with an heuristic and specified cost function.
<ol>
<li>Intially by using pandas module loading all the data from specified files to get road-segments and gps details and converting them to lists for better accessing. As mentioned, including the bidirectional condition as well.</li>
<li>Calculating the time taken for all segments and mistakes for delivery cost function and adding to the list.</li>
<li>Adding the start city into the frontier(fringe)</li>
<li>Maintaing explored routes which is empty at the initial point.</li>
<li>Looping till the frontier is not empty:</li>
<ol><li>Pop the latest city using heappop method in heapq module which gives the minheap board which has less f_score.</li>
<li>Checking whether the board popped is the destination city. If yes, the return and print the segments, distance travelled, time taken and delivery.</li>
<li>Otherwise, add this segment to explored list</li>
<li>Generate all the successors segments for this current_city.</li>

<ol>
<li>For each successor route, calculates the F_score which is the sum of heuristic score and cost function based on cost_attribute.</li>
<li>If the successor route is not in explored and not in frontier, then heappush the board into frontier with f_score of travelled route.</li>
</ol></ol>

</ol></ol><br>
References: Heuristic function idea is referred from https://python.plainenglish.io/calculating-great-circle-distances-in-python-cf98f64c1ea0

## Approach to Part 3: Choosing teams

From the survey form, we will get submitted person email address, group he wanted to work with (alone or decided group with 2 or 3 size or with missing roommates djcran-zzz-zzz or djcran-vkvats-zzz), members he don’t want to work with in comma separated values format.

<b>Given different time costs:</b>
<ol>
<li>5min to grade each assignment.</li>
<li>2min to read email sent by student if he is assigned to different group size.</li>
<li>If student is not assigned to someone they requested, then meeting time will be 0.05*60 min = 3min.</li>
<li>10min if a student is assigned with student whom he requested not to work with.</li>
</ol>

<b>Solution approach:</b>
<p>Firstly I have created cost functions for each of the above points to calculate the time spent by staff.

<ul>
<li><b>cost_per_team</b> – This function simply calculates numbers of total teams * 5</li>
<li><b>cost_wrong_groupsize</b> – This function calculates the cost of If a student is assigned to a wrong group size. Here I am comparing the team size the student is assigned to and the team size the student has entered in the survey form. If both the sizes are not same, I am adding 2 to the cost value.</li>
<li><b>cost_plagarism</b> – This function calculates the cost if a student is not assigned with a requested team mate and 5% of probability change and 60min for each meeting. So 0.05*60 overall =3.
Here I am checking for a student, if his preferred team member is present in his actual team. If not, I am adding 3 to the cost.</li>
<li>cost_exempt – This function calculated the cost if a student is assigned to a team member whom he requested not to work with. Here I am checking if the 3rd value a particular student entered in his survey form is present in the team which the student is assigned with. If yes then I am adding 10 to the cost.</li></ol><br>

Then, I have created possible teams from the students list randomly with size of 1 to 3 using randint

In the solver function, 
<ol>
<li>I have called possible_teams function by passing students list to the function and generated all the possible teams </li>
<li>Then I have called cost functions by passing the original survey and the possible teams.</li>
<li>Then I have compared the current_cost with the previous total_cost and updated total_cost, assigned_groups.</li> 
<li>This solver logic will be repeated till 100 sec.</li>
<li>In 100secs many random possible teams will be generated which will produce most of the possible teams and we can yield the minimum total_cost and assigned_group with minimun total_cost by the end of 100th sec.</li>
</ol>
