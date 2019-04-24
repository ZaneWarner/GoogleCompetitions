cases = int(input())
for case in range(cases):
   studentCount, pick = [int(s) for s in input().split(" ")]
   students = [int(s) for s in input().split(" ")]
   students.sort()
   skill = 0
   maxSkill = 0
   picked = 0
   l = 0
   minHours = None
   for r in range(len(students)):
       skill += students[r]
       if students[r] > maxSkill:
           maxSkill = students[r]
       if picked < pick:
           picked += 1
       else:
           skill -= students[l]
           l += 1
       if picked == pick:
           skillNeeded = pick*maxSkill
           hours = skillNeeded - skill
           if minHours==None:
                minHours = hours
           elif hours < minHours:
                minHours = hours
   print("Case #{}: {}".format(case+1, minHours))
