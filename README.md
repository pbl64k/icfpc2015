# ICFP Contest 2015: team "Replete With Abstract Joy" post-mortem (ranked 37th in qualifiers)

The team name is a slightly altered line from the song *Death To The World* by the H. P. Lovecraft Historical Society, which
is, of course, a parody of the famous carol. See e.g.:

https://www.youtube.com/watch?v=ptP0OR-e7rI

This contest sucked. I enjoyed it. In that sense, it was similar to the 2013 contest -- well, much better than that godawful disaster,
but distinctly inferior to some of the seriously awesome past contests, such as those held in 2011 and 2014.
The problem wasn't particularly interesting, as it boiled down to just solving Tetris on a board with hexagonal tiles (think honeycomb), with a few bells and whistles.
Compared to 2013, there were live leaderboards, a story to surround the problem, and "quest" elements in that teams had to go
looking for "phrases of power" essential for good standings.

I ended up at #37 in the qualifiers, which makes getting into the finals unlikely. My finest hour was at T-36, when I was
ranked fifth (see `my-finest-hour.png`). Unfortunately, I didn't manage to submit anything for the lightning round. If only I had spent
less time procrastinating and mulling over how much the problem sucked, how tired I was, and how I had no idea as to how to
solve the goddamn problem, I feel I would've had a good chance to compete for the top 10 in the lightning. Certainly shaving
twelve hours off the time needed to get that #5 submission was far from impossible.

Being misled by the pre-contest hints into thinking that the contest would have something to do with Turing machines, program
optimization, and, possibly, quantum computations, I spent quite some time preparing all sorts of potentially useful stuff in
Idris. Once the problem statement was released, I realized that all of that was completely useless to me, and the requirement to submit
a buildable solution to the organizers together with the need to do stuff like `curl`'ing and parsing the command line arguments
made Idris a highly suspect choice. So I quickly decided to abandon the original plan and go with Python 2.7 and PyPy. That
might have been a bad idea, as during the contest I often noticed that I was trying to write Haskell in Python -- longing for
lazy evaluation, persistent data structures etc. Oh well, what's done is done.

One of the first stumbling blocks for me was the seriously insane coordinate system. I actually don't know what is the right way
to handle that, but I discovered quickly enough that a small alteration (see `utils.py`) would lead to a system that has much
nicer properties, even though there are still some nasty details related to rotations. Consequently, I used that coordinate
system internally for all the operations involving translations, rotations, finding the neighbors etc.

Anyway, I progressed through a bunch of different solvers, but all of those were based on the same basic DFS/BFS algo looking
for a nice place to put a given piece on the board. All my
solvers considered just the current piece, and ignored the global optimization. Phrases of power were treated as atomic moves,
and despite the fact that I didn't have the proper scoring of phrases throughout the contest (couldn't be bothered), my solvers were quite good at
generating those.

The big problem was how to score a final position of a given piece. Obviously, clearing a row is good, but most of the moves
do not result in that. The key problem was getting the solver to recognize that leaving gaps in the overall structure was
bad. The kicker was that the algo needed to be reasonably efficient. Arguably, my final solution really isn't, but some of the
things I tried -- or considered -- were even worse in that respect, despite being more promising optimization-wise. I really
wanted to tinker with something like partition refinement and relatives but found no way to achieve reasonable performance
for evaluating a given position.

So I tried a variety of value functions, ranging from simply attempting to maximize the reachability of the board cells from the starting position (but
reachability is a vague term, especially when we're considering more sophisticated multi-cell pieces), and eventually
got to the point where I would simply consider:

1. Placing pieces lower to be a good thing.
2. Placing pieces connected to other pieces to be a good thing (essentially trying to maximize the filled neighbors of the given piece's cells).
3. Placing pieces that do not increase row-wise partitioning to be a good thing (which has obvious deficiencies, but it is really quick to compute, and adds a dash of sanity to the solver).

This is pretty much what my final submission does.

All my attempts to incorporate phrases of power into scoring resulted in suboptimal outcomes, as the solver would start to try stuffing as many phrases
as possible into the solution, with rather debilitating results to the packing efficiency, so I just relied on BFS getting
the phrases of power into solutions naturally.

Apart from the phrase listed in the original specification ("ei!") and the three phrases found in the 
initial positions of the provided problems ("ia! ia!", "r'lyeh", "yuggoth") I only managed to discover two other phrases related to the original
Cthulhu Mythos -- "necronomicon" and "yogsothoth". I also realized that the 51-character phrase is the famous one about the dreaming Cthulhu 
(actually it seems that both the original version and the English "translation" counted as phrases of power), but with it being so long I never
even bothered to try it, as I felt it would be largely useless and could degrade solver performance.
The rest of the phrases seemed to be related to the Extended Mythos
that I'm not familiar with (some guy named Stross and an obscure movie from the 80s, stuff like that).
So even with the hints in the official twitter I felt I had little chance to discover those. Larger teams had a big advantage here, as
they could dedicate the efforts of one or two of the team members to just discovering the phrases, and those played an important
role in the qualifying round, if not in the final, as adding two phrases to my solver about mid-contest resulted in a significant
improvement in my scores. Having more would have been even better.

I spent much of the last few hours on the contest simply gathering stats on my submissions to evaluate the different algos
and put together the best solutions for all the qualifying problems. Thankfully, the organizer's web service provided a
complete list of submitted solutions, as I managed to misplace some of the early ones that actually turned out to be quite
good, and thanks to my rather messy usage of git I would've had a hard time reproducing those from scratch. That was likely
worth a bunch of points to me.

Unfortunately, my final submission is unable to monitor and control its memory consumption, and cannot utilize multiple
cores if available, but as I don't expect to get into the finals that doesn't really matter.

All in all, solid fun, okay performance -- I met my minimum goal of getting into the top 50, but could've been better.
