#!/usr/bin/env python

import argparse
from manga_sites import MangaPark, MangaFox, MangaReader, MangaPanda

def main():
    parser = argparse.ArgumentParser(description='Search for mangas with a CLI')
    parser.add_argument('query', nargs='?', help="search term")
    parser.add_argument('-s', '--site', default='mangapark', help="site to search from")

    args = parser.parse_args()

    if args.query == None:
        print("Please specify the search term of the manga you are searching for.")
        return

    if args.site == 'mangapark':
        site = MangaPark()
    elif args.site == 'mangafox':
        site = MangaFox()
    elif args.site == 'mangareader':
        site = MangaReader()
    elif args.site == 'mangapanda':
        site = MangaPanda()
    else:
        raise NotImplementedError("The site you specified has not bee implemented yet.")

    site.search(args.query, print_results=True)

if __name__ == "__main__":
    main()


