from sets import Set
import sys
import utils
import collections
from prettytable import PrettyTable

table = PrettyTable(['Player', 'Total Games', 'Ascensions', 'Average Turns', 'Fastest',
                     'Slowest', 'Total Turns', 'Total Points', 'Average Points', 'Time Spent'])

def process_ascensions(player_dict):

    for p in player_dict:
        if len(player_dict[p]['ascension_games']) == 0:
            print "No ascensions for %s. Total games: %s" %(p, len(player_dict[p]['dates']))
            sys.exit(99)

    roles = [str(g['role']) for g in ascension_list]
    race = [str(g['race']) for g in ascension_list]
    gender0 = [str(g['gender0']) for g in ascension_list]
    gender = [str(g['gender']) for g in ascension_list]
    align0 = [str(g['align0']) for g in ascension_list]
    align = [str(g['align']) for g in ascension_list]
    points = [int(g['points']) for g in ascension_list]
    turns = [int(g['turns']) if g['turns'] else 0 for g in ascension_list]
    dates = [str(g['deathdate']) for g in ascension_list]
    maxlvl = [int(g['maxlvl']) for g in ascension_list]
    realtime = [int(g['realtime']) if g['realtime'] else 0 for g in ascension_list]

    # print ''
    # print '{:^40}'.format('[ Ascensions ]')
    # print ''
    #
    # print '{:40} {:,}'.format('Total Games', total_games)
    # #print '{:30} {:>10} ({:.2%})'.format('Ascensions', len(points), float(len(points)) / float(total_games))
    # print '{:40} {:,} ({:.2%})'.format('Ascensions', len(points), float(len(points)) / float(total_games))
    # print '{:40} {:,}'.format('Average turns/ascension', (sum(turns)) / len(turns))
    # print '{:40} {:,}'.format('Fastest Ascension', min(turns))
    # print '{:40} {:,}'.format('Slowest Ascension', max(turns))
    # print ''
    # print '{:40} {:,}'.format('Total Ascension Turns', sum(turns))
    # print ''
    # print '{:40} {:,}'.format('Total Points', sum(points))
    # print '{:40} {:,}'.format('Average Points/Ascension', (sum(points)) / (len(points)))
    # print '{:40} {} days {} hours {} minutes'.format('Time Spent Ascending', dhm[0], dhm[1], dhm[2])


    dhm = utils.seconds_to_days_hours_mins(sum(realtime))

    table.add_row([player_name, total_games, str(len(points))+' '+ str(round((float(len(points)) / float(total_games)),5)*100)+' %',
                   sum(turns) / len(turns), min(turns), max(turns), sum(turns),
                   sum(points), (sum(points)) / (len(points)), str(dhm[0])+'d '+str(dhm[1])+'h '+str(dhm[2])+'m '])

    table.align = 'r'
    print(table)

#    print ''
#    print 'Ascended Roles'
    roles_counter = collections.Counter(roles)
    roles_set = Set(roles)

    rs, count = [], []
    z_total = 0
    #for role in roles_set:
    #    rs.append(role)
    #    count.append(roles_counter[role])
#
#        z_total = z_total + sum(utils.lookup_z[:roles_counter[role]])
#        print '%s: %d %1.5f' % (role, roles_counter[role], sum(utils.lookup_z[:roles_counter[role]]))

#    print ''
#    print 'Z-score {:.8}'.format(z_total)
