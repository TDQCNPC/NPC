import ClassOutline

def main():
    Paul = AI(Position=[5,3],Inventory=["Cabbage","PB&J","Orange","Cornflakes"],Sprite="Pual.jpg")
    while True:
        Paul.state = "MakePBandJ"
        Paul.Sense.Hearing(Paul.Position)
        seen = Paul.Sense.Sight(Paul.Position, Paul.facingdirection)
        for item in items:
            touch = Paul.Sense.touch(item)
            If touch == "Attacked":
                Paul.Action.flee()        
        if seen:
            Paul.state = "wave"
        elif player.Position[1] == (Paul.Position[1]+1) and (player.Position[0] == paul.Position[0])
            Paul.state = input()
        elif Paul.state == "Buying":
            Paul.action.buy(read)
        elif Paul.state == "Selling":
            Paul.action.sell(read)
        elif Paul.state == "wave":
            Paul.action.wave()
        elif Paul.state == "Directions":
            Paul.action.giveDirections()
        elif Paul.state == "MakePBandJ":
            Paul.action.MakePBandJ()
        else:
            error "Not a state paul knows"
