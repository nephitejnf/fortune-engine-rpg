from random import choice
# Suit      Element Attribute           Description
# ====      ======  ========            ==========
# WANDS     Fire    Physical            incarnation of physical strength and resilience
# SWORDS    Air     Mental              mental aspects of life
# CUPS      Water   Emotional/Creative  ability to create and captivate in story
# PENTACLES Earth   Social              mastery of language and discourse
# # # # #
# PENTACLES also known as COINS
basic_arcana = {
        "w": ['1','2','3','4','5','6','7','8','9','10','p','n','q','k'],
        "c": ['1','2','3','4','5','6','7','8','9','10','p','n','q','k'],
        "s": ['1','2','3','4','5','6','7','8','9','10','p','n','q','k'],
        "p": ['1','2','3','4','5','6','7','8','9','10','p','n','q','k']
        }

major_arcana = [
        'fool', 'emperor', 'strength', 'hanged man', 'tower', 'judgement',
        'magican', 'hierophant', 'hermit', 'death', 'star', 'world',
        'high priestess', 'lover', "wheel of fortune", 'temperance', 'moon',
        'empress', 'chariot', 'justice', 'devil', 'sun'
        ]

suits = list(basic_arcana.keys())

full_basic = basic_arcana.copy()
full_major = major_arcana[:]

#########################################
# This draw a card from the minor arcana
# it first checks to see if you specified a suit, if not, it is randomized
# it then check to see if you specified a card, if not, same deal
# I then check to see if the suit you called for has any cards,
# then checks if the card is in the list
# is all those pass, we pop out the card you called and give it to you
#########################################
def draw_minor_card(suit="r", card="r"):
    if suit=='r':
        suit=choice(suits)
        if basic_arcana == []:
            suits.remove(suit)
            suit=choice(suits)
    if suit not in suits:
        return "na"
    if card=='r':
        card=choice(basic_arcana[suit])
    if basic_arcana[suit] == []:
        return "na"
    if card not in basic_arcana[suit]:
        return "na"
    s = basic_arcana[suit]
    card = basic_arcana[suit].pop(s.index(card))
    return suit+card

#########################################
# This draws out a major arcana for you
# first checking if you asked for a specific card, if not, then get a random one
# it checks to see if the card you asked for is in the list
# if it is, it gives it to you
#########################################
def draw_major_card(card="random"):
    if card=="random":
        card=choice(major_arcana)
    if card not in major_arcana:
        return "na"
    s = major_arcana
    major_arcana.remove(card)
    return card

#########################################
# it just puts a card into the deck
# we are sorting by suit, so that is why
# we ask if the suit is in the list
#########################################
def insert_minor_card(suit, card):
    if suit not in list(basic_arcana.keys()):
        return "na"
    basic_arcana[suit].append(card)
    return 0

#########################################
# I might regret this
# this allows us to add a card to the major arcana deck
# yes, no checks at all
#########################################
def insert_major_card(card):
    major_arcana.append(card)
    return 0

#########################################
# this recycles the desk, meaning resets it
# we have a variable that holds the original deck that it references
# it also refreshes the suits
#########################################
def recycle():
    major_arcana.clear()
    basic_arcana.clear()
    major_arcana = full_major.copy()
    basic_arcana = full_basic.copy()
    suits = list(basic_arcana.keys())
    return 0
