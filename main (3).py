class Player:
  def play_method(self):
    print("The player is playing cricket : ")

class Batsman(Player):
  def Batsman_play(self):
    print("The Batsman is batting : ")

class Bowler(Batsman):
  def Bowler_play1(self):
    print("The Bowler is Bowling : ")

play = Bowler()


play.play_method()
play.Batsman_play()
play.Bowler_play1()