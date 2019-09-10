import mysql.connector as mysql
from tkinter import *

db = mysql.connect(user='root', password='',
                   host='127.0.0.1',
                   database='warhammer')


# a simple query selecting all results from the
# given parameters
def selectAll(parameters, table):
    request = "SELECT "+parameters+" FROM "+table
    cursor = db.cursor()
    cursor.execute(request)
    results = cursor.fetchall()
    return results


# this makes a query with a single select where
# example: select * from process where process_id = 25
def selectWhere(parameters, table, where, amount):
    if type(amount) == int and amount > 0:
        request = "SELECT "+parameters+" FROM "+table+" WHERE "+where+"="+str(amount)
        cursor = db.cursor()
        cursor.execute(request)    
        results = cursor.fetchall()    
        return results
    else:
        raise Exception('Amounts must be positive integers.')


# this function makes a query based on the table the desired skills/ talents are,
# its source (race or career), and the table from whence the final output will come.
# Then, it makes a query to get the list of skills/talents, which is then ordered into
# the 'skills_talents' list: position [0] is for individual skill/talents, pos [1] for those
# with 'any', and position [2] for those with 'or', which is why they're assigned as sub lists,
# for the different options
def get_skills_talents(origin_table, skill_talent_column, origin_table_id, previous_query=0):
    if previous_query == 0:
        skills_talents_query = selectWhere('*', origin_table, skill_talent_column, origin_table_id[0])
    else:
        skills_talents_query = selectWhere('*', origin_table, skill_talent_column, previous_query[origin_table_id][0])

    skills_talents = [[], [], []]
    for skill in skills_talents_query:
        check = 0
        # print('aa', skills_talents[2])
        if skill[3] == 0 and skill[2] < 2:
            skills_talents[0].append(skill)
        elif skill[3] == 0 and skill[2] > 1:
            skills_talents[1].append(skill)
        elif skill[3] != 0:
            if len(skills_talents[2]) == 0:
                skills_talents[2].append([skill])
            else:
                for item in skills_talents[2]:
                    if skill[3] == item[0][3]:
                        item.append(skill)
                        check = 1
                if check == 0:
                    skills_talents[2].append([skill])
    return skills_talents


# this function takes a list (normally the result of the get_skill_talents function,
# and turns it into words to be displayed on the generator. Position [0] is for the
# simple skills, [1] is for the 'any' skills, and [2] is for the 'or' skills
def put_in_order(skill_list, skill_type):
    new_list = [[], [], []]
    if skill_type == 'skill':
        variable = 'skill_id'
        table = 'skills'
        name = 'skill_name'
    elif skill_type == 'talent':
        variable = 'talent_id'
        table = 'talents'
        name = 'talent_name'
    else:
        return 'Error, it could only be a skill or talent'
    for oobject in skill_list[0]:
        object_name = selectWhere(name, table, variable, oobject[1])
        new_list[0].append(object_name)
    if len(skill_list[1]) > 0:
        for any_object in skill_list[1]:
            any_object_name = selectWhere(name, table, variable, any_object[1])
            any_object_name = str(any_object_name[0][0][:-1])
            if any_object[2] == 1:
                any_object_name += ' one)'
            elif any_object[2] == 2:
                any_object_name += ' two)'
            elif any_object[2] == 3:
                any_object_name += ' three)'
            elif any_object[2] == 4:
                any_object_name += ' four)'
            elif any_object[2] == 5:
                any_object_name += ' five)'
            elif any_object[2] == 6:
                any_object_name += ' six)'
            elif any_object[2] == 7:
                any_object_name += ' seven)'
            elif any_object[2] == 8:
                any_object_name += ' eight)'
            elif any_object[2] == 9:
                any_object_name += ' nine)'
            elif any_object[2] == 10:
                any_object_name += ' ten)'
            new_list[1].append(any_object_name)
    if len(skill_list[2]) > 0:
        for or_object in skill_list[2]:

            new_or_object = []
            check = 1
            for iitem in or_object:
                or_object_name = selectWhere(name, table, variable, iitem[1])
                or_object_name = str(or_object_name[0][0])
                if check < len(or_object)-1:
                    or_object_name += ',\n'
                elif check == len(or_object)-1:
                    or_object_name += ' or\n '
                new_or_object.append(or_object_name)
                check += 1
            new_or_object = str(''.join(new_or_object))
            new_list[2].append(new_or_object)
    return new_list

# given that skills and talents for new characters are in a set order
# in the list (which has previously been queried and ordered), this function
# prints its contents in the appropriate order to the corresponding
# text widgets.


def print_skills_new_character(skill_list, widget):
    widget.delete('1.0', END)
    # print('gg', skill_list)
    for skill in skill_list:
        for talent in skill:
          #  print(talent, len(talent))
            if len(talent) == 1:
                talent = str(talent[0])
                talent = talent[2:-3]

            widget.insert(END, '- ')
            widget.insert(END, talent)
            widget.insert(END, '\n')





