from controllers.reports import ReportsManager
from controllers.tournament import TournamentManager
from models.player import Player
from models.tournament import Tournament
from views.menu import MenuViews
import re


class MenuManager:

    def __init__(self):
        self.menu_view = MenuViews()
        self.tour_cont = TournamentManager()
        self.reports = ReportsManager()

    def main_menu_start(self):
        """Main menu selector :
        Redirects to respective submenus"""

        USER_MENU_CHOICES = {
            "1": self.new_tournament,
            "2": self.resume_tournament,
            "3": self.new_player,
            "4": self.update_player,
            "5": self.reports_menu,
            "exit": self.menu_view.want_exit,
        }
        self.menu_view.main_menu()
        user_input = input().lower()
        self.menu_view.input_prompt()

        if user_input not in USER_MENU_CHOICES.keys():
            self.menu_view.input_error()
        else:
            return USER_MENU_CHOICES[user_input]()

    def new_tournament(self):
        """Create new tournament, serialize and save to DB"""
        self.menu_view.create_new_tournament_menu()
        tournament_info = []
        options = ["name", "location", "description"]

        for item in options:
            self.menu_view.input_prompt_text(item)
            user_input = input()

            if user_input == "back":
                self.main_menu_start()

            else:
                tournament_info.append(user_input)

        tour_players = self.select_players(8)

        self.menu_view.review_tournament(tournament_info, tour_players)
        user_input = input().lower()

        if user_input == "y":
            tournament = Tournament(
                t_id=0,
                name=tournament_info[0],
                location=tournament_info[1],
                start_date="Not started",
                end_date="Not defined",
                description=tournament_info[2],
                players=tour_players,
                current_round=1,
                rounds=[],
            )
            tournament.save_tournament_db()
            self.menu_view.tournament_saved()

            self.menu_view.start_tournament_prompt()
            user_input = input()

            if user_input == "y":
                self.tour_cont.start_tournament(tournament)
            elif user_input == "n":
                self.main_menu_start()

        elif user_input == "n":
            self.main_menu_start()

    def select_players(self, players_total):
        """Select players for new tournament

        @param players_total: number of players (int)
        @return: list of selected players
        """
        players = Player.load_player_db()
        id_list = []
        for i in range(len(players)):
            id_list.append(players[i]["id"])

        tour_players = []

        i = 0
        while i < players_total:
            self.menu_view.select_players(players, i + 1)
            self.menu_view.input_prompt()
            user_input = input()

            if user_input == "back":
                self.main_menu_start()

            elif not user_input.isdigit():
                self.menu_view.input_error()

            elif int(user_input) in id_list:
                index = id_list.index(int(user_input))
                tour_players.append(players[index])
                id_list.remove(id_list[index])
                players.remove(players[index])
                i += 1

            else:
                self.menu_view.player_already_selected()

        return tour_players

    def resume_tournament(self):
        """Select existing tournament to resume"""
        tournament_list = Tournament.load_tournament_db()

        self.menu_view.select_tournament(tournament_list)
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.main_menu_start()

        for i in range(len(tournament_list)):
            if user_input == str(tournament_list[i]["id"]):
                t = tournament_list[i]
                t = Tournament(
                    t["id"],
                    t["name"],
                    t["location"],
                    t["start_date"],
                    t["end_date"],
                    t["description"],
                    t["current_round"],
                    t["players"],
                    t["rounds"],
                    t["rounds_total"],
                )
                self.tour_cont.start_tournament(t)

    def new_player(self):
        """Create new player, serialize and save to DB"""
        self.menu_view.create_new_player_menu()
        player_info = []
        options = ["last name",
                   "first name",
                   "birthday (dd/mm/yyyy)",
                   "city",
                   "rank"]
        for item in options:
            self.menu_view.input_prompt_text(item)
            user_input = input()
            if user_input == "back":
                self.main_menu_start()
            elif item == "birthday (dd/mm/yyyy)":
                if not re.match(r"^\d{2}/\d{2}/\d{4}$", user_input):
                    print("Please enter date in the format dd/mm/yyyy.")
                    user_input = input("birthday (dd/mm/yyyy):")
                else:
                    player_info.append(user_input)
            else:
                player_info.append(user_input)

        MenuViews.review_player(player_info)
        user_input = input().lower()

        if user_input == "y":
            player = Player(
                player_id=0,
                last_name=player_info[0],
                first_name=player_info[1],
                birthday=player_info[2],
                city=player_info[3],
                rank=int(player_info[4]),
            )

            player.save_player_db()
            self.menu_view.player_saved()
            self.main_menu_start()

        elif user_input == "n":
            self.main_menu_start()

    def update_player(self):
        """Update existing player info"""
        players = Player.load_player_db()

        self.menu_view.select_players(players, "to update")
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.main_menu_start()

        p = players[int(user_input) - 1]
        p = Player(
            p["id"],
            p["last_name"],
            p["first_name"],
            p["birthday"],
            p["city"],
            p["rank"],
        )

        options = ["last name", "first name", "date of birth", "city", "rank"]
        self.menu_view.update_player_info(p, options)
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "back":
            self.main_menu_start()

        elif int(user_input) <= len(options):
            updated_info = (options[int(user_input) - 1]).replace(" ", "_")
            self.menu_view.input_prompt_text(
                f"new {options[int(user_input) - 1]}"
                )
            user_input = input()

            if user_input == "back":
                self.main_menu_start()

            else:
                p.update_player_db(user_input, updated_info)
                self.menu_view.player_saved()

                self.update_player()

        else:
            self.menu_view.input_error()
            self.update_player()

    def reports_menu(self):
        """Reports menu selector"""
        self.menu_view.reports_menu()
        self.menu_view.input_prompt()
        user_input = input()

        USER_REPORT_CHOICE = {
            "1": self.player_reports_sorting,
            "2": self.player_reports_sorting,
            "3": self.reports.all_tournaments,
            "4": self.reports.tournament_rounds,
            "5": self.reports.tournament_matches,
            "back": self.main_menu_start,
        }

        if user_input not in USER_REPORT_CHOICE.keys():
            self.menu_view.input_error()
            self.reports_menu()
        elif user_input == "1":
            USER_REPORT_CHOICE[user_input](Player.load_player_db())
        elif user_input == "2":
            USER_REPORT_CHOICE[user_input](self.reports.tournament_players())
        else:
            USER_REPORT_CHOICE[user_input]()

        self.menu_view.other_report()
        user_input = input()

        if user_input == "y":
            self.reports_menu()

        elif user_input == "n":
            self.main_menu_start()

    def player_reports_sorting(self, players):
        """Select sorting option (name or rank) for players

        @param players: list of players
        """
        self.menu_view.reports_player_sorting()
        self.menu_view.input_prompt()
        user_input = input()

        if user_input == "1":
            self.reports.all_players_name(players)

        elif user_input == "2":
            self.reports.all_players_rank(players)

        elif user_input == "back":
            self.main_menu_start()
