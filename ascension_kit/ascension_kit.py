import nao, format
import argparse
import sys

if __name__ == '__main__':
    # TODO make saving the file optional
    # TODO make a pretty table
    """ Fetches a users NAO data"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', help='NAO username')
    parser.add_argument('--list', '-l', help='NAO user list')
    cmd_args = parser.parse_args()

    if not cmd_args.list and not cmd_args.name:
        parser.print_help()
    elif cmd_args.list:
        player_list = [p.strip() for p in cmd_args.list.split(',')]
    else:
        player_list = [cmd_args.name.strip()]
    print "Fetching games for user(s) %s" % cmd_args.list.split(',')

    for player in player_list:

        dates, scores, roles, ascension_games = nao.process_html(player)

        format.process_ascensions(ascension_games, len(dates), cmd_args.name)