from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)

    def test_search(self):
        expected_empty_string_result = []
        self.assertEqual(search(''), expected_empty_string_result)

        expected_dog_result = [
            ['Black dog (ghost)', 'Pegship', 1220471117, 14746],
            ['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138], 
            ['Dalmatian (dog)', 'Mr Jake', 1207793294, 26582], 
            ['Guide dog', 'Jack Johnson', 1165601603, 7339], 
            ['Sun dog', 'Mr Jake', 1208969289, 18050]
            ]
        self.assertEqual(search('dog'), expected_dog_result)

        expected_MusIC_result = [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['Noise (music)', 'jack johnson', 1194207604, 15641], ['1922 in music', 'Gary King', 1242717698, 11576], ['1986 in music', 'jack johnson', 1048918054, 6632], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Arabic music', 'RussBot', 1209417864, 25114], ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], ['1936 in music', 'RussBot', 1243745950, 23417], ['1962 in country music', 'Mack Johnson', 1249862464, 7954], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['David Gray (musician)', 'jack johnson', 1159841492, 7203], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['Texture (music)', 'Bearcat', 1161070178, 3626], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]
        self.assertEqual(search('MusIC'), expected_MusIC_result)

        expected_STATE_result = [['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['2009 Louisiana Tech Bulldogs football team', 'Nihonjoe', 1245796406, 22410], ['Mode (computer interface)', 'Pegship', 1182732608, 2991]]
        self.assertEqual(search('STATE'), expected_STATE_result)

        self.assertEqual(search(""), [])

    def test_article_length(self):
        expected_dog_3000_result = [['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138]]
        self.assertEqual(article_length(4000, search('dog')), expected_dog_3000_result)

        expected_10000_FIlm_result = [['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], ['Geoff Smith (British musician)', 'Pegship', 1194687509, 2043], ['Joseph Williams (musician)', 'Pegship', 1140752684, 4253], ['The Hunchback of Notre Dame (musical)', 'Nihonjoe', 1192176615, 42]]
        self.assertEqual(article_length(10000, search('FIlm')), expected_10000_FIlm_result)

        expected_empty_str_0_result = []
        self.assertEqual(article_length(0, search('')), expected_empty_str_0_result)

    def test_unique_authors(self):
        expected_sound_result = [['Noise (music)', 'jack johnson', 1194207604, 15641], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Personal computer', 'Pegship', 1220391790, 45663]]
        self.assertEqual(unique_authors(7, search('sound')), expected_sound_result)

        self.assertEqual(unique_authors(0, search('YOU')), [])

        self.assertEqual(unique_authors(3, search('')), [])

        expected_song_5_result = [['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458]]
        self.assertEqual(unique_authors(5, search('song')), expected_song_5_result)

    def test_most_recent_article(self):
        expected_and_result = ['Fisk University', 'RussBot', 1263393671, 16246]
        self.assertEqual(most_recent_article(search('and')), expected_and_result)

        expected_album_result = ['Rock music', 'Mack Johnson', 1258069053, 119498]
        self.assertEqual(most_recent_article(search('album')), expected_album_result)

        self.assertEqual(most_recent_article(''), [])

    def test_favorite_author(self):
        self.assertEqual(favorite_author('Burna Boy', search('hot')), True)
        self.assertEqual(favorite_author('shakira', search('jazz')), False)
        self.assertEqual(favorite_author('', search('')), False)
        self.assertEqual(favorite_author('Beyonce', search('dance')), False)

    def test_title_and_author(self):
        expecetd_genre_result = [('Noise (music)', 'jack johnson'), ('Rock music', 'Mack Johnson'), ('Arabic music', 'RussBot')]
        self.assertEqual(title_and_author(search('genre')), expecetd_genre_result)

        expected_electronic_result = [('List of Canadian musicians', 'Jack Johnson'), ('Noise (music)', 'jack johnson'), ('Rock music', 'Mack Johnson'), ('2007 in music', 'Bearcat')]
        self.assertEqual(title_and_author(search('electronic')), expected_electronic_result)

        expected_post_result = [('Rock music', 'Mack Johnson'), ('List of dystopian music, TV programs, and games', 'Bearcat')]
        self.assertEqual(title_and_author(search('PosT')), expected_post_result)

        self.assertEqual(title_and_author(''), [])

    def test_refine_search(self):
        expected_have_his_result = [['Noise (music)', 'jack johnson', 1194207604, 15641], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Black dog (ghost)', 'Pegship', 1220471117, 14746], ['Arabic music', 'RussBot', 1209417864, 25114], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Time travel', 'Jack Johnson', 1140826049, 35170], ['Annie (musical)', 'Jack Johnson', 1223619626, 27558], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['Indian classical music', 'Burna Boy', 1222543238, 9503], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Mode (computer interface)', 'Pegship', 1182732608, 2991]]
        self.assertEqual(refine_search('have', search('his')), expected_have_his_result)

        expected_out_result =[['Alex Turner (musician)', 'jack johnson', 1187010135, 9718]]
        self.assertEqual(refine_search('out', search('get')), expected_out_result)

        self.assertEqual(refine_search('same', search('')), [])

        self.assertEqual(refine_search('era', search('year')), [])


    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_integration_test_2(self, input_mock):
        keyword = 'sun'
        advanced_option = 2
        advanced_response = 3

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Sun dog', 'Mr Jake', 1208969289, 18050]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_3(self, input_mock):
        keyword = 'computer'
        advanced_option = 3
        # advanced_response = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) +  "\nHere are your articles: ['Human computer', 'Bearcat', 1248275178, 4750]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_4(self, input_mock):
        keyword = 'band'
        advanced_option = 4
        advanced_response = 'RussBot'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['Lights (musician)', 'Burna Boy', 1213914297, 5898], ['Old-time music', 'Nihonjoe', 1124771619, 12755], ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], ['1996 in music', 'Nihonjoe', 1148585201, 21688], ['David Levi (musician)', 'Gary King', 1212260237, 3949], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['Sean Delaney (musician)', 'Nihonjoe', 1204328174, 5638], ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], ['2007 in music', 'Bearcat', 1169248845, 45652], ['2008 in music', 'Burna Boy', 1217641857, 107605]]\nYour favorite author is in the returned articles!\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_5(self, input_mock):
        keyword = 'london'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: [('1986 in music', 'jack johnson'), ('Tim Arnold (musician)', 'jack johnson'), ('Richard Wright (musician)', 'RussBot'), ('1936 in music', 'RussBot'), ('Alex Turner (musician)', 'jack johnson'), ('2008 in music', 'Burna Boy')]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_6(self, input_mock):
        keyword = 'after'
        advanced_option = 6
        advanced_response = 'here'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nNo articles found\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_7(self, input_mock):
        keyword = 'top'
        advanced_option = 7
        # advanced_response = 'here'

        output = get_print(input_mock, [keyword, advanced_option])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: [['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['2007 Bulldogs RLFC season', 'Burna Boy', 1177410119, 11116], ['2006 in music', 'Jack Johnson', 1171547747, 105280], ['2008 in music', 'Burna Boy', 1217641857, 107605]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_8(self, input_mock):
        keyword = 'early'
        advanced_option = 1
        advanced_response = 5000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Embryo drawing', 'Jack Johnson', 1034459202, 1712]]\n"

        self.assertEqual(output, expected)
    

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
