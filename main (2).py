class player:
  def play(self):
    print ("The player is playing cricket.")
class Batsman (player):
  def play(self):
    print ("The Batsman is Batting.")
class Bowler(player):
  def play(self):
    print("The Bowler is Bowlling.")
bastman=Batsman()
bowler=Bowler()
bastman.play ()
bowler.play()
