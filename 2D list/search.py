from wiki import article_metadata, ask_search, ask_advanced_search

# FOR ALL OF THESE FUNCTIONS, READ THE FULL INSTRUCTIONS.

# 1) 
#
# Function: search
#
# Parameters:
#   keyword - search word to look for in article metadata's relevant keywords
#
# Returns: list of metadata for articles in which the article is relevant to
#   the keyword. Relevance is determined by checking the metadata's "relevant
#   keywords" list for a case-insensitive match with the keyword parameter. #   The returned list should not include the "relevant keywords" list for each
#   article metadata.
#   
#   If the user does not enter anything, return an empty list
#
# Hint: to get list of existing article metadata, use article_metadata()
def search(keyword):
    """
    takes string as an argument and returns a list of articles relevant to the string keyword
    """

    articles = []
    article_data = article_metadata()

    if keyword == "":
        return articles

    for article in article_data:
        index = 0
        while index < len(article[4]):
            if keyword.lower() == article[4][index]:
                articles.append(article[0:4])            
            index += 1

    return articles



# 2) 
#
# Function: article_length
#
# Parameters:
#   max_length - max character length of articles
#   metadata - article metadata to search through
#
# Returns: list of article metadata from given metadata with articles not
#   exceeding max_length number of characters
def article_length(max_length, metadata):
    """
    takes int and a list as argument, and checks if the numbers of the characters in the list exceeds the int, returns 
    the list of article characters that do not exceed the int input.
    """

    articles = []
    
    for article in metadata:
        if article[3] <= max_length:
            articles.append(article)
    return articles


# 3) 
#
# Function: unique_authors
#
# Parameters:
#   count - max number of unique authors to include in the results
#   metadata - article metadata
#
# Returns: list of article metadata containing a maximum of `count` results,
#   each with a unique author. If two or more articles have the same author, 
#   include the first in the results and skip the others. Two authors are 
#   considered the same if they are a case-insensitive match. If count is 
#   larger than the number of unique authors, return all articles with the 
#   duplicate authors removed.
def unique_authors(count, metadata):
    """
    takes int and list as an argument, returns a list of article according to the number user specified.
    """
    duplicate = []
    article = []
    index = 0

    for data in metadata:
        if len(duplicate) < count:
            if data[1].lower() not in duplicate:
                duplicate.append(data[1].lower())
                article.append(data)

    return article
    # pass

# 4) 
#
# Function: most_recent_article
#
# Parameters:
#   metadata - article metadata
#
# Returns: article metadata of the article published most recently according
#   to the timestamp. Note this should return just a 1D list representing
#   a single article.
def most_recent_article(metadata):
    """
    takes a list as an argument and returns a list of article that was recent
    """
    most_recent = 0
    most_recent_list = []
    
    for data in metadata:
        if data[2] > most_recent:
            most_recent = data[2]
            most_recent_list = data
    return most_recent_list

    # pass

# 5) 
#
# Function: favorite_author
#
# Parameters:
#   favorite - favorite author title
#   metadata - article metadata
#
# Returns: True if favorite author is in the given articles (case 
#   insensitive), False otherwise
def favorite_author(favorite, metadata):
    """
    takes a string and list as argument, and checks if the string matches the string in the list, return a Boolean value(True or False)
    """
    for data in metadata:
        if favorite.lower() == data[1].lower():
            return True
    return False
    
    # pass

# 6) 
#
# Function: title_and_author
#
# Parameters:
#   metadata - article metadata
#
# Returns: list of Tuples containing (title, author) for all of the given 
#   metadata.
def title_and_author(metadata):
    """
    takes a list an argument, returns a tuple of article titles and author
    """
    articles = []
    for data in metadata:
        articles.append(tuple(data[0:2])) 

    return articles

    # pass

# 7) 
#
# Function: refine_search
#
# Parameters:
#   keyword - additional keyword to search
#   metadata - article metadata from basic search
#
# Returns: searches for article metadata from entire list of available
#   articles using keyword. Returns the article metadata that is returned in 
#   in *both* the additional search and the basic search. The results should
#   be in the same order that they were returned in the basic search. Two
#   articles can be considered the same if both their author and article title
#   match exactly.
def refine_search(keyword, metadata):
    """
    takes a string and a list as an argument, returns a list of articles that is not in the list argument and the list argument
    """
    articles_list = []

    for data_1 in search(keyword):
        for data_2 in metadata:
            if data_1[0] == data_2[0] and data_1[1] == data_2[1]:
                articles_list.append(data_1)

    return articles_list
    # pass

# Prints out articles based on searched keyword and advanced options
def display_result():
    # Stores list of articles returned from searching user's keyword
    articles = search(ask_search())

    # advanced stores user's chosen advanced option (1-7)
    # value stores user's response in being asked the advanced option
    advanced, value = ask_advanced_search()

    if advanced == 1:
        # value stores max article title length in number of characters
        # Update article metadata to contain only ones of the maximum length
        articles = article_length(value, articles)
    if advanced == 2:
        # value stores max number of unique authors
        # Update article metadata to contain only the max number of authors
        articles = unique_authors(value, articles)
    elif advanced == 3:
        # Update articles to only contain the most recent article
        articles = most_recent_article(articles)
    elif advanced == 4:
        # value stores author
        # Store whether author is in search results into variable named 
        # has_favorite
        has_favorite = favorite_author(value, articles)
    elif advanced == 5:
        # Update article metadata to only contain titles and authors
        articles = title_and_author(articles)
    elif advanced == 6:
        # value stores keyword to search
        # Update article metadata to contain only article metadata
        # that is contained in both searches
        articles = refine_search(value, articles)

    print()

    if not articles:
        print("No articles found")
    else:
        print("Here are your articles: " + str(articles))

    if advanced == 4:
        print("Your favorite author is" + ("" if has_favorite else " not") + " in the returned articles!")

if __name__ == "__main__":
    display_result()
