Ascension Kit
=============

Hello and welcome to ascension kit!

What is this?
-------------

Ascension Kit is a project I hacked together to show ascension details from the NAO player files.

How do I get it?
----------------

pip
^^^

.. code-block:: bash

   pip install ascension_kit

easy_install
^^^^^^^^^^^^

.. code-block:: bash

   easy_install ascension_kit

I recommend working in a virtual environment, if you have that option, so something like:

.. code-block:: bash

   ➜  virtualenv --no-site-packages ak

   New python executable in ak/bin/python2.7
   Also creating executable in ak/bin/python
   Installing setuptools, pip...done.
   
   ➜  activate
   
   (ak)➜  pip install ascension_kit


What does it do?
----------------

I'm glad you asked. It displays information about player ascensions, and will
return a table of user data if multiple user names are passed.

Single User
^^^^^^^^^^^

.. code-block:: text

   ascension-kit -l zomgreg

   Fetching games for user(s) ['zomgreg']
   File is still fresh. Using local cached file for zomgreg.
   
                [ Ascensions ]             
   
   Total Games                              367
   Ascensions                               37 (10.08%)
   Average turns/ascension                  58,000
   Fastest Ascension                        33,107
   Slowest Ascension                        123,889
   
   Total Ascension Turns                    2,146,018
   
   Total Points                             140,066,286
   Average Points/Ascension                 3,785,575
   Time Spent Ascending                     27 days 15 hours 59 minutes

Multiple Users
^^^^^^^^^^^^^^

The format for a multiple user call is a table.

.. code-block:: text

   ascension-kit -l zomgreg,bose,stth,anselmus,stenno,raisse,rschaff

   Fetching games for user(s) ['zomgreg', 'bose', 'stth', 'anselmus', 'stenno', 'raisse', 'rschaff']
   File is still fresh. Using local cached file for zomgreg.
   File is still fresh. Using local cached file for bose.
   No cache found for stth, downloading.
   No cache found for anselmus, downloading.
   No cache found for stenno, downloading.
   No cache found for raisse, downloading.
   No cache found for rschaff, downloading.

   +----------+-------------+------------+----------+------------+---------+---------+-------------+--------------+-------------+---------------+
   |   Player | Total Games | Ascensions |      Pct | Avg. Turns | Fastest | Slowest | Total Turns | Total Points | Avg. Points |    Time Spent |
   +----------+-------------+------------+----------+------------+---------+---------+-------------+--------------+-------------+---------------+
   | anselmus |         317 |         66 |  20.82 % |       8230 |       0 |   34405 |      543194 |    105952222 |     1605336 |  15d 17h 19m  |
   |   stenno |        2463 |        112 |  4.547 % |      21367 |   13572 |   44155 |     2393117 |    209373612 |     1869407 |   39d 7h 48m  |
   |     bose |        1419 |         57 |  4.017 % |      41232 |   26566 |   62440 |     2350273 |    209160008 |     3669473 | 118d 15h 34m  |
   |   raisse |        5988 |         56 |  0.935 % |      49041 |   31391 |   72425 |     2746299 |    186718579 |     3334260 |  52d 18h 43m  |
   |     stth |        1416 |        504 | 35.593 % |      55808 |   20357 |  439465 |    28127462 |   3504005732 |     6952392 |  373d 2h 14m  |
   |  zomgreg |         367 |         37 | 10.082 % |      58000 |   33107 |  123889 |     2146018 |    140066286 |     3785575 |  27d 15h 59m  |
   |  rschaff |        1159 |        207 |  17.86 % |      65794 |   35290 |  270229 |    13619559 |   1017595855 |     4915922 | 126d 14h 10m  |
   +----------+-------------+------------+----------+------------+---------+---------+-------------+--------------+-------------+---------------+

The player table is sorted by average turns, in ascending (heh, get it?) order.
Some of the data in the xlog files is incomplete, that's why anselmus seems to
have had a game with a 0-turn ascension. I'm not entirely sure what is the
cause of this anomaly, but I think it's to do with earlier game versions.

How does this work?
-------------------

Each player on NAO (http://alt.org/nethack/) has a player xlog file kept for
the games they've played. This utility fetches that file, and parses it to
present the data shown.

`Here is my xlog file <http://alt.org/nethack/player-all-xlog.php?player=zomGreg>`_

Files are fetched and saved to the `/tmp` directory and the cache timeout
period is 24 hours, which means the utility will not attempt to download an
xlog file if it was downloaded less than 24 hours ago. This is an effort to be
nice to the NAO server.
