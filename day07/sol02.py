from collections import Counter

mode = "test2"
with open(mode+".txt", "r") as f_in:
    lines = [line.strip() for line in f_in.readlines()]

cards = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
c_vals = {card:i+1 for i,card in enumerate(reversed(cards))}
hands = ["5","41","32","311","221","2111","11111"]
h_vals = {hand:i+1 for i,hand in enumerate(reversed(hands))}
ord_cards = {card:chr(i+1) for i,card in enumerate(reversed(cards))}
handWbids = [(line.split(" ")[0],int(line.split(" ")[1])) for line in lines]
ord_cards["J"] = chr(0)

by_handv = {k:[] for k in hands}
for hand, bid in handWbids:
    h_config = []

    
    print("Hand w/o J:", hand)
    
    if "J" in hand:
        hand_woJ = hand.replace("J","")
        if hand_woJ:
            most_common = Counter(hand_woJ).most_common()[0]
            hand = hand.replace("J",most_common[0])
    
    print("Hand w J:", hand)
    for c in Counter(hand).values():
        h_config.append(str(c))
    h_config = "".join(sorted(h_config, reverse=True))
    print(h_config)
    by_handv[h_config].append((hand,bid))  
print()


ranked = []
for x,handWbids in by_handv.items():
    if not handWbids:
        continue

    valueWhandWbids = []
    for handWbid in handWbids:
        v_cards = "".join([ord_cards[card] for card in handWbid[0]])
        valueWhandWbids.append([v_cards, handWbid[0], handWbid[1]])
    valueWhandWbids.sort(key=lambda x: x[0])
    handWbids_ranked = [(x[1],x[2]) for x in reversed(valueWhandWbids)]
    ranked.extend(handWbids_ranked)

print(sum([(rank+1)*handWbid[1] for rank,handWbid in enumerate(reversed(ranked))]))