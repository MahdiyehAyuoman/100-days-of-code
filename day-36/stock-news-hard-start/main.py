import requests
import json
import smtplib
from datetime import datetime, timedelta


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ALPHA_API_KEY = "V1C4P0Y1QIY8628C"
NEWS_API = "620a8bc10c35435daae076c98e1db9f7"

## Get the API & closing prices
url = f'{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_API_KEY}'

try:
    data_response = requests.get(url)
    data_response.raise_for_status()  # Raise an exception for HTTP errors
    data = data_response.json()
except requests.exceptions.RequestException as e:
    print(f"Error fetching stock data: {e}")
    data = None

if data and 'Time Series (Daily)' in data and data['Time Series (Daily)']:
    daily_data = data['Time Series (Daily)']
    # Get all dates and sort them from most recent to oldest
    dates = sorted(daily_data.keys(), reverse=True)

    if len(dates) >= 2:
        recent_trading_day = dates[0]
        previous_trading_day = dates[1]

        yesterday_price = float(daily_data[recent_trading_day]['4. close'])
        day_before_yesterday_price = float(daily_data[previous_trading_day]['4. close'])

        difference_price_orginal = yesterday_price - day_before_yesterday_price
        # Calculate percentage difference based on the previous day's closing price
        percentage_difference = round((difference_price_orginal / day_before_yesterday_price) * 100, 2)
        abs_percentage_difference = abs(percentage_difference)

        # Determine the emoji for price change
        up_down = ""
        if percentage_difference > 0:
            up_down = "\u25B2"  # Up arrow
        elif percentage_difference < 0:
            up_down = "\u25BE"  # Down arrow

        # Fetch news (consider adding a threshold check here, e.g., if abs_percentage_difference >= 5)
        # For now, fetching news based on the original structure (always)
        news_url = f'{NEWS_ENDPOINT}?q={COMPANY_NAME}&from={previous_trading_day}&to={recent_trading_day}&sortBy=popularity&apiKey={NEWS_API}'
        
        try:
            news_data_response = requests.get(news_url)
            news_data_response.raise_for_status()
            news_data = news_data_response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news data: {e}")
            news_data = None

        articles_title_list = []
        articles_description_list = []

        if news_data and 'articles' in news_data and news_data['articles']:
            # Get the first 3 articles
            for i in range(min(3, len(news_data['articles']))):
                articles_title = news_data['articles'][i]['title']
                articles_title_list.append(articles_title)
                articles_description = news_data['articles'][i]['description']
                articles_description_list.append(articles_description)

            # Send the email for stock news
            my_gmail = 'mahdiyehayuoman@gmail.com'
            gmail_password = 'Write your pass here'  
            uni_mail = 'm.ayuoman@iasbs.ac.ir'

            try:
                with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                    connection.starttls()
                    connection.login(user=my_gmail, password=gmail_password)

                    for i in range(len(articles_title_list)):
                        message_body = (f"subject: Your Stock News\n\nTSLA {up_down}{abs_percentage_difference}%\n\nHeadline: {articles_title_list[i]}\n\nBrief: {articles_description_list[i]}").encode('utf-8')
                        connection.sendmail(from_addr=my_gmail, to_addrs=uni_mail, msg=message_body)
                print("Emails sent successfully.")
            except smtplib.SMTPAuthenticationError:
                print("Failed to login to SMTP server. Check your email and password.")
            except smtplib.SMTPException as e:
                print(f"Error sending email: {e}")

        else:
            print("No articles found for the specified dates and company.")
    else:
        print("Not enough daily data points to compare. Need at least two trading days.")
else:
    print("Could not retrieve daily time series data or data is empty.")
