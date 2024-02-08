from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)

    def test_search(self):
        expected_cat_search_results = ['Voice classification in non-classical music']
        self.assertEqual(search('cat'), expected_cat_search_results)

        expected_can_search_results = ['List of Canadian musicians', 'Endogenous cannabinoid', 'Mexican dog-faced bat']
        self.assertEqual(search('can'), expected_can_search_results)

        expected_end_search_results = ['Endogenous cannabinoid', 'Endoglin']
        self.assertEqual(search('end'), expected_end_search_results)

        expected_foot_search_results = ['2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Georgia Bulldogs football under Robert Winston']
        self.assertEqual(search('foot'), expected_foot_search_results)

        expected_200_search_results = ['2009 in music', '2007 Bulldogs RLFC season', '2009 Louisiana Tech Bulldogs football team', "United States men's national soccer team 2009 results", '2006 in music', '2007 in music', '2008 in music']
        self.assertEqual(search('200'), expected_200_search_results)

        expected_2000_search_results = []
        self.assertEqual(search('2000'), expected_2000_search_results)

        expected_gEo_search_results = ['Geoff Smith (British musician)', 'Georgia Bulldogs football', 'George Crum (musician)', 'Georgia Bulldogs football under Robert Winston']
        self.assertEqual(search('gEo'), expected_gEo_search_results)

        expected_empty_search_results = []
        self.assertEqual(search(""), expected_empty_search_results)
    
    def test_title_length(self):
        expected_ca_result = ['List of Canadian musicians', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Medical value travel', 'Mexican dog-faced bat', 'List of Saturday Night Live musical sketches', 'Voice classification in non-classical music', 'Annie (musical)', 'Indian classical music', 'The Hunchback of Notre Dame (musical)', 'Traditional Thai musical instruments', 'Paul Carr (musician)']
        self.assertEqual(title_length(500, search('ca')), expected_ca_result)

        expected_geo_result = ['Geoff Smith (British musician)', 'Georgia Bulldogs football', 'George Crum (musician)', 'Georgia Bulldogs football under Robert Winston']
        self.assertEqual(title_length(50, search('gEo')), expected_geo_result)

        expected_dog_result = ['Guide dog', 'Endoglin', 'Sun dog']
        self.assertEqual(title_length(10, search('dog')), expected_dog_result)

        expected_negative_result = []
        self.assertEqual(title_length(-1, search('dog')), expected_negative_result)

        expected_end2_result = []
        self.assertEqual(title_length(5, search('end')), expected_end2_result)

    def test_article_count(self):
        self.assertEqual(article_count(8, search('ca')), ['List of Canadian musicians', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Medical value travel', 'Mexican dog-faced bat', 'List of Saturday Night Live musical sketches', 'Voice classification in non-classical music', 'Annie (musical)'])
        self.assertEqual(article_count(16, search('ba')),  ['USC Trojans volleyball', 'Mexican dog-faced bat', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Mets de Guaynabo (volleyball)', 'The Hunchback of Notre Dame (musical)', 'Georgia Bulldogs football under Robert Winston', 'Comparison of programming languages (basic instructions)'])
        self.assertEqual(article_count(100, search("")), [])
        self.assertEqual(article_count(4, search("grA")), ['C Sharp (programming language)', 'Reflection-oriented programming', 'B (programming language)', 'List of dystopian music, TV programs, and games'])

    def test_random_article(self):
        self.assertEqual(random_article(5, search('dog')), 'Mexican dog-faced bat')
        self.assertEqual(random_article(1, search('The')), 'The Mandogs')
        self.assertEqual(random_article(9, search('cat')), '')
        self.assertEqual(random_article(-1, search('ca')), '')

    def test_favorite_article(self):
        self.assertEqual(favorite_article('guide dog', search('dog')), True)
        self.assertEqual(favorite_article('god', search('ca')), False)
        self.assertEqual(favorite_article('EnDogLIn', search('end')), True)

    def test_multiple_keywords(self):

        self.assertEqual(multiple_keywords('dog', search('cat')), ['Voice classification in non-classical music', 'Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)'])
        self.assertEqual(multiple_keywords('ca', search('end')), ['Endogenous cannabinoid', 'Endoglin', 'List of Canadian musicians', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Medical value travel', 'Mexican dog-faced bat', 'List of Saturday Night Live musical sketches', 'Voice classification in non-classical music', 'Annie (musical)', 'Indian classical music', 'The Hunchback of Notre Dame (musical)', 'Traditional Thai musical instruments', 'Paul Carr (musician)'])
        self.assertEqual(multiple_keywords('and', search('THe')), ['The Hunchback of Notre Dame (musical)', 'The Mandogs', 'List of dystopian music, TV programs, and games', 'Covariance and contravariance (computer science)', 'The Mandogs', 'Landseer (dog)'])
        self.assertEqual(multiple_keywords('200', search('20')), ['2009 in music', '2007 Bulldogs RLFC season', '2009 Louisiana Tech Bulldogs football team', "United States men's national soccer team 2009 results", '2006 in music', '2007 in music', '2008 in music', '2009 in music', '2007 Bulldogs RLFC season', '2009 Louisiana Tech Bulldogs football team', "United States men's national soccer team 2009 results", '2006 in music', '2007 in music', '2008 in music'])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration1(self, input_mock):
        keyword = 'music'
        advanced_option = 1

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, 23])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "23\n" + "\nHere are your articles: ['French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'Tim Arnold (musician)', 'Old-time music', 'Arabic music', 'Joe Becker (musician)', 'Aco (musician)', '1936 in music', '1962 in country music', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', 'David Levi (musician)', 'George Crum (musician)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration2(self, input_mock):
        keyword = 'tom'
        advanced_option = 2

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, 100])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "100\n" + "\nHere are your articles: ['Tom Hooper (musician)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration3(self, input_mock):
        keyword = 'faith'
        advanced_option = 3

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, 3])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "3\n" + "\nNo articles found\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration2(self, input_mock):
        keyword = 'ThE'
        advanced_option = 4

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, 'facts'])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "facts\n" + """\nHere are your articles: ['The Hunchback of Notre Dame (musical)', 'The Mandogs']\nYour favorite article is not in the returned articles!\n"""

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration5(self, input_mock):
        keyword = 'end'
        advanced_option = 5

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option, 'football'])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "football\n" + "\nHere are your articles: ['Endogenous cannabinoid', 'Endoglin', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Georgia Bulldogs football under Robert Winston']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration6(self, input_mock):
        keyword = 'game'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['List of dystopian music, TV programs, and games', 'List of computer role-playing games', 'List of video games with time travel']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
