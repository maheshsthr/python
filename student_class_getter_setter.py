import student as std

s1= std.Student()

s1.set_id(1)
s1.set_name("Mahesh")
s1.set_marks(99)

s2=std.Student()
s2.set_id(2)
s2.set_name("Vinesh")
s2.set_marks(88)

print(f"\nName : {s1.get_name()}\nID : {s1.get_id()}\nMarks : {s1.get_marks()}")
print(f"\nName : {s2.get_name()}\nID : {s2.get_id()}\nMarks : {s2.get_marks()}")
