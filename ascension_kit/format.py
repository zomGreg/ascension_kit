from sets import Set
import sys
import utils
import collections
from prettytable import PrettyTable

table = PrettyTable(['Player', 'Total Games', 'Ascensions', 'Pct', 'Avg. Turns', 'Fastest',
                     'Slowest', 'Total Turns', 'Total Points', 'Avg. Points', 'Time Spent'])

def process_ascensions(player_dict):

    for p in player_dict:
        if len(player_dict[p]['ascension_games']) == 0:
            print "No ascensions for %s. Total games: %s" %(p, len(player_dict[p]['dates']))
            sys.exit(99)

        roles = [str(g['role']) for g in player_dict[p]['ascension_games']]
        race = [str(g['race']) for g in player_dict[p]['ascension_games']]
        gender0 = [str(g['gender0']) for g in player_dict[p]['ascension_games']]
        gender = [str(g['gender']) for g in player_dict[p]['ascension_games']]
        align0 = [str(g['align0']) for g in player_dict[p]['ascension_games']]
        align = [str(g['align']) for g in player_dict[p]['ascension_games']]
        points = [int(g['points']) for g in player_dict[p]['ascension_games']]
        turns = [int(g['turns']) if g['turns'] else 0 for g in player_dict[p]['ascension_games']]
        dates = [str(g['deathdate']) for g in player_dict[p]['ascension_games']]
        maxlvl = [int(g['maxlvl']) for g in player_dict[p]['ascension_games']]
        realtime = [int(g['realtime']) if g['realtime'] else 0 for g in player_dict[p]['ascension_games']]
        total_games = len(player_dict[p]['dates'])
        dhm = utils.seconds_to_days_hours_mins(sum(realtime))

        if len(player_dict) == 1:
            print ''
            print '{:^30}'.format('[ Ascensions ]')
            print ''
            print '{:30} {:,}'.format('Total Games', total_games)
            #print '{:30} {:>10} ({:.2%})'.format('Ascensions', len(points), float(len(points)) / float(total_games))
            print '{:30} {:,} ({:.2%})'.format('Ascensions', len(points), float(len(points)) / float(total_games))
            print '{:30} {:,}'.format('Avg. turns/ascension', (sum(turns)) / len(turns))
            print '{:30} {:,}'.format('Fastest Ascension', min(turns))
            print '{:30} {:,}'.format('Slowest Ascension', max(turns))
            print ''
            print '{:30} {:,}'.format('Total Ascension Turns', sum(turns))
            print ''
            print '{:30} {:,}'.format('Total Points', sum(points))
            print '{:30} {:,}'.format('Avg. Points/Ascension', (sum(points)) / (len(points)))
            print '{:30} {} days {} hours {} minutes'.format('Time Spent Ascending', dhm[0], dhm[1], dhm[2])
            sys.exit(0)

        table.add_row([p, len(player_dict[p]['dates']),
                       int(len(points)),str(round((float(len(points)) / float(len(player_dict[p]['dates']))),5)*100)+' %',
                       sum(turns) / len(turns), min(turns), max(turns), sum(turns),
                       sum(points), (sum(points)) / (len(points)), str(dhm[0])+'d '+str(dhm[1])+'h '+str(dhm[2])+'m '])

        table.align = 'r'
        #print x.get_string(sortby="Annual Rainfall", reversesort=True)

    table.sortby = 'Avg. Turns'
    print table

#    print ''
#    print 'Ascended Roles'
#    roles_counter = collections.Counter(roles)
#    roles_set = Set(roles)
#
#    rs, count = [], []
#    z_total = 0
    #for role in roles_set:
    #    rs.append(role)
    #    count.append(roles_counter[role])
#
#        z_total = z_total + sum(utils.lookup_z[:roles_counter[role]])
#        print '%s: %d %1.5f' % (role, roles_counter[role], sum(utils.lookup_z[:roles_counter[role]]))

#    print ''
#    print 'Z-score {:.8}'.format(z_total)
