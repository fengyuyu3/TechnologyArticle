__author__ = 'flq'

from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy", "crawl", "technologydetails"])
# execute(["scrapy", "crawl", "technology"])
