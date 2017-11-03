# coding=utf-8
import fresh_tomatoes
import media

""" This file creates the instances of the movie Class that needs
    to be displayed on the website.

    The arguments required to create an instance includes:
    1. The movie title as a string.
    2. The movie story line as a string.
    3. The movie poster image as a string, via a URL.
    4. The movie trailer video as a string, via a URL.
"""

star_wars_a_new_hope = media.Movie(
    "Star Wars Episode IV: A New Hope",
    "Nineteen years after the formation of the Empire,"
    "Luke Skywalker is thrust into the struggle of the Rebel Alliance when he"
    "meets Obi-Wan Kenobi, who has lived for years in seclusion on the desert"
    "planet of Tatooine.",
    "https://lumiere-a.akamaihd.net/v1/images/Star-Wars-New-Hope-IV-Poster_c217085b.jpeg?region=49%2C43%2C580%2C914",  # NOQA
    "https://www.youtube.com/watch?v=XHk5kCIiGoM")

star_wars_the_empire_strikes_back = media.Movie(
    "Star Wars: The Empire Strikes Back",
    "After the destruction of the Death Star,"
    "Imperial forces continue to pursue the Rebels.",
    "https://lumiere-a.akamaihd.net/v1/images/Star-Wars-Empire-Strikes-Back-V-Poster_878f7fce.jpeg?region=25%2C22%2C612%2C953&width=600",  # NOQA
    "https://www.youtube.com/watch?v=yCtaxF7XutI")

star_wars_return_of_the_jedi = media.Movie(
    "Star Wars Episode IV: The Last Jedi",
    "Luke Skywalker's peaceful and solitary existence gets upended when he"
    "meets Rey, a young woman who shows strong signs of the Force.",
    "https://lumiere-a.akamaihd.net/v1/images/Star-Wars-Return-Jedi-VI-Poster_a10501d2.jpeg?region=12%2C9%2C618%2C982&width=480",  # NOQA
    "https://www.youtube.com/watch?v=7-5nJa2sUXg")

star_wars_the_phantom_menace = media.Movie(
    "Star Wars Episode I: The Phantom Menace",
    "Stranded on the desert planet Tatooine after rescuing young"
    "Queen Amidala from the impending invasion of Naboo, Jedi apprentice"
    "Obi-Wan Kenobi and his Jedi Master Qui-Gon Jinn discover nine-year-old"
    "Anakin Skywalker, a young slave unusually strong in the Force",
    "https://lumiere-a.akamaihd.net/v1/images/Star-Wars-Phantom-Menace-I-Poster_3c1ff9eb.jpeg?region=15%2C9%2C651%2C979&width=600",  # NOQA
    "https://www.youtube.com/watch?v=7_Os-RdIRfc")

star_wars_attack_of_the_clones = media.Movie(
    "Star Wars Episode II: Attack of the Clones",
    "Ten years after the invasion of Naboo, the galaxy is on the brink of civil war."
    "Under the leadership of a renegade Jedi named Count Dooku, thousands of"
    "solar systems threaten to break away from the Galactic Republic.",
    "https://lumiere-a.akamaihd.net/v1/images/Star-Wars-Attack-Clones-II-Poster_53baa2e7.jpeg?region=18%2C0%2C660%2C1000&width=600",  # NOQA
    "https://www.youtube.com/watch?v=KgZBhg76XCo")

star_wars_revenge_of_the_sith = media.Movie(
    "Star Wars Episode III: Revenge of the Sith",
    "Years after the onset of the Clone Wars, the noble Jedi Knights lead a"
    "massive clone army into a galaxy-wide battle against the Separatists.",
    "https://lumiere-a.akamaihd.net/v1/images/Star-Wars-Revenge-Sith-III-Poster_646108ce.jpeg?region=0%2C0%2C736%2C1090&width=600",  # NOQA
    "https://www.youtube.com/watch?v=Yx6F46-_3Ec")

star_wars_the_force_awakens = media.Movie(
    "Star Wars Episode VII: The Force Awakens",
    "Thirty years after the defeat of the Empire, Luke Skywalker has vanished and"
    "a new threat has risen: The First Order, led by the mysterious Supreme Leader Snoke"
    "and his dark side enforcer, Kylo Ren.",
    "https://lumiere-a.akamaihd.net/v1/images/avco_payoff_1-sht_v7_lg_32e68793.jpeg?region=0%2C0%2C1620%2C2400&width=600",  # NOQA
    "https://www.youtube.com/watch?v=sGbxmsDFVnE")

star_wars_rogue_one = media.Movie(
    "Star Wars: Rogue One",
    "In a time of conflict, a group of unlikely heroes band together on a"
    "mission to steal the plans to the Death Star, the Empire’s ultimate"
    "weapon of destruction.",
    "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",  # NOQA
    "https://www.youtube.com/watch?v=vD19Ulth7l8")

star_wars_the_last_jedi = media.Movie(
    "Star Wars Episode VIII: The Last Jedi",
    "The next chapter in the Skywalker saga arrives December 2017.",
    "https://lumiere-a.akamaihd.net/v1/images/the-last-jedi-theatrical-poster-film-page_bca06283.jpeg?region=0%2C0%2C480%2C711",  # NOQA
    "https://www.youtube.com/watch?v=zB4I68XVPzQ")

""" "movies" is the array of the movie instances. """
movies = [star_wars_a_new_hope,
          star_wars_the_empire_strikes_back,
          star_wars_return_of_the_jedi,
          star_wars_the_phantom_menace,
          star_wars_attack_of_the_clones,
          star_wars_revenge_of_the_sith,
          star_wars_the_force_awakens,
          star_wars_rogue_one,
          star_wars_the_last_jedi]


""" This sends the movies array to the fresh_tomatoes open_movies_page() method which
    uses the movie instances to create the website. """

fresh_tomatoes.open_movies_page(movies)
