# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, he decides to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time (arriva time <= 0) to arrived late (arrival time > 0).
# Given the arrival time of each student and a threshhold number of attendees, determine if the class is canceled.


def angryProfessor(no_of_students , arrival_time):
    return ( "YES" if sum([1  for x in arrival_time if x <= 0 ]) < no_of_students else "NO")

print(angryProfessor(4 , [-1, -1, 0, 0, 1, 1]))
print(angryProfessor(5 , [-1, -1, 0, 0, 1, 1]))
print(angryProfessor(4 , [-1, -3, 4, 2]))
print(angryProfessor(3 , [-1, -3, 4, 2]))

