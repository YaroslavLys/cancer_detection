import csv
import random

NAMES = ['Anastasia', 'Andriy', 'Bohdan', 'Daria', 'Denys', 'Iryna', 'Ivan', 'Kateryna', 'Kyrylo', 'Larysa',
         'Liliya', 'Maksym', 'Mariia', 'Marko', 'Mykola', 'Nataliia', 'Oleh', 'Oksana', 'Pavlo', 'Petro',
         'Roksolana', 'Serhii', 'Sofiia', 'Stanislav', 'Svitlana', 'Taras', 'Tetiana', 'Uliana', 'Valentyn',
         'Valeriy', 'Vasyl', 'Veronika', 'Viktor', 'Volodymyr', 'Yana', 'Yaroslav', 'Yevhen', 'Yuliya',
         'Zakhar', 'Zinoviy', 'Zoryana', 'Bohdanna', 'Ihor', 'Iryna', 'Khrystyna', 'Lesia', 'Maksymilian',
         'Nadiya', 'Olena', 'Roman']

SURNAMES = ['Andrusiak', 'Bilous', 'Boiko', 'Cherniak', 'Danko', 'Dubovyi', 'Fedorchuk', 'Havryliuk', 'Holovko',
            'Horishny', 'Ivanchenko', 'Kovalenko', 'Kryvda', 'Kuznietsov', 'Lysenko', 'Melnik', 'Mykytiuk', 'Oliynyk',
            'Pavliuk', 'Petrenko', 'Protsyk', 'Rudenko', 'Savchuk', 'Shcherbak', 'Sokolov', 'Tkachenko', 'Tyshchenko',
            'Vasylchenko', 'Yakovenko', 'Zelenko', 'Zhyvotovskyi']

EMAILS = ['johndoe@example.com', 'jane.doe@example.com', 'alexsmith@example.com', 'bobross@example.com',
          'amy.wong@example.com', 'philip.fry@example.com', 'sarah.connor@example.com', 'john.connor@example.com',
          'clarke.griffin@example.com', 'bellamy.blake@example.com', 'tonystark@example.com',
          'steve.rogers@example.com', 'thor.odinson@example.com', 'bruce.banner@example.com',
          'natasha.romanoff@example.com', 'clint.barton@example.com', 'peter.parker@example.com',
          'wanda.maximoff@example.com', 'vision@example.com', 'sam.wilson@example.com', 'bucky.barnes@example.com',
          'tchalla@example.com', 'groot@example.com', 'rocket.raccoon@example.com', 'drax@example.com',
          'gamora@example.com', 'nebula@example.com', 'mantis@example.com', 'valkyrie@example.com', 'loki@example.com',
          'peter.quill@example.com', 'gamora.zoe@example.com', 'chris.pratt@example.com',
          'scarlet.johansson@example.com', 'mark.ruffalo@example.com', 'robert.downey@example.com',
          'chris.hemsworth@example.com', 'chris.evans@example.com', 'jeremy.renner@example.com',
          'tom.holland@example.com', 'elizabeth.olsen@example.com', 'sebastian.stan@example.com',
          'chadwick.boseman@example.com', 'vin.diesel@example.com', 'bradley.cooper@example.com',
          'dave.bautista@example.com', 'pom.klementieff@example.com', 'karen.gillan@example.com',
          'tessa.thompson@example.com', 'tom.hiddleston@example.com']

ADDRESS = ['Lviv', 'Kyiv', 'Odesa']


def generate_data():
    with open("data.csv", "w") as f:
        writer = csv.writer(f, delimiter=",")
        for _ in range(995):
            writer.writerow([random.choice(NAMES),
                             random.choice(SURNAMES),
                             random.choice(EMAILS),
                             random.randint(18, 60),
                             random.choice(ADDRESS)])
        for _ in range(5):
            writer.writerow([random.choice(NAMES),
                             random.choice(SURNAMES),
                             random.choice(EMAILS),
                             random.randint(18, 60),
                             random.randint(1000, 5000)])


generate_data()
