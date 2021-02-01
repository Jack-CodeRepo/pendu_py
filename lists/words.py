#!/usr/bin/env python
# coding: utf-8
# ==================================================================================================



# ==================================================================================================
#   IMPORT
# ==================================================================================================



# ==================================================================================================
#   VARIABLES GLOBALES
# ==================================================================================================



# ==================================================================================================
#   LISTS
# ==================================================================================================

NOMS = ["Francois Couperin","Marin Marais","Wolfgang Amadeus Mozart",
            "Giovanni Pierluigi da Palestrina","Ludwig van Beethoven","Camille Saint-Saens",
            "Maurice Ravel","Claude Debussy","Jean-Philippe Rameau",
            "Gustav Mahler","Leo Bouwer","Anthony Sylvestre",
            "Piotr Ilitch Tchaikovsky","Dmitri Chostakovitch","Modest Mussorgsky",
            "Jean-Sebastien Bach","Arcangelo Corelli","Antonio Vivaldi",
            "Giovanni Battista Pergolesi","Josquin des Pres","Domenico Scarlatti",
            "Henry Purcell","Georg Friedrich Haendel","Gabriel Faure",
            "Yann Tiersen","Bruno Coulais","Sylvain Rifflet",
            "Franz Schubert","Arvo Part","Marc-Antoine Charpentier",
            "Francis Poulenc","Guy Ropartz","Erik Satie",
            "Jean-Baptiste Lully","Robert de Visee","Clément Jannequin",
            "Alexandre Agricola","Gregorio Allegri","Claudio Monteverdi",
            "William Byrd","Michael Praetorius","Tomasi Albinoni",
            "Luigi Bocherini","Robert Schumann","Richard Wagner",
            "Bedrich Smetana","Wojciech Kilar","Johannes Brahms",
            "Richard Strauss","Antonin Dvorak","Edward Grieg",
            "Edward Elgar","Jean Sibelius","Serguei Prokofiev",
            "Aaron Copland","Samuel Barber","Benjamin Britten",
            "Philip Glass","John Dowland"
]



MHWI = ["Alatreon","Anjanath","Anjanath-Tonnerre",
            "Banbaro","Barioth","Barioth-Crocgivre",
            "Barroth","Bazelgeuse","Bazelgeuse-Vulcan",
            "Behemoth","Beotodus","Brachydios",
            "Brachydios-Tempete","Deviljho","Deviljho-Carnage",
            "Diablos","Diablos-Noire","Dodogama",
            "Fatalis","Glavenus","Glavenus-Acide",
            "Grand-Girros","Grand-Jagras","Jyuratodus",
            "Kirin","Kulu-Ya-Ku","Kulve-Taroth",
            "Kushala-Daora","Lavasioth","Legiana",
            "Legiana-Blizzard","Leshen","Lunastra",
            "Namielle","Nargacuga","Nergigante",
            "Nergigante-Chaos","Odogaron","Odogaron-Desastre",
            "Paolumu","Paolumu-Belladone","Pukei-Pukei",
            "Pukei-Pukei-Corail","Pukei-Pukei-Corail","Radobaan",
            "Rajang","Rajang-Orage","Rathalos",
            "Rathalos-Azur","Rathalos-D-Argent","Rathian",
            "Rathian-Sakura","Rathian-D-Or","Safi-Jiiva",
            "Shara-Ishvalda","Teostra","Tigrex",
            "Tigrex-berserk","Tobi-Kadachi","Tobi-Kadachi-Vipere",
            "Tzitzi-Ya-Ku","Uragaan","Vaal-Hazak",
            "Vaal-Hazak-Fleau","Velkhana","Vieux-Leshen",
            "Xeno-Jiiva","Yian Garuga","Yian-Garuga-Balafre",
            "Zinogre","Zinogre-stygien","Zorah-Magdaros"
]



