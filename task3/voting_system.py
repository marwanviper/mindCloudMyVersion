class VotingSystem:
    def __init__(self):
        self.__candidates = {}

    def add_candidate(self, name):
        if name in self.__candidates:
            print(f"Candidate '{name}' already exists.")
        else:
            self.__candidates[name] = 0
            print(f"Candidate '{name}' added.")

    def remove_candidate(self, name):
        if name in self.__candidates:
            self.__candidates.pop(name)
            print(f"Candidate '{name}' removed.")
        else:
            print(f"Candidate '{name}' not found.")

    def vote_to_candidate(self, name):
        if name in self.__candidates:
            self.__candidates[name] += 1
            print(f"Vote given to '{name}'.")
        else:
            print(f"Candidate '{name}' not found.")

    def display_winner(self):
        if not self.__candidates:
            print("No candidates available.")
            return
        max_votes = max(self.__candidates.values())
        winners = [
            name for name, votes in self.__candidates.items() if votes == max_votes
        ]

        if len(winners) == 1:
            print(f"The winner is '{winners[0]}' with {max_votes} votes.")
        else:
            print(
                "It's a tie between: "
                + ", ".join(winners)
                + f" with {max_votes} votes each."
            )


if __name__ == "__main__":
    system = VotingSystem()
    system.add_candidate("hamada")
    system.add_candidate("omer")
    system.vote_to_candidate("hamada")
    system.vote_to_candidate("hamada")
    system.vote_to_candidate("omer")
    system.display_winner()
