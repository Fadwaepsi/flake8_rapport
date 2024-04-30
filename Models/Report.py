import json


class Report:
    def __init__(self):
        self.players = []
        self.tournaments = []
        self.load_players()
        self.load_tournaments()

    def load_players(self):
        """
        Charge la list des jrs depuis le fichier players.json.
        En cas d'err (fichier intvable ou erreur
        de décodage JSON), un message d'erreur est affiché.

        Returns:
            list: Liste des joueurs. Retourne une liste vide en cas d'erreur.
        """
        try:
            with open('data/players.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Le fichier des joueurs n'existe pas.")
        except json.JSONDecodeError:
            print("Erreur lors de la lecture du fichier JSON.")
        return []

    # Optionnellement, si vous voulez aussi charger les tournois :
    def load_tournaments(self):
        """
        Charge la liste des trnois depuis le fichier tournaments.json. En cas d'err (fichier intrvble ou err
        de décodage JSON), un message d'erreur est affiché.

        Returns:
            list: Liste des tournois. Retourne une liste vide en cas d'erreur.
        """
        try:
            with open('data/tournaments.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Le fichier des tournois n'existe pas.")
        except json.JSONDecodeError:
            print("Erreur lors de la lecture du fichier JSON.")
        return []
