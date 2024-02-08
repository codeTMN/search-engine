from wiki import article_metadata, ask_search, ask_advanced_search
import datetime
import time

# FOR ALL OF THESE FUNCTIONS, READ THE FULL INSTRUCTIONS.

# 1) 
#
# Function: keyword_to_titles
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping keyword to list of article titles in which the
#         articles contain keyword
#
# Example return value:
# {
#   'keyword': ['article title', 'article title 2']
#   'another_keyword': ['article title 2', 'article title 3']
# }
def keyword_to_titles(metadata):
    """
    Takes a 2D list as an argument and returns a 
    dictionary mapping keyword to a list 
    of articles that contain the keyword
    """
    article_title = {}


    for data in metadata:
        for value in data[4]:
            # if value is not in the dictionary create a key with the keyword and value as a list
            if value not in article_title:
                article_title[value] = [data[0]]
            # If key exists append values of data to the key
            else:
                article_title[value].append(data[0])

    return article_title

# 2) 
#
# Function: title_to_info
#
# Parameters:
#   metadata - 2D list of article metadata containing 
#              [title, author, timestamp, article length, keywords]
#              for each article
#
# Return: dictionary mapping article title to a dictionary with the following
#         keys: author, timestamp, length of article. It may be assumed that
#         the input data has unique article titles.
#
# Example return value:
# {
#   'article title': {'author': 'some author', 'timestamp': 1234567890, 'length': 2491}
#   'article title 2': {'author': 'another author', 'timestamp': 9876543210, 'length': 85761}
# }
def title_to_info(metadata):
    """
    takes a 2D list as an argument and return dictionary 
    mapping article title to a dictionary with the following 
    keys: author, timestamp, length of article.
    """

    article_title_dict = {}

    for data in metadata:
        article_title_dict[data[0]] = {'author': data[1], 'timestamp': data[2], 'length': data[3]}

    return article_title_dict

# 3) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for
#   keyword_to_titles - dictionary mapping keyword to a list of all article
#                       titles containing that keyword
#
# Return: list of titles with articles containing the keyword, case-sensitive
#         or an empty list if none are found
def search(keyword, keyword_to_titles):
    """
    takes two argument, a string and dictionary and 
    returns a list of titles with articles containing the keyword
    """

    article = []

    for key, values in keyword_to_titles.items():
        for value in values:
            # If keyword is equal to the key in the dictionary append the value to article
            if keyword == key:
                article.append(value)
    
    return article


'''
Functions 4-8 are called after searching for a list of articles containing the user's keyword.
'''
# 4) 
#
# Function: article_length
#
# Parameters:
#   max_length - max character length of articles
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from given titles for articles that do not
#         exceed max_length number of characters
def article_length(max_length, article_titles, title_to_info):
    """
    takes three argument, an int, a list and a dictionary, and return a list 
    of article titles from given titles for articles that do not
    exceed max_length number of characters
    """

    article_data = []

    for data in article_titles:
        # If the number of characters does not exceed the max_length, append to the list
        if title_to_info[data]['length'] <= max_length:
            article_data.append(data)
 
    return article_data


# 5) 
#
# Function: key_by_author
#
# Parameters:
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: dictionary that maps author to a list of all articles titles written
#         by that author
#
# Example return value:
# {
#   'author': ['article title', 'article title 2'],
#   'another author': ['article title 3']
# }

def key_by_author(article_titles, title_to_info):
    """
    takes two argument, a list and a dictionary and return a 
    dictionary that maps author to a list of all articles titles written 
    by that author
    """

    key_dict = {}

    for data in article_titles:
        if data in title_to_info and 'author' in title_to_info[data]:
            if title_to_info[data]['author'] not in key_dict:
                key_dict[title_to_info[data]['author']] = []
            key_dict[title_to_info[data]['author']].append(data)

    return key_dict


# 6) 
#
# Function: filter_to_author
#
# Parameters:
#   author - author name to filter results to
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from the initial search written by the author
#         or an empty list if none.
def filter_to_author(author, article_titles, title_to_info):
    """
    takes 3 arguments, a string,  list and a dictionary and 
    return list of article titles from the initial 
    search written by the author or an empty list if none
    """

    data_list = []
    for data in article_titles:
        if data in title_to_info and 'author' in title_to_info[data]:
            if title_to_info[data]['author'] == author:
                data_list.append(data)

    return data_list


# 7) 
#
# Function: filter_out
#
# Parameters:
#   keyword - a second keyword to use to filter out results
#   article_titles - list of article titles resulting from basic search
#   keyword_to_titles - dictionary mapping keyword to a list of all article
#                       titles containing that keyword
#
# Return: list of articles from the basic search that do not include the
#         new keyword
def filter_out(keyword, article_titles, keyword_to_titles):
    """
    takes 3 argument a string, a list,  a dictionary and returns 
    list of articles from the basic search that do not include the
    new keyword
    """
    article_filter = []

    if keyword in keyword_to_titles:
        for value in article_titles:
            if value not in keyword_to_titles[keyword]:
                article_filter.append(value)
        return article_filter
    else:
        return article_titles


# 8) 
#
# Function: articles_from_year
#
# Parameters:
#   year - year (ex: 2009) to filter articles to
#   article_titles - list of article titles resulting from basic search
#   title_to_info - dictionary mapping article title to a dictionary with the 
#                   following keys: author, timestamp, length of article
#
# Return: list of article titles from the basic search that were published
#         during the provided year.
def articles_from_year(year, article_titles, title_to_info):
    """
    takes a3 argument an int,  a list,a dictionary and returns a 
    list of article titles from the basic search that were 
    published during the provided year
    """

    article_year = []

    for data in article_titles:
        # gets timestamp value in the dictionary
        year_dict = title_to_info[data]['timestamp']

        # converts the Unix/Epoch to a normal year(ex: 2009)
        year_convert = 1970 + year_dict // 31536000

        # if year inputted matches the year in timestamp we append the value of article_titles
        if year == year_convert:
            article_year.append(data)

    return article_year

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Preprocess all metadata to dictionaries
    keyword_to_titles_dict = keyword_to_titles(article_metadata())
    title_to_info_dict = title_to_info(article_metadata())
    
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search(), keyword_to_titles_dict)

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max length of articles
        # Update articles to contain only ones not exceeding the maximum length
        articles = article_length(value, articles, title_to_info_dict)
    if advanced == 2:
        # Update articles to be a dictionary keyed by author
        articles = key_by_author(articles, title_to_info_dict)
    elif advanced == 3:
        # value stores author name
        # Update article metadata to only contain titles and timestamps
        articles = filter_to_author(value, articles, title_to_info_dict)
    elif advanced == 4:
        # value stores a second keyword
        # Filter articles to exclude those containing the new keyword.
        articles = filter_out(value, articles, keyword_to_titles_dict)
    elif advanced == 5:
        # value stores year as an int
        # Update article metadata to contain only articles from that year
        articles = articles_from_year(value, articles, title_to_info_dict)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

if __name__ == "__main__":
    display_result()
