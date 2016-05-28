from utils import strip_jsonp_to_json
import urllib
import json
import pprint

pp = pprint.PrettyPrinter(indent=4)


class MangaSite:
    def __init__(self):
        raise NotImplementedError

    def search(self, query_string, print_results=False):
        return self._search(self.query_url + query_string, print_results)

    def _search(self, url, print_results=False):
        response = urllib.urlopen(url)
        raw_results = response.read()
        parsed_data = self.parse_results(raw_results)
        processed_data = self.process_results(parsed_data)

        if print_results: self.print_raw_results(processed_data)
        return processed_data

    def parse_results(self, data):
        if self.output_type == 'jsonp':
            data = json.loads(strip_jsonp_to_json(data))
        elif self.output_type == "json":
            data = json.loads(data)
        else:
            raise NotImplementedError
        return data

    def process_results(self, data, print_results=False):
        all_results = [dict([(key, manga[idx]) for (idx, key) in enumerate(self.output_format)]) for manga in data]
        return all_results

    def print_raw_results(self, data):
        for tmp in data:
            if tmp['url_title'][0] == '/': tmp['url_title'] = tmp['url_title'][1:]
            print "%s --- %s" % (tmp['title'], self.manga_url + tmp['url_title'])


class MangaPark(MangaSite):
    def __init__(self):
        self.main_url = "http://www.mangapark.me"
        self.query_url = "http://j.mangapark.me/ajax-autocomplete.js?q="
        self.manga_url = self.main_url + "/manga/"
        self.method = "GET"
        self.output_type = "jsonp"
        self.output_format = ['title', 'url_title', 'id', 'author', 'categories']


class MangaFox(MangaSite):
    def __init__(self):
        self.main_url = "http://www.mangafox.me"
        self.query_url = "http://mangafox.me/ajax/search.php?term="
        self.manga_url = self.main_url + "/manga/"
        self.method = "GET"
        self.output_type = "json"
        self.output_format = ['id', 'title', 'url_title', 'categories', 'author']


class MangaPanda(MangaSite):
    def __init__(self):
        self.main_url = "http://www.mangapanda.com"
        self.query_url = "http://www.mangapanda.com/actions/search/?limit=100&q="
        self.manga_url = self.main_url + "/"
        self.method = "GET"
        self.output_type = "mangareader"
        self.output_format = ['title', 'cover_pic', 'title', 'author', 'url_title', 'id']

    def parse_results(self, data):
        data = [row.split("|") for row in data.split("\n")[:-1]]
        return data


class MangaReader(MangaSite):
    def __init__(self):
        self.main_url = "http://www.mangareader.net"
        self.query_url = "http://www.mangareader.net/actions/search/?limit=100&q="
        self.manga_url = self.main_url + "/"
        self.method = "GET"
        self.output_type = "mangareader"
        self.output_format = ['title', 'cover_pic', 'title', 'author', 'url_title', 'id']

    def parse_results(self, data):
        data = [row.split("|") for row in data.split("\n")[:-1]]
        return data
