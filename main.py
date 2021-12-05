import morphic

world = morphic.World(400, 300)
morph = morphic.Morph()
world.add(morph)
world.prompt("MOEW")
world.loop()
