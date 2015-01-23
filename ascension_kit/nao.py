# !/usr/bin/python
import urllib2
import bs4
import sys
import os, time
import utils

def is_stale(player_name):
    file = './tmp/'+player_name+'.html'
    file_age = time.time() - os.path.getmtime(file)

    if file_age > 86400:
        return True
    else:
        return False

def check_cache(player_name, refresh = False):

    file = './tmp/'+player_name+'.html'

    if os.path.isfile(file):
        return True
    else:
        return False

def download_file(player_name):
    url = 'http://alt.org/nethack/player-all-xlog.php?player=%s' % (player_name)
    dir = './tmp/'

    response = urllib2.urlopen(url)

    html = response.read()

    with open(dir+player_name+'.html', 'wb') as f:
        f.write(html)

    return html

def get_player_file(player_name):
    '''
    This function will save the associated player_name html file
    # TODO accept a list of player names and download in threads.
    # TODO cache files for a length of time so we aren't always hitting the server.
    '''

    if check_cache(player_name):
        print "Using local cached file for %s" % (player_name)
        file = './tmp/'+player_name+'.html'

        if not is_stale(player_name):
            print "file is still fresh."
        else:
            print "file is stale, downloading"
    else:
        download_file(player_name)
        file = './tmp/'+player_name+'.html'

    return file


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
    with open(player_file, 'r') as file:
        soup = bs4._soup(file)
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
