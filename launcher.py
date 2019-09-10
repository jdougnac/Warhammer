from tkinter import *
from tkinter import ttk
import random
import query
import data


class Temp:
    raceStats = []
    firstCareerId = 0
    charGender = ''


temporary = Temp()


class MyApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (Skills, PageTwo, NewCharacter):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)
        self.show_frame(Skills)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, classname):
        # Returns an instance of a page given its class name as a string
        for page in self.frames.values():
            if str(page.__class__.__name__) == classname:
                return page
        return None
    def test_get_page(self, page_class):
        return self.frames[page_class]


class Skills(ttk.Frame):
    # creates all the necessary elements for the UI
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='PageOne').grid()
        self.nameLabel = Label(self, text="Name: ")
        self.nameTXT = Entry(self)
        self.raceLabel = Label(self, text="Race: ")
        self.raceText = Label(self, text="")
        self.currentCareerLabel = Label(self, text="Career: ")
        self.currentCareerText = Label(self, text="")
        self.distinguishingMarkLabel = Label(self, text="Mark: ")
        self.distinguishingMarkText = Label(self, text="")
        self.ageLabel = Label(self, text="Age: ")
        self.ageText = Label(self, text="")
        self.genderLabel = Label(self, text="Gender: ")
        self.genderText = Label(self, text="")
        self.eyeColorLabel = Label(self, text="Eye Color: ")
        self.eyeColorText = Label(self, text="")
        self.hairColorLabel = Label(self, text="Hair Color: ")
        self.hairColorText = Label(self, text="")
        self.heightLabel = Label(self, text="Height: ")
        self.heightText = Label(self, text="")
        self.weightLabel = Label(self, text="Weight: ")
        self.weightText = Label(self, text="")
        self.siblingsLabel = Label(self, text="Siblings: ")
        self.siblingsText = Label(self, text="")
        self.starSignLabel = Label(self, text="Star Sign: ")
        self.starSignText = Label(self, text="")
        self.birthPlaceLabel = Label(self, text="Birth Place: ")
        self.birthPlaceText = Label(self, text="")
        self.xpTotalLabel = Label(self, text="Total XP: ")
        self.xpTotalText = Label(self, text="")

        self.statsLabel = Label(self, text="Stats:")
        self.statsBaseLabel = Label(self, text="Base:")
        self.advancesLabel = Label(self, text="Advances:")
        self.statsTotalLabel = Label(self, text="Total:")

        # charLabel references the base value of the stat (ie 2d10 + racial mod)
        # advancesLabel means the amount of advances available to the character
        # in its career
        # advancesTakenLabel is the total value of a given stat (stat + advances taken)
        # defines all the labels:
        self.wsLabel = Label(self, text="WS")
        self.bsLabel = Label(self, text="BS")
        self.sLabel = Label(self, text="S")
        self.tLabel = Label(self, text="T")
        self.agLabel = Label(self, text="Ag")
        self.intLabel = Label(self, text="Int")
        self.wpLabel = Label(self, text="WP")
        self.felLabel = Label(self, text="Fel")

        self.wsBase = Label(self, text="")
        self.bsBase = Label(self, text="")
        self.sBase = Label(self, text="")
        self.tBase = Label(self, text="")
        self.agBase = Label(self, text="")
        self.intBase = Label(self, text="")
        self.wpBase = Label(self, text="")
        self.felBase = Label(self, text="")

        self.wsAdvancesLabel = Label(self, text="")
        self.bsAdvancesLabel = Label(self, text="")
        self.sAdvancesLabel = Label(self, text="")
        self.tAdvancesLabel = Label(self, text="")
        self.agAdvancesLabel = Label(self, text="")
        self.intAdvancesLabel = Label(self, text="")
        self.wpAdvancesLabel = Label(self, text="")
        self.felAdvancesLabel = Label(self, text="")

        self.wsAdvancesTakenLabel = Label(self, text="")
        self.bsAdvancesTakenLabel = Label(self, text="")
        self.sAdvancesTakenLabel = Label(self, text="")
        self.tAdvancesTakenLabel = Label(self, text="")
        self.agAdvancesTakenLabel = Label(self, text="")
        self.intAdvancesTakenLabel = Label(self, text="")
        self.wpAdvancesTakenLabel = Label(self, text="")
        self.felAdvancesTakenLabel = Label(self, text="")

        self.aLabel = Label(self, text="A")
        self.wLabel = Label(self, text="W")
        self.sbLabel = Label(self, text="SB")
        self.tbLabel = Label(self, text="TB")
        self.mLabel = Label(self, text="M")
        self.magLabel = Label(self, text="Mag")
        self.ipLabel = Label(self, text="IP")
        self.fpLabel = Label(self, text="FP")

        self.aBase = Label(self, text="")
        self.wBase = Label(self, text="")
        self.sbBase = Label(self, text="")
        self.tbBase = Label(self, text="")
        self.mBase = Label(self, text="")
        self.magBase = Label(self, text="")
        self.ipBase = Label(self, text="")
        self.fpBase = Label(self, text="")

        self.statsLabel2 = Label(self, text="Stats:")
        self.statsBaseLabel2 = Label(self, text="Base:")
        self.advancesLabel2 = Label(self, text="Advances:")
        self.statsTotalLabel2 = Label(self, text="Total:")

        self.aAdvancesLabel = Label(self, text="")
        self.wAdvancesLabel = Label(self, text="")
        self.sbAdvancesLabel = Label(self, text="")
        self.tbAdvancesLabel = Label(self, text="")
        self.mAdvancesLabel = Label(self, text="")
        self.magAdvancesLabel = Label(self, text="")
        self.ipAdvancesLabel = Label(self, text="")
        self.fpAdvancesLabel = Label(self, text="")

        self.aAdvancesTakenLabel = Label(self, text="")
        self.wAdvancesTakenLabel = Label(self, text="")
        self.sbAdvancesTakenLabel = Label(self, text="")
        self.tbAdvancesTakenLabel = Label(self, text="")
        self.mAdvancesTakenLabel = Label(self, text="")
        self.magAdvancesTakenLabel = Label(self, text="")
        self.ipAdvancesTakenLabel = Label(self, text="")
        self.fpAdvancesTakenLabel = Label(self, text="")

        button1 = ttk.Button(self, text='Next Page',
                             command=lambda: controller.show_frame(PageTwo))
        button2 = ttk.Button(self, text='Create New',
                             command=lambda: controller.show_frame(NewCharacter))

        # puts all elements in the frame
        self.nameLabel.grid(row=1, column=0)
        self.nameTXT.grid(row=1, column=1)
        self.raceLabel.grid(row=1, column=2)
        self.raceText.grid(row=1, column=3)
        self.currentCareerLabel.grid(row=1, column=4)
        self.currentCareerText.grid(row=1, column=5)
        self.distinguishingMarkLabel.grid(row=1, column=6)
        self.distinguishingMarkText.grid(row=1, column=7)

        self.ageLabel.grid(row=2, column=0)
        self.ageText.grid(row=2, column=1)
        self.genderLabel.grid(row=2, column=2)
        self.genderText.grid(row=2, column=3)
        self.eyeColorLabel.grid(row=2, column=4)
        self.eyeColorText.grid(row=2, column=5)
        self.hairColorLabel.grid(row=2, column=6)
        self.hairColorText.grid(row=2, column=7)
        self.heightLabel.grid(row=3, column=0)
        self.heightText.grid(row=3, column=1)
        self.weightLabel.grid(row=3, column=2)
        self.weightText.grid(row=3, column=3)
        self.siblingsLabel.grid(row=3, column=4)
        self.siblingsText.grid(row=3, column=5)
        self.starSignLabel.grid(row=3, column=6)
        self.starSignText.grid(row=3, column=7)
        self.birthPlaceLabel.grid(row=4, column=0)
        self.birthPlaceText.grid(row=4, column=1)
        self.xpTotalLabel.grid(row=4, column=2)
        self.xpTotalText.grid(row=4, column=3)

        self.statsLabel.grid(row=7, column=0)
        self.statsBaseLabel.grid(row=8, column=0)
        self.advancesLabel.grid(row=9, column=0)
        self.statsTotalLabel.grid(row=10, column=0)

        self.wsLabel.grid(row=7, column=1)
        self.bsLabel.grid(row=7, column=2)
        self.sLabel.grid(row=7, column=3)
        self.tLabel.grid(row=7, column=4)
        self.agLabel.grid(row=7, column=5)
        self.intLabel.grid(row=7, column=6)
        self.wpLabel.grid(row=7, column=7)
        self.felLabel.grid(row=7, column=8)

        self.wsBase.grid(row=8, column=1)
        self.bsBase.grid(row=8, column=2)
        self.sBase.grid(row=8, column=3)
        self.tBase.grid(row=8, column=4)
        self.agBase.grid(row=8, column=5)
        self.intBase.grid(row=8, column=6)
        self.wpBase.grid(row=8, column=7)
        self.felBase.grid(row=8, column=8)

        self.wsAdvancesLabel.grid(row=9, column=1)
        self.bsAdvancesLabel.grid(row=9, column=2)
        self.sAdvancesLabel.grid(row=9, column=3)
        self.tAdvancesLabel.grid(row=9, column=4)
        self.agAdvancesLabel.grid(row=9, column=5)
        self.intAdvancesLabel.grid(row=9, column=6)
        self.wpAdvancesLabel.grid(row=9, column=7)
        self.felAdvancesLabel.grid(row=9, column=8)

        self.wsAdvancesTakenLabel.grid(row=10, column=1)
        self.bsAdvancesTakenLabel.grid(row=10, column=2)
        self.sAdvancesTakenLabel.grid(row=10, column=3)
        self.tAdvancesTakenLabel.grid(row=10, column=4)
        self.agAdvancesTakenLabel.grid(row=10, column=5)
        self.intAdvancesTakenLabel.grid(row=10, column=6)
        self.wpAdvancesTakenLabel.grid(row=10, column=7)
        self.felAdvancesTakenLabel.grid(row=10, column=8)

        self.statsLabel2.grid(row=11, column=0)
        self.statsBaseLabel2.grid(row=12, column=0)
        self.advancesLabel2.grid(row=13, column=0)
        self.statsTotalLabel2.grid(row=14, column=0)

        self.aLabel.grid(row=11, column=1)
        self.wLabel.grid(row=11, column=2)
        self.sbLabel.grid(row=11, column=3)
        self.tbLabel.grid(row=11, column=4)
        self.mLabel.grid(row=11, column=5)
        self.magLabel.grid(row=11, column=6)
        self.ipLabel.grid(row=11, column=7)
        self.fpLabel.grid(row=11, column=8)

        self.aBase.grid(row=12, column=1)
        self.wBase.grid(row=12, column=2)
        self.sbBase.grid(row=12, column=3)
        self.tbBase.grid(row=12, column=4)
        self.mBase.grid(row=12, column=5)
        self.magBase.grid(row=12, column=6)
        self.ipBase.grid(row=12, column=7)
        self.fpBase.grid(row=12, column=8)

        self.aAdvancesLabel.grid(row=13, column=1)
        self.wAdvancesLabel.grid(row=13, column=2)
        self.sbAdvancesLabel.grid(row=13, column=3)
        self.tbAdvancesLabel.grid(row=13, column=4)
        self.mAdvancesLabel.grid(row=13, column=5)
        self.magAdvancesLabel.grid(row=13, column=6)
        self.ipAdvancesLabel.grid(row=13, column=7)
        self.fpAdvancesLabel.grid(row=13, column=8)

        self.aAdvancesTakenLabel.grid(row=14, column=1)
        self.wAdvancesTakenLabel.grid(row=14, column=2)
        self.sbAdvancesTakenLabel.grid(row=14, column=3)
        self.tbAdvancesTakenLabel.grid(row=14, column=4)
        self.mAdvancesTakenLabel.grid(row=14, column=5)
        self.magAdvancesTakenLabel.grid(row=14, column=6)
        self.ipAdvancesTakenLabel.grid(row=14, column=7)
        self.fpAdvancesTakenLabel.grid(row=14, column=8)
        button1.grid()
        button2.grid()

    def roll_new_character(self, race, gender, career):
        char_stats = self.roll_stats(race)
        secondary_stats = self.roll_secondary_stats(race[1], gender)

        # sets the values of the secondary stats according
        # to the results of roll_secondary_stats
        self.raceText.config(text=race[1].capitalize())
        self.genderText.config(text=gender)
        self.ageText.config(text=secondary_stats[0])
        self.birthPlaceText.config(text=secondary_stats[1])
        self.eyeColorText.config(text=secondary_stats[2])
        self.hairColorText.config(text=secondary_stats[3])
        self.heightText.config(text=secondary_stats[4])
        self.siblingsText.config(text=secondary_stats[5])
        self.weightText.config(text=secondary_stats[8])
        self.distinguishingMarkText.config(text=secondary_stats[9])
        self.starSignText.config(text=secondary_stats[10])

        self.wsBase.config(text=char_stats[0])
        self.bsBase.config(text=char_stats[1])
        self.sBase.config(text=char_stats[2])
        self.tBase.config(text=char_stats[3])
        self.agBase.config(text=char_stats[4])
        self.intBase.config(text=char_stats[5])
        self.wpBase.config(text=char_stats[6])
        self.felBase.config(text=char_stats[7])

        self.aBase.config(text=1)
        self.wBase.config(text=secondary_stats[7])
        self.mBase.config(text=char_stats[8])
        self.magBase.config(text=0)
        self.ipBase.config(text=0)
        self.fpBase.config(text=secondary_stats[6])

        print('test', race)
        print('test', career)

    def roll_stats(self, race):
        stat_list = []
        for stat in race[2:-1]:
            stat = stat + random.randint(1, 10) + random.randint(1, 10)
            stat_list.append(stat)
        stat_list.append(race[-1])
        return stat_list

    def roll_secondary_stats(self, race, gender):
        secondary_stats = []
        if race == 'dwarf':
            chosen_race = data.dwarf_list
        elif race == 'elf':
            chosen_race = data.elf_list
        elif race == 'halfling':
            chosen_race = data.halfling_list
        elif race == 'human':
            chosen_race = data.human_list
        secondary_stats.append(random.randrange(chosen_race[0][0], chosen_race[0][1], chosen_race[0][2]))
        secondary_stats.append(random.choice(chosen_race[1]))
        secondary_stats.append(random.choice(chosen_race[2]))
        secondary_stats.append(random.choice(chosen_race[3]))
        if gender == 'Male':
            secondary_stats.append(chosen_race[4][0]+random.randint(1, 25))
        elif gender == 'Female':
            secondary_stats.append(chosen_race[4][1]+random.randint(1, 25))
        secondary_stats.append(random.choice(chosen_race[5]))
        secondary_stats.append(random.choice(chosen_race[6]))
        secondary_stats.append(random.choice(chosen_race[7]))
        secondary_stats.append(random.randint(chosen_race[8][0], chosen_race[8][1]))
        secondary_stats.append(random.choice(chosen_race[9]))
        secondary_stats.append(random.choice(chosen_race[10]))
        return secondary_stats


