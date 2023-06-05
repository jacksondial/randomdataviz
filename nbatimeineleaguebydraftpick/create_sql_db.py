"""Create SQL database from the scraped data from data_scraping.py"""
import sqlite3


con = sqlite3.connect("nba.db")

cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS season_summary")