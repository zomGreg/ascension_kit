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

def check_cache(player_name):

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

def get_player_file(player_list):
    '''
    This function will save the associated player_name html file
    # TODO accept a list of player names and download in threads.
    # TODO cache files for a length of time so we aren't always hitting the server.
    '''

    for p in player_list.split(','):

        if check_cache(p):
            file = './tmp/'+p+'.html'

            if not is_stale(p):
                print "File is still fresh. Using local cached file for %s." % (p)
            else:
                print "file is stale, downloading"
        else:
            print "No cache found, downloading."
            download_file(p)
            file = './tmp/'+p+'.html'

    return file

def process_html(player_file):
    '''
    Processes the html file(s) of the users
    :param player_file:
    :return: lists of things
    '''
    dates, scores, roles, ascension_games = [], [], [], []
    with open('./tmp/'+player_file+'.html', 'r') as file:
        soup = bs4._soup(file)

    try:
        games = soup.findAll('pre')[0].string.split('\n')
    except IndexError:
        print "No games found for user %s. Maybe check spelling?" % os.path.basename(player_file).split('.')[0]
        os.remove('./tmp/'+player_file+'.html')
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
