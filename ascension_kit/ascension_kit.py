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

    if cmd_args.list:
        player_list = [p.strip() for p in cmd_args.list.split(',')]
        sys.exit(8)
    if not cmd_args.name:
        parser.print_help()
    else:
        player_list = [cmd_args.name.strip()]
        print "Fetching games for user %s" % cmd_args.name

        player_file = nao.get_player_file(cmd_args.name)

        dates, scores, roles, ascension_games = nao.process_html(player_file, cmd_args.name)

        format.process_ascensions(ascension_games, len(dates), cmd_args.name)