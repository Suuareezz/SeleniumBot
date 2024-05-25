from booking.booking import Booking
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument('--headless')

with Booking(options=options,teardown=False) as bot:
    bot.land_first_page()
    bot.select_place('New York')
    bot.select_flexi_month('Jun')

