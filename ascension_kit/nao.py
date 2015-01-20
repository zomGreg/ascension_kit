# !/usr/bin/python
import urllib2
import bs4
import sys

def get_player_file(player_name):
    '''
    This function will save the associated player_name html file
    into the ./player_html directory.
    # TODO accept a list of player names and download in threads.
    '''

    # player_name="zomgreg"

    url = 'http://alt.org/nethack/player-all-xlog.php?player=%s' % (player_name)
    dir = './player_files/'

    response = urllib2.urlopen(url)

    html = response.read()

    return html

    # with open(dir + player_name + '.html', 'wb') as handle:
    #     response = requests.get(url, stream=True)
    #
    #     if not response.ok:
    #         print "OMGWTF I'm outta here."
    #         sys.exit(99)
    #
    #     for block in response.iter_content(1024):
    #         if not block:
    #             break
    #
    #         handle.write(block)

def process_html(player_file, player_name):
    '''
    Processes the html file.
    :param player_file:
    :return: lists of things
    '''
    dates, scores, roles, ascension_games = [], [], [], []
    soup = bs4._soup(player_file)
    # with open(player_file, 'rb') as html_file:
    # soup = bs4._soup(html_file.read())

    try:
        games = soup.findAll('pre')[0].string.split('\n')
    except IndexError:
        print "No games found for %s. Maybe check spelling?" % player_name
        sys.exit(99)

    for i in range(0, len(games) - 1):
        keys = [t.split('=')[0] for t in games[i].split(':')]
        values = [t.split('=')[1] for t in games[i].split(':')]
        all_games = dict(zip(keys, values))

        dates.append(str(all_games['deathdate']))
        scores.append(int(all_games['points']))
        roles.append(str(all_games['role']))

        if str(all_games['death']) == 'ascended':
            ascension_games.append(all_games)

    return dates, scores, roles, ascension_games

def html_to_xlog(player_file):
    '''
    Not currently used.

    takes in an html file and produces an xlog file without any
    of the html tags
    :param player_file:
    :return:
    '''
    with open(player_file, 'rb') as html_file:
        soup = bs4._soup(html_file.read())

        games = soup.findAll('pre')[0].string.split('\n')

        # Write to file
        player_name = os.path.splitext(os.path.basename(player_file))[0]
        with open('./xlog/' + player_name + '.xlog', 'wb') as player_xlog:
            for game in games:
                if game:
                    player_xlog.write(game + "\n")
