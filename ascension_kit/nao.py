# !/usr/bin/python
import requests
import sys
import bs4

def html_to_xlog(player_file):
    '''
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

def get_player_file(player_name):
    '''
    This function will save the associated player_name html file
    into the ./player_html directory.
    '''

    #player_name="zomgreg"

    url = 'http://alt.org/nethack/player-all-xlog.php?player=%s' % (player_name)
    dir = './player_files/'

    with open(dir + player_name + '.html', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print "OMGWTF I'm outta here."
            sys.exit(99)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

def process_html(player_file):
    '''
    Processes the html file.
    :param player_file:
    :return: lists of things
    '''
    dates, scores, roles, ascension_games = [], [], [], []
    with open(player_file, 'rb') as html_file:
        soup = bs4._soup(html_file.read())

    games = soup.findAll('pre')[0].string.split('\n')
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
