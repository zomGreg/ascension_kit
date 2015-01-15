#!/usr/bin/python
import requests
import sys, os
import bs4
import collections
from sets import Set
import utils

def get_player_file(player_name):
    '''
    This function will save the associated player_name html file
    into the ./player_html directory.
    '''

    #player_name="zomgreg"

    url='http://alt.org/nethack/player-all-xlog.php?player=%s' % (player_name)
    dir='./player_files/'

    with open(dir+player_name+'.html', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print "OMGWTF I'm outta here."
            sys.exit(99)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

def html_to_xlog(player_file):
    '''
    takes in an html file and produces an xlog file without any
    of the html tags
    :param player_file:
    :return:
    '''
    with open(player_file, 'rb') as html_file:
        soup = bs4._soup(html_file.read())

        games=soup.findAll('pre')[0].string.split('\n')

        # Write to file
        player_name=os.path.splitext(os.path.basename(player_file))[0]
        with open ('./xlog/'+player_name+'.xlog', 'wb') as player_xlog:
            for game in games:
                if game:
                    player_xlog.write(game+"\n")

def process_ascensions(ascension_list, total_games):
    roles = [str(g['role']) for g in ascension_list]
    race = [str(g['race']) for g in ascension_list]
    gender0 = [str(g['gender0']) for g in ascension_list]
    gender = [str(g['gender']) for g in ascension_list]
    align0 = [str(g['align0']) for g in ascension_list]
    align = [str(g['align']) for g in ascension_list]
    points = [int(g['points']) for g in ascension_list]
    turns = [int(g['turns']) for g in ascension_list]
    dates = [str(g['deathdate']) for g in ascension_list]
    maxlvl = [int(g['maxlvl']) for g in ascension_list]
    realtime = [int(g['realtime']) for g in ascension_list]

    print ''
    print '{:^40}'.format('[ Ascensions ]')
    print ''

    print '{:40} {:,}'.format('Total Games', total_games)
    print '{:30} {:>10} ({:.2%})'.format('Ascensions', len(points), float(len(points))/float(total_games))
    print '{:40} {:,}'.format('Average turns/ascension', (sum(turns))/len(turns))
    print '{:40} {:,}'.format('Fastest Ascension', min(turns))
    print '{:40} {:,}'.format('Slowest Ascension', max(turns))
    print ''
    print '{:40} {:,}'.format('Total Ascension Turns', sum(turns))
    print ''
    print '{:40} {:,}'.format('Total Points', sum(points))
    print '{:40} {:,}'.format('Average Points/Ascension', (sum(points))/(len(points)))
    dhm = utils.seconds_to_days_hours_mins(sum(realtime))
    print '{:40} {} days {} hours {} minutes'.format('Time Spent Ascending', dhm[0], dhm[1], dhm[2])

    print ''
    print 'Ascended Roles'
    roles_counter = collections.Counter(roles)
    roles_set = Set(roles)

    rs,count = [], []
    z_total = 0
    for role in roles_set:
        rs.append(role)
        count.append(roles_counter[role])

        z_total = z_total+sum(utils.lookup_z[:roles_counter[role]])
        print '%s: %d %1.5f' % (role, roles_counter[role], sum(utils.lookup_z[:roles_counter[role]]))

    print ''
    print 'Z-score {:.8}'.format(z_total)

def process_html(player_file):
    '''
    Processes the html file.
    :param player_file:
    :return: lists of things
    '''
    with open(player_file, 'rb') as html_file:
        soup = bs4._soup(html_file.read())

    games=soup.findAll('pre')[0].string.split('\n')
    for i in range(0,len(games)-1):
        keys=[t.split('=')[0] for t in games[i].split(':')]
        values=[t.split('=')[1] for t in games[i].split(':')]
        all_games=dict(zip(keys,values))

        dates.append(str(all_games['deathdate']))
        scores.append(int(all_games['points']))
        roles.append(str(all_games['role']))

        if str(all_games['death']) == 'ascended':
            ascension_games.append(all_games)

    return dates, scores, roles, ascension_games

dates, scores, roles, ascension_games = [], [], [], []

#get_player_file('zomgreg')
#html_to_xlog('./player_files/zomgreg.html')
dates, scores, roles, ascension_games = process_html('./player_files/zomgreg.html')

process_ascensions(ascension_games, len(dates))

#a_game={u'align0': u'Neu', u'deathlev': u'-5', u'uid': u'5', u'deaths': u'0', u'turns': u'56614', u'points': u'2816148',
#        u'death': u'ascended', u'realtime': u'50761', u'version': u'3.4.3', u'role': u'Wiz', u'conduct': u'1280',
#        u'gender0': u'Mal', u'deathdate': u'20150112', u'hp': u'323', u'achieve': u'4095', u'gamedelta': u'625827',
#        u'maxlvl': u'52', u'maxhp': u'347', u'endtime': u'1421036204', u'nachieves': u'12', u'nconducts': u'2',
#        u'name': u'zomGreg', u'gender': u'Mal', u'align': u'Neu', u'birthdate': u'20150104', u'race': u'Hum',
#        u'flags': u'0', u'starttime': u'1420410377', u'deathdnum': u'7'}
