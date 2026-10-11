# Laboratoriya işi №1 - Singly Linked List-in reallaşdırılması və tətbiqi
# Fənn: Verilənlərin Strukturu və Alqoritmlər
# Qrup: KOM24X


# ---------------------------------------------------------------
# Tapşırıq 1. Node sinfi
# ---------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Tapşırıq 2 - sonuna əlavə etmə
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Tapşırıq 3 - əvvələ əlavə etmə
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Tapşırıq 4 - verilmiş elementdən sonra əlavə etmə
    def insert_after(self, target, data):
        current = self.head
        while current is not None:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return True
            current = current.next
        print(f"{target} siyahıda tapılmadı.")
        return False

    # Tapşırıq 5 - element silmə
    def delete(self, value):
        if self.head is None:
            return False
        # silinən element başlanğıcdadırsa
        if self.head.data == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return True
            current = current.next
        return False

    # Tapşırıq 6 - axtarış
    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                print("Element tapıldı.")
                return True
            current = current.next
        print("Element tapılmadı.")
        return False

    # Tapşırıq 7 - uzunluq
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # Tapşırıq 8 - maksimum və minimum
    def find_max(self):
        if self.head is None:
            return None
        max_val = self.head.data
        current = self.head.next
        while current is not None:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        return max_val

    def find_min(self):
        if self.head is None:
            return None
        min_val = self.head.data
        current = self.head.next
        while current is not None:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        return min_val

    # Tapşırıq 9 - siyahını tərs çevirmək (yeni list yaratmadan,
    # yalnız next göstəricilərinin istiqamətini dəyişirik)
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        result = ""
        while current is not None:
            result += str(current.data) + " -> "
            current = current.next
        print(result + "None")


# ---------------------------------------------------------------
# Tapşırıq 10 (Challenge) - Tələbə qeydiyyat sistemi
# ---------------------------------------------------------------
class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name, gpa):
        # eyni ID ilə ikinci tələbə əlavə olunmasın
        current = self.head
        while current is not None:
            if current.student_id == student_id:
                print(f"ID {student_id} artıq mövcuddur.")
                return False
            current = current.next

        new_node = StudentNode(student_id, name, gpa)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        return True

    def remove_student(self, student_id):
        if self.head is None:
            print("Siyahı boşdur.")
            return False
        if self.head.student_id == student_id:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.student_id == student_id:
                current.next = current.next.next
                return True
            current = current.next
        print(f"ID {student_id} tapılmadı.")
        return False

    def show_all(self):
        if self.head is None:
            print("Siyahı boşdur.")
            return
        current = self.head
        while current is not None:
            print(f"ID: {current.student_id} | Ad: {current.student_name} | GPA: {current.gpa}")
            current = current.next

    def show_high_gpa(self, limit=80):
        found = False
        current = self.head
        while current is not None:
            if current.gpa > limit:
                print(f"ID: {current.student_id} | Ad: {current.student_name} | GPA: {current.gpa}")
                found = True
            current = current.next
        if not found:
            print(f"GPA > {limit} olan tələbə yoxdur.")

    def search_by_name(self, name):
        found = False
        current = self.head
        while current is not None:
            if current.student_name.lower() == name.lower():
                print(f"Tapıldı -> ID: {current.student_id} | Ad: {current.student_name} | GPA: {current.gpa}")
                found = True
            current = current.next
        if not found:
            print("Bu adda tələbə tapılmadı.")
        return found

    def count(self):
        total = 0
        current = self.head
        while current is not None:
            total += 1
            current = current.next
        return total


# ---------------------------------------------------------------
# Testlər
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== Tapşırıq 1 ===")
    n = Node(15)
    print("Node data:", n.data, "| next:", n.next)

    print("\n=== Tapşırıq 2 ===")
    ll = LinkedList()
    for x in [10, 20, 30, 40]:
        ll.append(x)
    ll.display()

    print("\n=== Tapşırıq 3 ===")
    ll = LinkedList()
    for x in [20, 30, 40]:
        ll.append(x)
    ll.prepend(10)
    ll.display()

    print("\n=== Tapşırıq 4 ===")
    ll = LinkedList()
    for x in [10, 20, 40]:
        ll.append(x)
    ll.insert_after(20, 30)
    ll.display()

    print("\n=== Tapşırıq 5 ===")
    ll = LinkedList()
    for x in [10, 20, 30, 40, 50]:
        ll.append(x)
    ll.delete(30)
    ll.display()

    print("\n=== Tapşırıq 6 ===")
    ll.search(40)
    ll.search(99)

    print("\n=== Tapşırıq 7 ===")
    ll = LinkedList()
    for x in [11, 22, 33, 44, 55]:
        ll.append(x)
    print("List length =", ll.length())

    print("\n=== Tapşırıq 8 ===")
    ll = LinkedList()
    for x in [23, 8, 91, 15, 42]:
        ll.append(x)
    ll.display()
    print("Maksimum element:", ll.find_max())
    print("Minimum element:", ll.find_min())

    print("\n=== Tapşırıq 9 ===")
    ll = LinkedList()
    for x in [10, 20, 30, 40, 50]:
        ll.append(x)
    print("Əvvəl:", end=" ")
    ll.display()
    ll.reverse()
    print("Sonra:", end=" ")
    ll.display()

    print("\n=== Tapşırıq 10 (Challenge) ===")
    students = StudentList()
    students.add_student(1, "Aysel Məmmədova", 92)
    students.add_student(2, "Elvin Həsənov", 75)
    students.add_student(3, "Nigar Quliyeva", 88)
    students.add_student(4, "Rauf Əliyev", 64)

    print("\nBütün tələbələr:")
    students.show_all()

    print("\nGPA > 80 olanlar:")
    students.show_high_gpa()

    print("\nAda görə axtarış (Nigar Quliyeva):")
    students.search_by_name("Nigar Quliyeva")

    print("\nID=2 olan tələbəni silirik...")
    students.remove_student(2)
    students.show_all()

    print("\nTələbələrin sayı:", students.count())
