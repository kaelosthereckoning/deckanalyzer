#!/usr/bin/env python
#check out more data tools @ twitch.tv/kaelos_the_reckoning

#lists of cards granting max power
fire_power_cards = ['fire sigil','seat of impulse','seat of glory','seat of fury','seat of chaos','praxis banner','rakano banner','skycrag banner','stonescar banner','granite monument']
time_power_cards = ['time sigil','seat of impulse','seat of progress','seat of wisdom','seat of mystery','praxis banner','combrei banner','elysian banner','xenan banner','amber monument']
justice_power_cards = ['justice sigil','seat of glory','seat of progress','seat of order','seat of vengeance','rakano banner','combrei banner','hooru banner','argenport banner','emerald monument']
primal_power_cards = ['primal sigil','seat of wisdom','seat of order','seat of fury','seat of cunning','elysian banner','hooru banner','skycrag banner','feln banner','cobalt monument']
shadow_power_cards = ['shadow sigil','seat of vengeance','seat of cunning','seat of chaos','seat of mystery','argenport banner','feln banner','stonescar banner','xenan banner','amethyst monument']

#lists of cards granting power, but not influence
generic_power_cards = ['diplomatic seal','initiate of the sands','azindel, the wayfinder']

#lists of cards granting "extra" power
power_doubling_cards = ['voice of the speaker','marshal ironthorn']
power_advance_cards = ['initiate of the sands','marshal ironthorn','combrei emissary','minotaur ambassador','vodakhan, temple speaker','a new tomorrow']

#lists of card types that may be depleted
depleted_power = ['seat','banner','monument','find the way','secret pages','a new tomorrow']

#lists of power fetch cards per faction
any_power_fetch = ['seek power','find the way','amber acolyte','secret pages','celestial omen']
f_power_fetch = ['kaleb\'s favor']
t_power_fetch = ['talir\'s favored','minotaur ambassador']
j_power_fetch = ['rolant\'s favor','privilege of rank','spire chaplain','minotaur ambassador']
p_power_fetch = ['eilyn\'s favor']
s_power_fetch = ['vara\'s favor']

import re

#number of cards in deck for each category
num_factions = 0
factions_found = ""
a_fetch_found = 0
f_fetch_found = 0
t_fetch_found = 0
j_fetch_found = 0
p_fetch_found = 0
s_fetch_found = 0

#names of cards found from each category
thinning_found = []
cycling_found = []
power_draw_found = []
stack_draw_found = []
void_draw_found = []
card_creation_found = []

while True:
	print ("Deck path must point to a .txt file exported directly from the Eternal client, or formatted identically.")
	try:
		deck = input('Enter file path:  ')
	except ValueError:
		print("Could not locate file, is this a valid path?")
		continue
	else:
		print("File found.")
		break
	
	
	remove cards belonging to type "power" or listed as power fetch from the decklist
	calculate power needs based upon remaining cards
	
	if low power cost dual color cards are found in deck
		print ("Because your deck does contain very early dual-influence cards, you probably want the best chance of activated seats.")
		

toggle_seats_preferred
toggle_seals_preferred
	
print ("===============")	
print ("RECOMMENDATIONS")
print ("===============")
print ("Because your deck", yesno, 
print ("Because your deck contains", num_factions, "factions, )
print ("# Stack draw:  ", stack_draw)
print ("# Void draw:  ", void_draw)
print ("# Card creation:  ", card_creation)
print ("# Thinning:  ", deck_thinning)
print ("# Card-cycling:  ", card_cycling)
print (" ")
print ("CARDS MEETING CRITERIA")
print (" ")
print ("Power draw cards:  ", (", ").join(power_draw_found))
print ("Stack draw cards:  ", (", ").join(stack_draw_found))
print ("Void draw cards:  ", (", ").join(void_draw_found))
print ("Card creation cards:  ", (", ").join(card_creation_found))
print ("Thinning cards:  ", (", ").join(thinning_found))
print ("Card-cycling cards:  ", (", ").join(cycling_found))
print (" ")
print (" ")
print ("==========")
print ("REFERENCE")
print ("==========")
print("THINNING = Cards that remove additional cards from the player's deck.  A decrease in total remaining cards increases the relative proportion of desired cards, and thus odds of drawing a desirable card.")
print (" ")
print("CARD-CYCLING = Cards that provide access to units / spells / etc. that the player would otherwise not have access to this turn.  Includes cards drawn from deck, void, or enemy as well as created cards.")
print (" ")
print("POWER DRAW = Cards that remove extant power cards from the player's deck.  This does **not** include power cards, nor does it include units that create power (e.g. Voice of the Speaker, Marshal Ironthorn).")
print (" ")
print("STACK DRAW = Cards that can retrieve non-power cards from your deck's normal stack.  Includes all draw types including top, random, type-based, and player-selected.")
print (" ")
print("VOID DRAW = Cards that can DRAW others out of the void and place them back in the player's hand or deck.  This does **not** include cards that PLAY cards from the void.")
print (" ")
print("CARD CREATION = Cards that DRAW cards not originally in the player's deck, including cards generated by Echo / Fate or stolen from the enemy player.  This does **not** include cards that generate and PLAY others (e.g. Whispers in the Void, Marisen).")		


