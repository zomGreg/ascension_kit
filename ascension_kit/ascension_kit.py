import nao, format
import argparse

if __name__ == '__main__':
    # TODO make saving the file optional
    # TODO if the file is saved, "cache" it by testing ctime
    """ Fetches a users NAO data"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', '-n', help='NAO username')
    cmd_args = parser.parse_args()

    if not cmd_args.name:
        parser.print_help()
    else:
        print "Fetching games for user %s" % cmd_args.name

        player_file = nao.get_player_file(cmd_args.name)

        dates, scores, roles, ascension_games = nao.process_html(player_file)
        format.process_ascensions(ascension_games, len(dates))