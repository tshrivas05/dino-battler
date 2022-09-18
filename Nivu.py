from Dinosaur import *
from random import *

dino1 = Dinosaur('yutyrannus huali','cretaceous','carnivore', 1400, 'china', 'therepod')
dino2 = Dinosaur('siats meekerorum', 'cretaceous', 'carnivore', 3917, 'utah, usa', 'therepod')
dino3 = Dinosaur('patagotitan mayorum', 'cretaceous', 'herbivore', 69000, 'patagonia, argentina','sauropod')
dino4 = Dinosaur('stegoceras validum', 'cretaceous', 'herbivore', 40, 'canada', 'unknown')
dino5 = Dinosaur('daspletosaurus torosus', 'cretaceous', 'carnivore', 2500, ['alberta, canada','montana, usa'], 'therepod')
dino6 = Dinosaur('rajasaurus narmadensis', 'cretaceous', 'carnivore', 4000, 'india', 'therepod')
dino7 = Dinosaur('tsintaosaurus spinorhinus', 'cretaceous','herbivore', 3000,'shangdong province, china','unknown')
dino8 = Dinosaur('pachyrhinosaurus perotorum', 'cretaceous', 'herbivore', 4000, 'north slope, alaska', 'ceratopsian')
dino9 = Dinosaur('tyrannosaurus rex', 'cretaceous', 'carnivore', 6000, 'western north america', 'therepod')
dino10 = Dinosaur('spinosaurus aegyptiacus', 'cretaceous', 'carnivore', 9000, 'bahariya oasis, egypt', 'therepod')
dino11 = Dinosaur('muttaburasaurus langdoni', 'cretaceous', 'herbivore', 2800, 'australia', 'unknown')
dino12 = Dinosaur('diamantinasaurus matildae', 'cretaceous', 'herbivore', 10000, 'queensland, australia', 'sauropod')
dino13 = Dinosaur('rugops primus', 'cretaceous', 'carnivore', 750, 'abangharit, niger', 'therepod')
dino14 = Dinosaur('mapusaurus roseae', 'cretaceous', 'carnivore', 5000, 'argentina', 'therepod')
dino15 = Dinosaur('giraffatitan brancai', 'jurassic','herbivore', 23000, 'tendaguru, tanzania','sauropod')
dino16 = Dinosaur('stegosaurus armatus', 'jurassic', 'herbivore', 2300, ['usa', 'portugal', 'china(?)'], 'unknown')

#create a list of dinos
dino_list = [dino1,dino2,dino3,dino4,dino5,dino6,dino7,dino8,dino9,dino10,dino11,dino12,dino13,dino14,dino15,dino16]

def randomizer(l):
    a = l[randrange(len(l))]
    b = l[randrange(len(l))]
    return a, b;

#function to display dino facts
def printer(dino):
    print(f'--- DINO FACTS --- \n\
        name: {dino.name}\n\
        time period: {dino.tperiod}\n\
        diet: {dino.diet}\n\
        weight: {dino.weight} kgs \n\
        location: {dino.location} \n\
        phenotype: {dino.phytype}')

def battler(dino_a, dino_b):
    if dino_a.diet == dino_b.diet:
        if dino_a.weight > dino_b.weight:
            print(f'--- **{dino_a.name}** is the winner! ---')
        elif dino_a.weight < dino_b.weight:
            print(f'--- **{dino_b.name}** is the winner! ---')
        else:
            print(f'--- {dino_a.name} and {dino_b.name} have resulted in a tie! ---')
    else:
        if dino_a.diet == 'carnivore' and dino_a.weight >= dino_b.weight:
            print(f'--- **{dino_a.name}** is the winner! ---')
        elif dino_b.diet == 'carnivore' and dino_a.weight <= dino_b.weight:
            print(f'--- **{dino_b.name}** is the winner! ---')
        else:
            if random() > 0.5:
                if dino_a.diet == 'carnivore': 
                    print(f'--- **{dino_a.name}** is the winner! {dino_a.name} outsmarted the heavier {dino_b.name} and hit the {dino_b.name} where it hurts! ---')
                else:
                    print(f'--- **{dino_a.name}** is the winner! {dino_a.name} clearly was way out of {dino_b.name}\'s weight class - it crushed {dino_b.name} with its whole {dino_a.weight} kgs! ---')
            else:
                if dino_b.diet == 'carnivore': 
                    print(f'--- **{dino_b.name}** is the winner! {dino_b.name} outsmarted the heavier {dino_a.name} and hit the {dino_a.name} where it hurts! ---')
                else:
                    print(f'--- **{dino_b.name}** is the winner! {dino_b.name} clearly was way out of {dino_a.name}\'s weight class - it crushed {dino_a.name} with its whole {dino_b.weight} kgs! ---')

#function to create rounds of battle sessions 
def battl_sesh(rnds):
    for rnd in range(rnds):
        print(f'--- Battle # {rnd+1} ---') 
        a, b = randomizer(dino_list)
        printer(a)
        printer(b)
        print('\n')
        battler(a,b)
        print('\n\n')

#function to create summary stats of battle run 

r = int(input('Enter how many dino battles you want to see: \n'))
print('\n')
battl_sesh(r)