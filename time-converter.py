# coding: utf-8
# python 3.7

# important: Multi-language content is draft only, NOT FINAL TEXTS; require additional copywriting

# PRE-DEFINED PARAMETERS:

# lines of output content
output_lines = {'en': 'Sale starts on {DD} of November at {HH}:{MM} {am/pm} ({TIMEZONE})',
                'ru': 'Распродажа начнётся {DD} ноября в {HH}:{MM} ({TIMEZONE})',
                'es': 'La oferta comienza el {DD} de noviembre a las {HH}:{MM} ({TIMEZONE})',
                'pt': 'A venda começa em {DD} de novembro às {HH}: {MM} {am/pm} ({TIMEZONE})',
                'fr': 'La vente commence le {JJ} de novembre à {HH}: {MM} {am/pm} ({TIMEZONE})'}

# connects time zone and sale day (first number) and sale hour (second number)
sale_start_time = {'''}

# convert 24 hour to 12 hour system
am_pm = {'''}

# name of time zones common in English
time_zone_names_EN = {
    'GMT': 'Greenwich Time',
    'GMT-1': 'GMT-1',
    'GMT-2': 'GMT-2',
    'GMT-3': 'GMT-3',
    'GMT-4': 'Atlantic Standard Time',
    'GMT-5': 'Eastern Time Zone',
    'GMT-6': 'Central Time Zone',
    'GMT-7': 'Pacific Daylight Time',
    'GMT-8': 'GMT-8',
    'GMT-9': 'Alaska Standard Time',
    'GMT-10': 'Hawaii-Aleutian Time',
    'GMT-11': 'Samoa Standard Time',
    'GMT+1': 'Central European Time',
    'GMT+2': 'Eastern European Time',
    'GMT+3': 'Moscow Time',
    'GMT+4': 'GMT+4',
    'GMT+5': 'GMT+5',
    'GMT+6': 'GMT+6',
    'GMT+7': 'GMT+7',
    'GMT+8': 'GMT+8',
    'GMT+9': 'GMT+9',
    'GMT+10': 'Chamorro Standard Time',
    'GMT+11': 'Australian Eastern Time',
    'GMT+12': 'New Zealand Time',
    'GMT+13': 'GMT+13',
    'GMT+14': 'Line Islands Time'}

# name of time zones common in Russian
time_zone_names_RU = {
    'GMT': 'МСК+5',
    'GMT-1': 'МСК+6',
    'GMT-2': 'МСК+7',
    'GMT-3': 'МСК+8',
    'GMT-4': 'МСК+9',
    'GMT-5': 'МСК+10',
    'GMT-6': 'МСК+11',
    'GMT-7': 'МСК-12',
    'GMT-8': 'МСК-11',
    'GMT-9': 'МСК-10',
    'GMT-10': 'МСК-9',
    'GMT-11': 'МСК-8',
    'GMT+1': 'МСК-7',
    'GMT+2': 'МСК-6',
    'GMT+3': 'МСК-5',
    'GMT+4': 'МСК-4',
    'GMT+5': 'МСК-3',
    'GMT+6': 'МСК-2',
    'GMT+7': 'МСК-1',
    'GMT+8': 'по Москве',
    'GMT+9': 'МСК+1',
    'GMT+10': 'МСК+2',
    'GMT+11': 'МСК+3',
    'GMT+12': 'МСК+4',
    'GMT+13': 'МСК+5',
    'GMT+14': 'МСК+6'}

# dict with all time zones by language
time_zones_all = {'en': time_zone_names_EN, 'ru': time_zone_names_RU}


# FUNCTIONS:
def time_converter_output(gmt, language):  # input only GMT time zone and user language
    time_and_date = (sale_start_time.get(gmt)).split('-')  # split date from hour
    sale_day = time_and_date[0]  # set day of the sale
    sale_hour = time_and_date[1]  # set hour of the sale
    text_line = output_lines.get(language)  # pick line of text with correct language
    time_zone = (time_zones_all.get(language)).get(gmt)  # pick time zone name in correct language
    if int(sale_hour) >= 13:  # convert 24 hours into 12 hours system
        sale_hour = am_pm.get(sale_hour)
        sale_hour_am_pm = 'pm'  # PM for time from 13:00 to 24:00
    else:
        sale_hour_am_pm = 'am'  # AM for time from 00:00 to 12:00
    # parameters to pass to string
    params = {'DD': sale_day, 'HH': sale_hour, 'MM': '00', 'am/pm': sale_hour_am_pm, 'TIMEZONE': time_zone}
    return text_line.format(**params)

# print(time_converter_output('GMT+11', 'en'))


while True:
    prompt_timezone = str(input('Please input GMT offset, from from -11 to +14:   >  '))
    prompt_timezone = str('GMT'+prompt_timezone)
    prompt_language = str(input('Please input language code, like "en", "ru", etc.:   >   '))
    print('\n\n')
    print(time_converter_output(prompt_timezone, prompt_language))
    print('\n\n')
