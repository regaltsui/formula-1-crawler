#!/usr/bin/env python3
from requests import session
from bs4 import BeautifulSoup


class F1Crawler:
    DATA_URL = "https://fiaresultsandstatistics.motorsportstats.com/"

    def __init__(self):
        self.session = session()

    def get_event_list(self, year):
        """Extracting The event names and the directories of a Championship year user specified.

        :param year:int Year of Championship
        :returns: results:dict Dictionary containing the name of the Grand Prix and it's respective directory
        """
        url = "https://fiaresultsandstatistics.motorsportstats.com/results/{}-monaco-grand-prix".format(
            year
        )
        res = self.session.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        gp_list = soup.select(".slick-list .slick-slide a")
        gp_names = [i.text for i in gp_list]
        gp_links = [i["href"] for i in gp_list]
        return {i: j for i, j in zip(gp_names, gp_links)}

    def get_event_names(self, year):
        """Alias function to extract event names of a championship year ONLY.

        :param year: Year of championship
        :returns: results:list List of Grand prix names
        """
        return list(self.get_event_list(year).keys())
