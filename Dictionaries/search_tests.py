from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        input_value = ['French pop music', 'Mack Johnson', 1172208041, 5569, ['french', 'pop', 'music', 'the', 'france', 'and', 'radio']], ['Edogawa, Tokyo', 'jack johnson', 1222607041, 4526, ['edogawa', 'the', 'with', 'and', 'koiwa', 'kasai', 'player', 'high', 'school']], ['Noise (music)', 'jack johnson', 1194207604, 15641, ['noise', 'music', 'that', 'the', 'use', 'musical', 'this', 'made', 'and', 'sound', 'based', 'some', 'can', 'instruments', 'may', 'machine', 'sounds', 'audio', 'recordings', 'recording', 'other', 'produced', 'electronic', 'such', 'also', 'more', 'with', 'art', 'was', 'for', 'aesthetic', 'example', 'being', 'fluxus', 'artists', 'composition', 'early', 'young', 'rock', 'wave', 'industrial', 'works', 'his', 'from', 'one', 'not', 'signal', 'what', 'any', 'have', 'time', 'like', 'paul', 'hegarty', 'work', 'these', 'john', 'cage', 'which', 'all', 'japanese', 'genre', 'but', 'russolo', 'used', 'white', 'same', 'track', 'artist', 'first', 'had', 'found', 'called', 'created', 'paris', 'sirens', 'piece', 'using', 'percussion', 'tape', 'musique', 'concrète', 'group', 'recorded', 'various', '1960', 'album', 'cassette', 'ubuweb', 'com', 'ubu']]
        output = {'french': ['French pop music'], 'pop': ['French pop music'], 'music': ['French pop music', 'Noise (music)'], 'the': ['French pop music', 'Edogawa, Tokyo', 'Noise (music)'], 'france': ['French pop music'], 'and': ['French pop music', 'Edogawa, Tokyo', 'Noise (music)'], 'radio': ['French pop music'], 'edogawa': ['Edogawa, Tokyo'], 'with': ['Edogawa, Tokyo', 'Noise (music)'], 'koiwa': ['Edogawa, Tokyo'], 'kasai': ['Edogawa, Tokyo'], 'player': ['Edogawa, Tokyo'], 'high': ['Edogawa, Tokyo'], 'school': ['Edogawa, Tokyo'], 'noise': ['Noise (music)'], 'that': ['Noise (music)'], 'use': ['Noise (music)'], 'musical': ['Noise (music)'], 'this': ['Noise (music)'], 'made': ['Noise (music)'], 'sound': ['Noise (music)'], 'based': ['Noise (music)'], 'some': ['Noise (music)'], 'can': ['Noise (music)'], 'instruments': ['Noise (music)'], 'may': ['Noise (music)'], 'machine': ['Noise (music)'], 'sounds': ['Noise (music)'], 'audio': ['Noise (music)'], 'recordings': ['Noise (music)'], 'recording': ['Noise (music)'], 'other': ['Noise (music)'], 'produced': ['Noise (music)'], 'electronic': ['Noise (music)'], 'such': ['Noise (music)'], 'also': ['Noise (music)'], 'more': ['Noise (music)'], 'art': ['Noise (music)'], 'was': ['Noise (music)'], 'for': ['Noise (music)'], 'aesthetic': ['Noise (music)'], 'example': ['Noise (music)'], 'being': ['Noise (music)'], 'fluxus': ['Noise (music)'], 'artists': ['Noise (music)'], 'composition': ['Noise (music)'], 'early': ['Noise (music)'], 'young': ['Noise (music)'], 'rock': ['Noise (music)'], 'wave': ['Noise (music)'], 'industrial': ['Noise (music)'], 'works': ['Noise (music)'], 'his': ['Noise (music)'], 'from': ['Noise (music)'], 'one': ['Noise (music)'], 'not': ['Noise (music)'], 'signal': ['Noise (music)'], 'what': ['Noise (music)'], 'any': ['Noise (music)'], 'have': ['Noise (music)'], 'time': ['Noise (music)'], 'like': ['Noise (music)'], 'paul': ['Noise (music)'], 'hegarty': ['Noise (music)'], 'work': ['Noise (music)'], 'these': ['Noise (music)'], 'john': ['Noise (music)'], 'cage': ['Noise (music)'], 'which': ['Noise (music)'], 'all': ['Noise (music)'], 'japanese': ['Noise (music)'], 'genre': ['Noise (music)'], 'but': ['Noise (music)'], 'russolo': ['Noise (music)'], 'used': ['Noise (music)'], 'white': ['Noise (music)'], 'same': ['Noise (music)'], 'track': ['Noise (music)'], 'artist': ['Noise (music)'], 'first': ['Noise (music)'], 'had': ['Noise (music)'], 'found': ['Noise (music)'], 'called': ['Noise (music)'], 'created': ['Noise (music)'], 'paris': ['Noise (music)'], 'sirens': ['Noise (music)'], 'piece': ['Noise (music)'], 'using': ['Noise (music)'], 'percussion': ['Noise (music)'], 'tape': ['Noise (music)'], 'musique': ['Noise (music)'], 'concrète': ['Noise (music)'], 'group': ['Noise (music)'], 'recorded': ['Noise (music)'], 'various': ['Noise (music)'], '1960': ['Noise (music)'], 'album': ['Noise (music)'], 'cassette': ['Noise (music)'], 'ubuweb': ['Noise (music)'], 'com': ['Noise (music)'], 'ubu': ['Noise (music)']}
        self.assertEqual(keyword_to_titles(input_value), output)
        input_value2 = [['Fiskerton, Lincolnshire', 'Bearcat', 1259869948, 5853, ['fiskerton', 'village', 'and', 'the', 'was', 'which', 'that', 'been']], ['Reflection-oriented programming', 'Nihonjoe', 1143366937, 38, []], ['B (programming language)', 'jack johnson', 1196622610, 5482, ['language', 'the', 'thompson', 'ritchie', 'was', 'from', 'bcpl', 'and', 'that', 'for', 'pdp', 'version', 'this']]]
        output_value2 = {'fiskerton': ['Fiskerton, Lincolnshire'], 'village': ['Fiskerton, Lincolnshire'], 'and': ['Fiskerton, Lincolnshire', 'B (programming language)'], 'the': ['Fiskerton, Lincolnshire', 'B (programming language)'], 'was': ['Fiskerton, Lincolnshire', 'B (programming language)'], 'which': ['Fiskerton, Lincolnshire'], 'that': ['Fiskerton, Lincolnshire', 'B (programming language)'], 'been': ['Fiskerton, Lincolnshire'], 'language': ['B (programming language)'], 'thompson': ['B (programming language)'], 'ritchie': ['B (programming language)'], 'from': ['B (programming language)'], 'bcpl': ['B (programming language)'], 'for': ['B (programming language)'], 'pdp': ['B (programming language)'], 'version': ['B (programming language)'], 'this': ['B (programming language)']}
        self.assertEqual(keyword_to_titles(input_value2), output_value2)

        # Edge case
        self.assertEqual(keyword_to_titles([['', '', 0, 0, []]]), {})
    
    def test_title_to_info(self):
        input_value = ['List of Saturday Night Live musical sketches', 'Pegship', 1134966249, 13287, ['saturday', 'night', 'live', 'the', 'chris']], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842, ['becker', 'and', 'guitar', 'the', 'joe', 'music', 'records', 'film', 'soundtrack', 'horror', 'released', 'performed']], ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562, ['johnson', 'canadian', 'soccer', 'player', 'played', 'for', 'league', 'canada', 'was', 'the', 'his', 'and', 'team', 'season', 'after', 'year', 'mls', 'first', 'scored', 'goal', 'with', 'december', '2008', 'real', 'salt', 'lake', 'against', 'cup', '2013', '2016']]
        output_value = {'List of Saturday Night Live musical sketches': {'author': 'Pegship', 'timestamp': 1134966249, 'length': 13287}, 'Joe Becker (musician)': {'author': 'Nihonjoe', 'timestamp': 1203234507, 'length': 5842}, 'Will Johnson (soccer)': {'author': 'Burna Boy', 'timestamp': 1218489712, 'length': 3562}}
        self.assertEqual(title_to_info(input_value), output_value)

        input_value2 = [['Dalmatian (dog)', 'Mr Jake', 1207793294, 26582, ['the', 'dalmatian', 'breed', 'dog', 'for', 'its', 'with', 'liver', 'spots', 'and', 'used', 'can', 'that', 'were', 'breeds', 'dalmatians', 'kennel', 'club', 'well', 'akc', 'standard', 'from', 'both', 'but', 'not', 'are', 'usually', 'color', 'blue', 'dogs', 'other', 'puppies', 'their', 'first', 'they', 'have', 'may', 'which', 'often', 'health', 'deafness', 'hearing', 'years', 'was', 'this', 'also', 'been', 'hyperuricemia', 'uric', 'acid', 'backcross', 'project', 'horses', 'fire']], ['1936 in music', 'RussBot', 1243745950, 23417, ['music', 'the', '1936', 'country', 'january', 'march', 'symphony', 'orchestra', 'april', 'concerto', 'may', 'and', 'little', 'time', 'december', 'film', 'opera', 'cole', 'with', 'his', 'conductor', 'introduced', 'shirley', 'dorothy', 'fields', 'jerome', 'kern', 'fred', 'astaire', 'swing', 'your', 'for', 'musical', 'love', 'dance', 'billy', 'harry', 'you', 'ginger', 'rogers', 'irving', 'berlin', 'follow', 'fleet', 'richard', 'johnny', 'rhythm', 'bing', 'crosby', 'sing', 'singer', 'jack', 'string', 'quartet', 'london', 'production', 'opened', 'theatre', 'ran', 'performances', 'september', 'october', 'starring', 'november', 'featuring', 'composer', 'pianist', 'songwriter', 'february', 'june', 'august']]]
        output_value2 = {'Dalmatian (dog)': {'author': 'Mr Jake', 'timestamp': 1207793294, 'length': 26582}, '1936 in music': {'author': 'RussBot', 'timestamp': 1243745950, 'length': 23417}}
        self.assertEqual(title_to_info(input_value2), output_value2)

        self.assertEqual(title_to_info([['', '', 0, 0, []]]), {'': {'author': '', 'timestamp': 0, 'length': 0}})

    def test_search(self):
        keyword_titles = {
        'musical': ['List of Canadian musicians', 'Noise (music)', '1986 in music', '2009 in music', 'Rock music', 'Arabic music', 'Richard Wright (musician)', '1936 in music', 'Annie (musical)', 'Indian classical music', '1996 in music', 'The Hunchback of Notre Dame (musical)', 'Traditional Thai musical instruments', 'Texture (music)', '2007 in music', '2008 in music']
        }
        search_result = ['List of Canadian musicians', 'Noise (music)', '1986 in music', '2009 in music', 'Rock music', 'Arabic music', 'Richard Wright (musician)', '1936 in music', 'Annie (musical)', 'Indian classical music', '1996 in music', 'The Hunchback of Notre Dame (musical)', 'Traditional Thai musical instruments', 'Texture (music)', '2007 in music', '2008 in music']
        self.assertEqual(search('musical', keyword_titles), search_result)

        self.assertEqual(search('ViRus', {'virus': ['List of dystopian music, TV programs, and games', 'Scores (computer virus)']}), [])
        self.assertEqual(search('forest', {'forest': ["Wake Forest Demon Deacons men's soccer"]}), ["Wake Forest Demon Deacons men's soccer"])

    def test_article_length(self):
        self.assertEqual(article_length(10000, search('british', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), ['1986 in music'])
        self.assertEqual(article_length(4000, search('lens', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), [])
        self.assertEqual(article_length(-10, search('NucLEar', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), [])
        self.assertEqual(article_length(0, search('parts', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), [])
    
    def test_key_by_author(self):
        self.assertEqual(key_by_author(search('songwriter', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), {'Jack Johnson': ['List of Canadian musicians', '2006 in music'], 'jack johnson': ['1986 in music'], 'RussBot': ['2009 in music', '1936 in music'], 'Nihonjoe': ['1996 in music'], 'Bearcat': ['2007 in music'], 'Burna Boy': ['2008 in music']})
        self.assertEqual(key_by_author(search('mode', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), {'Pegship': ['Mode (computer interface)']})
        self.assertEqual(key_by_author(search('General', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), {})
        self.assertEqual(key_by_author(search('', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), {})

    def test_filter_to_author(self):
        self.assertEqual(filter_to_author('Mr Jake', search('breed', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), ['Dalmatian (dog)'])
        self.assertEqual(filter_to_author('Jack Johnson', search('project', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), [])
        self.assertEqual(filter_to_author('', search('', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), [])
        self.assertEqual(filter_to_author('russbot', search('', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), [])

    def test_filter_out(self):
        self.assertEqual(filter_out('compare', search('comparison', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), ['Embryo drawing'])
        self.assertEqual(filter_out('many', search('social', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), ['List of Canadian musicians', 'Rock music', 'Digital photography'])
        self.assertEqual(filter_out('', search('stage', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), ['2009 in music', 'Alex Turner (musician)', 'The Hunchback of Notre Dame (musical)'])

    def test_articles_from_year(self):
        self.assertEqual(articles_from_year(2007, search('michael', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), ['List of Canadian musicians'])
        self.assertEqual(articles_from_year(2006, search('time', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), ['List of dystopian music, TV programs, and games', 'Georgia Bulldogs football', 'Time travel', 'Python (programming language)', 'Tony Kaye (musician)', 'Semaphore (programming)'])
        self.assertEqual(articles_from_year(1990, search('concept', keyword_to_titles(article_metadata())), title_to_info(article_metadata())), [])
          
    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

    @patch('builtins.input')
    def test_article_length_integration_test(self, input_mock):
        keyword = 'top'
        advanced_option = 1
        advanced_response = 20000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['2007 Bulldogs RLFC season']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_key_by_author_integration_test(self, input_mock):
        keyword = 'may'
        advanced_option = 2
        # advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: {'jack johnson': ['Noise (music)', '1986 in music'], 'Gary King': ['1922 in music'], 'RussBot': ['2009 in music', '1936 in music', 'Comparison of programming languages (basic instructions)'], 'Pegship': ['Black dog (ghost)', 'Personal computer', 'Mode (computer interface)'], 'Mr Jake': ['Dalmatian (dog)', 'Digital photography'], 'Jack Johnson': ['Time travel', 'Annie (musical)', '2006 in music'], 'Burna Boy': ['Python (programming language)', 'Indian classical music', '2008 in music'], 'Nihonjoe': ['1996 in music', 'Semaphore (programming)'], 'Bearcat': ['Covariance and contravariance (computer science)', 'Ruby (programming language)', '2007 in music']}\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_filter_to_author_integration_test(self, input_mock):
        keyword = 'states'
        advanced_option = 3
        advanced_response = 'Nihonjoe'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Old-time music']\n"

        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_filter_out_keyword_integration_test(self, input_mock):
        keyword = 'work'
        advanced_option = 4
        advanced_response = 'employ'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Noise (music)', 'Rock music', 'Human computer', 'Embryo drawing', 'Sean Delaney (musician)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_None_integration_test(self, input_mock):
        keyword = 'key'
        advanced_option = 6
        # advanced_response = 20000

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Rock music', 'Lua (programming language)', 'Mode (computer interface)']\n"

        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_filter_out_year_integration_test(self, input_mock):
        keyword = 'from'
        advanced_option = 5
        advanced_response = 2006

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Kevin Cadogan', 'Guide dog', 'List of dystopian music, TV programs, and games', 'Georgia Bulldogs football', 'Time travel', 'Python (programming language)', '1996 in music', 'Joseph Williams (musician)', 'Tony Kaye (musician)', 'Semaphore (programming)']\n"

        self.assertEqual(output, expected)
# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