class NewCharacter(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller # CAMBIAR EN CASO DE BUGS
        self.raceQuery = query.selectAll('*', 'race')
        self.careerAdvanceQuery = query.selectWhere('*', 'career', 'is_basic', 1)

        button1 = ttk.Button(self, text='Cancel',
                             command=lambda: controller.show_frame(Skills))

        confirmButton = ttk.Button(self, text='Confirm',
                                   # command=lambda: controller.show_frame(Skills))
                                   command=lambda: self.confirmCharacter())

        self.genderLabel = Label(self, text = 'Gender:')
        pickedGender = StringVar()
        genderMale = Radiobutton(self, text='Male', variable=pickedGender,
                                 value=0, indicator=0,
                                 background="light blue", command=lambda: self.setGender('Male'))
        genderFemale = Radiobutton(self, text='Female', variable=pickedGender,
                                   value=1, indicator=0,
                                   background="light blue", command=lambda: self.setGender('Female'))

        self.raceLabel = Label(self, text="Race: ")
        # these are the four buttons that will determine the character's race,
        # passing the values from the query to the text and label, as set in the function below
        pickedRace = StringVar()
        raceOption1 = Radiobutton(self, text='Dwarf', variable=pickedRace,
                                  value=0, indicator=0,
                                  background="light blue", command=lambda: self.selectRace(0))
        raceOption2 = Radiobutton(self, text='Elf', variable=pickedRace,
                                  value=1, indicator=0,
                                  background="light blue", command=lambda: self.selectRace(1))
        raceOption3 = Radiobutton(self, text='Halfling', variable=pickedRace,
                                  value=2, indicator=0,
                                  background="light blue", command=lambda: self.selectRace(2))
        raceOption4 = Radiobutton(self, text='Human', variable=pickedRace,
                                  value=3, indicator=0,
                                  background="light blue", command=lambda: self.selectRace(3))

        self.careerLabel = Label(self, text="Career: ")

        self.wsLabel = Label(self, text="WS")
        self.bsLabel = Label(self, text="BS")
        self.sLabel = Label(self, text="S")
        self.tLabel = Label(self, text="T")
        self.agLabel = Label(self, text="Ag")
        self.intLabel = Label(self, text="Int")
        self.wpLabel = Label(self, text="WP")
        self.felLabel = Label(self, text="Fel")

        self.raceSkillsLabel = Label(self, text="Skills:")
        self.raceTalentsLabel = Label(self, text="Talents:")

        self.wsText = Label(self, text="0")
        self.bsText = Label(self, text="0")
        self.sText = Label(self, text="0")
        self.tText = Label(self, text="0")
        self.agText = Label(self, text="0")
        self.intText = Label(self, text="0")
        self.wpText = Label(self, text="0")
        self.felText = Label(self, text="0")

        self.raceSkillText = Text(self, height=6, width=22, wrap = WORD)
        self.raceTalentText = Text(self, height=6, width=22, wrap = WORD)

        self.aLabel = Label(self, text="A")
        self.wLabel = Label(self, text="W")
        self.sbLabel = Label(self, text="SB")
        self.tbLabel = Label(self, text="TB")
        self.mLabel = Label(self, text="M")
        self.magLabel = Label(self, text="Mag")
        self.ipLabel = Label(self, text="IP")
        self.fpLabel = Label(self, text="FP")

        self.aText = Label(self, text="0")
        self.wText = Label(self, text="0")
        self.sbText = Label(self, text="0")
        self.tbText = Label(self, text="0")
        self.mText = Label(self, text="0")
        self.magText = Label(self, text="0")
        self.ipText = Label(self, text="0")
        self.fpText = Label(self, text="0")

        self.wsCareerLabel = Label(self, text="WS")
        self.bsCareerLabel = Label(self, text="BS")
        self.sCareerLabel = Label(self, text="S")
        self.tCareerLabel = Label(self, text="T")
        self.agCareerLabel = Label(self, text="Ag")
        self.intCareerLabel = Label(self, text="Int")
        self.wpCareerLabel = Label(self, text="WP")
        self.felCareerLabel = Label(self, text="Fel")
        self.careerSkillsLabel = Label(self, text="Skills:")
        self.careerTalentsLabel = Label(self, text="Talents:")

        self.wsCareerText = Label(self, text="0")
        self.bsCareerText = Label(self, text="0")
        self.sCareerText = Label(self, text="0")
        self.tCareerText = Label(self, text="0")
        self.agCareerText = Label(self, text="0")
        self.intCareerText = Label(self, text="0")
        self.wpCareerText = Label(self, text="0")
        self.felCareerText = Label(self, text="0")

        self.careerSkillText = Text(self, height=6, width=22, wrap=WORD)
        self.careerTalentText = Text(self, height=6, width=22, wrap=WORD)

        self.aCareerLabel = Label(self, text="A")
        self.wCareerLabel = Label(self, text="W")
        self.sbCareerLabel = Label(self, text="SB")
        self.tbCareerLabel = Label(self, text="TB")
        self.mCareerLabel = Label(self, text="M")
        self.magCareerLabel = Label(self, text="Mag")
        self.ipCareerLabel = Label(self, text="IP")
        self.fpCareerLabel = Label(self, text="FP")

        self.aCareerText = Label(self, text="0")
        self.wCareerText = Label(self, text="0")
        self.sbCareerText = Label(self, text="0")
        self.tbCareerText = Label(self, text="0")
        self.mCareerText = Label(self, text="0")
        self.magCareerText = Label(self, text="0")
        self.ipCareerText = Label(self, text="0")
        self.fpCareerText = Label(self, text="0")

        raceOption1.grid(row=1, column=0)
        raceOption2.grid(row=2, column=0)
        raceOption3.grid(row=3, column=0)
        raceOption4.grid(row=4, column=0)

        self.careerLabel.grid(row=5, column=0)

    # for each basic career, this loop
        pickedCareer = StringVar()
        pos = 0
        for career in self.careerAdvanceQuery:
            careerPos = pos
            Radiobutton(self,
                        text=career[1],
                        variable=pickedCareer,
                        value=careerPos,
                        indicator=0,
                        background="light blue",
                        # command=lambda: self.selectCareer(career[0]).grid(column=0))
                        command=lambda careerPos=careerPos: self.selectCareer(careerPos)).grid(column=0)
            pos += 1

        self.raceLabel.grid(row=0, column=0)
        self.raceSkillsLabel.grid(row=0, column=9)
        self.raceTalentsLabel.grid(row=0, column=10)
        self.wsLabel.grid(row=1, column=1)
        self.bsLabel.grid(row=1, column=2)
        self.sLabel.grid(row=1, column=3)
        self.tLabel.grid(row=1, column=4)
        self.agLabel.grid(row=1, column=5)
        self.intLabel.grid(row=1, column=6)
        self.wpLabel.grid(row=1, column=7)
        self.felLabel.grid(row=1, column=8)

        self.raceSkillText.grid(row=1, column=9)
        self.raceTalentText .grid(row=1, column=10)

        self.wsText.grid(row=2, column=1)
        self.bsText.grid(row=2, column=2)
        self.sText.grid(row=2, column=3)
        self.tText.grid(row=2, column=4)
        self.agText.grid(row=2, column=5)
        self.intText.grid(row=2, column=6)
        self.wpText.grid(row=2, column=7)
        self.felText.grid(row=2, column=8)

        self.aLabel.grid(row=3, column=1)
        self.wLabel.grid(row=3, column=2)
        self.sbLabel.grid(row=3, column=3)
        self.tbLabel.grid(row=3, column=4)
        self.mLabel.grid(row=3, column=5)
        self.magLabel.grid(row=3, column=6)
        self.ipLabel.grid(row=3, column=7)
        self.fpLabel.grid(row=3, column=8)

        self.aText.grid(row=4, column=1)
        self.wText.grid(row=4, column=2)
        self.sbText.grid(row=4, column=3)
        self.tbText.grid(row=4, column=4)
        self.mText.grid(row=4, column=5)
        self.magText.grid(row=4, column=6)
        self.ipText.grid(row=4, column=7)
        self.fpText.grid(row=4, column=8)

        self.careerSkillsLabel.grid(row=5, column=9)
        self.careerTalentsLabel.grid(row=5, column=10)
        self.wsCareerLabel.grid(row=6, column=1)
        self.bsCareerLabel.grid(row=6, column=2)
        self.sCareerLabel.grid(row=6, column=3)
        self.tCareerLabel.grid(row=6, column=4)
        self.agCareerLabel.grid(row=6, column=5)
        self.intCareerLabel.grid(row=6, column=6)
        self.wpCareerLabel.grid(row=6, column=7)
        self.felCareerLabel.grid(row=6, column=8)

        self.careerSkillText.grid(row=6, column=9)
        self.careerTalentText .grid(row=6, column=10)

        self.wsCareerText.grid(row=7, column=1)
        self.bsCareerText.grid(row=7, column=2)
        self.sCareerText.grid(row=7, column=3)
        self.tCareerText.grid(row=7, column=4)
        self.agCareerText.grid(row=7, column=5)
        self.intCareerText.grid(row=7, column=6)
        self.wpCareerText.grid(row=7, column=7)
        self.felCareerText.grid(row=7, column=8)

        self.aCareerLabel.grid(row=8, column=1)
        self.wCareerLabel.grid(row=8, column=2)
        self.sbCareerLabel.grid(row=8, column=3)
        self.tbCareerLabel.grid(row=8, column=4)
        self.mCareerLabel.grid(row=8, column=5)
        self.magCareerLabel.grid(row=8, column=6)
        self.ipCareerLabel.grid(row=8, column=7)
        self.fpCareerLabel.grid(row=8, column=8)

        self.aCareerText.grid(row=9, column=1)
        self.wCareerText.grid(row=9, column=2)
        self.sbCareerText.grid(row=9, column=3)
        self.tbCareerText.grid(row=9, column=4)
        self.mCareerText.grid(row=9, column=5)
        self.magCareerText.grid(row=9, column=6)
        self.ipCareerText.grid(row=9, column=7)
        self.fpCareerText.grid(row=9, column=8)
        self.genderLabel.grid(row=10, column=0)
        genderMale.grid(row=11, column=0)
        genderFemale.grid(row=11, column=1)
        confirmButton.grid()
        button1.grid()

# when the button is pressed, it takes the appropriate race from the race list
# (self.racequery) and displays its advances.

    def selectRace(self, position):
        self.wsText.config(text=str(self.raceQuery[position][2]))
        self.bsText.config(text=str(self.raceQuery[position][3]))
        self.sText.config(text=str(self.raceQuery[position][4]))
        self.tText.config(text=str(self.raceQuery[position][5]))
        self.agText.config(text=str(self.raceQuery[position][6]))
        self.intText.config(text=str(self.raceQuery[position][7]))
        self.wpText.config(text=str(self.raceQuery[position][8]))
        self.felText.config(text=str(self.raceQuery[position][9]))
        self.mText.config(text=str(self.raceQuery[position][10]))
        temporary.raceStats = self.raceQuery[position]
        raceSkills = query.get_skills_talents('join_race_skill', 'race_id', position, self.raceQuery)
        raceSkills = query.put_in_order(raceSkills, 'skill')
        raceTalents = query.get_skills_talents('join_race_talent', 'race_id', position, self.raceQuery)
        raceTalents = query.put_in_order(raceTalents, 'talent')
        if temporary.raceStats[1]=='halfling':
            raceTalents[2].append('One Random Talent')
        elif temporary.raceStats[1] == 'human':
            raceTalents[2].append('Two Random Talents')

        query.print_skills_new_character(raceSkills, self.raceSkillText)
        query.print_skills_new_character(raceTalents, self.raceTalentText)

    def selectCareer(self, position):
        # this part writes down the available advances for the selected career
        self.wsCareerText.config(text=str(self.careerAdvanceQuery[position][4]*5))
        self.bsCareerText.config(text=str(self.careerAdvanceQuery[position][5]*5))
        self.sCareerText.config(text=str(self.careerAdvanceQuery[position][6]*5))
        self.tCareerText.config(text=str(self.careerAdvanceQuery[position][7]*5))
        self.agCareerText.config(text=str(self.careerAdvanceQuery[position][8]*5))
        self.intCareerText.config(text=str(self.careerAdvanceQuery[position][9]*5))
        self.wpCareerText.config(text=str(self.careerAdvanceQuery[position][10]*5))
        self.felCareerText.config(text=str(self.careerAdvanceQuery[position][11]*5))
        self.aCareerText.config(text=str(self.careerAdvanceQuery[position][12]))
        self.wCareerText.config(text=str(self.careerAdvanceQuery[position][13]))
        self.mCareerText.config(text=str(self.careerAdvanceQuery[position][14]))
        self.magCareerText.config(text=str(self.careerAdvanceQuery[position][15]))

        temporary.firstCareerId = self.careerAdvanceQuery[position][0]
        print(temporary.firstCareerId)
        # temporary.raceStats = self.raceQuery[position] # is it necessary for career?
        careerSkills = query.get_skills_talents('join_career_skill', 'career_id', position, self.careerAdvanceQuery)
        careerSkills = query.put_in_order(careerSkills, 'skill')
        careerTalents = query.get_skills_talents('join_career_talent', 'career_id', position, self.careerAdvanceQuery)
        careerTalents = query.put_in_order(careerTalents, 'talent')

        query.print_skills_new_character(careerSkills, self.careerSkillText)
        query.print_skills_new_character(careerTalents, self.careerTalentText)

    def setGender(self, gender):
        temporary.charGender = gender

    def confirmCharacter(self):
        # self.controller.show_frame(Skills)
        page = self.controller.test_get_page(Skills)
        page.roll_new_character(temporary.raceStats, temporary.charGender, temporary.firstCareerId)
        self.controller.show_frame(Skills)
        print(temporary.charGender)
        print(temporary.raceStats)
        print(temporary.firstCareerId)


class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='PageTwo').grid()
        button1 = ttk.Button(self, text='Previous Page',
                             command=lambda: controller.show_frame(Skills))
        button1.grid()


app = MyApp()
app.title('Multi-Page Test App')
app.mainloop()