MHGU = ["Agnaktor","Akantor","Arzuros",
            "Arzuros Crâne-ardent","Astalos","Astalos-Prince-Orage",
            "Barroth","Barioth","Basarios",
            "Blangonga","Brachydios","Brachydios-Tempete",
            "Bulldrome","Ceanataur-Shogun","Ceanataur-Brise-Os",
            "Cephadrome","Congalala","Deviljho",
            "Deviljho-Carnage","Diablos","Diablos-Bain-de-sang",
            "Duramboros","Gammoth","Gammoth Givre-ancien",
            "Gendrome","Giadrome","Glavenus",
            "Glavenus Lame-chaos","Gore Magala","Gore Magala du chaos",
            "Grand Maccao","Gravios","Gypceros",
            "Hermitaur Daimyo","Hermitaur Poing-fer","Iodrome",
            "Kecha Wacha","Khezu","Lagiacrus",
            "Lagombi","Lagombi Maître-neige","Lavasioth",
            "Ludroth royal","Malfestio","Malfestio Lune-noire",
            "Mizutsune","Mizutsune Perce-âme","Najarala",
            "Nargacuga","Nargacuga Vent-acier","Nerscylla",
            "Nibelsnarf","Plesioth","Rajang",
            "Rajang orage","Rathalos","Rathalos-Roi-Enfer",
            "Rathalos-D-Argent","Rathian","Rathian Reine-poison",
            "Rathian-D-Or","Reine-Seltas","Seltas",
            "Seregios","Tetsucabra","Tetsucabra-Brise-Roc",
            "Tigrex","Tigrex-Griffe-Sombre","Ukanlos",
            "Uragaan","Uragaan-Roi-Cristal","Velocidrome",
            "Volvidon","Yian-Garuga","Yian-Garuga-Œil-Mort",
            "Yian-Kut-Ku","Zamtrios","Zinogre",
            "Zinogre-Feu-Du-Ciel","Alatreon","Amatsu",
            "Ahtal-Ka","Chameleos","Fatalis",
            "Fatalis-Pourpre","Fatalis-Ancien","Kirin",
            "Kushala-Daora","Lao-Shan-Lung","Nakarkos",
            "Shagaru-Magala","Teostra","Valstrax"
]



MH4U = ["Akantor","Basarios","Basarios rubis",
            "Brachydios","Brachydios enrage","Cephadrome",
            "Congalala","Congalala emeraude","Deviljho",
            "Deviljho carnage","Diablos","Diablos noire",
            "Gendrome","Gore Magala","Gore Magala du chaos",
            "Grand Jaggi","Gravios","Gravios onyx",
            "Gypceros","Gypceros amethyste","Hermitaur Daimyo",
            "Hermitaur Daimyo prune","Iodrome","Kecha Wacha",
            "Kecha Wacha blanc","Khezu","Khezu grenat",
            "Lagombi","Monoblos","Monoblos ivoire",
            "Najarala","Najarala du deluge","Nerscylla",
            "Nerscylla spectrale","Rajang","Rajang orage",
            "Rathalos","Rathalos azur","Rathalos d'argent",
            "Rathian","Rathian sakura","Rathian d'or",
            "Reine Seltas","Reine Seltas du desert","Seltas",
            "Seltas du desert","Seregios","Tetsucabra",
            "Tetsucabra feroce","Tigrex","Tigrex berserk",
            "Tigrex magma","Ukanlos","Velocidrome",
            "Yian Garuga","Yian Kut-Ku","Yian Kut-Ku bleu",
            "Zamtrios","Zamtrios tigre","Zinogre",
            "Zinogre stygien","Chameleos","Dalamadur",
            "Dalamadur Shah","Dah'ren Mohran","Fatalis",
            "Fatalis blanc","Fatalis pourpre","Gogmazios",
            "Kirin","Kirin Oroshi","Kushala Daora",
            "Kushala Daora rouille","Shagaru Magala","Teostra"
]



MH3U = ["Agnaktor","Agnaktor-Glacial","Alatreon",
            "Arzuros","Barioth","Barioth-Des-Sables",
            "Barroth","Barroth-De-Jade","Brachydios",
            "Ceadeus","Ceadeus-Barbedor","Deviljho",
            "Deviljho-Affame","Diablos","Diablos-Noire",
            "Dire-Miralis","Duramboros","Duramboros-Rouille",
            "Gigginox","Gigginox-Foudroyant","Gobul",
            "Grand-Baggi","Grand-Jaggi","Grand-Wroggi",
            "Jhen-Mohran","Jhen-Mohran-Sacre","Qurupeco",
            "Qurupeco-Vermillon","Lagiacrus","Lagiacrus-Ivoire",
            "Lagiacrus-Abyssal","Lagombi","Ludroth-Royal",
            "Ludroth-Pourpre","Nargacuga","Nargacuga-Vert",
            "Nargacuga-Selenite","Nibelsnarf","Plesioth",
            "Plesioth-Vert","Rathalos","Rathalos-Azur",
            "Silver","Rathalos","Rathalos-Argente",
            "Rathian","Rathian-Rose","Rathian-Doree",
            "Uragaan","Uragaan-D-Acier","Volvidon",
            "Zinogre","Zinogre-Stygien"
]

