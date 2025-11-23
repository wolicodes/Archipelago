
from enum import Enum
from BaseClasses import Item, ItemClassification

class Items(str, Enum):
    # Shop
    KNIFE = "Knife"
    SCRAMASAX = "Scramasax"
    DAGGER = "Dagger"
    SHORTSWORD = "Shortsword"
    BOAR_SPEAR = "Boar Spear"
    BROADSWORD = "Broadsword"
    RAPIER = "Rapier"
    VIKING = "Viking"
    SHAMSHIR = "Shamshir"
    CLAYMORE = "Claymore"
    EXECUTOR = "Executor"
    KATZBALGER = "Katzbalger"
    STEELSWORD = "Steelsword"
    EPEE = "Epee"
    LAST_ESTOC = "Last Estoc"
    PATTISA = "Pattisa"
    FLAMBERGE = "Flamberge"
    DUERGAR = "Duergar"
    DRAGONBANE = "Dragonbane"
    BONE_AXE = "Bone Axe"
    HAND_AXE = "Hand Axe"
    CELTIS = "Celtis"
    BROADAXE = "Broadaxe"
    BATTLE_AXE = "Battle Axe"
    BILIOMG = "Biliomg"
    TABAR = "Tabar"
    GREAT_AXE = "Great Axe"
    BARDICHE = "Bardiche"
    HALBERD = "Halberd"
    WAND = "Wand"
    BREAKER = "Breaker"
    LABYRIS = "Labyris"
    FRANCISCA = "Francisca"
    BHUJ = "Bhuj"
    FASCES_AXE = "Fasces Axe"
    FLAME_AXE = "Flame Axe"
    METEOR_AXE = "Meteor Axe"
    HATCHET = "Hatchet"
    STAFF = "Staff"
    BONE_STAFF = "Bone Staff"
    BONE_MACE = "Bone Mace"
    DOWN_STAFF = "Down Staff"
    BONE_FLAIL = "Bone Flail"
    GEM_STAFF = "Gem Staff"
    WAR_MACE = "War Mace"
    LUCK_STAFF = "Luck Staff"
    GODENDAG = "Godendag"
    MYSTIC_ROD = "Mystic Rod"
    WARHAMMER = "Warhammer"
    ARCANA_ROD = "Arcana Rod"
    SAGE_WAND = "Sage Wand"
    WAKIZASHI = "Wakizashi"
    UCHIGATANA = "Uchigatana"
    OHDACHI = "Ohdachi"
    KOGARASU = "Kogarasu"
    SHIDA = "Shida"
    ZANMATOU = "Zanmatou"
    KUZUNOSADA = "Kuzunosada"
    HACHI = "Hachi"
    HISAMEMARU = "Hisamemaru"
    MASAMUNE = "Masamune"
    WOOD_BOW = "Wood Bow"
    ENAMEL_BOW = "Enamel Bow"
    SHORT_BOW = "Short Bow"
    BEAST_BOW = "Beast Bow"
    HARD_SLING = "Hard Sling"
    LONG_BOW = "Long Bow"
    HINDI = "Hindi"
    SELF_BOW = "Self Bow"
    HUNTER_BOW = "Hunter Bow"
    FIN_BOW = "Fin Bow"
    VINE_BOW = "Vine Bow"
    HEAVEN_BOW = "Heaven Bow"
    SHIDGEDOU = "Shidgedou"
    WAR_BOW = "War Bow"
    ARBALEST = "Arbalest"
    FAILNAUGHT = "Failnaught"
    ZAMIEL_BOW = "Zamiel Bow"
    ARC_DRAWER = "Arc Drawer"
    LIGHT_WHIP = "Light Whip"
    FANG_WHIP = "Fang Whip"
    BULLWHIP = "Bullwhip"
    VINE_WHIP = "Vine Whip"
    NAIL_WHIP = "Nail Whip"
    EDGE_WHIP = "Edge Whip"
    TOXIC_WHIP = "Toxic Whip"
    GUM_WHIP = "Gum Whip"
    WIND_WHIP = "Wind Whip"
    SHRED_WHIP = "Shred Whip"
    STING_WHIP = "Sting Whip"
    BLADE_WHIP = "Blade Whip"
    NINE_TAILS = "Nine Tails"
    KNOUT = "Knout"
    DEAD_WHIP = "Dead Whip"
    TORMENTOR = "Tormentor"
    DOMINATOR = "Dominator"
    VOLT_WHIP = "Volt Whip"
    THORN_WHIP = "Thorn Whip"
    TWEED = "Tweed"
    JERKIN = "Jerkin"
    LEAF_COAT = "Leaf Coat"
    HIDE_VEST = "Hide Vest"
    HIDE_ARMOR = "Hide Armor"
    PLATE = "Plate"
    DOUBLET = "Doublet"
    BUFFCOAT = "Buffcoat"
    BRIAULT = "Briault"
    CHAIN_MAIL = "Chain Mail"
    PETAL_COAT = "Petal Coat"
    LEAF_TUNIC = "Leaf Tunic"
    IRON_PLATE = "Iron Plate"
    RING_MAIL = "Ring Mail"
    OAK_JACKET = "Oak Jacket"
    WING_COAT = "Wing Coat"
    HAUBERK = "Hauberk"
    STUD_VEST = "Stud Vest"
    FANCY_COAT = "Fancy Coat"
    COTARDIE = "Cotardie"
    FULL_ARMOR = "Full Armor"
    PLATE_MAIL = "Plate Mail"
    SEVEN_DOUBLET = "7 Doublet"
    SURCOAT = "Surcoat"
    TIGER_COAT = "Tiger Coat"
    FAIRY_ROBE = "Fairy Robe"
    DARK_TUNIC = "Dark Tunic"
    BRIGANDINE = "Brigandine"
    EBON_PLATE = "Ebon Plate"
    LYCORIS = "Lycoris"
    WYVERNMAIL = "Wyvernmail"
    JAZERAINT = "Jazeraint"
    DEMON_COAT = "Demon Coat"
    RUNE_TWEED = "Rune Tweed"
    RUNE_TUNIC = "Rune Tunic"
    BLOOD_MAIL = "Blood Mail"
    COMPOSITE = "Composite"
    AZURE_COAT = "Azure Coat"
    BLOOD_COAT = "Blood Coat"
    DINO_PLATE = "Dino Plate"
    DEMON_MAIL = "Demon Mail"
    SYLPHEED = "Sylpheed"
    HOLY_ARMOR = "Holy Armor"
    GHOST_VEST = "Ghost Vest"
    MOBIUS_ALB = "Mobius Alb"
    ANGEL_ROBE = "Angel Robe"
    FAIRY_MAIL = "Fairy Mail"
    RUBY_MAIL = "Ruby Mail"
    HEX_MANTLE = "Hex Mantle"
    MOSS_COAT = "Moss Coat"
    FLAME_COAT = "Flame Coat"
    FROST_COAT = "Frost Coat"
    VOLT_COAT = "Volt Coat"
    HAIRPIN = "Hairpin"
    HIDE_HAT = "Hide Hat"
    PLUMED_HAT = "Plumed Hat"
    CHAIN_HELM = "Chain Helm"
    GUM_HELM = "Gum Helm"
    SCALE_HELM = "Scale Helm"
    SCALE_CAP = "Scale Cap"
    SANDY_PIN = "Sandy Pin"
    TIGER_CAP = "Tiger Cap"
    CIRCLET = "Circlet"
    BLOOD_HELM = "Blood Helm"
    ANGEL_HELM = "Angel Helm"
    KNIT_GLOVE = "Knit Glove"
    HIDE_GLOVE = "Hide Glove"
    DOWN_GLOVE = "Down Glove"
    IRON_GLOVE = "Iron Glove"
    BEAR_GLOVE = "Bear Glove"
    GUM_GLOVE = "Gum Glove"
    FANG_GLOVE = "Fang Glove"
    SAND_GLOVE = "Sand Glove"
    TIGER_HAND = "Tiger Hand"
    RUNE_GLOVE = "Rune Glove"
    BLOOD_GAGE = "Blood Gage"
    BRAVE_GAGE = "Brave Gage"
    EBON_GLOVE = "Ebon Glove"
    ATHANOR = "Athanor"
    RUBY_GAGE = "Ruby Gage"
    TOXIC_GAGE = "Toxic Gage"
    TARGE = "Targe"
    HIDE_ASPIS = "Hide Aspis"
    ASPIS = "Aspis"
    OVAL_ASPIS = "Oval Aspis"
    HEAT_ASPIS = "Heat Aspis"
    GUM_ASPIS = "Gum Aspis"
    BODY_ASPIS = "Body Aspis"
    EBON_ASPIS = "Ebon Aspis"
    MOON_ASPIS = "Moon Aspis"
    KING_ASPIS = "King Aspis"
    HALO_ASPIS = "Halo Aspis"
    HOLY_ASPIS = "Holy Aspis"
    PAIN_ASPIS = "Pain Aspis"
    LEAF_BOOT = "Leaf Boot"
    HIDE_BOOT = "Hide Boot"
    PLUME_BOOT = "Plume Boot"
    CHAIN_BOOT = "Chain Boot"
    MOCCASINS = "Moccasins"
    SCALE_BOOT = "Scale Boot"
    FAIRY_BOOT = "Fairy Boot"
    TIGER_BOOT = "Tiger Boot"
    FLAME_BOOT = "Flame Boot"
    FUR_BOOT = "Fur Boot"
    DYED_BOOT = "Dyed Boot"
    SPEED_BOOT = "Speed Boot"
    HIDE_BELT = "Hide Belt"
    HIDE_RING = "Hide Ring"
    RED_CHARM = "Red Charm"
    PETAL_RING = "Petal Ring"
    CUT_CHARM = "Cut Charm"
    GEM_RING = "Gem Ring"
    LEAF_CAPE = "Leaf Cape"
    FIRE_RING = "Fire Ring"
    STAR_CHARM = "Star Charm"
    TUSK_CHARM = "Tusk Charm"
    OLD_CHOKER = "Old Choker"
    HIDE_CAPE = "Hide Cape"
    AMBER_RING = "Amber Ring"
    SEA_CHARM = "Sea Charm"
    BLUE_RING = "Blue Ring"
    RED_CAPE = "Red Cape"
    EVIL_CHARM = "Evil Charm"
    ROSE_RING = "Rose Ring"
    ROYAL_RING = "Royal Ring"
    GOLD_CAPE = "Gold Cape"
    ANGEL_RING = "Angel Ring"
    WARD_GEM = "Ward Gem"
    JEWEL_EYE = "Jewel Eye"
    RUBY = "Ruby"
    SAPPHIRE = "Sapphire"
    TOPAZ = "Topaz"
    TOURMALINE = "Tourmaline"
    ADAMAS = "Adamas"
    HEX_DOLL = "Hex Doll"
    OCARINA = "Ocarina"
    LUTE = "Lute"
    FLUTE = "Flute"
    KITHARA = "Kithara"
    AULOS = "Aulos"
    ANGEL_HARP = "Angel Harp"
    SYRINX = "Syrinx"
    TOWN_MEDAL = "Town Medal"
    TOWN_CROWN = "Town Crown"
    MOSS_RING = "Moss Ring"
    MOSS_BAND = "Moss Band"
    MEDICA = "Medica"
    MEDICA_II = "Medica II"
    MEDICA_III = "Medica III"
    MEDICA_IV = "Medica IV"
    MEDICA_V = "Medica V"
    AMRITA = "Amrita"
    AMRITA_II = "Amrita II"
    HAMAO = "Hamao"
    HAMAO_PRIME = "Hamao Prime"
    SOMA = "Soma"
    SOMA_PRIME = "Soma Prime"
    NECTAR = "Nectar"
    NECTAR_II = "Nectar II"
    NECTAR_III = "Nectar III"
    THERIACA_A = "Theriaca A"
    THERIACA_B = "Theriaca B"
    AXCELA = "Axcela"
    AXCELA_II = "Axcela II"
    AXCELA_III = "Axcela III"
    BRAVANT = "Bravant"
    BRAVANT_II = "Bravant II"
    STONARD = "Stonard"
    STONARD_II = "Stonard II"
    FIRE_MIST = "Fire Mist"
    ICE_MIST = "Ice Mist"
    VOLT_MIST = "Volt Mist"
    ALL_MIST = "All Mist"
    BLAZE_OIL = "Blaze Oil"
    FREEZE_OIL = "Freeze Oil"
    SHOCK_OIL = "Shock Oil"
    WARD_CHIME = "Ward Chime"
    GOLD_CHIME = "Gold Chime"
    POLE_STONE = "Pole Stone"
    ARIADNE_THREAD = "Ariadne Thread"

    # Materials - TODO List with real ids
    WHITESTONE = "Whitestone"

    # Key items - TODO List with real ids
    CLEAR_KEY = "Clear Key"
    VIOLET_KEY = "Violet Key"
    RADHA_NOTE = "Radha Note"

    # Custom items
    FIRST_STRATUM_CLEARED = "First Stratum Cleared"
    VICTORY = "Victory"
    EN500 = "500en"
    EN200 = "200en"
    EN100 = "100en"
    NIGHT_10TP = "Feeling Refreshed"
    FIRST_CHAR_10HP = "Red Fruit Eaten"
    EN50 = "50en"
    EN1 = "1en"

