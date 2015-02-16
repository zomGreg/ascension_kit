Ascension Kit
=============

Ascension kit is a pet project that parses nethack player xlog data from the
player files over at `NAO <http://alt.org/nethack/>`_

What is Nethack?
----------------

`Nethack <http://en.wikipedia.org/wiki/NetHack>`_ is a game. The public server
at alt.org processes a couple hundred games per day.

What's All This, Then?
----------------------

The primary reason I started this project was to learn more Python. I also
wanted to compare nethack players to see what interesting information could be
gained. 

NAO already provides a summary of user game data. `Here's a link to mine.
<http://alt.org/nethack/player-stats.php?player=zomGreg>`_

My early goals were these:

1. Provide a fast way to parse ascended game data for each player.
2. Provide a comparison of the ascension game information.

What's it do?
-------------

Single user ascension information:

.. code-block:: bash

   ➜  ascension_kit git:(master) ✗ python ascension_kit.py -l zomgreg
   Fetching games for user(s) ['zomgreg']
   File is still fresh. Using local cached file for zomgreg.
   
           [ Ascensions ]
   
   Total Games                    355
   Ascensions                     34 (9.58%)
   Avg. turns/ascension           58,479
   Fastest Ascension              33,107
   Slowest Ascension              123,889
   
   Total Ascension Turns          1,988,301
   
   Total Points                   119,550,072
   Avg. Points/Ascension          3,516,178
   Time Spent Ascending           26 days 7 hours 38 minutes



What's Next, Then?
------------------

I'll probably add on a roles comparison.
