from tinydb import TinyDB


class Player:

    def __init__(
        self,
        player_id: int,
        last_name: str,
        first_name: str,
        birthday: str,
        city: str,
        rank: int,
    ):
        self.player_id = player_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.city = city
        self.rank = rank
        self.score = 0.0
        self.adversaries = []

        self.player_db = TinyDB("data/players.json")

    def serialize_player(self):
        """Return players info"""
        return {
            "id": self.player_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "city": self.city,
            "rank": self.rank,
            "score": self.score,
            "adversaries": self.adversaries,
        }

    def save_player_db(self):
        """Save players in database
        Set player ID as document ID
        """
        players_db = self.player_db
        self.player_id = players_db.insert(self.serialize_player())
        players_db.update({"id": self.player_id}, doc_ids=[self.player_id])

    def update_player_db(self, info, option):
        """Update player info (from user input) in database

        param info: user input (str, or int inf "rank")
        param option: update info category
        """
        db = self.player_db
        if option == "rank":
            db.update({option: int(info)}, doc_ids=[self.player_id])
        else:
            db.update({option: info}, doc_ids=[self.player_id])

    @staticmethod
    def load_player_db():
        """Load player database

        return: list of players
        """
        players_db = TinyDB("data/players.json")
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players
