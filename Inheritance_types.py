# -------------------------
# 1. Single Inheritance
# -------------------------
class Parent:
    def show_parent(self):
        print("This is Parent class.")

class Child(Parent):  # Inheriting Parent
    def show_child(self):
        print("This is Child class.")

c = Child()
c.show_parent()
c.show_child()


# -------------------------
# 2. Multiple Inheritance
# -------------------------
class Father:
    def skill_father(self):
        print("Father: Knows driving.")

class Mother:
    def skill_mother(self):
        print("Mother: Knows cooking.")

class Son(Father, Mother):  # Inheriting from both Father & Mother
    def skill_son(self):
        print("Son: Knows programming.")

s = Son()
s.skill_father()
s.skill_mother()
s.skill_son()


# -------------------------
# 3. Multilevel Inheritance
# -------------------------
class Grandfather:
    def property(self):
        print("Grandfather's property.")

class Father(Grandfather):   # Inherits Grandfather
    def father_property(self):
        print("Father's property.")

class Son(Father):           # Inherits Father (and indirectly Grandfather)
    def son_property(self):
        print("Son's property.")

s = Son()
s.property()
s.father_property()
s.son_property()


# -------------------------
# 4. Hierarchical Inheritance
# -------------------------
class Parent:
    def common_property(self):
        print("This is common property from Parent.")

class Child1(Parent):  # First child
    def child1_property(self):
        print("Child1 specific property.")

class Child2(Parent):  # Second child
    def child2_property(self):
        print("Child2 specific property.")

c1 = Child1()
c1.common_property()
c1.child1_property()

c2 = Child2()
c2.common_property()
c2.child2_property()


# -------------------------
# 5. Hybrid Inheritance
# (Combination of two or more types)
# -------------------------
class A:
    def feature_a(self):
        print("Feature from class A")

class B(A):  # Single inheritance from A
    def feature_b(self):
        print("Feature from class B")

class C(A):  # Another child of A (Hierarchical)
    def feature_c(self):
        print("Feature from class C")

class D(B, C):  # Multiple inheritance (B + C)
    def feature_d(self):
        print("Feature from class D")

d = D()
d.feature_a()  # From A
d.feature_b()  # From B
d.feature_c()  # From C
d.feature_d()  # From D
