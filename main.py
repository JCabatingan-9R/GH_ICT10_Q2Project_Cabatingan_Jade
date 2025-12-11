from pyscript import display, document

#grade calculator page
def gwacalc(e):
    # remove repeat
    document.querySelector("#about").innerText = ""
    document.querySelector("#ave").innerText = ""
    document.querySelector("#h2").innerText = ""

    # get name of student
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    name = fname + ' ' + lname # combine to get fullname of student

    # use float() for calculations
    sci_ = float(document.getElementById('sci').value)
    eng_ = float(document.getElementById('eng').value)
    ict_ = float(document.getElementById('ict').value)
    math_ = float(document.getElementById('math').value)
    fil_ = float(document.getElementById('fil').value)
    pe_ = float(document.getElementById('pe').value)
    
    # list with subjects
    subjects = ['SCIENCE', 'ENGLISH', 'ICT', 'MATH', 'FILIPINO', 'PHYSICAL EDUCATION']
    
    #tuple with subjects with numerical value
    grades = (sci_, eng_, ict_, math_, fil_, pe_)

    # tuple with subect units
    subjunits= (5, 5, 2, 5, 3, 1)

    # multiplying grade to number of units
    sci_calc = grades[0] * subjunits[0]
    eng_calc = grades[1] * subjunits[1]
    ict_calc = grades[2] * subjunits[2]
    math_calc = grades[3] * subjunits[3]
    fil_calc = grades[4] * subjunits[4]
    pe_calc = grades[5] * subjunits[5]

    # adds total grades
    final_calc = sci_calc + eng_calc + ict_calc + math_calc + fil_calc + pe_calc

    # adds total units
    subjunits_total = subjunits[0] + subjunits[1] + subjunits[2] + subjunits[3] + subjunits[4] + subjunits[5]

    # gets the average
    average = final_calc / subjunits_total

    # multisting for grade information
    multi = f"""
    {subjects[0]}: {sci_:.2f}
    {subjects[1]}: {eng_:.2f}
    {subjects[2]}: {ict_:.2f}
    {subjects[3]}: {math_:.2f}
    {subjects[4]}: {fil_:.2f}
    {subjects[5]}: {pe_:.2f}
    """

    display(f"Student Name: " + name, target='h2')
    display(multi, target='about')
    display(f'Your General Weighted Average is {average:.2f}', target='ave')

#school clubs page
def monarchs(e):
    # remove repeat
    document.querySelector("#cluboutput").innerText = ""

    info_title = ['Description', 'Meeting Time', 'Location', 'Moderator', 'Number of Members', 'Category'] #list of kinds of information about club
    
    desc = 'A club for dancers and those who want to improve'
    time = 'Mondays and Tuesdays from 3:00 p.m. to 5:00 p.m.'
    loc = 'Room 501-502'
    mod = 'Sir Marutani'
    members = '12'
    categ = 'non-academic'
    
    info = [desc, time, loc, mod, members, categ] #list of information about club

    multi = f"""
    {info_title[0]}:  {desc}
    {info_title[1]}: {time}
    {info_title[2]}: {loc}
    {info_title[3]}: {mod}
    {info_title[4]}: {members}
    {info_title[5]}: {categ}
    """

    display(multi, target='cluboutput')
#repeated code but for different clubs
def commarts(e): 
    # remove repeat
    document.querySelector("#cluboutput").innerText = ""

    info_title = ['Description', 'Meeting Time', 'Location', 'Moderator', 'Number of Members', 'Category']
    
    desc = 'A club for writing, speaking, and performing enthusiasts'
    time = 'Mondays from 2:30 p.m to 3:30 p.m. and Tuesdays 2:30 p.m. to 4:30 p.m.'
    loc = 'Room 711'
    mod = 'Sir Loreto'
    members = '40'
    categ = 'academic'
    
    info = [desc, time, loc, mod, members, categ]

    multi = f"""
    {info_title[0]}:  {desc}
    {info_title[1]}: {time}
    {info_title[2]}: {loc}
    {info_title[3]}: {mod}
    {info_title[4]}: {members}
    {info_title[5]}: {categ}
    """

    display(multi, target='cluboutput')

def art(e):
    # remove repeat
    document.querySelector("#cluboutput").innerText = ""

    info_title = ['Description', 'Meeting Time', 'Location', 'Moderator', 'Number of Members', 'Category']
    
    desc = 'A club for art enthusiasts to express themselves through painting and creation'
    time = 'Tuesdays and Thursdays from 3:00 p.m. to 4:00 p.m.'
    loc = 'Event Room'
    mod = 'Ma\'am Suarez'
    members = '30'
    categ = 'non-academic'
    
    info = [desc, time, loc, mod, members, categ]

    multi = f"""
    {info_title[0]}:  {desc}
    {info_title[1]}: {time}
    {info_title[2]}: {loc}
    {info_title[3]}: {mod}
    {info_title[4]}: {members}
    {info_title[5]}: {categ}
    """

    display(multi, target='cluboutput')

def science(e):
    # remove repeat
    document.querySelector("#cluboutput").innerText = ""

    info_title = ['Description', 'Meeting Time', 'Location', 'Moderator', 'Number of Members', 'Category']
    
    desc = 'A club for science enthusiasts to work on laboratory experiments and learn advanced topics on the subject'
    time = 'Tuesdays from 2:00 p.m. to 4:00 p.m.'
    loc = 'Room 712 and 5th floor Chemistry Laboratory'
    mod = 'Sir Celzo'
    members = '37'
    categ = 'academic'
    
    info = [desc, time, loc, mod, members, categ]

    multi = f"""
    {info_title[0]}:  {desc}
    {info_title[1]}: {time}
    {info_title[2]}: {loc}
    {info_title[3]}: {mod}
    {info_title[4]}: {members}
    {info_title[5]}: {categ}
    """

    display(multi, target='cluboutput')

def math(e):
    # remove repeat
    document.querySelector("#cluboutput").innerText = ""

    info_title = ['Description', 'Meeting Time', 'Location', 'Moderator', 'Number of Members', 'Category']
    
    desc = 'A club for math enthusiasts to learn advanced techniques and formulas'
    time = 'Mondays from 2:30 p.m. to 4:30 p.m.'
    loc = 'Room 711'
    mod = 'Sir Tamon'
    members = '20'
    categ = 'academic'
    
    info = [desc, time, loc, mod, members, categ]

    multi = f"""
    {info_title[0]}:  {desc}
    {info_title[1]}: {time}
    {info_title[2]}: {loc}
    {info_title[3]}: {mod}
    {info_title[4]}: {members}
    {info_title[5]}: {categ}
    """

    display(multi, target='cluboutput')
