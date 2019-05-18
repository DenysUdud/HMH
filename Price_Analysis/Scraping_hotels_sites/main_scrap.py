from Price_Analysis.Scraping_hotels_sites.hotelscan_parser import run_scrapping_scan
from Price_Analysis.Scraping_hotels_sites.hotels24_parser import run_scrapping_24
from Price_Analysis.Scraping_hotels_sites.price_writer import json_maker



def main_scrap(city_name, stars, kind, size):
	hotelscan_lst = run_scrapping_scan(city_name, 2, stars, kind, size)
	hotels24_lst = run_scrapping_24(city_name)
	return json_maker(hotelscan_lst + hotels24_lst)

if __name__ == "__main__":
	main_scrap("Lviv", 5, "apartments", 69)