import datetime

from django.db import models

# Create your models here.


class ChessGame(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    player_name_white = models.CharField(max_length=100)
    player_name_black = models.CharField(max_length=100)
    moves = models.JSONField()
    date = models.DateField(default=datetime.date.today)
    winner = models.CharField(max_length=100, null=True, blank=True, default="Undecided")

    def determine_winner(self):
        # Logic to determine the winner based on moves or game status
        # For example, random winner for demonstration purposes
        import random
        winner = random.choice([self.player_name_white, self.player_name_black])
        self.winner = winner

    def __str__(self):
        moves_str = "\n".join([f"   {move_number}: {move[0]} - {move[1]}" for move_number, move in self.moves.items()])
        return (
            f'Game {self.id}: {self.player_name_white} Vs {self.player_name_black}\n'
            f'Moves:\n{moves_str}'
        )






