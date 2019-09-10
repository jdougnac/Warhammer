# starting wounds
dwarf_start_wounds = [11, 11, 11, 12, 12, 12, 13, 13, 13, 14]
elf_start_wounds = [9, 9, 9, 10, 10, 10, 11, 11, 11, 12]
halfling_start_wounds = [8, 8, 8, 9, 9, 9, 10, 10, 10, 11]
human_start_wounds = [10, 10, 10, 11, 11, 11, 12, 12, 12, 13]

# starting fate points
dwarf_start_fp = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
elf_start_fp = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
halfling_start_fp = [2, 2, 2, 2, 2, 2, 2, 3, 3, 3]
human_start_fp = [2, 2, 2, 2, 3, 3, 3, 3, 3, 3]

# height in cm., [0] is for males, [1] for females
dwarf_height = [132, 127]
elf_height = [167, 162]
halfling_height = [101, 96]
human_height = [162, 154]

# weight minimum and maximum in kilos. It should be random within those two values
dwarf_weight = [40, 84]
elf_weight = [36, 80]
halfling_weight = [34, 66]
human_weight = [48, 100]

# hair color
dwarf_hair_color = ['Ash Blond', 'Yellow', 'Red', 'Copper', 'Light Brown', 'Brown', 'Brown',
                    'Dark Brown', 'Blue Black', 'Black']
elf_hair_color = ['Silver', 'Ash Blond', 'Corn', 'Yellow', 'Copper', 'Light Brown', 'Light Brown',
                  'Brown', 'Dark Brown', 'Black']
halfling_hair_color = ['Yellow', 'Yellow', 'Ash Blond', 'Corn', 'Red', 'Copper', 'Light Brown',
                       'Brown', 'Dark Brown', 'Black']
human_hair_color = ['Ash Blond', 'Corn', 'Yellow', 'Copper', 'Light Brown', 'Red', 'Brown', 'Brown',
                    'Dark Brown', 'Black']


dwarf_eye_color = ['Pale Grey', 'Blue', 'Copper', 'Light Brown', 'Light Brown', 'Brown', 'Brown',
                   'Dark Brown', 'Dark Brown', 'Purple']
elf_eye_color = ['Grey Blue', 'Green', 'Blue', 'Copper', 'Light Brown', 'Brown', 'Dark Brown', 'Silver',
                 'Purple', 'Black']
halfling_eye_color = ['Light Brown', 'Light Brown', 'Brown', 'Brown', 'Dark Brown', 'Dark Brown',
                      'Dark Brown', 'Blue', 'Hazel', 'Hazel']
human_eye_color = ['Pale Grey', 'Blue', 'Copper', 'Light Brown', 'Grey Blue', 'Green',
                   'Brown', 'Dark Brown', 'Purple', 'Black']


dwarf_siblings = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3]
elf_siblings = [0, 1, 1, 1, 1, 2, 2, 2, 2, 3]
halfling_siblings = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
human_siblings = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5]

# [0] is minimum, [1] is maximum, [2] is the interval
dwarf_age = [20, 115, 5]
elf_age = [30, 125, 5]
halfling_age = [20, 60, 2]
human_age = [16, 35, 1]

dwarf_birthplace = ['Karak Norn', 'Karak Izor', 'Karak Hirn', 'Karak Kadrin', 'Karaz-A-Karak', 'Zhufbar',
                    'Barak Varr', 'Karak Norn', 'Karak Izor', 'Karak Hirn', 'Karak Kadrin', 'Karaz-A-Karak',
                    'Zhufbar', 'Barak Varr', 'Karak Norn', 'Karak Izor', 'Karak Hirn', 'Karak Kadrin',
                    'Karaz-A-Karak', 'Zhufbar', 'Barak Varr', 'Averland', 'Hochland', 'Middenland', 'Nordland',
                    'Ostermark', 'Ostland', 'Reikland', 'Stirland', 'Talabecland', 'Wissenland']

elf_birthplace = ['Altdorf', 'Marienburg', 'Laurelorn Forest', 'The Great Forest', 'Reikwald Forest']

halfling_birthplace = ['Averland', 'Hochland', 'Middenland', 'Nordland', 'Ostermark', 'Ostland', 'Reikland',
                       'Stirland', 'Talabecland', 'Wissenland', 'The Moot', 'The Moot', 'The Moot', 'The Moot',
                       'The Moot', 'The Moot', 'The Moot', 'The Moot', 'The Moot', 'The Moot']

human_birthplace = ['Averland', 'Hochland', 'Middenland', 'Nordland', 'Ostermark', 'Ostland', 'Reikland',
                    'Stirland', 'Talabecland', 'Wissenland']

star_signs = ['Wymund the Anchorite', 'The Big Cross Sign', 'The Limner’s Line', 'Gnuthus the Ox',
              'Dragomas the Drake', 'The Gloaming', 'Grungni’s  Baldric', 'Mammit the Wise',
              'Mummit the Fool', 'The Two Bullocks', 'The Dancer', 'The Drummer', 'The Piper',
              'Vobist the Faint ', 'The Broken', 'The Greased Goat', 'Rhya’s Cauldron', 'Cackelfax the Cockerel',
              'The Bonesaw', 'The Witchling Star']

distinguishing_mark = ['Pox Marks', 'Ruddy Faced', 'Scar', 'Tattoo', 'Earring', 'Ragged Ear', 'Nose Ring',
                       'Wart', 'Broken Nose', 'Missing Tooth', 'Snaggle Teeth', 'Lazy Eye', 'Missing Eyebrow(s)',
                       'Missing Digit', 'Missing Nail', 'Distinctive Gait', 'Curious Smell', 'Huge Nose',
                       'Large Mole', 'Small Bald Patch', 'Strange Colored Eye(s)']

dwarf_list = [dwarf_age, dwarf_birthplace, dwarf_eye_color, dwarf_hair_color, dwarf_height, dwarf_siblings,
              dwarf_start_fp, dwarf_start_wounds, dwarf_weight, distinguishing_mark, star_signs]

elf_list = [elf_age, elf_birthplace, elf_eye_color, elf_hair_color, elf_height, elf_siblings, elf_start_fp,
            elf_start_wounds, elf_weight, distinguishing_mark, star_signs]

halfling_list = [halfling_age, halfling_birthplace, halfling_eye_color, halfling_hair_color, halfling_height,
                 halfling_siblings, halfling_start_fp, halfling_start_wounds, halfling_weight, distinguishing_mark,
                 star_signs]

human_list = [human_age, human_birthplace, human_eye_color, human_hair_color, human_height, human_siblings,
              human_start_fp, human_start_wounds, human_weight, distinguishing_mark, star_signs]
