from random import choice
# Suit      Element Attribute           Description
# ====      ======  ========            ==========
# WANDS     Fire    Physical            incarnation of physical strength and resilience
# SWORDS    Air     Mental              mental aspects of life
# CUPS      Water   Emotional/Creative  ability to create and captivate in story
# PENTACLES Earth   Social              mastery of language and discourse
basic_arcana = {
        "wands": ['1','2','3','4','5','6','7','8','9','10','p','n','q','k'],
        "cups": ['1','2','3','4','5','6','7','8','9','10','p','n','q','k'],
        "swords": ['1','2','3','4','5','6','7','8','9','10','p','n','q','k'],
        "coins": ['1','2','3','4','5','6','7','8','9','10','p','n','q','k']
        }

major_arcana = [
        'fool', 'emperor', 'strength', 'hanged man', 'tower', 'judgement',
        'magican', 'hierophant', 'hermit', 'death', 'star', 'world',
        'high priestess', 'lover', "wheel of fortune", 'temperance', 'moon',
        'empress', 'chariot', 'justice', 'devil', 'sun'
        ]

suits = ['wands', 'cups', 'swords', 'coins']

full_basic = basic_arcana
full_major = major_arcana

def draw_minor_card(suit="random", card="r"):
    if suit=='random':
        suit=choice(suits)
    if card=='r':
        card=basic_arcana.pop(choice(basic_arcana[suit]))
    return suit+card

def draw_major_card(card="random"):
    if card=="random":
        card=choice(major_arcana)
    return card

def recycle():
    return 0
