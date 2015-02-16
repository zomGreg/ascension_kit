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

Multi-User Comparison
---------------------

.. code-block:: bash

   ➜  ascension_kit git:(master) ✗ python ascension_kit.py -l stth,Stroller,78291,Tariru,YumYum,zomgreg
   Fetching games for user(s) ['stth', 'Stroller', '78291', 'Tariru', 'YumYum', 'zomgreg']
   file is stale, downloading xlog for stth.
   file is stale, downloading xlog for Stroller.
   No cache found for 78291, downloading.
   file is stale, downloading xlog for Tariru.
   file is stale, downloading xlog for YumYum.
   file is stale, downloading xlog for zomgreg.
   +----------+-------------+------------+----------+------------+---------+---------+-------------+--------------+-------------+---------------+
   |   Player | Total Games | Ascensions |      Pct | Avg. Turns | Fastest | Slowest | Total Turns | Total Points | Avg. Points |    Time Spent |
   +----------+-------------+------------+----------+------------+---------+---------+-------------+--------------+-------------+---------------+
   |    78291 |         365 |        234 |  64.11 % |          0 |       0 |       0 |           0 |    386036215 |     1649727 |     0d 0h 0m  |
   |   Tariru |        1044 |        184 | 17.625 % |      28492 |    8108 |   61751 |     5242697 |    356090249 |     1935273 |   61d 12h 4m  |
   |   YumYum |         632 |        181 | 28.639 % |      35324 |   18924 |   85549 |     6393735 |    376671064 |     2081055 |  105d 9h 19m  |
   | Stroller |         546 |        303 | 55.495 % |      46077 |       0 |  110298 |    13961348 |    875575342 |     2889687 | 252d 23h 37m  |
   |     stth |        1412 |        500 | 35.411 % |      55880 |   20357 |  439465 |    27940163 |   3476855835 |     6953711 |  371d 6h 14m  |
   |  zomgreg |         355 |         34 |  9.577 % |      58479 |   33107 |  123889 |     1988301 |    119550072 |     3516178 |   26d 7h 38m  |
   +----------+-------------+------------+----------+------------+---------+---------+-------------+--------------+-------------+---------------+

What's Next, Then?
------------------

I'll probably add on a roles comparison.
