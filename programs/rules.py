from question import Ask, If, AND, OR


rules = {
    "default": Ask(["y", "n"]),
    "color": Ask(["red", "orange", "yellow", "green", "cyan", "blue", "purple", "black", "other"]),
    "power": Ask(["low", "medium", "high"]),
    "truck": If(OR([AND(["trailer", "long"]),  "low speed", "six wheels"])),
    "auto": If(OR([AND(["four wheels", "four doors"]), "medium speed"])),
    "race": If(OR([AND(["four wheell", "cockpit"]), "high speed"])),
    "car:Mercedes": If(["auto", "color:black", "power:medium", "four wheels"]),
    "car:BMW": If(["auto", "color:other", "power:medium", "low speed"]),
    "car:Ford": If(["auto", "color:blue", "power:low", "four doors", "low speed"]),
    "car:Aston Martin": If(["race", "color:other", "power:high", "four wheels"]),
    "car:Ferrari": If(["race", "color:red", "power:high", "high speed"]),
    "car:Alfa Romeo": If(["race", "color:other", "power:high", "four wheels", "cockpit"]),
    "car:Renault": If(["truck", "color:green", "trailer", "low speed"]),
    "car:Man": If(["truck", "color:black", "long", "six wheels", "power:medium"]),
    "car:Volvo": If(["truck", "power:medium", "color:yellow", "six wheels"])
}
