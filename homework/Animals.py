class Animals:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def about_animal(self):
        print(f'{self.name}.\nShort description about animal: {self.description}')


class Manual(Animals):
    def about_animal(self):
        print(f'{self.name} is wild animal.\nShort description about animal: {self.description}')


class Bird(Animals):
    def about_animal(self):
        print(f'{self.name} is bird.\nShort description about animal: {self.description}')


class Reptilian(Animals):
    def about_animal(self):
        print(f'{self.name} is reptilian.\nShort description about animal: {self.description}')

    @staticmethod
    def special_description():
        print('Most tortoise species can live 80–150 years')


class Arachnids(Animals):
    def about_animal(self):
        print(f'{self.name} is arachnids.\nShort description about animal: {self.description}')

    @staticmethod
    def dangerous():
        print('Be careful!!!')


class Placental_mammals(Animals):
    def about_animal(self):
        print(f'{self.name} is placental mammals.\nShort description about animal: {self.description}')




manual = Manual("Lion", "Living in the grasslands, scrub, and open woodlands of sub-Saharan Africa, the lion is the "
                        "second largest cat in the world. It is dwarfed slightly by the tiger, which is closely "
                        "related and has a very similar body typeUnlike other cats, lions are very social animals. "
                        "They live in groups, called prides, of around 30 lions. A pride consists of up to three "
                        "males, a dozen related females, and their young. The size of the pride is determined by the "
                        "availability of food and water. If resources are scarce, the pride becomes smallerPride "
                        "members keep track of one another by roaring. Both males and females have a very powerful "
                        "roar that can be heard up to 8 km (5 mi. away.Males and females take on very different roles "
                        "in the pride. Male lions spend their time guarding their territory and their cubs. They "
                        "maintain the boundaries of their territory, which can be as large as 260 sq. km (100 sq. "
                        "mi.), by roaring, marking it with urine, and chasing off intruders. Their thick manes, "
                        "a unique trait to male lions, protect their necks when they fight with challengers.")
manual.about_animal()

bird = Bird("Owal", "There are around 200 different owl species.Owls are active at night (nocturnal).A group of owls "
                    "is called a parliament.Most owls hunt insects, small mammals and other birds.Some owl species "
                    "hunt fish.Owls have powerful talons (claws) which help them catch and kill prey.Owls have large "
                    "eyes and a flat face.Owls can turn their heads as much as 270 degrees.Owls are farsighted, "
                    "meaning they can’t see things close to their eyes clearly.Owls are very quiet in flight compared "
                    "to other birds of prey.The color of owl’s feathers helps them blend into their environment ("
                    "camouflage).Barn owls can be recognized by their heart shaped face.")
bird.about_animal()

reptilian = Reptilian("Tortoise", "A tortoise's shell is made up of 60 different bones all connected to each other "
                                  "The top of a tortoise's shell is called a “carapace” The underside of the shell is "
                                  "called a “plastron” The carapace and the plastron of a tortoises shell is "
                                  "connected by what is known as a bridge Tortoises can retract their heads and all "
                                  "their limbs including their tails into their shells when they feel threatened or "
                                  "attacked by predators Tortoises have extremely strong mouths but no teeth instead "
                                  "they have horny type beaks Tortoises have good all round vision and a very good "
                                  "sense of smell Tortoises are cold-blooded – they draw heat from their environment "
                                  "and are more active during the day than at night Tortoises can live a very long "
                                  "time, some to the ripe old age of 150. However, the average age a tortoise can "
                                  "live to ranges from 90 to 150 years Tortoises are what is known as herbivores, "
                                  "they eat grass, ferns, flowers, tree leaves and fruit Female tortoises are usually "
                                  "larger than their male counterparts Females dig burrows in which they can lay up "
                                  "anything from 1 to 30 eggs A male tortoise has a longer tail than that of a "
                                  "female, which is one way of sexing them When baby tortoises break out of their "
                                  "shells they are called hatchlingsTortoise eggs incubate between 90 to 120 days to "
                                  "hatch out Tortoises hibernate in the winter time and before they do, they starve "
                                  "themselves so their stomachs are empty ready for hibernation")
reptilian.about_animal()
reptilian.special_description()

arachnids = Arachnids("Spider", "Spiders are arachnids, not insects.Other members of the arachnid family include "
                                "scorpions, mites, ticks and harvestmen.Spiders have 8 legs while insects have "
                                "6.Spiders don’t have antennae while insects do.Spiders are found on every continent "
                                "of the world except Antarctica.There are around 40000 different species of "
                                "spider.Most spiders make silk which they use to create spider webs and capture "
                                "prey.Abandoned spider webs are called cobwebs.Most spiders are harmless to humans "
                                "but a few spider species, such as the black widow, can bite humans and inject venom. "
                                "Deaths from spider bites are rare however.An abnormal fear of spiders is called "
                                "‘arachnophobia’.Tarantulas are large and often hairy spiders, the biggest species "
                                "have been known to kill mice, lizards and birds.Most tarantula species pose no "
                                "threat to humans.The largest specie of tarantula is the Goliath Birdeater.Giant "
                                "Huntsman spiders have leg-spans of around 30cm (12 in).")
arachnids.about_animal()
arachnids.dangerous()

placental_mammals = Placental_mammals("Monkey", "There are currently 264 known monkey species.Monkeys can be divided "
                                                "into two groups, Old World monkeys that live in Africa and Asia, "
                                                "and New World monkeys that live in South America.A baboon is an "
                                                "example of an Old World monkey, while a marmoset is an example of a "
                                                "New World monkey.Apes are not monkeys.Some monkeys live on the "
                                                "ground, while others live in trees.Different monkey species eat a "
                                                "variety of foods, such as fruit, insects, flowers, leaves and "
                                                "reptiles.Most monkeys have tails.Groups of monkeys are known as a "
                                                "‘tribe’, ‘troop’ or ‘mission’.The Pygmy Marmoset is the smallest "
                                                "type of monkey, with adults weighing between 120 and 140 grams.The "
                                                "Mandrill is the largest type of monkey, with adult males weighing up "
                                                "to 35 kg.Capuchin monkeys are believed to be one of the smartest New "
                                                "World monkey species. They have the ability to use tools, "
                                                "learn new skills and show various signs of self-awareness.Spider "
                                                "monkeys get their name because of their long arms, legs and tail.The "
                                                "monkey is the 9th animal that appears on the Chinese zodiac, "
                                                "appearing as the zodiac sign in 2016.")
placental_mammals.about_animal()
