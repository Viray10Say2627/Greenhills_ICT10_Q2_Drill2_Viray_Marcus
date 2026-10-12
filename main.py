from pyscript import display, document


def name_finder(e):
    document.getElementById('result').innerHTML = ''
    First_name = document.getElementById('first_name').value.title().strip()
    Last_name = document.getElementById('last_name').value.title().strip()
    Name = First_name + " " + Last_name
    Candidates = ['Alexa Agnote', 'Adrianna Allas', 'Jaena Ambata', 'Al-Makram Arbison', 'Alex Bueno', 'Ethan Chase De Guzman', 'Eliana De La Cruz', 'Xyruoz De Lara', 'Franco Deocampo', 'Leiane Gabia', 'Elise Lim', 'Helena Magsino', 'Misha Manalo', 'Ashley Mangondato', 'Jacob Mendoza', 'Sancho Mercado', 'David Niosco', 'Bonnie Nubla', 'Keane Pacaña', 'Aisha Padua', 'Katherine Peñas', 'Zoe Reyes', 'Cassey Rigodon', 'Princess Sagum', 'Aldrich Samar', 'Antonio Soliman', 'Frances Toculas', 'Sebastian Uclaray', 'Marcus Viray']
    student_checker = Name in Candidates

    display_message = (f'Sorry {Name}, your name is not in the list', f'Congratulations {Name}, you are now a part of ICT Club',)
    display(display_message[student_checker], target='result')