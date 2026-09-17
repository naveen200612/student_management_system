with open("student_report.txt", "w") as f:
    f.write("==================================================\n")
    f.write(" STUDENT MANAGEMENT & ACADEMIC PERFORMANCE REPORT \n")
    f.write("==================================================\n")
    f.write("Total Registered Students: 250\n")
    f.write("Average Class Grade Point: 8.4 / 10.0\n")
    f.write("Students on Academic Probation: 5\n")
    f.write("Top Performing Course: Agile Development Process & DevOps\n")
    f.write("==================================================\n")
    f.write("Report generated successfully by automated CI/CD pipeline.\n")

print("Student academic performance report generated.")
