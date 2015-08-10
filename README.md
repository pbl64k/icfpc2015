# ICFP Contest 2015: team "Replete With Abstract Joy" (ranked 37th in qualifiers)

This contest sucked. I enjoyed it. In that sense, it was similar to the 2013 (though much better than that godawful disaster).
The problem wasn't particularly interesting, as it was just solving Tetris on a hex* board, with a few bell and whistles.
Compared to 2013, there were live leaderboards, a story to surround the problem, and "quest" elements in that teams had to go
looking for "phrases of power" essential for good standings. So, a whole ton better than 2013.

I ended up at #37 in the qualifiers, which makes getting into the finals unlikely. My finest hour was at T-36, when I was
ranked fifth (see my-finest-hour.png). Unfortunately, I didn't submit anything for the lightning round. If only I had spent
less time procrastinating and mulling over how much the problem sucked, how tired I was, and how I had no idea as to how to
solve the goddamn problem, I feel I would've had a good chance to compete for the top 10 in the lightning. Certainly cutting
twelve hours off that result was far from impossible.

Anyway, I progressed through a bunch of different solvers, but all of those were based on the same basic DFS/BFS algo. All my
solvers considered just the current piece, and ignored the global optimization. Phrases of power were treated as atomic moves,
and despite the fact that I didn't have the proper scoring of phrases throughout the contest, my solvers were quite good at
generating those.

The big problem was how to score a final position of a given piece. Obviously, clearing a row is good, but most of the moves
do not result in that. The key problem was getting the solver to recognize that leaving gaps in the overall structure was
bad.

I used a variety of value functions, ranging from simply discounting the reachability from the starting position (but
reachability is a vague term, especially when we're considering more sophisticated multi-cell pieces), and eventually
getting to the point where I would consider:

1. Placing pieces lower to be a good thing.
2. Placing pieces connected to other pieces to be a good thing.
3. Placing pieces that do not increase row-wise partitioning to be a good thing.

This is pretty much what my final submission does.

All attempts to incorporate phrases of power into scoring resulted in suboptimal outcomes, so I just relied on BFS getting
the phrases of power into solutions naturally.

Apart from the phrase listed in the original specification ("ei!") and the three phrases listed in the qualification problem
initial positions ("ia! ia!", "r'lyeh", "yuggoth") I only managed to discover two other phrases related to the original
Cthulhu Mythos -- "necronomicon" and "yogsothoth". The rest of the phrases seemed to be related to the Extended Mythos
that I'm not familiar with. So even with the hints in the official twitter I felt I had little chance to discover those.

(*) triangular lattice
