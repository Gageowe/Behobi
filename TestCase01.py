from Map import Map
tally = Map()
tally.newLoc("Gaghaus",[])
tally.newLoc("Samhaus",[])
tally.newLoc("Moe",[])
tally.newLoc("Chiles",[])
tally.printLocs()
tally.addCon(tally.whereIs("Gaghaus"),[tally.whereIs("Samhaus"),tally.whereIs("Moe"),tally.whereIs("Chiles")])
tally.addCon(tally.whereIs("Samhaus"),[tally.whereIs("Moe"),tally.whereIs("Chiles")])
tally.addCon(tally.whereIs("Moe"),[tally.whereIs("Chiles")])
tally.printCons()