ITEM_NAME_TO_ID = {
    Items.KNIFE.value: 1,
    Items.SCRAMASAX.value: 2,
    Items.DAGGER.value: 3,
    Items.SHORTSWORD.value: 4,
    Items.BOAR_SPEAR.value: 5,
    Items.BROADSWORD.value: 6,
    Items.RAPIER.value: 7,
    Items.VIKING.value: 8,
    Items.SHAMSHIR.value: 9,
    Items.CLAYMORE.value: 10,
    Items.EXECUTOR.value: 11,
    Items.KATZBALGER.value: 12,
    Items.STEELSWORD.value: 13,
    Items.EPEE.value: 14,
    Items.LAST_ESTOC.value: 15,
    Items.PATTISA.value: 16,
    Items.FLAMBERGE.value: 17,
    Items.DUERGAR.value: 21,
    Items.DRAGONBANE.value: 23,
    Items.BONE_AXE.value: 30,
    Items.HAND_AXE.value: 31,
    Items.CELTIS.value: 32,
    Items.BROADAXE.value: 33,
    Items.BATTLE_AXE.value: 34,
    Items.BILIOMG.value: 35,
    Items.TABAR.value: 36,
    Items.GREAT_AXE.value: 37,
    Items.BARDICHE.value: 38,
    Items.HALBERD.value: 39,
    Items.WAND.value: 40,
    Items.BREAKER.value: 41,
    Items.LABYRIS.value: 42,
    Items.FRANCISCA.value: 43,
    Items.BHUJ.value: 44,
    Items.FASCES_AXE.value: 45,
    Items.FLAME_AXE.value: 48,
    Items.METEOR_AXE.value: 49,
    Items.HATCHET.value: 50,
    Items.STAFF.value: 54,
    Items.BONE_STAFF.value: 55,
    Items.BONE_MACE.value: 56,
    Items.DOWN_STAFF.value: 57,
    Items.BONE_FLAIL.value: 58,
    Items.GEM_STAFF.value: 59,
    Items.WAR_MACE.value: 60,
    Items.LUCK_STAFF.value: 61,
    Items.GODENDAG.value: 62,
    Items.MYSTIC_ROD.value: 63,
    Items.WARHAMMER.value: 64,
    Items.ARCANA_ROD.value: 65,
    Items.SAGE_WAND.value: 66,
    Items.WAKIZASHI.value: 73,
    Items.UCHIGATANA.value: 74,
    Items.OHDACHI.value: 75,
    Items.KOGARASU.value: 76,
    Items.SHIDA.value: 77,
    Items.ZANMATOU.value: 78,
    Items.KUZUNOSADA.value: 79,
    Items.HACHI.value: 80,
    Items.HISAMEMARU.value: 81,
    Items.MASAMUNE.value: 82,
    Items.WOOD_BOW.value: 88,
    Items.ENAMEL_BOW.value: 89,
    Items.SHORT_BOW.value: 90,
    Items.BEAST_BOW.value: 91,
    Items.HARD_SLING.value: 92,
    Items.LONG_BOW.value: 93,
    Items.HINDI.value: 94,
    Items.SELF_BOW.value: 95,
    Items.HUNTER_BOW.value: 96,
    Items.FIN_BOW.value: 97,
    Items.VINE_BOW.value: 98,
    Items.HEAVEN_BOW.value: 99,
    Items.SHIDGEDOU.value: 100,
    Items.WAR_BOW.value: 101,
    Items.ARBALEST.value: 102,
    Items.FAILNAUGHT.value: 103,
    Items.ZAMIEL_BOW.value: 105,
    Items.ARC_DRAWER.value: 106,
    Items.LIGHT_WHIP.value: 112,
    Items.FANG_WHIP.value: 113,
    Items.BULLWHIP.value: 114,
    Items.VINE_WHIP.value: 115,
    Items.NAIL_WHIP.value: 116,
    Items.EDGE_WHIP.value: 117,
    Items.TOXIC_WHIP.value: 118,
    Items.GUM_WHIP.value: 119,
    Items.WIND_WHIP.value: 120,
    Items.SHRED_WHIP.value: 121,
    Items.STING_WHIP.value: 122,
    Items.BLADE_WHIP.value: 123,
    Items.NINE_TAILS.value: 124,
    Items.KNOUT.value: 125,
    Items.DEAD_WHIP.value: 126,
    Items.TORMENTOR.value: 127,
    Items.DOMINATOR.value: 129,
    Items.VOLT_WHIP.value: 131,
    Items.THORN_WHIP.value: 132,
    Items.TWEED.value: 1001,
    Items.JERKIN.value: 1002,
    Items.LEAF_COAT.value: 1003,
    Items.HIDE_VEST.value: 1004,
    Items.HIDE_ARMOR.value: 1005,
    Items.PLATE.value: 1006,
    Items.DOUBLET.value: 1007,
    Items.BUFFCOAT.value: 1008,
    Items.BRIAULT.value: 1009,
    Items.CHAIN_MAIL.value: 1010,
    Items.PETAL_COAT.value: 1011,
    Items.LEAF_TUNIC.value: 1012,
    Items.IRON_PLATE.value: 1013,
    Items.RING_MAIL.value: 1014,
    Items.OAK_JACKET.value: 1015,
    Items.WING_COAT.value: 1016,
    Items.HAUBERK.value: 1017,
    Items.STUD_VEST.value: 1019,
    Items.FANCY_COAT.value: 1020,
    Items.COTARDIE.value: 1021,
    Items.FULL_ARMOR.value: 1022,
    Items.PLATE_MAIL.value: 1023,
    Items.SEVEN_DOUBLET.value: 1024,
    Items.SURCOAT.value: 1025,
    Items.TIGER_COAT.value: 1027,
    Items.FAIRY_ROBE.value: 1028,
    Items.DARK_TUNIC.value: 1029,
    Items.BRIGANDINE.value: 1030,
    Items.EBON_PLATE.value: 1031,
    Items.LYCORIS.value: 1032,
    Items.WYVERNMAIL.value: 1033,
    Items.JAZERAINT.value: 1034,
    Items.DEMON_COAT.value: 1035,
    Items.RUNE_TWEED.value: 1036,
    Items.RUNE_TUNIC.value: 1037,
    Items.BLOOD_MAIL.value: 1038,
    Items.COMPOSITE.value: 1039,
    Items.AZURE_COAT.value: 1040,
    Items.BLOOD_COAT.value: 1041,
    Items.DINO_PLATE.value: 1042,
    Items.DEMON_MAIL.value: 1043,
    Items.SYLPHEED.value: 1044,
    Items.HOLY_ARMOR.value: 1045,
    Items.GHOST_VEST.value: 1046,
    Items.MOBIUS_ALB.value: 1047,
    Items.ANGEL_ROBE.value: 1048,
    Items.FAIRY_MAIL.value: 1049,
    Items.RUBY_MAIL.value: 1050,
    Items.HEX_MANTLE.value: 1051,
    Items.MOSS_COAT.value: 1052,
    Items.FLAME_COAT.value: 1053,
    Items.FROST_COAT.value: 1054,
    Items.VOLT_COAT.value: 1055,
    Items.HAIRPIN.value: 2001,
    Items.HIDE_HAT.value: 2002,
    Items.PLUMED_HAT.value: 2003,
    Items.CHAIN_HELM.value: 2004,
    Items.GUM_HELM.value: 2005,
    Items.SCALE_HELM.value: 2006,
    Items.SCALE_CAP.value: 2007,
    Items.SANDY_PIN.value: 2008,
    Items.TIGER_CAP.value: 2009,
    Items.CIRCLET.value: 2010,
    Items.BLOOD_HELM.value: 2011,
    Items.ANGEL_HELM.value: 2012,
    Items.KNIT_GLOVE.value: 2018,
    Items.HIDE_GLOVE.value: 2019,
    Items.DOWN_GLOVE.value: 2020,
    Items.IRON_GLOVE.value: 2021,
    Items.BEAR_GLOVE.value: 2022,
    Items.GUM_GLOVE.value: 2023,
    Items.FANG_GLOVE.value: 2024,
    Items.SAND_GLOVE.value: 2025,
    Items.TIGER_HAND.value: 2026,
    Items.RUNE_GLOVE.value: 2027,
    Items.BLOOD_GAGE.value: 2028,
    Items.BRAVE_GAGE.value: 2029,
    Items.EBON_GLOVE.value: 2030,
    Items.ATHANOR.value: 2031,
    Items.RUBY_GAGE.value: 2032,
    Items.TOXIC_GAGE.value: 2033,
    Items.TARGE.value: 2038,
    Items.HIDE_ASPIS.value: 2039,
    Items.ASPIS.value: 2040,
    Items.OVAL_ASPIS.value: 2041,
    Items.HEAT_ASPIS.value: 2042,
    Items.GUM_ASPIS.value: 2043,
    Items.BODY_ASPIS.value: 2044,
    Items.EBON_ASPIS.value: 2045,
    Items.MOON_ASPIS.value: 2046,
    Items.KING_ASPIS.value: 2047,
    Items.HALO_ASPIS.value: 2048,
    Items.HOLY_ASPIS.value: 2049,
    Items.PAIN_ASPIS.value: 2050,
    Items.LEAF_BOOT.value: 2056,
    Items.HIDE_BOOT.value: 2057,
    Items.PLUME_BOOT.value: 2058,
    Items.CHAIN_BOOT.value: 2059,
    Items.MOCCASINS.value: 2060,
    Items.SCALE_BOOT.value: 2061,
    Items.FAIRY_BOOT.value: 2062,
    Items.TIGER_BOOT.value: 2063,
    Items.FLAME_BOOT.value: 2064,
    Items.FUR_BOOT.value: 2065,
    Items.DYED_BOOT.value: 2066,
    Items.SPEED_BOOT.value: 2067,
    Items.HIDE_BELT.value: 3001,
    Items.HIDE_RING.value: 3002,
    Items.RED_CHARM.value: 3003,
    Items.PETAL_RING.value: 3004,
    Items.CUT_CHARM.value: 3005,
    Items.GEM_RING.value: 3006,
    Items.LEAF_CAPE.value: 3007,
    Items.FIRE_RING.value: 3008,
    Items.STAR_CHARM.value: 3009,
    Items.TUSK_CHARM.value: 3010,
    Items.OLD_CHOKER.value: 3011,
    Items.HIDE_CAPE.value: 3012,
    Items.AMBER_RING.value: 3013,
    Items.SEA_CHARM.value: 3014,
    Items.BLUE_RING.value: 3015,
    Items.RED_CAPE.value: 3016,
    Items.EVIL_CHARM.value: 3017,
    Items.ROSE_RING.value: 3018,
    Items.ROYAL_RING.value: 3019,
    Items.GOLD_CAPE.value: 3020,
    Items.ANGEL_RING.value: 3021,
    Items.WARD_GEM.value: 3022,
    Items.JEWEL_EYE.value: 3023,
    Items.RUBY.value: 3024,
    Items.SAPPHIRE.value: 3025,
    Items.TOPAZ.value: 3026,
    Items.TOURMALINE.value: 3027,
    Items.ADAMAS.value: 3028,
    Items.HEX_DOLL.value: 3029,
    Items.OCARINA.value: 3030,
    Items.LUTE.value: 3031,
    Items.FLUTE.value: 3032,
    Items.KITHARA.value: 3033,
    Items.AULOS.value: 3034,
    Items.ANGEL_HARP.value: 3035,
    Items.SYRINX.value: 3036,
    Items.TOWN_MEDAL.value: 3037,
    Items.TOWN_CROWN.value: 3038,
    Items.MOSS_RING.value: 3039,
    Items.MOSS_BAND.value: 3040,
    Items.MEDICA.value: 4279,
    Items.MEDICA_II.value: 4280,
    Items.MEDICA_III.value: 4281,
    Items.MEDICA_IV.value: 4282,
    Items.MEDICA_V.value: 4283,
    Items.AMRITA.value: 4284,
    Items.AMRITA_II.value: 4285,
    Items.HAMAO.value: 4286,
    Items.HAMAO_PRIME.value: 4287,
    Items.SOMA.value: 4288,
    Items.SOMA_PRIME.value: 4289,
    Items.NECTAR.value: 4290,
    Items.NECTAR_II.value: 4291,
    Items.NECTAR_III.value: 4292,
    Items.THERIACA_A.value: 4295,
    Items.THERIACA_B.value: 4296,
    Items.AXCELA.value: 4301,
    Items.AXCELA_II.value: 4302,
    Items.AXCELA_III.value: 4303,
    Items.BRAVANT.value: 4305,
    Items.BRAVANT_II.value: 4306,
    Items.STONARD.value: 4307,
    Items.STONARD_II.value: 4308,
    Items.FIRE_MIST.value: 4311,
    Items.ICE_MIST.value: 4312,
    Items.VOLT_MIST.value: 4313,
    Items.ALL_MIST.value: 4314,
    Items.BLAZE_OIL.value: 4315,
    Items.FREEZE_OIL.value: 4316,
    Items.SHOCK_OIL.value: 4317,
    Items.WARD_CHIME.value: 4319,
    Items.GOLD_CHIME.value: 4320,
    Items.POLE_STONE.value: 4332,
    Items.ARIADNE_THREAD.value: 4374,

    # Materials - TODO List with real ids
    Items.WHITESTONE.value: 1000000,

    # Key items - TODO List with real ids
    Items.CLEAR_KEY.value: 1000001,
    Items.VIOLET_KEY.value: 1000002,
    Items.RADHA_NOTE.value: 1000004,

    # Custom items
    Items.FIRST_STRATUM_CLEARED.value: 1000003,
    Items.VICTORY.value: 1000005,
    Items.EN500.value: 1000006,
    Items.EN200.value: 1000007,
    Items.EN100.value: 1000008,
    Items.NIGHT_10TP.value: 1000009,
    Items.FIRST_CHAR_10HP.value: 1000010,
    Items.EN50.value: 1000011,
    Items.EN1.value: 1000012,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    Items.KNIFE.value: ItemClassification.useful,
    Items.SCRAMASAX.value: ItemClassification.useful,
    Items.DAGGER.value: ItemClassification.useful,
    Items.SHORTSWORD.value: ItemClassification.useful,
    Items.BOAR_SPEAR.value: ItemClassification.useful,
    Items.BROADSWORD.value: ItemClassification.useful,
    Items.RAPIER.value: ItemClassification.useful,
    Items.VIKING.value: ItemClassification.useful,
    Items.SHAMSHIR.value: ItemClassification.useful,
    Items.CLAYMORE.value: ItemClassification.useful,
    Items.EXECUTOR.value: ItemClassification.useful,
    Items.KATZBALGER.value: ItemClassification.useful,
    Items.STEELSWORD.value: ItemClassification.useful,
    Items.EPEE.value: ItemClassification.useful,
    Items.LAST_ESTOC.value: ItemClassification.useful,
    Items.PATTISA.value: ItemClassification.useful,
    Items.FLAMBERGE.value: ItemClassification.useful,
    Items.DUERGAR.value: ItemClassification.useful,
    Items.DRAGONBANE.value: ItemClassification.useful,
    Items.BONE_AXE.value: ItemClassification.useful,
    Items.HAND_AXE.value: ItemClassification.useful,
    Items.CELTIS.value: ItemClassification.useful,
    Items.BROADAXE.value: ItemClassification.useful,
    Items.BATTLE_AXE.value: ItemClassification.useful,
    Items.BILIOMG.value: ItemClassification.useful,
    Items.TABAR.value: ItemClassification.useful,
    Items.GREAT_AXE.value: ItemClassification.useful,
    Items.BARDICHE.value: ItemClassification.useful,
    Items.HALBERD.value: ItemClassification.useful,
    Items.WAND.value: ItemClassification.useful,
    Items.BREAKER.value: ItemClassification.useful,
    Items.LABYRIS.value: ItemClassification.useful,
    Items.FRANCISCA.value: ItemClassification.useful,
    Items.BHUJ.value: ItemClassification.useful,
    Items.FASCES_AXE.value: ItemClassification.useful,
    Items.FLAME_AXE.value: ItemClassification.useful,
    Items.METEOR_AXE.value: ItemClassification.useful,
    Items.HATCHET.value: ItemClassification.useful,
    Items.STAFF.value: ItemClassification.useful,
    Items.BONE_STAFF.value: ItemClassification.useful,
    Items.BONE_MACE.value: ItemClassification.useful,
    Items.DOWN_STAFF.value: ItemClassification.useful,
    Items.BONE_FLAIL.value: ItemClassification.useful,
    Items.GEM_STAFF.value: ItemClassification.useful,
    Items.WAR_MACE.value: ItemClassification.useful,
    Items.LUCK_STAFF.value: ItemClassification.useful,
    Items.GODENDAG.value: ItemClassification.useful,
    Items.MYSTIC_ROD.value: ItemClassification.useful,
    Items.WARHAMMER.value: ItemClassification.useful,
    Items.ARCANA_ROD.value: ItemClassification.useful,
    Items.SAGE_WAND.value: ItemClassification.useful,
    Items.WAKIZASHI.value: ItemClassification.useful,
    Items.UCHIGATANA.value: ItemClassification.useful,
    Items.OHDACHI.value: ItemClassification.useful,
    Items.KOGARASU.value: ItemClassification.useful,
    Items.SHIDA.value: ItemClassification.useful,
    Items.ZANMATOU.value: ItemClassification.useful,
    Items.KUZUNOSADA.value: ItemClassification.useful,
    Items.HACHI.value: ItemClassification.useful,
    Items.HISAMEMARU.value: ItemClassification.useful,
    Items.MASAMUNE.value: ItemClassification.useful,
    Items.WOOD_BOW.value: ItemClassification.useful,
    Items.ENAMEL_BOW.value: ItemClassification.useful,
    Items.SHORT_BOW.value: ItemClassification.useful,
    Items.BEAST_BOW.value: ItemClassification.useful,
    Items.HARD_SLING.value: ItemClassification.useful,
    Items.LONG_BOW.value: ItemClassification.useful,
    Items.HINDI.value: ItemClassification.useful,
    Items.SELF_BOW.value: ItemClassification.useful,
    Items.HUNTER_BOW.value: ItemClassification.useful,
    Items.FIN_BOW.value: ItemClassification.useful,
    Items.VINE_BOW.value: ItemClassification.useful,
    Items.HEAVEN_BOW.value: ItemClassification.useful,
    Items.SHIDGEDOU.value: ItemClassification.useful,
    Items.WAR_BOW.value: ItemClassification.useful,
    Items.ARBALEST.value: ItemClassification.useful,
    Items.FAILNAUGHT.value: ItemClassification.useful,
    Items.ZAMIEL_BOW.value: ItemClassification.useful,
    Items.ARC_DRAWER.value: ItemClassification.useful,
    Items.LIGHT_WHIP.value: ItemClassification.useful,
    Items.FANG_WHIP.value: ItemClassification.useful,
    Items.BULLWHIP.value: ItemClassification.useful,
    Items.VINE_WHIP.value: ItemClassification.useful,
    Items.NAIL_WHIP.value: ItemClassification.useful,
    Items.EDGE_WHIP.value: ItemClassification.useful,
    Items.TOXIC_WHIP.value: ItemClassification.useful,
    Items.GUM_WHIP.value: ItemClassification.useful,
    Items.WIND_WHIP.value: ItemClassification.useful,
    Items.SHRED_WHIP.value: ItemClassification.useful,
    Items.STING_WHIP.value: ItemClassification.useful,
    Items.BLADE_WHIP.value: ItemClassification.useful,
    Items.NINE_TAILS.value: ItemClassification.useful,
    Items.KNOUT.value: ItemClassification.useful,
    Items.DEAD_WHIP.value: ItemClassification.useful,
    Items.TORMENTOR.value: ItemClassification.useful,
    Items.DOMINATOR.value: ItemClassification.useful,
    Items.VOLT_WHIP.value: ItemClassification.useful,
    Items.THORN_WHIP.value: ItemClassification.useful,
    Items.TWEED.value: ItemClassification.useful,
    Items.JERKIN.value: ItemClassification.useful,
    Items.LEAF_COAT.value: ItemClassification.useful,
    Items.HIDE_VEST.value: ItemClassification.useful,
    Items.HIDE_ARMOR.value: ItemClassification.useful,
    Items.PLATE.value: ItemClassification.useful,
    Items.DOUBLET.value: ItemClassification.useful,
    Items.BUFFCOAT.value: ItemClassification.useful,
    Items.BRIAULT.value: ItemClassification.useful,
    Items.CHAIN_MAIL.value: ItemClassification.useful,
    Items.PETAL_COAT.value: ItemClassification.useful,
    Items.LEAF_TUNIC.value: ItemClassification.useful,
    Items.IRON_PLATE.value: ItemClassification.useful,
    Items.RING_MAIL.value: ItemClassification.useful,
    Items.OAK_JACKET.value: ItemClassification.useful,
    Items.WING_COAT.value: ItemClassification.useful,
    Items.HAUBERK.value: ItemClassification.useful,
    Items.STUD_VEST.value: ItemClassification.useful,
    Items.FANCY_COAT.value: ItemClassification.useful,
    Items.COTARDIE.value: ItemClassification.useful,
    Items.FULL_ARMOR.value: ItemClassification.useful,
    Items.PLATE_MAIL.value: ItemClassification.useful,
    Items.SEVEN_DOUBLET.value: ItemClassification.useful,
    Items.SURCOAT.value: ItemClassification.useful,
    Items.TIGER_COAT.value: ItemClassification.useful,
    Items.FAIRY_ROBE.value: ItemClassification.useful,
    Items.DARK_TUNIC.value: ItemClassification.useful,
    Items.BRIGANDINE.value: ItemClassification.useful,
    Items.EBON_PLATE.value: ItemClassification.useful,
    Items.LYCORIS.value: ItemClassification.useful,
    Items.WYVERNMAIL.value: ItemClassification.useful,
    Items.JAZERAINT.value: ItemClassification.useful,
    Items.DEMON_COAT.value: ItemClassification.useful,
    Items.RUNE_TWEED.value: ItemClassification.useful,
    Items.RUNE_TUNIC.value: ItemClassification.useful,
    Items.BLOOD_MAIL.value: ItemClassification.useful,
    Items.COMPOSITE.value: ItemClassification.useful,
    Items.AZURE_COAT.value: ItemClassification.useful,
    Items.BLOOD_COAT.value: ItemClassification.useful,
    Items.DINO_PLATE.value: ItemClassification.useful,
    Items.DEMON_MAIL.value: ItemClassification.useful,
    Items.SYLPHEED.value: ItemClassification.useful,
    Items.HOLY_ARMOR.value: ItemClassification.useful,
    Items.GHOST_VEST.value: ItemClassification.useful,
    Items.MOBIUS_ALB.value: ItemClassification.useful,
    Items.ANGEL_ROBE.value: ItemClassification.useful,
    Items.FAIRY_MAIL.value: ItemClassification.useful,
    Items.RUBY_MAIL.value: ItemClassification.useful,
    Items.HEX_MANTLE.value: ItemClassification.useful,
    Items.MOSS_COAT.value: ItemClassification.useful,
    Items.FLAME_COAT.value: ItemClassification.useful,
    Items.FROST_COAT.value: ItemClassification.useful,
    Items.VOLT_COAT.value: ItemClassification.useful,
    Items.HAIRPIN.value: ItemClassification.useful,
    Items.HIDE_HAT.value: ItemClassification.useful,
    Items.PLUMED_HAT.value: ItemClassification.useful,
    Items.CHAIN_HELM.value: ItemClassification.useful,
    Items.GUM_HELM.value: ItemClassification.useful,
    Items.SCALE_HELM.value: ItemClassification.useful,
    Items.SCALE_CAP.value: ItemClassification.useful,
    Items.SANDY_PIN.value: ItemClassification.useful,
    Items.TIGER_CAP.value: ItemClassification.useful,
    Items.CIRCLET.value: ItemClassification.useful,
    Items.BLOOD_HELM.value: ItemClassification.useful,
    Items.ANGEL_HELM.value: ItemClassification.useful,
    Items.KNIT_GLOVE.value: ItemClassification.useful,
    Items.HIDE_GLOVE.value: ItemClassification.useful,
    Items.DOWN_GLOVE.value: ItemClassification.useful,
    Items.IRON_GLOVE.value: ItemClassification.useful,
    Items.BEAR_GLOVE.value: ItemClassification.useful,
    Items.GUM_GLOVE.value: ItemClassification.useful,
    Items.FANG_GLOVE.value: ItemClassification.useful,
    Items.SAND_GLOVE.value: ItemClassification.useful,
    Items.TIGER_HAND.value: ItemClassification.useful,
    Items.RUNE_GLOVE.value: ItemClassification.useful,
    Items.BLOOD_GAGE.value: ItemClassification.useful,
    Items.BRAVE_GAGE.value: ItemClassification.useful,
    Items.EBON_GLOVE.value: ItemClassification.useful,
    Items.ATHANOR.value: ItemClassification.useful,
    Items.RUBY_GAGE.value: ItemClassification.useful,
    Items.TOXIC_GAGE.value: ItemClassification.useful,
    Items.TARGE.value: ItemClassification.useful,
    Items.HIDE_ASPIS.value: ItemClassification.useful,
    Items.ASPIS.value: ItemClassification.useful,
    Items.OVAL_ASPIS.value: ItemClassification.useful,
    Items.HEAT_ASPIS.value: ItemClassification.useful,
    Items.GUM_ASPIS.value: ItemClassification.useful,
    Items.BODY_ASPIS.value: ItemClassification.useful,
    Items.EBON_ASPIS.value: ItemClassification.useful,
    Items.MOON_ASPIS.value: ItemClassification.useful,
    Items.KING_ASPIS.value: ItemClassification.useful,
    Items.HALO_ASPIS.value: ItemClassification.useful,
    Items.HOLY_ASPIS.value: ItemClassification.useful,
    Items.PAIN_ASPIS.value: ItemClassification.useful,
    Items.LEAF_BOOT.value: ItemClassification.useful,
    Items.HIDE_BOOT.value: ItemClassification.useful,
    Items.PLUME_BOOT.value: ItemClassification.useful,
    Items.CHAIN_BOOT.value: ItemClassification.useful,
    Items.MOCCASINS.value: ItemClassification.useful,
    Items.SCALE_BOOT.value: ItemClassification.useful,
    Items.FAIRY_BOOT.value: ItemClassification.useful,
    Items.TIGER_BOOT.value: ItemClassification.useful,
    Items.FLAME_BOOT.value: ItemClassification.useful,
    Items.FUR_BOOT.value: ItemClassification.useful,
    Items.DYED_BOOT.value: ItemClassification.useful,
    Items.SPEED_BOOT.value: ItemClassification.useful,
    Items.HIDE_BELT.value: ItemClassification.useful,
    Items.HIDE_RING.value: ItemClassification.useful,
    Items.RED_CHARM.value: ItemClassification.useful,
    Items.PETAL_RING.value: ItemClassification.useful,
    Items.CUT_CHARM.value: ItemClassification.useful,
    Items.GEM_RING.value: ItemClassification.useful,
    Items.LEAF_CAPE.value: ItemClassification.useful,
    Items.FIRE_RING.value: ItemClassification.useful,
    Items.STAR_CHARM.value: ItemClassification.useful,
    Items.TUSK_CHARM.value: ItemClassification.useful,
    Items.OLD_CHOKER.value: ItemClassification.useful,
    Items.HIDE_CAPE.value: ItemClassification.useful,
    Items.AMBER_RING.value: ItemClassification.useful,
    Items.SEA_CHARM.value: ItemClassification.useful,
    Items.BLUE_RING.value: ItemClassification.useful,
    Items.RED_CAPE.value: ItemClassification.useful,
    Items.EVIL_CHARM.value: ItemClassification.useful,
    Items.ROSE_RING.value: ItemClassification.useful,
    Items.ROYAL_RING.value: ItemClassification.useful,
    Items.GOLD_CAPE.value: ItemClassification.useful,
    Items.ANGEL_RING.value: ItemClassification.useful,
    Items.WARD_GEM.value: ItemClassification.useful,
    Items.JEWEL_EYE.value: ItemClassification.useful,
    Items.RUBY.value: ItemClassification.useful,
    Items.SAPPHIRE.value: ItemClassification.useful,
    Items.TOPAZ.value: ItemClassification.useful,
    Items.TOURMALINE.value: ItemClassification.useful,
    Items.ADAMAS.value: ItemClassification.useful,
    Items.HEX_DOLL.value: ItemClassification.useful,
    Items.OCARINA.value: ItemClassification.useful,
    Items.LUTE.value: ItemClassification.useful,
    Items.FLUTE.value: ItemClassification.useful,
    Items.KITHARA.value: ItemClassification.useful,
    Items.AULOS.value: ItemClassification.useful,
    Items.ANGEL_HARP.value: ItemClassification.useful,
    Items.SYRINX.value: ItemClassification.useful,
    Items.TOWN_MEDAL.value: ItemClassification.useful,
    Items.TOWN_CROWN.value: ItemClassification.useful,
    Items.MOSS_RING.value: ItemClassification.useful,
    Items.MOSS_BAND.value: ItemClassification.useful,
    Items.MEDICA.value: ItemClassification.useful,
    Items.MEDICA_II.value: ItemClassification.useful,
    Items.MEDICA_III.value: ItemClassification.useful,
    Items.MEDICA_IV.value: ItemClassification.useful,
    Items.MEDICA_V.value: ItemClassification.useful,
    Items.AMRITA.value: ItemClassification.useful,
    Items.AMRITA_II.value: ItemClassification.useful,
    Items.HAMAO.value: ItemClassification.useful,
    Items.HAMAO_PRIME.value: ItemClassification.useful,
    Items.SOMA.value: ItemClassification.useful,
    Items.SOMA_PRIME.value: ItemClassification.useful,
    Items.NECTAR.value: ItemClassification.useful,
    Items.NECTAR_II.value: ItemClassification.useful,
    Items.NECTAR_III.value: ItemClassification.useful,
    Items.THERIACA_A.value: ItemClassification.useful,
    Items.THERIACA_B.value: ItemClassification.useful,
    Items.AXCELA.value: ItemClassification.useful,
    Items.AXCELA_II.value: ItemClassification.useful,
    Items.AXCELA_III.value: ItemClassification.useful,
    Items.BRAVANT.value: ItemClassification.useful,
    Items.BRAVANT_II.value: ItemClassification.useful,
    Items.STONARD.value: ItemClassification.useful,
    Items.STONARD_II.value: ItemClassification.useful,
    Items.FIRE_MIST.value: ItemClassification.useful,
    Items.ICE_MIST.value: ItemClassification.useful,
    Items.VOLT_MIST.value: ItemClassification.useful,
    Items.ALL_MIST.value: ItemClassification.useful,
    Items.BLAZE_OIL.value: ItemClassification.useful,
    Items.FREEZE_OIL.value: ItemClassification.useful,
    Items.SHOCK_OIL.value: ItemClassification.useful,
    Items.WARD_CHIME.value: ItemClassification.useful,
    Items.GOLD_CHIME.value: ItemClassification.useful,
    Items.POLE_STONE.value: ItemClassification.useful,
    Items.ARIADNE_THREAD.value: ItemClassification.useful,

    # Materials - TODO List with real ids
    Items.WHITESTONE.value: ItemClassification.useful,

    # Key items - TODO List with real ids
    Items.CLEAR_KEY.value: ItemClassification.progression,
    Items.VIOLET_KEY.value: ItemClassification.progression,
    Items.RADHA_NOTE.value: ItemClassification.progression,
    
    # Custom items
    Items.FIRST_STRATUM_CLEARED.value: ItemClassification.progression,
    Items.VICTORY.value: ItemClassification.progression,
    Items.EN500.value: ItemClassification.useful,
    Items.EN200.value: ItemClassification.filler,
    Items.EN100.value: ItemClassification.filler,
    Items.NIGHT_10TP.value: ItemClassification.filler,
    Items.FIRST_CHAR_10HP.value: ItemClassification.filler,
    Items.EN50.value: ItemClassification.filler,
    Items.EN1.value: ItemClassification.filler,
}