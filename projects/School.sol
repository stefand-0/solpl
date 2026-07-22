/* ============================================================
   SOL - School Management System
   Features:
   - Student records with templates
   - Grade tracking and GPA calculation
   - Class enrollment with lists
   - Teacher assignments
   - Report generation
   - Search and filter operations
   ============================================================ */

/* Template for a student */
templ Student
    id: integer
    name: string
    grade: integer
    gpa: float
    enrolled: boolean
end

/* Template for a teacher */
templ Teacher
    id: integer
    name: string
    subject: string
    students: list
end

/* Template for a class/course */
templ Course
    code: string
    name: string
    teacher: Teacher
    students: list
    maxCapacity: integer
end

/* Global school data */
imm nextStudentId: integer -> 1000
imm nextTeacherId: integer -> 2000
imm nextCourseCode: integer -> 100

nonimm allStudents: list
nonimm allTeachers: list
nonimm allCourses: list

/* Initialize the school */
fun initSchool(): nothing
    allStudents -> []
    allTeachers -> []
    allCourses -> []
    std.outln("School Management System initialized!")
    std.outln("")
end

/* Create a new student */
fun createStudent(name: string, grade: integer): Student
    imm student: Student -> Student(nextStudentId, name, grade, 0.0, true)
    nextStudentId -> nextStudentId + 1
    allStudents -> list.push(allStudents, student)
    ret student
end

/* Create a new teacher */
fun createTeacher(name: string, subject: string): Teacher
    imm teacher: Teacher -> Teacher(nextTeacherId, name, subject, [])
    nextTeacherId -> nextTeacherId + 1
    allTeachers -> list.push(allTeachers, teacher)
    ret teacher
end

/* Create a new course */
fun createCourse(name: string, teacher: Teacher, maxCapacity: integer): Course
    imm code: string -> "CS" + type.toString(nextCourseCode)
    imm course: Course -> Course(code, name, teacher, [], maxCapacity)
    nextCourseCode -> nextCourseCode + 1
    allCourses -> list.push(allCourses, course)
    ret course
end

/* Enroll a student in a course */
fun enrollStudent(course: Course, student: Student): Result<string, string>
    if (list.len(course.students) >= course.maxCapacity)
        ret Err("Course is full!")
    end
    if (!student.enrolled)
        ret Err("Student is not active!")
    end
    course.students -> list.push(course.students, student)
    student.gpa -> 3.5
    ret Ok("Enrolled successfully!")
end

/* Calculate class average GPA */
fun classAverageGPA(course: Course): float
    if (list.len(course.students) == 0)
        ret 0.0
    end
    nonimm total: float -> 0.0
    for (student in course.students)
        total -> total + student.gpa
    end
    ret total / type.iToFloat(list.len(course.students))
end

/* Find student by ID */
fun findStudent(id: integer): Result<Student, string>
    for (student in allStudents)
        if (student.id == id)
            ret Ok(student)
        end
    end
    ret Err("Student not found")
end

/* List all students in a grade */
fun studentsInGrade(grade: integer): list
    nonimm result: list -> []
    for (student in allStudents)
        if (student.grade == grade)
            result -> list.push(result, student)
        end
    end
    ret result
end

/* Print student info */
fun printStudent(student: Student): nothing
    std.outln("ID: " + type.toString(student.id))
    std.outln("Name: " + student.name)
    std.outln("Grade Level: " + type.toString(student.grade))
    std.outln("GPA: " + type.toString(student.gpa))
    std.outln("Enrolled: " + type.toString(student.enrolled))
    std.outln("---")
end

/* Print course info */
fun printCourse(course: Course): nothing
    std.outln("Course: " + course.code + " - " + course.name)
    std.outln("Teacher: " + course.teacher.name)
    std.outln("Students: " + type.toString(list.len(course.students)) + "/" + type.toString(course.maxCapacity))
    std.outln("Avg GPA: " + type.toString(classAverageGPA(course)))
    std.outln("---")
end

/* Generate school report */
fun generateReport(): nothing
    std.outln("")
    std.outln("========================================")
    std.outln("       SCHOOL MANAGEMENT REPORT")
    std.outln("========================================")
    std.outln("")
    
    std.outln("Total Students: " + type.toString(list.len(allStudents)))
    std.outln("Total Teachers: " + type.toString(list.len(allTeachers)))
    std.outln("Total Courses: " + type.toString(list.len(allCourses)))
    std.outln("")
    
    std.outln("--- Students ---")
    for (student in allStudents)
        printStudent(student)
    end
    
    std.outln("--- Courses ---")
    for (course in allCourses)
        printCourse(course)
    end
    
    std.outln("========================================")
end

/* Main demo */
fun main(): nothing
    initSchool()
    
    std.outln("Creating students...")
    imm alice: Student -> createStudent("Alice Johnson", 10)
    imm bob: Student -> createStudent("Bob Smith", 11)
    imm charlie: Student -> createStudent("Charlie Brown", 10)
    imm diana: Student -> createStudent("Diana Prince", 12)
    
    std.outln("Creating teachers...")
    imm mrMath: Teacher -> createTeacher("Mr. Euler", "Mathematics")
    imm msScience: Teacher -> createTeacher("Ms. Curie", "Physics")
    
    std.outln("Creating courses...")
    imm algebra: Course -> createCourse("Algebra II", mrMath, 30)
    imm physics: Course -> createCourse("AP Physics", msScience, 25)
    
    std.outln("Enrolling students...")
    enrollStudent(algebra, alice)
    enrollStudent(algebra, bob)
    enrollStudent(algebra, charlie)
    enrollStudent(physics, bob)
    enrollStudent(physics, diana)
    
    std.outln("")
    std.outln("Searching for student ID 1001...")
    imm found: Result<Student, string> -> findStudent(1001)
    if (result.isOk(found))
        std.outln("Found:")
        printStudent(result.unwrap(found))
    else
        std.outln("Not found: " + result.unwrapOrElse(found, ld() ret "error" end))
    end
    
    std.outln("")
    std.outln("Grade 10 students:")
    imm grade10: list -> studentsInGrade(10)
    for (student in grade10)
        std.outln("  - " + student.name)
    end
    
    generateReport()
end

main()
