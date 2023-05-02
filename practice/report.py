
for week in range(1, 51):
    weekreport = open("{0}주차.txt".format(week), "w", encoding="utf8")
    weekreport.write("""
    - {0}주차 주간보고 -
    부서 : 
    이름 :
    업무 요약 :
    """.format(week))
    weekreport.close()


for week in range(1, 51):
    with open(str(week)+ "주차.txt", "w", encoding="utf8") as weekreport:
        weekreport.write("- {0}주차 주간보고 -".format(week))
        weekreport.write("\n부서 : ")
        weekreport.write("\n이름 : ")
        weekreport.write("\n업무 요약 : ")