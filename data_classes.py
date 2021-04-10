from enum import Enum
from dataclasses import dataclass
from dataclasses import field
from typing import List
# Make sure to import things needed here.

Position = Enum('Position', 'GK LB CB RB DM CM LM RM LW SS RW CF')
Role = Enum("Role", "Manager AssistantManager GoalkeepingCoach FitnessCoach ConditioningCoach Nutritionist Physiotherapist Masseur Scouter YouthTeamCoach")

@dataclass(order=True, frozen=True)
class Player:
    age: int
    last_name: str
    first_name: str
    position: Position = field(compare = False)

@dataclass(frozen=True)
class Squad:
    players: List[Player]

@dataclass(frozen=True)
class Staff:
    first_name: str
    last_name: str
    age: int
    role: Role
# Define data classes here

if __name__ == "__main__":
    # Players
    player1 = Player(first_name="Manuel", last_name="Neuer", age=17, position=Position.GK)
    player2 = Player(first_name="Sergio", last_name="Ramos", age=26, position=Position.CB)
    player3 = Player(first_name="Gerard", last_name="Pique", age=25, position=Position.CB)
    player4 = Player(first_name="Giorgio", last_name="Chiellini", age=24, position=Position.CB)
    player5 = Player(first_name="Raphael", last_name="Varane", age=27, position=Position.CB)
    player6 = Player(first_name="Aymeric", last_name="Laporte", age=20, position=Position.CB)
    player7 = Player(first_name="Andrew", last_name="Robertson", age=18, position=Position.LB)
    player8 = Player(first_name="Trent", last_name="Alexander-Arnold", age=17, position=Position.RB)
    player9 = Player(first_name="Joshua", last_name="Kimmich", age=17, position=Position.DM)
    player10 = Player(first_name="Marcelo", last_name="Brozovic", age=28, position=Position.DM)
    player11 = Player(first_name="Kevin", last_name="Bruyne", age=30, position=Position.CM)
    player12 = Player(first_name="Luka", last_name="Modric", age=28, position=Position.CM)
    player13 = Player(first_name="Neymar", last_name="Santos", age=22, position=Position.LM)
    player14 = Player(first_name="Jadon", last_name="Sancho", age=32, position=Position.RM)
    player15 = Player(first_name="Cristiano", last_name="Ronaldo", age=34, position=Position.LW)
    player16 = Player(first_name="Lionel", last_name="Messi", age=29, position=Position.SS)
    player17 = Player(first_name="Angel", last_name="Di Maria", age=33, position=Position.RW)
    player18 = Player(first_name="Luis", last_name="Suarez", age=22, position=Position.CF)
    player19 = Player(first_name="Robert", last_name="Leqandowski", age=27, position=Position.CF)

    # Squad
    main_squad = Squad(players=[player1, player2, player3, player7, player8, player10, player11, player13, player15, player16, player19])

    # Let's sort
    players = main_squad.players

    print("Squad before sorting:")
    for player in players:
        print(f"{player.first_name} {player.last_name} ({player.age})")

    players.sort()

    print()
    print("Squad after sorting (based on age, then surname, then first name):")
    for player in players:
        print(f"{player.first_name} {player.last_name} ({player.age})")

    # Staff
    manager = Staff(first_name="Gergo", last_name="Cseh", age="21", role=Role.Manager)
    assistant_manager = Staff(first_name="Rafael", last_name="from WillowBits", age="30", role=Role.AssistantManager)
