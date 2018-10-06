# Python_Class_Inheritance
This is a deep example of Python Class Inhertience with the usage of generators and understanding the hierarchy of classes inherited

What we have in this:
1. We've got a data structure, a grade book. Inside of it, we have a set of classes. Notice how I'm storing them. 
2. We have class Person which is a super class of MITPerson which is a super class of MITProfessor and Student. Student is super class of UG, Grad and TransferStudent classes.
3. Person can be sorted out on the basis of their name using defined method __lt__()
4. We have a list of the students. Those are the classes and I have associated with that a dictionary that, by ID number, lets me retrieve information about each student.
5. Students can be sorted out using their ids defined by __lt__() in MITPerson class.
6. We have a Grade class which contains methods to add students grades and calculate average of students' grades.
